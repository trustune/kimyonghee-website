"""
MediaINT AI Curation Script
DB 클러스터 → LLM 초안 생성 → stories_weekly_draft.json

Usage:
  python curate_mediaint.py                     # 초안 생성 (stdout + JSON)
  python curate_mediaint.py --provider ollama   # Ollama 로컬 LLM
  python curate_mediaint.py --provider anthropic # Claude API
  python curate_mediaint.py --approve           # 초안 → 확정 (stories_weekly.json)

Claude Agent 워크플로우:
  1. python collect_mediaint.py --source all --cluster
  2. python curate_mediaint.py  → stories_weekly_draft.json 생성
  3. Agent가 draft 검토/수정
  4. python curate_mediaint.py --approve → stories_weekly.json 확정
  5. 배포 (git push)
"""
import sys, os, json, argparse
from datetime import datetime, timedelta

import psycopg2
import psycopg2.extras
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, '..', 'services', 'newsletter', 'config.yaml')
DRAFT_PATH = os.path.join(BASE_DIR, '..', 'services', 'newsletter', 'stories_weekly_draft.json')
FINAL_PATH = os.path.join(BASE_DIR, '..', 'services', 'newsletter', 'stories_weekly.json')

with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    CFG = yaml.safe_load(f)

DB_CONFIG = {
    'host': os.environ.get('PG_HOST', 'localhost'),
    'port': int(os.environ.get('PG_PORT', 5432)),
    'dbname': os.environ.get('PG_DATABASE', 'mediaint_db'),
    'user': os.environ.get('PG_USER', 'postgres'),
    'password': os.environ.get('PG_PASSWORD', ''),
}

CAT_COLORS = {
    "OTT/Streaming": "#e53935", "Film/Cinema": "#8e24aa",
    "Music/Audio": "#2e7d32", "Gaming/Esports": "#ef6c00",
    "K-Content": "#d81b60", "Media Business": "#1565c0",
    "Regulation": "#ff6f00",
}


def get_top_clusters(days=7, limit=15):
    """DB에서 최근 N일 상위 클러스터 조회"""
    conn = psycopg2.connect(**DB_CONFIG)
    cutoff = datetime.now().date() - timedelta(days=days)

    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("""
            SELECT sc.*, c.name_en as category
            FROM story_clusters sc
            LEFT JOIN categories c ON c.id = sc.primary_category_id
            WHERE sc.cluster_date >= %s
            ORDER BY sc.score DESC
            LIMIT %s
        """, (cutoff, limit))
        clusters = cur.fetchall()

        result = []
        for cl in clusters:
            cur.execute("""
                SELECT a.title, a.url, a.source_domain, a.published_at
                FROM cluster_articles ca
                JOIN articles a ON a.id = ca.article_id
                WHERE ca.cluster_id = %s
                ORDER BY a.published_at DESC
                LIMIT 10
            """, (cl['id'],))
            articles = cur.fetchall()

            result.append({
                "cluster_id": cl['id'],
                "headline": cl['headline'],
                "category": cl.get('category', 'Other'),
                "article_count": cl['article_count'],
                "score": float(cl.get('score', 0)),
                "articles": [
                    {"title": a['title'], "url": a['url'], "domain": a['source_domain'],
                     "date": a['published_at'].isoformat() if a['published_at'] else ""}
                    for a in articles
                ],
            })

    conn.close()
    return result


def generate_draft_with_llm(clusters, provider='none'):
    """LLM으로 각 클러스터의 한국어 요약 초안 생성"""
    stories = []

    for i, cl in enumerate(clusters[:12]):
        titles = [a['title'] for a in cl['articles'][:8]]
        sources = [(a['domain'], a['url']) for a in cl['articles'][:4]]
        category = cl['category']
        color = CAT_COLORS.get(category, '#666')

        # LLM 프롬프트
        prompt = f"""아래는 '{category}' 카테고리의 {cl['article_count']}개 뉴스 기사 제목입니다.
이 기사들을 종합하여 미디어 산업 주간 리포트용 기사 1건을 작성하세요.

기사 제목들:
{chr(10).join(f'- {t}' for t in titles)}

규칙:
1. title: 한국 신문 스타일 헤드라인 (명사형/체언 종결, "~다"로 끝내지 않음)
2. body: 5-8문장, 완결된 문장으로 작성 (300자 이상)
3. key_points: 3개, 각각 완결된 한 문장
4. 모든 수치와 고유명사는 정확하게

JSON으로 응답:
{{"title": "...", "body": "...", "key_points": ["...", "...", "..."]}}"""

        title = cl['headline']
        body = ""
        key_points = []

        if provider == 'ollama':
            model = CFG.get('llm', {}).get('model', 'deepseek-v3')
            try:
                import requests
                r = requests.post("http://localhost:11434/api/generate", json={
                    "model": model, "prompt": prompt, "stream": False,
                    "options": {"temperature": 0.3}
                }, timeout=120)
                if r.status_code == 200:
                    text = r.json().get('response', '')
                    parsed = json.loads(text[text.find('{'):text.rfind('}') + 1])
                    title = parsed.get('title', title)
                    body = parsed.get('body', '')
                    key_points = parsed.get('key_points', [])
            except Exception as e:
                print(f"  LLM error for cluster {i}: {e}")

        elif provider == 'anthropic':
            api_key = os.environ.get('ANTHROPIC_API_KEY', '')
            if api_key:
                try:
                    import requests
                    r = requests.post("https://api.anthropic.com/v1/messages", headers={
                        "x-api-key": api_key,
                        "anthropic-version": "2023-06-01",
                        "content-type": "application/json",
                    }, json={
                        "model": "claude-sonnet-4-20250514",
                        "max_tokens": 1024,
                        "messages": [{"role": "user", "content": prompt}],
                    }, timeout=60)
                    if r.status_code == 200:
                        text = r.json()['content'][0]['text']
                        parsed = json.loads(text[text.find('{'):text.rfind('}') + 1])
                        title = parsed.get('title', title)
                        body = parsed.get('body', '')
                        key_points = parsed.get('key_points', [])
                except Exception as e:
                    print(f"  LLM error for cluster {i}: {e}")

        stories.append({
            "rank": i + 1,
            "title": title,
            "category": category,
            "color": color,
            "body": body or f"[초안 필요] {cl['headline']} — {cl['article_count']}개 소스",
            "key_points": key_points,
            "sources": sources,
            "source_count": cl['article_count'],
            "image": "",
            "cluster_id": cl['cluster_id'],
        })

    return stories


def save_draft(stories):
    with open(DRAFT_PATH, 'w', encoding='utf-8') as f:
        json.dump(stories, f, ensure_ascii=False, indent=2)
    print(f"\n  Draft saved: {DRAFT_PATH}")
    print(f"  Stories: {len(stories)}")
    print(f"\n  Top 5:")
    for s in stories[:5]:
        status = "✓" if s['body'] and not s['body'].startswith('[초안') else "✗"
        print(f"    {status} [{s['category']:18s}] {s['title'][:60]}")


def approve_draft():
    """초안을 확정하여 stories_weekly.json으로 복사"""
    if not os.path.exists(DRAFT_PATH):
        print(f"  Error: Draft not found at {DRAFT_PATH}")
        return

    with open(DRAFT_PATH, 'r', encoding='utf-8') as f:
        stories = json.load(f)

    # sources를 list of lists로 변환 (JSON 호환)
    for s in stories:
        if isinstance(s.get('sources'), list):
            s['sources'] = [[n, u] for n, u in s['sources']]

    with open(FINAL_PATH, 'w', encoding='utf-8') as f:
        json.dump(stories, f, ensure_ascii=False, indent=2)

    print(f"  Approved: {FINAL_PATH}")
    print(f"  {len(stories)} stories confirmed for weekly report.")


def main():
    parser = argparse.ArgumentParser(description="MediaINT AI Curation")
    parser.add_argument("--provider", choices=["none", "ollama", "anthropic"], default="none")
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--approve", action="store_true", help="Approve draft → final")
    parser.add_argument("--show", action="store_true", help="Show current draft")
    args = parser.parse_args()

    if args.approve:
        approve_draft()
        return

    if args.show:
        if os.path.exists(DRAFT_PATH):
            with open(DRAFT_PATH, 'r', encoding='utf-8') as f:
                stories = json.load(f)
            for s in stories:
                print(f"\n[{s['rank']}] {s['title']}")
                print(f"    Category: {s['category']}, Sources: {s['source_count']}")
                if s['body'] and not s['body'].startswith('[초안'):
                    print(f"    Body: {s['body'][:100]}...")
        return

    print(f"\n{'='*60}")
    print(f"MediaINT Curation — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Provider: {args.provider}, Days: {args.days}")
    print(f"{'='*60}")

    print(f"\n[1/2] Loading clusters from DB...")
    clusters = get_top_clusters(days=args.days)
    print(f"  Found {len(clusters)} clusters")

    print(f"\n[2/2] Generating draft...")
    stories = generate_draft_with_llm(clusters, provider=args.provider)
    save_draft(stories)

    print(f"\n  Next steps:")
    print(f"  1. Review/edit: {DRAFT_PATH}")
    print(f"  2. Approve:     python curate_mediaint.py --approve")


if __name__ == "__main__":
    main()

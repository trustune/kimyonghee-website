"""
JournalINT × MediaINT 교차 참조
papers_db의 topic_tags ↔ mediaint_db의 기사/클러스터 자동 매칭

Usage:
  python crossref_journalint.py                  # 자동 매칭 실행
  python crossref_journalint.py --cluster-id 5   # 특정 클러스터에 대해 매칭
  python crossref_journalint.py --show            # 현재 매칭 결과 조회
"""
import os, json, argparse
from datetime import datetime, timedelta

import psycopg2
import psycopg2.extras

MEDIAINT_DB = {
    'host': os.environ.get('PG_HOST', 'localhost'),
    'port': int(os.environ.get('PG_PORT', 5432)),
    'dbname': 'mediaint_db',
    'user': os.environ.get('PG_USER', 'postgres'),
    'password': os.environ.get('PG_PASSWORD', ''),
}

PAPERS_DB = {
    'host': os.environ.get('PG_HOST', 'localhost'),
    'port': int(os.environ.get('PG_PORT', 5432)),
    'dbname': 'papers_db',
    'user': os.environ.get('PG_USER', 'research'),
    'password': os.environ.get('PG_PASSWORD', ''),
}

# MediaINT 카테고리 → 관련 topic_tags 키워드
CATEGORY_TAG_MAP = {
    "OTT/Streaming": ["OTT", "streaming", "Netflix", "Disney+", "subscription", "SVOD", "cord-cutting", "platform"],
    "Film/Cinema": ["film", "cinema", "box office", "movie", "theatrical"],
    "Music/Audio": ["music", "streaming", "Spotify", "K-pop", "record label"],
    "Gaming/Esports": ["gaming", "esports", "video game", "mobile game"],
    "K-Content": ["Korean", "K-drama", "hallyu", "Korean wave", "K-content", "webtoon"],
    "Media Business": ["media industry", "advertising", "media company", "content creation", "creator economy"],
    "Regulation": ["regulation", "policy", "content regulation", "media regulation", "net neutrality", "digital tax"],
}


def find_matching_papers(papers_conn, search_tags, limit=10):
    """papers_db에서 topic_tags가 매칭되는 논문 검색"""
    with papers_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        # topic_tags JSONB에서 매칭
        cur.execute("""
            SELECT id, title, doi, topic_tags, publication_year, journal_id
            FROM journal_research_items
            WHERE topic_tags IS NOT NULL
              AND topic_tags != '[]'::jsonb
              AND EXISTS (
                SELECT 1 FROM jsonb_array_elements_text(topic_tags) t
                WHERE LOWER(t) = ANY(%s)
              )
            ORDER BY publication_year DESC
            LIMIT %s
        """, ([t.lower() for t in search_tags], limit))
        return cur.fetchall()


def auto_match(days=7):
    """최근 N일 클러스터에 대해 자동으로 논문 매칭"""
    mi_conn = psycopg2.connect(**MEDIAINT_DB)

    try:
        pa_conn = psycopg2.connect(**PAPERS_DB)
    except Exception as e:
        print(f"  papers_db 연결 실패: {e}")
        print(f"  JournalINT 교차 참조를 건너뜁니다.")
        mi_conn.close()
        return 0

    cutoff = datetime.now().date() - timedelta(days=days)
    matches = 0

    with mi_conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("""
            SELECT sc.id, sc.headline, c.name_en as category
            FROM story_clusters sc
            LEFT JOIN categories c ON c.id = sc.primary_category_id
            WHERE sc.cluster_date >= %s
            ORDER BY sc.score DESC LIMIT 20
        """, (cutoff,))
        clusters = cur.fetchall()

    for cl in clusters:
        category = cl.get('category', '')
        tags = CATEGORY_TAG_MAP.get(category, [])

        # 헤드라인에서 추가 키워드 추출
        headline_words = cl['headline'].lower().split()
        for keyword in ['netflix', 'disney', 'amazon', 'spotify', 'bts', 'paramount', 'warner']:
            if keyword in ' '.join(headline_words):
                tags.append(keyword)

        if not tags:
            continue

        papers = find_matching_papers(pa_conn, tags, limit=5)
        for paper in papers:
            # 매칭 점수 계산
            paper_tags = [t.lower() for t in (paper.get('topic_tags') or [])]
            matched = set(t.lower() for t in tags) & set(paper_tags)
            score = len(matched) / max(len(tags), 1)

            if score < 0.1:
                continue

            with mi_conn.cursor() as insert_cur:
                try:
                    insert_cur.execute("""
                        INSERT INTO journalint_crossref
                            (cluster_id, research_item_id, journal_id, paper_title, paper_doi,
                             match_type, matched_tags, relevance_score)
                        VALUES (%s, %s, %s, %s, %s, 'auto', %s, %s)
                        ON CONFLICT DO NOTHING
                    """, (
                        cl['id'], paper['id'], paper.get('journal_id'),
                        paper['title'], paper.get('doi'),
                        json.dumps(list(matched), ensure_ascii=False),
                        round(score, 3),
                    ))
                    mi_conn.commit()
                    matches += 1
                except:
                    mi_conn.rollback()

    mi_conn.close()
    pa_conn.close()
    return matches


def show_crossrefs():
    conn = psycopg2.connect(**MEDIAINT_DB)
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("""
            SELECT jc.*, sc.headline as cluster_headline
            FROM journalint_crossref jc
            LEFT JOIN story_clusters sc ON sc.id = jc.cluster_id
            ORDER BY jc.relevance_score DESC
            LIMIT 30
        """)
        rows = cur.fetchall()

    if not rows:
        print("  교차 참조 없음")
        return

    print(f"\n  {'Cluster':40s} {'Paper':40s} {'Score':6s} {'Tags'}")
    print(f"  {'─'*40} {'─'*40} {'─'*6} {'─'*20}")
    for r in rows:
        cl = (r.get('cluster_headline') or '')[:38]
        pa = (r.get('paper_title') or '')[:38]
        sc = f"{r.get('relevance_score', 0):.2f}"
        tags = ', '.join(r.get('matched_tags', [])[:3])
        print(f"  {cl:40s} {pa:40s} {sc:6s} {tags}")

    conn.close()


def main():
    parser = argparse.ArgumentParser(description="JournalINT × MediaINT Cross-Reference")
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()

    if args.show:
        show_crossrefs()
        return

    print(f"\n{'='*60}")
    print(f"JournalINT × MediaINT Cross-Reference")
    print(f"{'='*60}")

    matches = auto_match(days=args.days)
    print(f"\n  New matches: {matches}")
    show_crossrefs()


if __name__ == "__main__":
    main()

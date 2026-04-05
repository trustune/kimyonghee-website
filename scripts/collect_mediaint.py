"""
MediaINT Multi-Source Collector
GDELT + Google News RSS + 한국 전문지 RSS → PostgreSQL

Usage:
  python collect_mediaint.py                    # 전체 수집
  python collect_mediaint.py --source gdelt     # GDELT만
  python collect_mediaint.py --source rss       # RSS만
  python collect_mediaint.py --dry-run          # DB 저장 없이 테스트
"""
import sys, os, json, time, hashlib, re, argparse
from datetime import datetime, timedelta
from collections import Counter

import requests
import psycopg2
import psycopg2.extras
import feedparser
import yaml
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering

# ── Config ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, '..', 'services', 'newsletter', 'config.yaml')

with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    CFG = yaml.safe_load(f)

DB_CONFIG = {
    'host': os.environ.get('PG_HOST', 'localhost'),
    'port': int(os.environ.get('PG_PORT', 5432)),
    'dbname': os.environ.get('PG_DATABASE', 'mediaint_db'),
    'user': os.environ.get('PG_USER', 'postgres'),
    'password': os.environ.get('PG_PASSWORD', ''),
}

GDELT_API = "https://api.gdeltproject.org/api/v2/doc/doc"
_tmdb_token_cfg = CFG.get('tmdb', {}).get('token', '')
# Load from env if placeholder or empty
if not _tmdb_token_cfg or _tmdb_token_cfg.startswith('${'):
    _tmdb_token_cfg = os.environ.get('TMDB_TOKEN', '')
TMDB_TOKEN = _tmdb_token_cfg
TMDB_LANG = CFG.get('tmdb', {}).get('language', 'ko-KR')

# ── Category mapping ──
CAT_SLUG_MAP = {
    "OTT/Streaming": "ott_streaming",
    "Film/Cinema": "film_cinema",
    "Music/Audio": "music_audio",
    "Gaming/Esports": "gaming_esports",
    "K-Content": "k_content",
    "Media Business": "media_business",
    "Regulation": "regulation",
}

# ── Google News RSS feeds ──
GOOGLE_NEWS_FEEDS = [
    # 영문
    {"name": "GNews OTT EN", "url": "https://news.google.com/rss/search?q=netflix+OR+%22disney+plus%22+OR+streaming+OR+OTT&hl=en&gl=US&ceid=US:en", "category": "OTT/Streaming", "lang": "en"},
    {"name": "GNews Film EN", "url": "https://news.google.com/rss/search?q=%22box+office%22+OR+%22film+industry%22+OR+cinema&hl=en&gl=US&ceid=US:en", "category": "Film/Cinema", "lang": "en"},
    {"name": "GNews Music EN", "url": "https://news.google.com/rss/search?q=spotify+OR+%22music+streaming%22+OR+%22music+industry%22&hl=en&gl=US&ceid=US:en", "category": "Music/Audio", "lang": "en"},
    {"name": "GNews Gaming EN", "url": "https://news.google.com/rss/search?q=%22video+game%22+OR+esports+OR+%22gaming+industry%22&hl=en&gl=US&ceid=US:en", "category": "Gaming/Esports", "lang": "en"},
    # 한국어
    {"name": "GNews OTT KR", "url": "https://news.google.com/rss/search?q=넷플릭스+OR+디즈니플러스+OR+OTT+OR+스트리밍&hl=ko&gl=KR&ceid=KR:ko", "category": "OTT/Streaming", "lang": "ko"},
    {"name": "GNews K-Content KR", "url": "https://news.google.com/rss/search?q=한류+OR+K콘텐츠+OR+K드라마+OR+웹툰&hl=ko&gl=KR&ceid=KR:ko", "category": "K-Content", "lang": "ko"},
    {"name": "GNews Media KR", "url": "https://news.google.com/rss/search?q=미디어+규제+OR+방송+정책+OR+OTT+규제&hl=ko&gl=KR&ceid=KR:ko", "category": "Regulation", "lang": "ko"},
    {"name": "GNews Film KR", "url": "https://news.google.com/rss/search?q=박스오피스+OR+한국+영화+OR+극장+흥행&hl=ko&gl=KR&ceid=KR:ko", "category": "Film/Cinema", "lang": "ko"},
    {"name": "GNews Music KR", "url": "https://news.google.com/rss/search?q=케이팝+OR+음악+산업+OR+음원+차트&hl=ko&gl=KR&ceid=KR:ko", "category": "Music/Audio", "lang": "ko"},
    {"name": "GNews Gaming KR", "url": "https://news.google.com/rss/search?q=게임+산업+OR+e스포츠+OR+모바일게임&hl=ko&gl=KR&ceid=KR:ko", "category": "Gaming/Esports", "lang": "ko"},
    {"name": "GNews Media Biz KR", "url": "https://news.google.com/rss/search?q=미디어+산업+OR+콘텐츠+산업+OR+광고+시장&hl=ko&gl=KR&ceid=KR:ko", "category": "Media Business", "lang": "ko"},
]

# 한국 전문지 RSS
KOREAN_MEDIA_FEEDS = [
    {"name": "전자신문 방송/미디어", "url": "https://rss.etnews.com/Section901.xml", "category": "Media Business", "lang": "ko"},
    {"name": "디지털데일리", "url": "https://www.ddaily.co.kr/rss/S1010.xml", "category": "Media Business", "lang": "ko"},
    {"name": "ZDNet Korea", "url": "https://zdnet.co.kr/xml/rss.xml", "category": "Media Business", "lang": "ko"},
]


# ════════════════════════════════════════
# DATABASE
# ════════════════════════════════════════
def get_db():
    return psycopg2.connect(**DB_CONFIG)


def get_category_id(conn, cat_name):
    slug = CAT_SLUG_MAP.get(cat_name, cat_name.lower().replace('/', '_').replace(' ', '_'))
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM categories WHERE slug = %s", (slug,))
        row = cur.fetchone()
        return row[0] if row else None


def ensure_feed_source(conn, name, source_type, feed_url, category, lang):
    cat_id = get_category_id(conn, category)
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM feed_sources WHERE name = %s", (name,))
        row = cur.fetchone()
        if row:
            return row[0]
        cur.execute(
            "INSERT INTO feed_sources (name, source_type, feed_url, category_id, language) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (name, source_type, feed_url, cat_id, lang)
        )
        conn.commit()
        return cur.fetchone()[0]


def insert_article(conn, article, source_id, log_id):
    cat_id = get_category_id(conn, article.get('category', ''))
    published = article.get('published_at')
    if isinstance(published, str):
        try:
            published = datetime.fromisoformat(published.replace('Z', '+00:00'))
        except:
            published = None

    with conn.cursor() as cur:
        try:
            cur.execute("""
                INSERT INTO articles (url, title, source_domain, source_name, language, country, category_id,
                    tone, image_url, published_at, gdelt_seendate, feed_source_id, fetch_log_id, extra_json)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING
                RETURNING id
            """, (
                article['url'], article['title'], article.get('domain', ''),
                article.get('source_name', ''), article.get('language', 'English'),
                article.get('country', ''), cat_id, article.get('tone'),
                article.get('image', ''), published, article.get('seendate', ''),
                source_id, log_id, json.dumps(article.get('extra', {}), ensure_ascii=False)
            ))
            row = cur.fetchone()
            return row[0] if row else None
        except Exception as e:
            conn.rollback()
            return None


def start_fetch_log(conn, source_id):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO fetch_logs (source_id) VALUES (%s) RETURNING id", (source_id,))
        conn.commit()
        return cur.fetchone()[0]


def finish_fetch_log(conn, log_id, found, new, failed, status='success', error=None):
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE fetch_logs SET finished_at=now(), status=%s, articles_found=%s,
                articles_new=%s, articles_failed=%s, error_message=%s
            WHERE id=%s
        """, (status, found, new, failed, error, log_id))
        conn.commit()


# ════════════════════════════════════════
# GDELT COLLECTOR
# ════════════════════════════════════════
def collect_gdelt(conn, timespan='168h', max_records=250, rate_limit=6):
    categories = CFG.get('categories', {})
    total_new = 0

    for cat_name, info in categories.items():
        source_id = ensure_feed_source(conn, f"GDELT-{cat_name}", 'gdelt', None, cat_name, 'en')
        log_id = start_fetch_log(conn, source_id)
        found, new, failed = 0, 0, 0

        for q in info.get('queries', []):
            try:
                r = requests.get(GDELT_API, params={
                    "query": q, "mode": "artlist", "maxrecords": max_records,
                    "format": "json", "timespan": timespan, "sort": "DateDesc"
                }, timeout=30)
                if r.status_code == 200 and r.text.strip() and r.text.strip()[0] != '<':
                    articles = r.json().get("articles", [])
                    for a in articles:
                        found += 1
                        aid = insert_article(conn, {
                            'url': a.get('url', ''),
                            'title': a.get('title', '').strip(),
                            'domain': a.get('domain', ''),
                            'language': a.get('language', 'English'),
                            'country': a.get('sourcecountry', ''),
                            'category': cat_name,
                            'image': a.get('socialimage', ''),
                            'seendate': a.get('seendate', ''),
                            'tone': None,
                        }, source_id, log_id)
                        if aid:
                            new += 1
                    conn.commit()
            except Exception as e:
                failed += 1
            time.sleep(rate_limit)

        finish_fetch_log(conn, log_id, found, new, failed)
        print(f"  GDELT {cat_name:25s}: {found:4d} found, {new:4d} new")
        total_new += new

    return total_new


# ════════════════════════════════════════
# RSS COLLECTOR (Google News + 한국 전문지)
# ════════════════════════════════════════
def collect_rss(conn, feeds, source_type='rss'):
    total_new = 0

    for feed_info in feeds:
        name = feed_info['name']
        url = feed_info['url']
        cat = feed_info['category']
        lang = feed_info.get('lang', 'en')

        source_id = ensure_feed_source(conn, name, source_type, url, cat, lang)
        log_id = start_fetch_log(conn, source_id)
        found, new, failed = 0, 0, 0

        try:
            parsed = feedparser.parse(url)
            for entry in parsed.entries[:100]:
                found += 1
                link = entry.get('link', '')
                title = entry.get('title', '').strip()
                if not link or not title:
                    continue

                # Extract domain
                from urllib.parse import urlparse
                domain = urlparse(link).netloc.replace('www.', '')

                # Parse date
                published = None
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    try:
                        published = datetime(*entry.published_parsed[:6])
                    except:
                        pass

                aid = insert_article(conn, {
                    'url': link,
                    'title': title,
                    'domain': domain,
                    'source_name': name,
                    'language': 'Korean' if lang == 'ko' else 'English',
                    'country': 'KR' if lang == 'ko' else 'US',
                    'category': cat,
                    'image': '',
                    'published_at': published.isoformat() if published else None,
                }, source_id, log_id)
                if aid:
                    new += 1

            conn.commit()
            finish_fetch_log(conn, log_id, found, new, failed)

        except Exception as e:
            failed = found
            finish_fetch_log(conn, log_id, found, new, failed, 'failed', str(e))

        print(f"  RSS {name:35s}: {found:4d} found, {new:4d} new")
        total_new += new
        time.sleep(1)

    return total_new


# ════════════════════════════════════════
# CLUSTERING
# ════════════════════════════════════════
def cluster_articles(conn, days=7, threshold=0.55):
    """최근 N일 기사를 클러스터링하고 story_clusters에 저장"""
    cutoff = datetime.now() - timedelta(days=days)

    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("""
            SELECT a.id, a.title, a.url, a.source_domain, a.country, a.language,
                   a.category_id, a.image_url, a.published_at, c.name_en as category
            FROM articles a
            LEFT JOIN categories c ON c.id = a.category_id
            WHERE a.collected_at >= %s
            ORDER BY a.published_at DESC NULLS LAST
        """, (cutoff,))
        articles = cur.fetchall()

    if len(articles) < 2:
        print(f"  Not enough articles for clustering ({len(articles)})")
        return 0

    titles = [a['title'] for a in articles]

    try:
        vec = TfidfVectorizer(max_features=3000, stop_words='english', ngram_range=(1, 2), min_df=1, max_df=0.95)
        tfidf = vec.fit_transform(titles)
        norms = np.array(tfidf.power(2).sum(axis=1)).flatten()
        nz = norms > 0
        if nz.sum() < 2:
            return 0

        nz_idx = np.where(nz)[0]
        model = AgglomerativeClustering(n_clusters=None, distance_threshold=threshold, metric='cosine', linkage='average')
        labels = model.fit_predict(tfidf[nz].toarray())

        groups = {}
        for j, lb in enumerate(labels):
            groups.setdefault(lb, []).append(nz_idx[j])
        for j in np.where(~nz)[0]:
            groups.setdefault(max(groups.keys()) + 1 if groups else 0, []).append(j)

    except Exception as e:
        print(f"  Clustering error: {e}")
        return 0

    # Save clusters to DB
    cluster_count = 0
    today = datetime.now().date()

    with conn.cursor() as cur:
        # Clear today's clusters
        cur.execute("DELETE FROM story_clusters WHERE cluster_date = %s", (today,))

        for label, idxs in sorted(groups.items(), key=lambda x: -len(x[1])):
            cluster_arts = [articles[i] for i in idxs]
            n = len(cluster_arts)
            if n < 2:
                continue

            headline_art = max(cluster_arts[:5], key=lambda a: len(a['title']))
            cats = Counter(a['category'] for a in cluster_arts if a.get('category'))
            countries = Counter(a['country'] for a in cluster_arts if a.get('country'))
            primary_cat = cats.most_common(1)[0][0] if cats else 'Other'
            cat_id = get_category_id(conn, primary_cat)

            cur.execute("""
                INSERT INTO story_clusters (cluster_date, headline, headline_url, primary_category_id,
                    article_count, score, countries, domains, image_url)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
            """, (
                today, headline_art['title'], headline_art['url'], cat_id, n,
                round(n ** 0.6, 2),
                json.dumps(dict(countries.most_common(5)), ensure_ascii=False),
                json.dumps(dict(Counter(a['source_domain'] for a in cluster_arts).most_common(8)), ensure_ascii=False),
                headline_art.get('image_url', '')
            ))
            cluster_id = cur.fetchone()[0]

            # Link articles to cluster
            for i, a in enumerate(cluster_arts):
                cur.execute("""
                    INSERT INTO cluster_articles (cluster_id, article_id, is_headline)
                    VALUES (%s, %s, %s) ON CONFLICT DO NOTHING
                """, (cluster_id, a['id'], i == 0))

            cluster_count += 1

    conn.commit()
    print(f"  Clusters created: {cluster_count}")
    return cluster_count


# ════════════════════════════════════════
# EXPORT (latest.json 생성 for kimyonghee.com)
# ════════════════════════════════════════
def export_latest_json(conn, output_path):
    """PostgreSQL 데이터를 latest.json 형식으로 내보내기"""
    today = datetime.now().date()

    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        # Get clusters with articles
        cur.execute("""
            SELECT sc.*, c.name_en as primary_cat
            FROM story_clusters sc
            LEFT JOIN categories c ON c.id = sc.primary_category_id
            WHERE sc.cluster_date = %s
            ORDER BY sc.score DESC
        """, (today,))
        clusters = cur.fetchall()

        result_clusters = []
        for cl in clusters:
            cur.execute("""
                SELECT a.title, a.url, a.source_domain as domain, a.country as sourcecountry,
                       a.language, a.gdelt_seendate as seendate, a.image_url as socialimage,
                       c.name_en as category
                FROM cluster_articles ca
                JOIN articles a ON a.id = ca.article_id
                LEFT JOIN categories c ON c.id = a.category_id
                WHERE ca.cluster_id = %s
                ORDER BY ca.is_headline DESC, a.published_at DESC
            """, (cl['id'],))
            arts = cur.fetchall()

            result_clusters.append({
                "entity": cl.get('entity_name', ''),
                "headline": cl['headline'],
                "headline_url": cl.get('headline_url', ''),
                "synthesis_title": cl.get('synthesis_title', ''),
                "synthesis": cl.get('synthesis_body', ''),
                "key_points": cl.get('key_points', []),
                "image": cl.get('image_url', ''),
                "article_count": cl['article_count'],
                "score": float(cl.get('score', 0)),
                "primary_cat": cl.get('primary_cat', 'Other'),
                "hours_ago": float(cl.get('hours_ago', 0)) if cl.get('hours_ago') else 0,
                "countries": cl.get('countries', {}),
                "domains": cl.get('domains', {}),
                "articles": [dict(a) for a in arts],
            })

        # Category counts
        cur.execute("""
            SELECT c.name_en, COUNT(*) as cnt
            FROM articles a JOIN categories c ON c.id = a.category_id
            WHERE a.collected_at >= %s - INTERVAL '7 days'
            GROUP BY c.name_en ORDER BY cnt DESC
        """, (today,))
        cat_counts = {row['name_en']: row['cnt'] for row in cur.fetchall()}

        total = sum(cat_counts.values())

    # TMDb
    tmdb = {}
    if TMDB_TOKEN and TMDB_TOKEN != 'YOUR_TMDB_TOKEN_HERE':
        hdr = {"Authorization": f"Bearer {TMDB_TOKEN}", "accept": "application/json"}
        try:
            for ep, k in [("trending/movie/day", "movies"), ("trending/tv/day", "tv")]:
                r = requests.get(f"https://api.themoviedb.org/3/{ep}", headers=hdr, params={"language": TMDB_LANG}, timeout=15)
                tmdb[k] = r.json().get("results", [])[:12]
        except:
            pass

    data = {
        "timestamp": datetime.now().isoformat(),
        "issue_date": str(today),
        "clusters": result_clusters,
        "tmdb": tmdb,
        "cat_counts": cat_counts,
        "cat_colors": {
            "OTT/Streaming": "#e53935", "Film/Cinema": "#8e24aa",
            "Music/Audio": "#2e7d32", "Gaming/Esports": "#ef6c00",
            "K-Content": "#d81b60", "Media Business": "#1565c0",
            "Regulation": "#455a64",
        },
        "stats": {
            "total_articles": total,
            "total_clusters": len(result_clusters),
            "multi": len([c for c in result_clusters if c['article_count'] >= 2]),
        },
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)

    print(f"  Exported: {output_path} ({total} articles, {len(result_clusters)} clusters)")
    return data


# ════════════════════════════════════════
# MAIN
# ════════════════════════════════════════
def main():
    parser = argparse.ArgumentParser(description="MediaINT Multi-Source Collector")
    parser.add_argument("--source", choices=["all", "gdelt", "rss", "google_news"], default="all")
    parser.add_argument("--timespan", default="168h", help="GDELT timespan")
    parser.add_argument("--cluster", action="store_true", help="Run clustering after collection")
    parser.add_argument("--export", default="", help="Export latest.json path")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"MediaINT Collector — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Source: {args.source}, Timespan: {args.timespan}")
    print(f"{'='*60}")

    conn = get_db()
    total = 0

    if args.source in ('all', 'gdelt'):
        print(f"\n[GDELT] Collecting...")
        total += collect_gdelt(conn, timespan=args.timespan)

    if args.source in ('all', 'google_news', 'rss'):
        print(f"\n[Google News RSS] Collecting...")
        total += collect_rss(conn, GOOGLE_NEWS_FEEDS, 'google_news')

    if args.source in ('all', 'rss'):
        print(f"\n[Korean Media RSS] Collecting...")
        total += collect_rss(conn, KOREAN_MEDIA_FEEDS, 'rss')

    if args.cluster or args.source == 'all':
        print(f"\n[Clustering]...")
        cluster_articles(conn)

    if args.export:
        print(f"\n[Export]...")
        export_latest_json(conn, args.export)

    # Stats
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM articles")
        total_db = cur.fetchone()[0]

    print(f"\n{'='*60}")
    print(f"Done! New articles: {total}, Total in DB: {total_db}")
    print(f"{'='*60}")

    conn.close()


if __name__ == "__main__":
    main()

-- ═══════════════════════════════════════════════════════════════
-- MediaINT Database Schema
-- PostgreSQL 17+ / UTF-8
-- 생성: CREATE DATABASE mediaint_db ENCODING 'UTF8';
-- ═══════════════════════════════════════════════════════════════

CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS dblink;

-- 1. 카테고리 마스터
CREATE TABLE categories (
    id          BIGSERIAL PRIMARY KEY,
    slug        TEXT NOT NULL UNIQUE,
    name_en     TEXT NOT NULL,
    name_ko     TEXT,
    color       TEXT DEFAULT '#666666',
    sort_order  INTEGER DEFAULT 0,
    created_at  TIMESTAMPTZ DEFAULT now()
);

INSERT INTO categories (slug, name_en, name_ko, color, sort_order) VALUES
    ('ott_streaming',  'OTT/Streaming',   'OTT/스트리밍',    '#e53935', 1),
    ('film_cinema',    'Film/Cinema',      '영화/극장',       '#8e24aa', 2),
    ('music_audio',    'Music/Audio',      '음악/오디오',     '#2e7d32', 3),
    ('gaming_esports', 'Gaming/Esports',   '게임/e스포츠',    '#ef6c00', 4),
    ('k_content',      'K-Content',        'K-콘텐츠',       '#d81b60', 5),
    ('media_business', 'Media Business',   '미디어 비즈니스',  '#1565c0', 6),
    ('regulation',     'Regulation',       '규제/정책',       '#455a64', 7);

-- 2. 수집 소스 관리
CREATE TABLE feed_sources (
    id          BIGSERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    source_type TEXT NOT NULL CHECK (source_type IN ('gdelt', 'rss', 'google_news', 'manual')),
    feed_url    TEXT,
    category_id BIGINT REFERENCES categories(id),
    language    TEXT DEFAULT 'en',
    country     TEXT DEFAULT 'US',
    is_active   BOOLEAN DEFAULT true,
    fetch_interval_min INTEGER DEFAULT 360,
    config_json JSONB,
    created_at  TIMESTAMPTZ DEFAULT now(),
    updated_at  TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_feed_sources_active ON feed_sources (is_active) WHERE is_active = true;

CREATE TABLE fetch_logs (
    id          BIGSERIAL PRIMARY KEY,
    source_id   BIGINT NOT NULL REFERENCES feed_sources(id),
    started_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    finished_at TIMESTAMPTZ,
    status      TEXT NOT NULL DEFAULT 'running' CHECK (status IN ('running', 'success', 'partial', 'failed')),
    articles_found   INTEGER DEFAULT 0,
    articles_new     INTEGER DEFAULT 0,
    articles_failed  INTEGER DEFAULT 0,
    error_message    TEXT,
    metadata_json    JSONB
);

CREATE INDEX idx_fetch_logs_source ON fetch_logs (source_id, started_at DESC);
CREATE INDEX idx_fetch_logs_status ON fetch_logs (status) WHERE status = 'failed';

-- 3. 뉴스 기사 (연구용 아카이브)
CREATE TABLE articles (
    id              BIGSERIAL PRIMARY KEY,
    url             TEXT NOT NULL UNIQUE,
    url_hash        TEXT GENERATED ALWAYS AS (md5(url)) STORED,
    title           TEXT NOT NULL,
    title_ko        TEXT,
    source_domain   TEXT NOT NULL,
    source_name     TEXT,
    language        TEXT DEFAULT 'English',
    country         TEXT,
    category_id     BIGINT REFERENCES categories(id),
    tone            REAL,
    image_url       TEXT,
    published_at    TIMESTAMPTZ,
    collected_at    TIMESTAMPTZ DEFAULT now(),
    gdelt_seendate  TEXT,
    feed_source_id  BIGINT REFERENCES feed_sources(id),
    fetch_log_id    BIGINT REFERENCES fetch_logs(id),
    topic_tags      JSONB DEFAULT '[]'::jsonb,
    extra_json      JSONB,
    search_vector   TSVECTOR,
    created_at      TIMESTAMPTZ DEFAULT now()
);

CREATE UNIQUE INDEX idx_articles_url_hash    ON articles (url_hash);
CREATE INDEX idx_articles_category           ON articles (category_id, published_at DESC);
CREATE INDEX idx_articles_published          ON articles (published_at DESC);
CREATE INDEX idx_articles_collected          ON articles (collected_at DESC);
CREATE INDEX idx_articles_country            ON articles (country, published_at DESC);
CREATE INDEX idx_articles_language           ON articles (language);
CREATE INDEX idx_articles_domain             ON articles (source_domain);
CREATE INDEX idx_articles_tone               ON articles (tone) WHERE tone IS NOT NULL;
CREATE INDEX idx_articles_topic_tags         ON articles USING GIN (topic_tags);
CREATE INDEX idx_articles_search             ON articles USING GIN (search_vector);

CREATE OR REPLACE FUNCTION articles_search_vector_update() RETURNS trigger AS $$
BEGIN
    NEW.search_vector :=
        setweight(to_tsvector('simple', coalesce(NEW.title, '')), 'A') ||
        setweight(to_tsvector('simple', coalesce(NEW.title_ko, '')), 'A') ||
        setweight(to_tsvector('simple', coalesce(NEW.source_domain, '')), 'B');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_articles_search_vector
    BEFORE INSERT OR UPDATE OF title, title_ko, source_domain
    ON articles FOR EACH ROW
    EXECUTE FUNCTION articles_search_vector_update();

-- 4. 기사 클러스터링
CREATE TABLE story_clusters (
    id              BIGSERIAL PRIMARY KEY,
    cluster_date    DATE NOT NULL DEFAULT CURRENT_DATE,
    entity_name     TEXT,
    headline        TEXT NOT NULL,
    headline_url    TEXT,
    primary_category_id BIGINT REFERENCES categories(id),
    article_count   INTEGER DEFAULT 0,
    score           REAL DEFAULT 0,
    hours_ago       REAL,
    countries       JSONB DEFAULT '{}'::jsonb,
    domains         JSONB DEFAULT '{}'::jsonb,
    synthesis_title TEXT,
    synthesis_body  TEXT,
    key_points      JSONB DEFAULT '[]'::jsonb,
    image_url       TEXT,
    created_at      TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_clusters_date     ON story_clusters (cluster_date DESC, score DESC);
CREATE INDEX idx_clusters_entity   ON story_clusters (entity_name) WHERE entity_name IS NOT NULL;
CREATE INDEX idx_clusters_category ON story_clusters (primary_category_id);

CREATE TABLE cluster_articles (
    cluster_id  BIGINT NOT NULL REFERENCES story_clusters(id) ON DELETE CASCADE,
    article_id  BIGINT NOT NULL REFERENCES articles(id) ON DELETE CASCADE,
    is_headline BOOLEAN DEFAULT false,
    added_at    TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (cluster_id, article_id)
);

CREATE INDEX idx_cluster_articles_article ON cluster_articles (article_id);

-- 5. 주간 큐레이션
CREATE TABLE weekly_reports (
    id              BIGSERIAL PRIMARY KEY,
    year_week       TEXT NOT NULL UNIQUE,
    title           TEXT,
    intro_text      TEXT,
    published_at    TIMESTAMPTZ,
    status          TEXT DEFAULT 'draft' CHECK (status IN ('draft', 'published', 'archived')),
    cover_image_url TEXT,
    metadata_json   JSONB,
    created_at      TIMESTAMPTZ DEFAULT now(),
    updated_at      TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE curated_stories (
    id              BIGSERIAL PRIMARY KEY,
    report_id       BIGINT NOT NULL REFERENCES weekly_reports(id) ON DELETE CASCADE,
    sort_order      INTEGER DEFAULT 0,
    title           TEXT NOT NULL,
    body            TEXT NOT NULL,
    key_points      JSONB DEFAULT '[]'::jsonb,
    category_id     BIGINT REFERENCES categories(id),
    source_summary  TEXT,
    image_url       TEXT,
    cluster_id      BIGINT REFERENCES story_clusters(id),
    created_at      TIMESTAMPTZ DEFAULT now(),
    updated_at      TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_curated_stories_report ON curated_stories (report_id, sort_order);

CREATE TABLE curated_story_articles (
    story_id    BIGINT NOT NULL REFERENCES curated_stories(id) ON DELETE CASCADE,
    article_id  BIGINT NOT NULL REFERENCES articles(id) ON DELETE CASCADE,
    quote_text  TEXT,
    PRIMARY KEY (story_id, article_id)
);

-- 6. 정책 트래커
CREATE TABLE policy_issues (
    id              BIGSERIAL PRIMARY KEY,
    title           TEXT NOT NULL,
    title_en        TEXT,
    country         TEXT NOT NULL,
    description     TEXT,
    current_stage   TEXT DEFAULT 'proposed'
                        CHECK (current_stage IN ('proposed','discussion','passed','enacted','amended','withdrawn')),
    impact_sectors  JSONB DEFAULT '[]'::jsonb,
    key_entities    JSONB DEFAULT '[]'::jsonb,
    importance      TEXT DEFAULT 'medium' CHECK (importance IN ('low','medium','high','critical')),
    source_url      TEXT,
    created_at      TIMESTAMPTZ DEFAULT now(),
    updated_at      TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_policy_country    ON policy_issues (country);
CREATE INDEX idx_policy_stage      ON policy_issues (current_stage);
CREATE INDEX idx_policy_sectors    ON policy_issues USING GIN (impact_sectors);

CREATE TABLE policy_timeline (
    id          BIGSERIAL PRIMARY KEY,
    policy_id   BIGINT NOT NULL REFERENCES policy_issues(id) ON DELETE CASCADE,
    stage       TEXT NOT NULL,
    event_date  DATE NOT NULL,
    description TEXT,
    source_url  TEXT,
    created_at  TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_policy_timeline ON policy_timeline (policy_id, event_date DESC);

CREATE TABLE policy_articles (
    policy_id   BIGINT NOT NULL REFERENCES policy_issues(id) ON DELETE CASCADE,
    article_id  BIGINT NOT NULL REFERENCES articles(id) ON DELETE CASCADE,
    relevance   TEXT DEFAULT 'related' CHECK (relevance IN ('primary','related','background')),
    added_at    TIMESTAMPTZ DEFAULT now(),
    PRIMARY KEY (policy_id, article_id)
);

-- 7. 구독자 관리
CREATE TABLE subscribers (
    id              BIGSERIAL PRIMARY KEY,
    email           TEXT NOT NULL UNIQUE,
    name            TEXT,
    organization    TEXT,
    subscribed_at   TIMESTAMPTZ DEFAULT now(),
    status          TEXT DEFAULT 'active' CHECK (status IN ('active','paused','unsubscribed','bounced')),
    interest_categories JSONB DEFAULT '[]'::jsonb,
    source          TEXT,
    notes           TEXT,
    unsubscribed_at TIMESTAMPTZ,
    created_at      TIMESTAMPTZ DEFAULT now(),
    updated_at      TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_subscribers_status ON subscribers (status) WHERE status = 'active';

CREATE TABLE send_logs (
    id              BIGSERIAL PRIMARY KEY,
    report_id       BIGINT REFERENCES weekly_reports(id),
    subject         TEXT NOT NULL,
    sent_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
    total_recipients INTEGER DEFAULT 0,
    successful      INTEGER DEFAULT 0,
    failed          INTEGER DEFAULT 0,
    metadata_json   JSONB
);

CREATE TABLE send_recipients (
    id          BIGSERIAL PRIMARY KEY,
    send_log_id BIGINT NOT NULL REFERENCES send_logs(id) ON DELETE CASCADE,
    subscriber_id BIGINT NOT NULL REFERENCES subscribers(id),
    status      TEXT DEFAULT 'sent' CHECK (status IN ('sent','delivered','opened','clicked','bounced','failed')),
    opened_at   TIMESTAMPTZ,
    clicked_at  TIMESTAMPTZ,
    error_message TEXT
);

-- 8. JournalINT 교차 참조
CREATE TABLE journalint_crossref (
    id                  BIGSERIAL PRIMARY KEY,
    article_id          BIGINT REFERENCES articles(id) ON DELETE CASCADE,
    cluster_id          BIGINT REFERENCES story_clusters(id) ON DELETE CASCADE,
    curated_story_id    BIGINT REFERENCES curated_stories(id) ON DELETE CASCADE,
    research_item_id    BIGINT NOT NULL,
    journal_id          BIGINT,
    paper_title         TEXT,
    paper_doi           TEXT,
    match_type          TEXT DEFAULT 'auto' CHECK (match_type IN ('auto','manual','ai_suggested')),
    matched_tags        JSONB DEFAULT '[]'::jsonb,
    relevance_score     REAL DEFAULT 0.0,
    notes               TEXT,
    created_at          TIMESTAMPTZ DEFAULT now(),
    CHECK (article_id IS NOT NULL OR cluster_id IS NOT NULL OR curated_story_id IS NOT NULL)
);

CREATE INDEX idx_crossref_article  ON journalint_crossref (article_id) WHERE article_id IS NOT NULL;
CREATE INDEX idx_crossref_research ON journalint_crossref (research_item_id);
CREATE INDEX idx_crossref_tags     ON journalint_crossref USING GIN (matched_tags);

-- 9. 연구용 분석 뷰
CREATE VIEW v_daily_category_counts AS
SELECT DATE(published_at) AS pub_date, c.slug, c.name_en, COUNT(*) AS article_count, ROUND(AVG(a.tone)::numeric, 2) AS avg_tone
FROM articles a JOIN categories c ON c.id = a.category_id
WHERE a.published_at IS NOT NULL
GROUP BY DATE(published_at), c.slug, c.name_en ORDER BY pub_date DESC, article_count DESC;

CREATE VIEW v_weekly_tone_trend AS
SELECT TO_CHAR(DATE_TRUNC('week', published_at), 'IYYY-"W"IW') AS year_week, c.name_en, COUNT(*) AS article_count, ROUND(AVG(a.tone)::numeric, 2) AS avg_tone
FROM articles a JOIN categories c ON c.id = a.category_id
WHERE a.tone IS NOT NULL AND a.published_at IS NOT NULL
GROUP BY year_week, c.name_en ORDER BY year_week DESC;

CREATE VIEW v_source_rankings AS
SELECT source_domain, source_name, language, COUNT(*) AS total_articles, COUNT(DISTINCT category_id) AS category_spread, MIN(published_at) AS first_seen, MAX(published_at) AS last_seen
FROM articles GROUP BY source_domain, source_name, language ORDER BY total_articles DESC;

-- 10. updated_at 자동 갱신
CREATE OR REPLACE FUNCTION fn_set_updated_at() RETURNS trigger AS $$
BEGIN NEW.updated_at = now(); RETURN NEW; END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_feed_sources_updated   BEFORE UPDATE ON feed_sources   FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();
CREATE TRIGGER trg_weekly_reports_updated  BEFORE UPDATE ON weekly_reports  FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();
CREATE TRIGGER trg_curated_stories_updated BEFORE UPDATE ON curated_stories FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();
CREATE TRIGGER trg_policy_issues_updated   BEFORE UPDATE ON policy_issues   FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();
CREATE TRIGGER trg_subscribers_updated     BEFORE UPDATE ON subscribers     FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();

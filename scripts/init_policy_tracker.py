"""
정책 트래커 초기 데이터 입력
Usage: python init_policy_tracker.py
"""
import os, json
import psycopg2

DB_CONFIG = {
    'host': os.environ.get('PG_HOST', 'localhost'),
    'port': int(os.environ.get('PG_PORT', 5432)),
    'dbname': os.environ.get('PG_DATABASE', 'mediaint_db'),
    'user': os.environ.get('PG_USER', 'postgres'),
    'password': os.environ.get('PG_PASSWORD', ''),
}

POLICIES = [
    {
        "title": "통합미디어법",
        "title_en": "Integrated Media Act",
        "country": "KR",
        "description": "방송·OTT·유튜브를 '시청각미디어서비스'로 통합하는 미디어법. 넷플릭스·유튜브 등 제2유형에 신고제 적용, 광고 규제 네거티브 방식 전환.",
        "current_stage": "discussion",
        "impact_sectors": ["OTT", "Broadcasting", "YouTube", "Advertising"],
        "key_entities": ["방송미디어통신위원회", "과학기술정보방송통신위원회"],
        "importance": "high",
        "timeline": [
            {"date": "2026-01-26", "stage": "discussion", "description": "국회 논의 본격화"},
            {"date": "2026-02-02", "stage": "discussion", "description": "광고 규제 네거티브 전환 방향 발표"},
            {"date": "2026-02-19", "stage": "discussion", "description": "OTT '필요·최소 규율' 쟁점 보도"},
        ]
    },
    {
        "title": "캐나다 온라인 스트리밍법 (C-11)",
        "title_en": "Canada Online Streaming Act (Bill C-11)",
        "country": "CA",
        "description": "해외 스트리밍 사업자에 캐나다 수익의 5% 콘텐츠 펀드 기여 의무화. 미국 공화당이 USTR 조사 법안 발의.",
        "current_stage": "enacted",
        "impact_sectors": ["OTT", "Content Quota", "Trade"],
        "key_entities": ["CRTC", "USTR", "CUSMA"],
        "importance": "critical",
        "timeline": [
            {"date": "2023-04-27", "stage": "passed", "description": "캐나다 의회 C-11 법안 통과"},
            {"date": "2026-03-20", "stage": "enacted", "description": "미 공화당 의원, C-11 USTR 조사 법안 발의"},
            {"date": "2026-03-23", "stage": "enacted", "description": "ITIF, 의회 조사 정당성 분석 발표"},
        ]
    },
    {
        "title": "EU 시청각미디어서비스지침 (AVMSD) 개정",
        "title_en": "EU AVMSD Review 2026",
        "country": "EU",
        "description": "유럽위원회가 AVMSD 사후평가 증거 수집 착수. 유럽 콘텐츠 쿼터 30%, 아동 프라이버시, AI 콘텐츠 규제 핵심 의제.",
        "current_stage": "discussion",
        "impact_sectors": ["OTT", "Content Quota", "AI", "Child Safety"],
        "key_entities": ["European Commission", "DG CNECT"],
        "importance": "high",
        "timeline": [
            {"date": "2025-12-01", "stage": "proposed", "description": "유럽위원회 증거 수집 공식 착수"},
            {"date": "2026-12-19", "stage": "discussion", "description": "평가 보고서 제출 기한 (예정)"},
        ]
    },
    {
        "title": "인도 OTT 규제 강화",
        "title_en": "India OTT Content Regulation",
        "country": "IN",
        "description": "의회 상임위가 OTT 10~15개 플랫폼 불법/선정적 콘텐츠 조사 착수. 5개 플랫폼 이미 차단.",
        "current_stage": "discussion",
        "impact_sectors": ["OTT", "Content Regulation"],
        "key_entities": ["MIB", "IT Act 2021", "Parliamentary Standing Committee"],
        "importance": "medium",
        "timeline": [
            {"date": "2026-02-15", "stage": "discussion", "description": "5개 OTT 플랫폼 IT법 위반 차단"},
            {"date": "2026-03-15", "stage": "discussion", "description": "상임위 10~15개 플랫폼 조사 착수"},
        ]
    },
    {
        "title": "Disney ESPN 번들링 반독점 합의",
        "title_en": "Disney ESPN Bundling Antitrust Settlement",
        "country": "US",
        "description": "디즈니가 ESPN 포함 고가 패키지를 유통사에 강제한 번들링 정책에 대한 반독점 소송 잠정 합의.",
        "current_stage": "passed",
        "impact_sectors": ["OTT", "Sports Broadcasting", "Antitrust"],
        "key_entities": ["Disney", "ESPN", "YouTube TV", "DIRECTV"],
        "importance": "medium",
        "timeline": [
            {"date": "2026-03-05", "stage": "passed", "description": "디즈니 반독점 잠정 합의"},
        ]
    },
    {
        "title": "파라마운트-WBD 합병 반독점 심사",
        "title_en": "Paramount-WBD Merger Antitrust Review",
        "country": "US",
        "description": "파라마운트 스카이댄스의 WBD $1,100억 인수. HBO Max+Paramount+ 통합. 4월 주주투표 후 Q3 완료 목표.",
        "current_stage": "discussion",
        "impact_sectors": ["OTT", "Film", "Antitrust", "M&A"],
        "key_entities": ["Paramount", "WBD", "FTC", "DOJ"],
        "importance": "critical",
        "timeline": [
            {"date": "2025-12-08", "stage": "proposed", "description": "파라마운트 스카이댄스 역제안"},
            {"date": "2026-02-26", "stage": "discussion", "description": "WBD 이사회, 파라마운트 제안 수락"},
            {"date": "2026-02-27", "stage": "discussion", "description": "합병 계약 공식 발표"},
        ]
    },
]


def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    for p in POLICIES:
        cur.execute("""
            INSERT INTO policy_issues (title, title_en, country, description, current_stage,
                impact_sectors, key_entities, importance)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
            RETURNING id
        """, (
            p['title'], p['title_en'], p['country'], p['description'],
            p['current_stage'],
            json.dumps(p['impact_sectors'], ensure_ascii=False),
            json.dumps(p['key_entities'], ensure_ascii=False),
            p['importance'],
        ))
        row = cur.fetchone()
        if row:
            policy_id = row[0]
            for t in p.get('timeline', []):
                cur.execute("""
                    INSERT INTO policy_timeline (policy_id, stage, event_date, description)
                    VALUES (%s, %s, %s, %s)
                """, (policy_id, t['stage'], t['date'], t['description']))
            print(f"  Added: {p['title']} ({len(p.get('timeline', []))} events)")
        else:
            print(f"  Skipped (exists): {p['title']}")

    conn.commit()
    cur.close()
    conn.close()
    print(f"\nDone! {len(POLICIES)} policies processed.")


if __name__ == "__main__":
    main()

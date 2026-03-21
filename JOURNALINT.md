# JournalINT 운영 가이드

## 개요

JournalINT는 95개 학술 저널를 모니터링하는 인텔리전스 대시보드입니다.
에이전트(Claude)가 주간 단위로 sweep하여 콘텐츠를 생성합니다.

- **페이지**: `/journalint` (최신호), `/journalint/{issue}` (아카이브)
- **데이터**: `public/data/journalint/latest.json` + `archive/*.json`
- **DB**: `D:\sunmoon_2026\manage` PostgreSQL papers_db

---

## 주간 업데이트 절차

### 1. 데이터 수집 (Claude Agent)

에이전트에게 다음을 요청:

```
JournalINT 2026-W{N} 이슈를 만들어줘.
- 95개 저널 중 주요 변동 사항 확인 (WebSearch)
- 새로운 CFP/SI 확인
- 주목 논문 1편 선정 (DB에서 고인용 + 관련성)
- top story 1건, featured 3-5건, spotlight 1건, briefs 5-8건
```

### 2. 데이터 파일 생성

에이전트가 `public/data/journalint/latest.json`을 생성합니다.

#### JSON 구조

```json
{
  "timestamp": "2026-04-04T09:00:00",
  "issue": "2026-W14",
  "issue_title": "2026년 4월 1주차",
  "stats": {
    "total_journals": 95,
    "total_papers": 64711,
    "papers_2026": 18254,
    "total_calls": 85,
    "grades": [
      { "grade": "A", "cnt": 58 },
      { "grade": "B", "cnt": 34 },
      { "grade": "C", "cnt": 3 }
    ]
  },
  "stories": [ ... ],
  "topTopics": [ ... ]
}
```

#### Story Types

| type | 용도 | 필수 필드 |
|------|------|-----------|
| `top` | TOP STORY (1건) | id, date, title, synthesis, key_points, sources, tags |
| `spotlight` | 주목 논문 (1건) | id, date, title, paper_title, journal, authors, year, citations, doi, synthesis, tags |
| `featured` | 주요 기사 (3-5건) | id, date, title, synthesis, key_points, sources, tags |
| `brief` | 헤드라인 (5-8건) | id, date, title, journal, grade, url |

#### 기사 작성 원칙

- **완결성**: 모든 기사는 잘리지 않고 끝까지 읽을 수 있어야 함
- **구체성**: 저널명, IF, 등급, 마감일, 에디터 이름 등 구체적 정보 포함
- **연구자 관점**: "연구자 시사점"을 반드시 포함
- **출처 링크**: 모든 source에 실제 URL 연결
- **한국어**: 기사 본문은 한국어로 작성

### 3. 아카이브 저장

```bash
# 현재 이슈를 아카이브에 복사
cp public/data/journalint/latest.json public/data/journalint/archive/2026-W{N}.json
```

### 4. 빌드 & 배포

```bash
cd D:/PROJECT_2025/kimyonghee-website
npx astro build
# 배포는 FTP 또는 스크립트로
```

---

## 파일 구조

```
public/data/journalint/
  latest.json              # 최신호 (항상 덮어씀)
  archive/
    2026-W12.json          # 3월 3주차
    2026-W13.json          # 3월 4주차
    2026-W14.json          # 4월 1주차
    ...

src/pages/journalint/
  index.astro              # /journalint — 최신호 렌더링
  [issue].astro            # /journalint/2026-W12 — 아카이브 렌더링
```

---

## 데이터 소스

| 소스 | 용도 | 접근 방법 |
|------|------|-----------|
| Papers DB (PostgreSQL) | 64,711편 논문, 95개 저널 메타데이터 | `lib/db.js` 또는 MCP `sql_query` |
| WebSearch | 저널 CFP, 에디터 변경, 뉴스 | Claude WebSearch 도구 |
| 저널 홈페이지 | scope, 투고 가이드라인 | Claude WebFetch (일부 403) |

---

## DB 테이블 참조

| 테이블 | 용도 |
|--------|------|
| `journal_rankings` | 저널 메타데이터 (95개, grade, IF, category) |
| `journal_details` | aims_scope, submission_url, publisher |
| `journal_research_items` | 64,711편 논문 (title, abstract, year, citations) |
| `journal_news_items` | 저널 뉴스 (에디터 교체, scope 변경 등) |
| `journal_calls` | CFP/SI 공모 (title, due_date, call_type) |
| `journal_curation_snapshots` | 저널별 트렌드 분석 스냅샷 |

---

## 메인 페이지 연동

`src/pages/index.astro`에서 `latest.json`의 top story와 spotlight을 읽어 표시합니다.
섹션명: "Journal Intelligence" — 영어로 표시.

---

## 주의사항

- `latest.json`을 교체할 때 반드시 이전 이슈를 `archive/`에 먼저 저장
- stats의 숫자는 DB에서 실시간 조회하여 업데이트 (`sql_query` 또는 `get_db_stats`)
- topTopics는 DB의 `topic_tags`에서 2025-2026 빈도순 집계
- 기사의 `id`는 `{날짜}-{slug}` 형식으로 고유하게

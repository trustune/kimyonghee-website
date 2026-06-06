---
title: "Korean Film Holdback Analysis: Maximizing Revenue Across Distribution Windows"
title_ko: "한국 영화 홀드백 분석: 유통 창구별 수익 극대화"
title_en: "Korean Film Holdback Analysis: Maximizing Revenue Across Distribution Windows"
subtitle: "An Empirical Analysis of 395 Films and 500 Audience Members Reveals the 6-Month Rule Has No Empirical Basis"
subtitle_ko: "영화 395편과 관객 500명을 실증 분석한 결과, 6개월 규칙에는 실증적 근거가 없다"
subtitle_en: "An Empirical Analysis of 395 Films and 500 Audience Members Reveals the 6-Month Rule Has No Empirical Basis"
date: "2026-02-27"
category: "Media Economics"
tags: ["Holdback", "Film Distribution", "OTT", "IPTV", "Window Strategy", "PSM", "KOFIC"]
keywords: ["Holdback", "Theatrical Window", "SVOD", "TVOD", "OTT Distribution", "Propensity Score Matching", "Stale Fruit Effect", "Film Revenue", "Korean Cinema", "Windowing Strategy", "Stakeholder Analysis"]
methodology: ["Propensity Score Matching (PSM)", "Permutation Importance (Random Forest)", "Bootstrap Confidence Intervals (1,000 iterations)", "Regression Discontinuity Design (RDD)", "Exponential Decay Model", "Stakeholder Salience Model (Mitchell et al., 1997)", "Survey Analysis (n=500)"]
data_period:
  start: "2021"
  end: "2024"
sample_size: 395
data_sources:
  - name: "KOBIS (Korean Box Office Information System)"
    type: "primary"
  - name: "SVOD Holdback Records (239 films)"
    type: "primary"
  - name: "IPTV Distribution Records (381 films)"
    type: "primary"
  - name: "FlixPatrol OTT Performance Data"
    type: "primary"
  - name: "Audience Survey (n=500, aged 14-59)"
    type: "primary"
  - name: "Expert Interviews (Dec 2025)"
    type: "secondary"
related_publications: []
related_projects: ["netflix-korea-economic-impact-2024"]
conference: ""
description: "KOFIC commissioned study analyzing holdback periods for 395 Korean films (2021-2024). PSM analysis shows holdback contributes less than 3% to box office revenue, while 82% of audiences complete viewing within 90 days. The conventional 6-month holdback has no empirical support."
description_ko: "영화진흥위원회 수탁 연구로, 영화 395편(2021~2024)의 홀드백 기간을 분석했다. 성향점수매칭 분석 결과 홀드백이 극장 매출에 기여하는 비중은 3% 미만이며, 관객의 82%는 개봉 90일 안에 관람을 마친다. 관행으로 굳어진 6개월 홀드백에는 실증적 근거가 없다."
description_en: "KOFIC commissioned study analyzing holdback periods for 395 Korean films (2021-2024). PSM analysis shows holdback contributes less than 3% to box office revenue, while 82% of audiences complete viewing within 90 days. The conventional 6-month holdback has no empirical support."
summary: "Using PSM, Bootstrap, and RDD methods on 395 films and 500 survey respondents, this study finds that film quality (93%) overwhelmingly determines box office performance, not holdback length (less than 3%). The optimal holdback window is 45-105 days depending on film scale, and the 6-month convention produces near-zero residual audience value. OTT viewers visit theaters more frequently than non-viewers, suggesting a complementary rather than substitutive relationship."
summary_ko: "영화 395편과 설문 응답자 500명을 대상으로 성향점수매칭, 부트스트랩, 회귀불연속설계를 적용한 결과, 극장 성과를 압도적으로 좌우하는 것은 작품의 완성도(93%)이며 홀드백 기간(3% 미만)이 아니었다. 최적 홀드백 기간은 영화 규모에 따라 45~105일이며, 관행적인 6개월은 잔여 관객 가치를 사실상 0에 가깝게 만든다. 온라인 동영상 서비스 이용자는 비이용자보다 극장을 더 자주 찾아, 두 매체가 대체재가 아니라 보완재 관계임을 시사한다."
summary_en: "Using PSM, Bootstrap, and RDD methods on 395 films and 500 survey respondents, this study finds that film quality (93%) overwhelmingly determines box office performance, not holdback length (less than 3%). The optimal holdback window is 45-105 days depending on film scale, and the 6-month convention produces near-zero residual audience value. OTT viewers visit theaters more frequently than non-viewers, suggesting a complementary rather than substitutive relationship."
key_findings:
  - "Holdback contributes less than 3% to box office revenue; film quality accounts for 93% (Random Forest)"
  - "PSM causal analysis: 90-day holdback ATE = +25,621 KRW, p = 0.912 (statistically insignificant)"
  - "82% of audiences complete viewing within 90 days of theatrical release"
  - "At 180 days (6 months), residual audience value drops to approximately 0%"
  - "Optimal holdback range: 45-105 days (blockbusters 90-120, mid-scale 30-60 days)"
  - "Stale Fruit Effect RDD test: No structural break at 180 days (t=1.15, p=0.253)"
  - "OTT users visit theaters 0.70 more times per year than non-users (complementary goods)"
  - "Only 6.2% of audiences skip theaters due to OTT availability"
  - "Audience spending ratio: 25.5% theater vs 74.5% OTT (3:1 OTT dominance)"
  - "77.4% of industry stakeholders believe consensus on holdback reform is achievable"
key_findings_ko:
  - "홀드백이 극장 매출에 기여하는 비중은 3% 미만이며, 작품 완성도가 93%를 설명한다(랜덤 포레스트)"
  - "성향점수매칭 인과 분석: 90일 홀드백 평균처치효과 = +25,621원, p = 0.912(통계적으로 유의하지 않음)"
  - "관객의 82%는 극장 개봉 후 90일 안에 관람을 마친다"
  - "180일(6개월) 시점에서 잔여 관객 가치는 약 0%로 떨어진다"
  - "최적 홀드백 구간: 45~105일(대작 90~120일, 중소 규모 30~60일)"
  - "신선도 저하 효과 회귀불연속 검정: 180일 지점에 구조적 단절 없음(t=1.15, p=0.253)"
  - "온라인 동영상 서비스 이용자는 비이용자보다 연간 0.70회 더 극장을 찾는다(보완재 관계)"
  - "온라인 동영상 서비스 때문에 극장 관람을 건너뛰는 관객은 6.2%에 불과하다"
  - "관객 지출 비율: 극장 25.5% 대 온라인 동영상 서비스 74.5%(3:1로 온라인 동영상 서비스 우세)"
  - "업계 이해관계자의 77.4%가 홀드백 개편에 대한 합의가 가능하다고 본다"
policy_proposals:
  - "Replace the conventional 6-month holdback with an evidence-based 45-105 day flexible window"
  - "Adopt differentiated holdback by film scale: blockbusters 90-120 days, mid-tier 60-90 days, small-scale 30-60 days"
  - "Establish an industry consensus framework involving theaters, distributors, OTT platforms, and producers"
  - "Shift the policy frame from 'theater vs OTT' zero-sum to 'theater + OTT' total revenue maximization"
  - "Monitor IPTV-SVOD cannibalization effects and coordinate cross-platform release timing"
policy_proposals_ko:
  - "관행적인 6개월 홀드백을 실증 근거에 기반한 45~105일 유연 창구로 대체한다"
  - "영화 규모별 차등 홀드백 도입: 대작 90~120일, 중급 60~90일, 소규모 30~60일"
  - "극장, 배급사, 온라인 동영상 서비스 사업자, 제작사가 참여하는 업계 합의 틀을 마련한다"
  - "'극장 대 온라인 동영상 서비스'의 제로섬 구도를 '극장 + 온라인 동영상 서비스'의 총수익 극대화로 전환한다"
  - "IPTV와 가입형 온라인 동영상 서비스 간 잠식 효과를 점검하고 매체별 출시 시점을 조율한다"
funding:
  agency: "Korean Film Council (KOFIC)"
featured: false
---

<div data-lang="ko">

전체 보고서(KOFIC Research 2025-14)는 [영화진흥위원회 누리집](https://www.kofic.or.kr/kofic/business/rsch/findPolicyDetail.do)에서 내려받을 수 있다.

## 연구 배경

극장 창구, 곧 영화의 극장 개봉과 이후 매체(IPTV, 온라인 동영상 서비스) 출시 사이의 홀드백 기간은 오랫동안 영화 유통 전략의 핵심이었다. 한국에서는 가입형 온라인 동영상 서비스 출시에 대한 관행적인 "6개월 규칙"이 업계 관례로 적용되어 왔지만, 그 실증적 근거가 체계적으로 검증된 적은 없었다.

코로나19 대유행으로 온라인 동영상 서비스 이용이 빠르게 확산되면서(2021년 66.3%에서 2024년 79%로 증가), 극장 상영과 디지털 유통 사이의 긴장은 더욱 깊어졌다. 영화진흥위원회 수탁으로 수행한 이 연구는 홀드백이 한국 영화 수익에 실제로 미치는 영향을 처음으로 종합 실증 분석한 것이다.

## 자료와 범위

| 구분 | 내용 |
|----------|--------|
| 분석 기간 | 2021~2024년(온라인 동영상 서비스 대중화 이후) |
| 분석 영화 | 395편(한국 246편, 외국 149편) |
| 가입형 온라인 동영상 서비스 홀드백 자료 | 239편 |
| IPTV 유통 자료 | 381편 |
| 온라인 동영상 서비스 성과 | 109~111편(FlixPatrol) |
| 관객 설문 | 응답자 500명(14~59세, 2025년 11월) |
| 전문가 면담 | 제작사, 배급사, 극장, 온라인 동영상 서비스 사업자(2025년 12월) |

## 주요 정량 분석 결과

### 1. 홀드백은 극장 매출을 지켜 주지 못한다

랜덤 포레스트 변수 중요도 분석 결과, **극장 매출 변동의 93%는 작품 완성도가 설명**하며, 홀드백 기간이 기여하는 비중은 3% 미만이다. 홀드백 90일을 기준으로 위아래로 나눈 영화들을 성향점수매칭으로 비교한 결과, 통계적으로 유의한 인과 효과는 나타나지 않았다.

| 지표 | 값 |
|--------|-------|
| 평균처치효과(ATE) | +25,621원 |
| p값 | 0.912 |
| 95% 신뢰구간 | 0을 포함 |
| 홀드백 변수 중요도 | 3% 미만 |
| 작품 완성도 중요도 | 93% |

### 2. 관객 소진: 95% 소진 시점

지수 감쇠 모형을 적용한 결과, 잠재 극장 관객은 빠르게 소진되는 것으로 나타났다.

| 영화 규모 | 95% 소진 시점(일) | 최적 홀드백 |
|------------|----------------------|------------------|
| 대작(100만 명 초과) | 30 | 90~120일 |
| 대형(50만~100만 명) | 22 | 60~90일 |
| 중형(10만~50만 명) | 22 | 45~90일 |
| 소형(10만 명 미만) | 22 | 30~60일 |

95% 소진 시점의 중앙값은 **22일**로, 전체 영화의 절반이 단 3주 만에 잠재 관객의 95%를 잃는다는 뜻이다.

### 3. 6개월 규칙에는 근거가 없다

- **한국 영화의 83.1%**는 이미 6개월 안에 가입형 온라인 동영상 서비스로 전환된다
- 한국 영화의 가입형 온라인 동영상 서비스 홀드백 중앙값: 105일(3.5개월)
- 외국 영화의 가입형 온라인 동영상 서비스 홀드백 중앙값: 181일(6개월)
- 180일 시점의 잔여 관객 가치: **약 0%**
- 180일 지점의 회귀불연속 신선도 저하 효과 검정: t=1.15, **p=0.253**(구조적 단절 없음)

### 4. 온라인 동영상 서비스와 극장은 대체재가 아니라 보완재다

| 지표 | 극장만 이용 | 온라인 동영상 서비스 이용 |
|--------|-------------|-----------|
| 연간 극장 방문 | 1.43 | 2.13(+0.70) |
| 극장 관람을 건너뛴 이유(온라인 동영상 서비스) | - | 6.2%에 불과 |
| 지출 비율 | 25.5% | 74.5% |

온라인 동영상 서비스를 많이 쓰는 이용자는 극장을 **더 자주** 찾는다. 온라인 동영상 서비스로 볼 수 있다는 이유로 극장 관람을 건너뛰었다고 답한 관객은 6.2%에 그쳤다.

### 5. IPTV와 가입형 온라인 동영상 서비스의 역학

| 매체 | 홀드백 중앙값 | 전환율(0~30일) |
|----------|----------------|---------------------------|
| IPTV | 35일(약 5주) | 27.6% |
| 가입형 온라인 동영상 서비스 | 105일(약 3.5개월) | 6.6%(120일 이후) |

IPTV는 가입형 온라인 동영상 서비스보다 약 70일 먼저 출시되며, 가입형 온라인 동영상 서비스 출시가 늦어질수록 전환율은 4.2배 낮아지는 것으로 측정됐다.

## 이해관계자 분석

Mitchell 외(1997)의 이해관계자 현저성 모형을 활용해, 권력(Power), 정당성(Legitimacy), 긴급성(Urgency)을 기준으로 업계 주체들을 분류했다.

| 이해관계자 | 유형 | 홀드백 선호 |
|------------|------|-------------------|
| 극장(CGV, 롯데, 메가박스) | 확정적(Definitive) | 긴 홀드백 |
| 온라인 동영상 서비스 사업자(넷플릭스, 티빙, 웨이브) | 지배적(Dominant) | 짧은 홀드백 |
| 제작사/배급사 | 의존적(Dependent) | 유연한 홀드백 |
| 관객 | 임의적(Discretionary) | 짧은 홀드백 |

핵심적인 구조 요인이 하나 있다. 한국의 상위 3개 수직계열화 대기업(CJ, 롯데 등)이 **배급의 86.1%**와 **극장 스크린의 95.3%**를 차지하고 있어, 같은 기업 안에서도 극장 부문과 온라인 동영상 서비스 부문 사이에 복잡한 내부 갈등이 발생한다.

## 국제 비교

| 국가 | 극장-건당 결제형 | 극장-가입형 | 작동 방식 |
|---------|----------------|-----------------|-----------|
| 프랑스 | 4개월 | 15~17개월 | 법령 규제 |
| 이탈리아 | - | 90일 | 공적 지원 조건 |
| 미국 | - | 45일 | 업계 합의(NATO) |
| 독일 | 4개월(주문형 비디오) | 12개월 | FFG 법령 |
| 일본 | - | 6~12개월 | 업계 관례 |
| 인도 | - | 8주(56일) | 극장업계 압박 |
| **한국** | **IPTV 약 35일** | **가입형 약 105일** | **업계 관례** |

## 설문 주요 결과(응답자 500명)

- **85.2%가 온라인 동영상 서비스를 이용**(30~39세에서 91%로 가장 높음)
- **82%가 개봉 후 90일 안에 극장 관람을 마침**
- 극장을 선호하는 주된 이유: 몰입감 있는 화면 경험(67.6%), 함께하는 경험(42.2%)
- **69.6%가 현행 극장 홀드백이 적절하다고 인식**
- **61.8%가 현행 온라인 동영상 서비스 홀드백이 너무 길다고 인식**
- 관객 10만 명 이상 영화의 홀드백을 단축할 경우: 관객 10% 감소 가능성 68.2%, 다만 50% 감소 가능성은 3.2%에 불과
- **이해관계자의 75.2%가 업계 합의가 가능하다고 봄**

## 게임이론 관점

이 연구는 홀드백 딜레마를 **죄수의 딜레마**로 본다. 개별 제작사는 홀드백을 줄이는 데서 이득을 얻지만, 모두가 함께 줄이면 극장 매출이 잠식될 수 있다. 그러나 실증 근거를 보면 우려하던 잠식은 미미한 수준(대체 효과 6.2%에 불과)이어서, 딜레마는 흔히 가정하는 것만큼 심각하지 않다.

개별 주체의 우월 전략은 홀드백을 줄이는 것이며, 이는 점점 짧은 창구로 수렴하는 내시 균형을 만든다. 다만 극장과 온라인 동영상 서비스가 보완 관계라는 점을 고려하면, 이 균형이 반드시 파괴적인 것은 아니라고 본다.

## 정책 시사점

1. **6개월 관행을 실증 근거에 기반한 유연 창구(45~105일)로 대체해야 한다**
2. **영화 규모별 차등화**가 획일적 홀드백보다 합리적이다
3. **극장과 온라인 동영상 서비스는 보완재**다. 정책은 한 채널을 보호하기보다 생태계 전체의 총수익을 극대화해야 한다
4. **업계 합의 장치**가 필요하며, 이해관계자의 75.2%가 합의에 열려 있다
5. **IPTV 시점 조율**이 중요하다. IPTV와 가입형 온라인 동영상 서비스 사이 70일 격차는 측정 가능한 가치 잠식을 낳는다

## 한계

- 자료는 2021~2024년을 다루며, 코로나19 이후 회복 국면의 영향이 남아 있다
- 온라인 동영상 서비스 수익 자료는 여전히 비공개이며 접근이 거의 불가능하다
- 성향점수매칭은 관측되지 않은 교란 요인을 완전히 통제하지 못한다
- "관람하지 않기로 한 관객"과 "다른 곳에서 관람한 관객"을 구분하려면 추가 연구가 필요하다
- 온라인 동영상 서비스 대중화 이후 자료가 4년에 그쳐, 더 긴 시계열이 확보되면 인과 주장을 한층 강화할 수 있다

</div>

<div data-lang="en">

The full report (KOFIC Research 2025-14) is available for download from the [Korean Film Council website](https://www.kofic.or.kr/kofic/business/rsch/findPolicyDetail.do).

## Research Background

The theatrical window -- the holdback period between a film's theatrical release and its availability on subsequent platforms (IPTV, OTT) -- has been a cornerstone of film distribution strategy. In Korea, a conventional "6-month rule" for SVOD release has been applied by industry practice, but its empirical basis has never been systematically tested.

Since the COVID-19 pandemic accelerated OTT adoption (from 66.3% in 2021 to 79% in 2024), the tension between theatrical exhibition and digital distribution has intensified. This KOFIC-commissioned study provides the first comprehensive empirical analysis of holdback's actual impact on Korean film revenue.

## Data and Scope

| Category | Detail |
|----------|--------|
| Analysis Period | 2021-2024 (post-OTT mainstream era) |
| Films Analyzed | 395 (Korean 246, Foreign 149) |
| SVOD Holdback Data | 239 films |
| IPTV Distribution Data | 381 films |
| OTT Performance | 109-111 films (FlixPatrol) |
| Audience Survey | 500 respondents (ages 14-59, Nov 2025) |
| Expert Interviews | Producers, distributors, exhibitors, OTT platforms (Dec 2025) |

## Key Quantitative Results

### 1. Holdback Does Not Protect Box Office Revenue

Random Forest feature importance analysis reveals that **film quality accounts for 93% of box office variation**, while holdback period contributes less than 3%. PSM analysis comparing films with holdback above and below 90 days shows no statistically significant causal effect:

| Metric | Value |
|--------|-------|
| ATE (Average Treatment Effect) | +25,621 KRW |
| p-value | 0.912 |
| 95% Confidence Interval | Includes zero |
| Holdback feature importance | < 3% |
| Film quality importance | 93% |

### 2. Audience Decay: The 95% Exhaustion Point

Using exponential decay modeling, the study finds that potential theatrical audiences are exhausted rapidly:

| Film Scale | 95% Exhaustion (days) | Optimal Holdback |
|------------|----------------------|------------------|
| Blockbuster (>1M admissions) | 30 | 90-120 days |
| Large (500K-1M) | 22 | 60-90 days |
| Medium (100K-500K) | 22 | 45-90 days |
| Small (<100K) | 22 | 30-60 days |

The median 95% exhaustion point is **22 days**, meaning half of all films lose 95% of their potential audience within just three weeks.

### 3. The 6-Month Rule Has No Basis

- **83.1% of Korean films** already transition to SVOD within 6 months
- Median Korean film SVOD holdback: 105 days (3.5 months)
- Median foreign film SVOD holdback: 181 days (6 months)
- At 180 days, residual audience value: **approximately 0%**
- RDD Stale Fruit Effect test at 180 days: t=1.15, **p=0.253** (no structural break)

### 4. OTT and Theaters Are Complements, Not Substitutes

| Metric | Theater-only | OTT Users |
|--------|-------------|-----------|
| Annual theater visits | 1.43 | 2.13 (+0.70) |
| Reason for skipping theater (OTT) | - | Only 6.2% |
| Spending ratio | 25.5% | 74.5% |

OTT heavy users visit theaters **more often**, not less. Only 6.2% of audiences reported skipping theatrical viewing because of OTT availability.

### 5. IPTV-SVOD Dynamics

| Platform | Median Holdback | Conversion Rate (0-30 days) |
|----------|----------------|---------------------------|
| IPTV | 35 days (~5 weeks) | 27.6% |
| SVOD | 105 days (~3.5 months) | 6.6% (at 120+ days) |

IPTV releases approximately 70 days before SVOD, creating a measurable conversion rate decline of 4.2x for later SVOD releases.

## Stakeholder Analysis

Using Mitchell et al.'s (1997) Stakeholder Salience Model, the study maps industry players by Power, Legitimacy, and Urgency:

| Stakeholder | Type | Holdback Preference |
|------------|------|-------------------|
| Theaters (CGV, Lotte, Megabox) | Definitive | Longer holdback |
| OTT Platforms (Netflix, Tving, Wavve) | Dominant | Shorter holdback |
| Producers/Distributors | Dependent | Flexible holdback |
| Audiences | Discretionary | Shorter holdback |

A critical structural factor: Korea's top 3 vertically integrated conglomerates (CJ, Lotte, etc.) control **86.1% of distribution** and **95.3% of theatrical screens**, creating complex internal conflicts between their theater and OTT divisions.

## International Comparison

| Country | Theater-to-TVOD | Theater-to-SVOD | Mechanism |
|---------|----------------|-----------------|-----------|
| France | 4 months | 15-17 months | Statutory regulation |
| Italy | - | 90 days | Public funding condition |
| USA | - | 45 days | Industry agreement (NATO) |
| Germany | 4 months (VOD) | 12 months | FFG statutory |
| Japan | - | 6-12 months | Industry convention |
| India | - | 8 weeks (56 days) | Exhibitor pressure |
| **Korea** | **IPTV ~35 days** | **SVOD ~105 days** | **Industry convention** |

## Survey Highlights (n=500)

- **85.2% use OTT platforms** (highest among ages 30-39 at 91%)
- **82% complete theatrical viewing within 90 days** of release
- Top reasons for theater preference: immersive screen experience (67.6%), social experience (42.2%)
- **69.6% consider current theatrical holdback appropriate**
- **61.8% consider current OTT holdback too long**
- If holdback shortened for 100K+ audience films: 68.2% probability of 10% attendance decline, but only 3.2% probability of 50% decline
- **75.2% of stakeholders believe industry consensus is achievable**

## Game Theory Perspective

The study frames the holdback dilemma as a **Prisoner's Dilemma**: individual producers benefit from shortening holdback, but collective shortening could erode theatrical revenue. However, the empirical evidence suggests the feared cannibalization is minimal (only 6.2% substitution effect), making the dilemma less severe than assumed.

The dominant strategy for individual players is to shorten holdback, creating a Nash Equilibrium that trends toward shorter windows. The study argues this equilibrium is not necessarily destructive, given the complementary relationship between theaters and OTT.

## Policy Implications

1. **The 6-month convention should be replaced** with evidence-based flexible windows (45-105 days)
2. **Differentiation by film scale** is more rational than a uniform holdback
3. **Theater and OTT are complements**: policy should maximize total ecosystem revenue, not protect one channel
4. **Industry consensus mechanisms** are needed, with 75.2% of stakeholders open to agreement
5. **IPTV timing coordination** matters: the 70-day gap between IPTV and SVOD creates measurable value erosion

## Limitations

- Data covers 2021-2024, still influenced by post-COVID recovery patterns
- OTT revenue data remains proprietary and largely inaccessible
- PSM cannot fully control for unobserved confounders
- The distinction between "audiences who chose not to watch" and "audiences who watched elsewhere" requires further investigation
- Only 4 years of post-OTT mainstream data; longer time series would strengthen causal claims

</div>

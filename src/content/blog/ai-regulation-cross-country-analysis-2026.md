---
title: "AI Regulation Across Three Legislatures: A Cross-Country Comparative Analysis of Korea, the EU, and the United States"
title_en: "AI Regulation Across Three Legislatures: A Cross-Country Comparative Analysis of Korea, the EU, and the United States"
title_ko: "세 입법부의 인공지능 규제: 한국, 유럽연합, 미국 국가 간 비교 분석"
excerpt: "A comprehensive comparative analysis of AI regulation frameworks across Korea's AI Basic Act, the EU AI Act, and the US regulatory landscape, with all legislative data retrieved in real time via MCP (Model Context Protocol) tools."
excerpt_en: "A comprehensive comparative analysis of AI regulation frameworks across Korea's AI Basic Act, the EU AI Act, and the US regulatory landscape, with all legislative data retrieved in real time via MCP (Model Context Protocol) tools."
excerpt_ko: "한국의 AI 기본법, 유럽연합 AI법, 미국의 규제 지형을 아우르는 인공지능 규제 체계 비교 분석으로, 모든 입법 데이터는 MCP(Model Context Protocol) 도구를 통해 실시간으로 수집했습니다."
date: 2026-04-05
category: Analysis
tags:
  - AI Regulation
  - Artificial Intelligence
  - Comparative Law
  - EU AI Act
  - Korea AI Basic Act
  - MCP
  - Legislative Analysis
  - Digital Policy
author: Yonghee Kim
enableShare: true
language: both
keywords:
  - AI regulation comparison
  - EU AI Act
  - Korea AI Basic Act
  - artificial intelligence governance
  - cross-country legislative analysis
  - Model Context Protocol
  - world-parliament-mcp
---

<div data-lang="ko">

## 방법론: MCP를 활용한 인공지능 기반 입법 연구

이 보고서는 **world-parliament-mcp**를 사용해 작성했습니다. 이는 인공지능(Claude)에게 세 주요 관할권의 입법 데이터베이스에 대한 직접적이고 실시간인 접근을 제공하는 Model Context Protocol(MCP) 서버입니다.

- **한국**: 법제처(MOLEG) 오픈 API + 열린국회정보 오픈 API
- **유럽연합**: EUR-Lex SPARQL 엔드포인트 + 유럽의회 오픈 데이터 포털
- **미국**: congress.gov API + 연방규정 전자판(eCFR) + 연방관보(Federal Register)

이 보고서에 제시된 모든 법률 본문, 조문 단위 규정, 표결 기록, 규제 데이터는 집필 시점에 이러한 공식 공공 API를 통해 프로그래밍 방식으로 수집한 것입니다. 법률 내용에 관해서는 2차 자료를 사용하지 않았습니다.

---

## 1. 개관: 인공지능 거버넌스를 향한 세 가지 접근

인공지능이 의료와 교육에서 법 집행과 공공 행정에 이르기까지 핵심 영역에 깊이 자리 잡으면서, 전 세계 정부는 혁신과 안전 사이의 균형이라는 과제에 직면해 있습니다. 한국, 유럽연합, 미국은 뚜렷하게 다른 접근을 택했습니다.

| | **한국** | **유럽연합** | **미국** |
|---|---|---|---|
| **법률** | 인공지능 발전과 신뢰 기반 조성에 관한 기본법(AI 기본법) | Regulation (EU) 2024/1689 (AI법) | 포괄적 연방 법률 없음 |
| **제정** | 2026년 1월 20일 | 2024년 6월 13일 | 해당 없음 |
| **시행** | 2026년 1월 22일 | 2024년 8월 1일(2027년까지 단계적) | 해당 없음 |
| **규모** | 38개 조문 + 대통령령(시행령) | 13개 장에 걸친 113개 조문 | 분야별 규제 + 행정명령 |
| **방식** | 진흥과 규제의 균형 | 위험 기반 포괄 규제 | 산업 자율 규제 + 주(州) 단위 분산 입법 |
| **본회의 표결** | 찬성 260 / 반대 1 / 기권 3(재석 300, 2024년 12월 26일) | 의회와 이사회 채택 | 해당 없음 |

한국 AI 기본법은 제22대 국회에서 거의 만장일치에 가까운 지지로 통과되었습니다. 2026년 4월 기준 이미 27건의 개정안이 발의되어 활발한 입법 논의가 이어지고 있습니다. 유럽연합 AI법은 세계 최초의 포괄적 위험 기반 인공지능 규제입니다. 반면 미국은 포괄적인 연방 인공지능 법률이 없으며, 대신 행정부의 조치, 기관별 규칙, 새롭게 등장하는 주 단위 법률에 의존하고 있습니다.

---

## 2. 인공지능의 정의: 세 가지 법적 정의

각 관할권이 "인공지능"을 법적으로 어떻게 정의하는지가 그 규제 체계 전체의 범위를 결정합니다.

### 2.1 한국 (제2조 제1호)

> "인공지능"이란 학습, 추론, 지각, 판단, 언어의 이해 등 인간이 가진 지적 능력을 전자적 방법으로 구현한 것을 말한다.

한국의 정의는 **능력 기반**으로, 인공지능을 인간 인지 과정의 기능적 재현에 연결합니다. 이 접근은 넓고 기술 중립적이어서, 특정 기술 구조에 정의를 얽매지 않고 현재와 미래의 인공지능 시스템을 모두 포괄합니다.

### 2.2 유럽연합 (AI법 제3조)

유럽연합 AI법은 인공지능 시스템을, 다양한 수준의 자율성과 적응성을 가지고 작동하도록 설계되어 물리적 또는 가상의 환경에 영향을 줄 수 있는 예측, 권고, 결정과 같은 산출물을 추론하는 기계 기반 시스템으로 정의합니다.

유럽연합의 정의는 **산출물 중심**으로, 시스템의 자율적 행동과 결과를 낳는 산출물을 생성하는 능력에 초점을 둡니다. 이는 경제협력개발기구(OECD)의 인공지능 작업 정의와 의도적으로 정합성을 맞춘 것입니다.

### 2.3 미국

미국에는 인공지능에 대한 **통일된 연방 정의가 없습니다.** 여러 기관과 입법안이 서로 다른 정의를 제시해 왔습니다. 2020년 국가 인공지능 이니셔티브법(National AI Initiative Act of 2020)은 연방 연구 목적의 작업 정의를 제공하지만, 여러 분야에 걸쳐 구속력 있는 규제 효력을 갖지는 않습니다.

### 2.4 생성형 인공지능: 정의의 분기

한국과 유럽연합은 생성형 인공지능을 다루는 방식에서 갈립니다.

- **한국** (제2조 제5호)은 별도의 정의를 도입합니다. *"생성형 인공지능이란 입력한 데이터의 구조와 특성을 모방하여 텍스트, 음성, 이미지, 영상 등의 산출물을 생성하는 인공지능 시스템을 말한다."*
- **유럽연합**은 이를 **범용 인공지능 모델**(제5장, 제51조부터 제56조)이라는 개념으로 다루며, 시스템적 위험이 있는 모델 제공자에게 특정 의무를 부과합니다.

한국의 접근은 생성형 인공지능을 별개의 범주로 다루는 반면, 유럽연합은 이를 더 넓은 모델 거버넌스 체계의 하위 집합으로 봅니다.

---

## 3. 위험 분류: 인공지능 피해의 분류 체계

세 관할권 사이의 가장 근본적인 구조적 차이는 인공지능 위험을 분류하는 방식에 있습니다.

### 3.1 한국: 2단계 체계

한국은 이분법적 분류를 사용합니다.

- **일반 인공지능**: 기본 원칙과 자율적 준수의 대상
- **고영향 인공지능** (제2조 제4호): 강화된 의무의 대상

고영향 인공지능은 기술적 위험 평가가 아니라 적용 분야로 정의됩니다. 법은 **11개의 구체적 분야**를 열거합니다.

1. 에너지 공급
2. 먹는물의 생산
3. 보건의료의 제공
4. 의료기기 및 디지털 의료기기
5. 핵물질과 시설의 안전
6. 범죄 수사를 위한 생체인식 분석(얼굴 인식, 지문, 홍채, 손바닥 정맥)
7. 채용, 대출, 그리고 개인의 권리와 의무에 중대한 영향을 미치는 결정
8. 교통 체계, 시설, 기반시설의 운영
9. 시민에게 영향을 미치는 정부 결정(자격, 비용 징수 등)
10. 유아 교육부터 중등 교육까지의 학생 평가
11. 대통령령으로 정하는 추가 분야

이러한 열거 방식은 규제 명확성을 제공하지만, 새로운 인공지능 활용에 발맞추기 위해 법 개정이 필요할 수 있습니다.

### 3.2 유럽연합: 4단계 위험 피라미드

유럽연합 AI법은 네 개의 위험 단계를 설정하여 세계에서 가장 세분화된 인공지능 위험 분류를 만들었습니다.

**1단계: 금지된 인공지능 관행 (제5조)**

여덟 개 범주의 인공지능이 전면 금지됩니다.

1. **잠재의식 조작**: 사람의 의식을 넘어서는 기법을 사용해 행동을 실질적으로 왜곡하는 인공지능
2. **취약성 악용**: 연령, 장애, 사회경제적 상황을 이유로 개인을 표적으로 삼는 행위
3. **사회적 평점**: 사회적 행동에 근거해 사람을 평가하거나 분류하여 불리한 처우로 이어지게 하는 행위
4. **예측적 범죄 프로파일링**: 오로지 프로파일링이나 성격 특성에 근거한 위험 평가
5. **무차별적 얼굴 인식 데이터베이스**: 인터넷이나 CCTV에서 무차별적으로 수집하여 얼굴 인식 데이터베이스를 구축하거나 확장하는 행위
6. **직장 및 교육 현장의 감정 추론**: 직장과 교육 환경에서 감정을 추론하는 행위(의료 또는 안전 목적은 예외)
7. **생체 정보 기반 보호 특성 추론**: 생체 데이터로 개인을 분류하여 인종, 정치적 견해, 종교, 성적 지향 등을 추론하는 행위
8. **공공장소 실시간 원격 생체 식별**: 법 집행 목적의 식별로, 엄격히 제한된 예외(실종자, 임박한 위협, 특정 중대 범죄)만 허용

**2단계: 고위험 인공지능 (제6조부터 제49조)**

생체 인식, 핵심 기반시설, 교육, 고용, 필수 서비스, 법 집행, 이민, 사법 및 민주적 절차에 사용되는 인공지능 시스템은 의무적 적합성 평가, CE 마킹, 유럽연합 데이터베이스 등록의 대상입니다.

**3단계: 제한적 위험 (제50조)**

사람과 상호작용하거나, 합성 콘텐츠(딥페이크)를 생성하거나, 감정 인식을 수행하는 인공지능 시스템은 투명성 의무를 충족해야 합니다.

**4단계: 최소 위험**

그 밖의 모든 인공지능 시스템은 특정한 규제 의무 없이 배치될 수 있습니다.

### 3.3 미국: 연방 차원의 분류 없음

미국은 인공지능에 대한 연방 차원의 위험 분류를 마련하지 않았습니다. 규제 지형은 다음으로 구성됩니다.

- **수출 통제**: 15 CFR 740.27은 인공지능 인가에 대한 라이선스 예외(AIA)를 두어, 고급 인공지능 모델과 컴퓨팅 자원의 수출을 통제합니다
- **분야별 규칙**: 개별 기관(FDA, SEC, FTC 등)이 자기 영역 안에서 기존 규제 권한을 인공지능에 적용합니다
- **주 단위 법률**: 콜로라도와 캘리포니아 등 일부 주가 인공지능 관련 법률을 제정하거나 발의했습니다

---

## 4. 의무와 준수

### 4.1 인증과 적합성 평가

세 관할권은 자율적 준수에서 의무적 준수에 이르는 스펙트럼을 보여 줍니다.

| | **한국** | **유럽연합** | **미국** |
|---|---|---|---|
| **체계** | 정부 지원을 동반한 자율 인증 | 의무적 적합성 평가 | 연방 차원의 체계 없음 |
| **방식** | 자발적 검증 및 인증(제30조) | CE 마킹 + 유럽연합 데이터베이스 등록(제43조부터 제49조) | 해당 없음 |
| **고위험 의무** | 고영향 인공지능 제공자의 사전 인증 취득 "노력" 의무(제30조 제3항) | 고위험 인공지능에 대한 의무적 사전 적합성 평가 | 해당 없음 |
| **공공 부문** | 정부 기관은 인증된 인공지능 제품을 우선 사용(제30조 제4항) | 동일한 요건 적용 | 해당 없음 |
| **중소기업 지원** | 중소기업 인증에 대한 재정 및 행정 지원(제30조 제2항) | 중소기업 대상 수수료 감면과 규제 샌드박스(제57조부터 제63조) | 해당 없음 |

한국의 접근은 "연성 의무화"라는 점에서 주목할 만합니다. 인증은 기술적으로 자발적이지만, 법은 공공 기관이 인증 제품을 우선하도록 요구하고 중소기업을 지원함으로써 강한 유인을 만듭니다.

### 4.2 고영향/고위험 인공지능 평가

**한국 (제33조)**: 인공지능 사업자는 시장 출시 전에 자신의 인공지능이 고영향 인공지능에 해당하는지를 선제적으로 검토해야 합니다. 과학기술정보통신부 장관에게 공식 판단을 요청할 수 있으며, 장관은 자문을 위해 전문가 위원회를 구성할 수 있습니다.

**유럽연합 (제9조부터 제15조)**: 고위험 인공지능 제공자는 포괄적 위험 관리 체계를 구현하고, 데이터 거버넌스를 보장하며, 기술 문서를 유지하고, 기록 보관을 가능하게 하며, 배치자에게 투명성을 제공하고, 인간의 감독을 가능하게 하며, 정확성, 견고성, 사이버보안을 보장해야 합니다.

### 4.3 윤리와 원칙

**한국 (제27조)**: 정부는 안전성, 신뢰성, 접근성, 인간 복지 기여를 아우르는 인공지능 윤리 원칙을 수립하고 공표하여야 합니다. 과학기술정보통신부 장관은 실행 계획을 마련하고 이를 보급하며 교육을 제공해야 합니다. 다른 정부 기관이 인공지능 윤리 지침을 만들 경우, 장관은 일관성과 정합성에 관한 권고를 할 수 있습니다.

**유럽연합 (제95조)**: 고위험이 아닌 인공지능에 대한 자발적 행동 강령을 장려하지만, 정부 주도의 윤리 원칙을 의무화하지는 않습니다.

---

## 5. 거버넌스 구조

### 5.1 한국

- **주무 기관**: 과학기술정보통신부
- **자문 기구**: 대통령 소속 국가인공지능위원회
- **역외 적용**: 국외에서 이루어진 행위라도 국내 시장이나 이용자에게 영향을 미치면 이 법을 적용합니다(제4조)
- **국방 예외**: 오로지 국방 또는 국가안보 목적으로 개발된 인공지능은 대통령령으로 정하는 바에 따라 제외됩니다(제4조 제2항)

### 5.2 유럽연합

- **주무 기관**: 유럽연합 AI사무국(유럽위원회 산하)(제64조)
- **자문 기구**: 유럽 인공지능위원회(제65조-제66조), 자문 포럼(제67조), 독립 전문가 과학 패널(제68조)
- **역외 적용**: 설립지와 무관하게 유럽연합 시장에 인공지능을 출시하는 제공자에게 적용

### 5.3 미국

연방 차원의 중앙집중적 인공지능 거버넌스 구조가 없습니다. 이전 행정부의 인공지능 관련 행정명령은 철회되었습니다. 개별 기관이 각자의 영역 안에서 권한을 유지합니다.

---

## 6. 제재와 집행

제재 구조는 각 관할권의 규제 강도를 드러냅니다.

| **위반 유형** | **한국** | **유럽연합 (제99조)** | **미국** |
|---|---|---|---|
| 금지된 인공지능 관행 | 해당 없음 | 최대 3,500만 유로 또는 전 세계 연간 매출의 7% | 해당 없음 |
| 고위험 인공지능 위반 | 해당 없음 | 최대 1,500만 유로 또는 전 세계 연간 매출의 3% | 해당 없음 |
| 당국에 대한 허위 정보 제공 | 해당 없음 | 최대 750만 유로 또는 전 세계 연간 매출의 1% | 해당 없음 |
| 중소기업 규정 | 해당 없음 | 비율과 절대 금액 중 낮은 쪽 적용 | 해당 없음 |

진흥과 신뢰 구축에 초점을 둔 기본법으로서 한국 AI 기본법은 제재 규정을 두지 않습니다. 집행은 분야별 입법과 하위 법령의 정비에 달려 있게 됩니다.

유럽연합의 제재 체계는 개인정보보호 일반규정(GDPR)의 방식을 본떴으며, 세계에서 가장 엄격한 인공지능 집행 체계입니다. 과징금은 전 세계 매출을 기준으로 산정되어, 규제 당국이 다국적 기술 기업에 상당한 영향력을 행사하게 합니다. 특히 이 규정은 사업자의 규모, 당국과의 협력, 취한 시정 조치 등 완화 요소를 고려하도록 의무화합니다(제99조 제7항).

---

## 7. 입법 동학: 살아 있는 지형

### 7.1 한국: 빠른 개정 활동

AI 기본법은 2024년 12월 26일 압도적 지지(260-1-3)로 통과되었고, 이어 2025년 12월 30일 개정안이 통과되었습니다(221-0-4). 2026년 4월 기준 AI 기본법과 관련된 **27건의 개정안**이 제22대 국회에 발의되었으며, 인공지능 관련 법안은 총 **65건**이 논의되고 있습니다. 이는 AI 기본법이 입법부가 능동적으로 갱신하는 살아 있는 체계로 기능함을 보여 줍니다.

최근 개정 제안으로는 다음이 있습니다.
- 중소기업 인공지능 도입 및 활용 지원법(2026년 4월 2일 발의)
- 인공지능 데이터센터 건설 및 운영 활성화법(2026년 3월 24일 발의)
- 특정 규제 공백을 다루는 AI 기본법 다수 개정안

### 7.2 유럽연합: 단계적 시행

유럽연합 AI법은 단계적 시행 일정을 따릅니다.
- **2024년 8월**: 발효
- **2025년 2월**: 금지된 인공지능 관행 적용 금지
- **2025년 8월**: 범용 인공지능 모델에 대한 의무
- **2026년 8월**: 대부분의 조항 적용
- **2027년 8월**: 부속서 III의 고위험 인공지능을 포함한 전면 적용

### 7.3 미국: 분절된 진전

제119대 미국 의회에는 인공지능 관련 법안이 다수 계류 중이지만, 포괄적인 연방 법률은 제정되지 않았습니다. 규제 접근은 분야별로 유지되며, 연방거래위원회(FTC), 증권거래위원회(SEC) 등 기관이 인공지능 관련 사안에 기존 권한을 적용합니다. 한편 미국의 수출 통제 규정(15 CFR 740.27)은 고급 인공지능 모델과 컴퓨팅 인프라의 국제 이전을 통제하는, 가장 구체적인 연방 인공지능 정책입니다.

---

## 8. 비교 평가

### 8.1 규제 철학

세 관할권은 뚜렷하게 다른 규제 철학을 구현합니다.

- **한국**은 **발전 국가 모형**을 추구합니다. 정부가 인공지능 산업 발전을 적극 진흥하는 동시에 신뢰 구축을 위한 안전장치를 마련합니다. 기본법은 대통령령과 분야별 입법을 통해 정교화할 수 있는 토대를 만듭니다.

- **유럽연합**은 **사전 예방적 규제 모형**을 시행합니다. 포괄적 위험 분류, 의무적 준수, 상당한 제재가 특징입니다. AI법은 혁신을 다소 늦추는 비용을 감수하더라도 피해 예방을 우선합니다.

- **미국**은 **시장 주도 모형**을 따릅니다. 최소한의 연방 개입, 산업 자율 규제 의존, 기존 기관을 통한 분야별 집행이 특징입니다. 이 접근은 유연성을 극대화하지만 규제 불확실성과 분절을 낳습니다.

### 8.2 정의의 범위

한국의 능력 기반 정의("인간의 지적 능력을 전자적 방법으로 구현")는 가장 인간 중심적입니다. 유럽연합의 산출물 기반 정의("산출물을 추론하는 기계 기반 시스템")는 가장 기술적으로 정밀합니다. 통일된 미국 연방 정의의 부재는 기관 간 해석상의 모호함을 낳습니다.

### 8.3 위험 구조

한국의 2단계 체계(일반 대 고영향)는 가장 단순하고 행정 친화적입니다. 유럽연합의 4단계 피라미드(금지, 고위험, 제한적 위험, 최소 위험)는 가장 포괄적입니다. 미국의 분야별 접근은 가장 분절되어 있습니다.

### 8.4 집행의 간극

가장 큰 구조적 차이는 집행에 있습니다. 유럽연합은 전 세계 매출의 최대 7%까지 과징금을 부과할 수 있으며, 주요 기술 기업의 경우 수십억 달러에 이를 수 있습니다. 한국의 기본법은 제재가 없어, 연성 거버넌스와 분야별 집행에 의존합니다. 미국에는 인공지능 전용 연방 집행 장치가 없습니다.

---

## 9. 국제 인공지능 거버넌스에 대한 함의

세 국가 비교는 몇 가지 중요한 동학을 드러냅니다.

**규제의 수렴**: 접근이 다름에도 한국과 유럽연합은 핵심 개념을 공유합니다. 둘 다 적용 분야로 "고영향" 또는 "고위험" 인공지능을 구분하고, 둘 다 일정한 형태의 사전 평가를 요구하며, 둘 다 자국 시장에 영향을 미치는 인공지능에 대해 역외 관할권을 주장합니다.

**브뤼셀 효과**: 유럽연합 AI법의 선도자 이점과 역외 적용은 사실상의 글로벌 표준을 세울 수 있습니다. 유럽연합 시장에 서비스를 제공하는 기업은 본국 관할권과 무관하게 이를 준수해야 하기 때문입니다.

**한국의 중간 경로**: 유럽연합보다는 가볍고 미국보다는 구조화된 한국의 접근은, 경쟁력과 거버넌스의 균형을 추구하는 다른 아시아 경제권에 하나의 모델을 제시할 수 있습니다.

**미국의 규제 공백**: 포괄적 연방 인공지능 법률의 부재는 세계 최대 인공지능 생태계를 통일된 거버넌스 없이 두게 되며, 이미 체계를 갖춘 교역 상대국과의 마찰을 낳을 수 있습니다.

---

## 10. 결론

이 분석은 인공지능 거버넌스가 단일한 과제가 아니라, 서로 다른 정치 체제가 각자의 제도적 전통, 경제적 우선순위, 위험 감수 성향에 따라 다루는 다차원적 정책 문제임을 보여 줍니다.

한국의 AI 기본법, 유럽연합의 AI법, 미국의 분절된 접근은 포괄 규제에서 시장 주도 거버넌스에 이르는 스펙트럼의 세 지점을 나타냅니다. 인공지능 능력이 가속화될수록, 각 접근의 효과성은 유익한 혁신을 가능하게 하면서도 피해를 예방하는 능력으로 시험받게 될 것입니다.

이 분석을 가능하게 한 입법 데이터 인프라, 즉 MCP를 통한 세 국가 입법 체계로의 실시간 접근은 그 자체로 비교 법 연구의 새로운 역량을 보여 줍니다. 연구자가 전례 없는 속도와 정밀성으로 여러 관할권의 규제 변화를 추적하고 비교할 수 있게 하기 때문입니다.

---

*이 보고서는 world-parliament-mcp와 korean-law MCP 서버를 사용해 작성했습니다. 이 서버들은 인공지능(Claude)에게 한국 법제처, 한국 국회, EUR-Lex, 유럽의회, 미국 의회, 연방규정 전자판의 입법 데이터베이스에 대한 직접 접근을 제공합니다. 모든 입법 데이터는 2026년 4월 5일에 공식 공공 API에서 실시간으로 수집한 것입니다.*

</div>

<div data-lang="en">

## Methodology: AI-Powered Legislative Research via MCP

This report was produced using **world-parliament-mcp**, a Model Context Protocol (MCP) server that provides AI (Claude) with direct, real-time access to legislative databases across three major jurisdictions:

- **Korea**: Korea Ministry of Government Legislation (MOLEG) Open API + Open National Assembly API
- **European Union**: EUR-Lex SPARQL endpoint + European Parliament Open Data Portal
- **United States**: congress.gov API + Electronic Code of Federal Regulations (eCFR) + Federal Register

All legislative texts, article-level provisions, vote records, and regulatory data presented in this report were retrieved programmatically through these official public APIs at the time of writing. No secondary sources were used for the legal content.

---

## 1. Overview: Three Approaches to AI Governance

As artificial intelligence becomes deeply embedded in critical sectors, from healthcare and education to law enforcement and public administration, governments worldwide face the challenge of balancing innovation with safety. Korea, the EU, and the US have taken markedly different approaches.

| | **Korea** | **EU** | **US** |
|---|---|---|---|
| **Law** | Framework Act on AI Development and Trust (AI Basic Act) | Regulation (EU) 2024/1689 (AI Act) | No comprehensive federal law |
| **Enacted** | January 20, 2026 | June 13, 2024 | N/A |
| **Effective** | January 22, 2026 | August 1, 2024 (phased through 2027) | N/A |
| **Scale** | 38 articles + Presidential Enforcement Decree | 113 articles across 13 chapters | Sectoral regulations + Executive Orders |
| **Approach** | Balanced promotion and regulation | Risk-based comprehensive regulation | Industry self-regulation + state-level patchwork |
| **Floor Vote** | 260 Yes / 1 No / 3 Abstain (of 300 present, December 26, 2024) | Adopted by Parliament and Council | N/A |

The Korean AI Basic Act was passed by the 22nd National Assembly with near-unanimous support. As of April 2026, 27 amendment bills have already been filed, signaling active legislative engagement. The EU AI Act represents the world's first comprehensive risk-based AI regulation. The United States, by contrast, has no overarching federal AI legislation, relying instead on executive action, agency-specific rules, and emerging state-level laws.

---

## 2. Defining Artificial Intelligence: Three Legal Definitions

How each jurisdiction legally defines "artificial intelligence" shapes the entire scope of its regulatory framework.

### 2.1 Korea (Article 2, Paragraph 1)

> "Artificial intelligence" means the electronic implementation of intellectual capabilities possessed by humans, including learning, reasoning, perception, judgment, and language understanding.

Korea's definition is **capability-based**, anchoring AI to the functional replication of human cognitive processes. This approach is broad and technology-neutral, encompassing current and future AI systems without tying the definition to specific technical architectures.

### 2.2 EU (Article 3, AI Act)

The EU AI Act defines an AI system as a machine-based system designed to operate with varying levels of autonomy and adaptiveness, that infers outputs such as predictions, recommendations, or decisions that may influence physical or virtual environments.

The EU definition is **output-oriented**, focusing on the system's autonomous behavior and its capacity to generate consequential outputs. It deliberately aligns with the OECD's working definition of AI.

### 2.3 United States

The US has **no unified federal definition** of artificial intelligence. Various agencies and legislative proposals have offered differing definitions. The National AI Initiative Act of 2020 provides a working definition for federal research purposes, but it does not carry binding regulatory force across sectors.

### 2.4 Generative AI: A Definitional Divergence

Korea and the EU diverge in how they address generative AI:

- **Korea** (Article 2, Paragraph 5) introduces a standalone definition: *"Generative AI means an AI system that generates text, sound, images, video, and other outputs by mimicking the structure and characteristics of input data."*
- **EU** addresses this through the concept of **General-Purpose AI Models** (Chapter V, Articles 51-56), imposing specific obligations on providers of models with systemic risk.

Korea's approach treats generative AI as a distinct category; the EU treats it as a subset of a broader model governance framework.

---

## 3. Risk Classification: Taxonomy of AI Harm

The most fundamental structural difference among the three jurisdictions lies in how they classify AI risk.

### 3.1 Korea: Two-Tier System

Korea employs a binary classification:

- **General AI**: Subject to baseline principles and voluntary compliance
- **High-Impact AI** (Article 2, Paragraph 4): Subject to enhanced obligations

High-Impact AI is defined by application domain rather than technical risk assessment. The law enumerates **11 specific domains**:

1. Energy supply
2. Drinking water production
3. Healthcare provision
4. Medical devices and digital medical devices
5. Nuclear materials and facility safety
6. Biometric analysis for criminal investigation (facial recognition, fingerprints, iris, palm vein)
7. Hiring, lending, and decisions with significant impact on individual rights and obligations
8. Operation of transportation systems, facilities, and infrastructure
9. Government decisions affecting citizens (eligibility, cost collection, etc.)
10. Student assessment in early childhood through secondary education
11. Additional domains designated by Presidential Decree

This enumerated approach provides regulatory clarity but may require legislative amendments to keep pace with new AI applications.

### 3.2 EU: Four-Tier Risk Pyramid

The EU AI Act establishes four risk tiers, creating the world's most granular AI risk classification:

**Tier 1: Prohibited AI Practices (Article 5)**

Eight categories of AI are outright banned:

1. **Subliminal manipulation**: AI deploying techniques beyond a person's consciousness to materially distort behavior
2. **Exploitation of vulnerabilities**: Targeting individuals due to age, disability, or socioeconomic situation
3. **Social scoring**: Evaluating or classifying persons based on social behavior leading to detrimental treatment
4. **Predictive criminal profiling**: Risk assessment based solely on profiling or personality traits
5. **Untargeted facial recognition databases**: Creating or expanding facial recognition databases through untargeted scraping from the internet or CCTV
6. **Workplace/education emotion inference**: Inferring emotions in workplace and educational settings (except for medical or safety purposes)
7. **Biometric-based protected characteristic inference**: Categorizing individuals by biometric data to infer race, political opinions, religion, sexual orientation, etc.
8. **Real-time remote biometric identification in public spaces**: For law enforcement, with strictly limited exceptions (missing persons, imminent threats, specific serious crimes)

**Tier 2: High-Risk AI (Articles 6-49)**

AI systems used in biometrics, critical infrastructure, education, employment, essential services, law enforcement, immigration, and justice/democratic processes are subject to mandatory conformity assessment, CE marking, and EU database registration.

**Tier 3: Limited Risk (Article 50)**

AI systems interacting with humans, generating synthetic content (deepfakes), or performing emotion recognition must meet transparency obligations.

**Tier 4: Minimal Risk**

All other AI systems may be deployed without specific regulatory obligations.

### 3.3 United States: No Federal Classification

The US has not established a federal risk classification for AI. The regulatory landscape consists of:

- **Export controls**: 15 CFR 740.27 establishes a License Exception for Artificial Intelligence Authorization (AIA), controlling the export of advanced AI models and computing resources
- **Sector-specific rules**: Individual agencies (FDA, SEC, FTC, etc.) apply existing regulatory authority to AI within their domains
- **State-level laws**: States such as Colorado and California have enacted or proposed AI-specific legislation

---

## 4. Obligations and Compliance

### 4.1 Certification and Conformity Assessment

The three jurisdictions represent a spectrum from voluntary to mandatory compliance:

| | **Korea** | **EU** | **US** |
|---|---|---|---|
| **Regime** | Voluntary certification with government support | Mandatory conformity assessment | No federal regime |
| **Mechanism** | Self-initiated verification/certification (Article 30) | CE marking + EU database registration (Articles 43-49) | N/A |
| **High-risk obligation** | "Best-effort" duty for high-impact AI providers to obtain pre-market certification (Article 30.3) | Mandatory pre-market conformity assessment for high-risk AI | N/A |
| **Public sector** | Government agencies must prioritize certified AI products (Article 30.4) | Same requirements apply | N/A |
| **SME support** | Financial and administrative support for SME certification (Article 30.2) | SME-specific fee reductions and regulatory sandboxes (Articles 57-63) | N/A |

Korea's approach is notable for its "soft mandate": while certification is technically voluntary, the law creates strong incentives by requiring public agencies to prioritize certified products and providing SME support.

### 4.2 High-Impact/High-Risk AI Assessment

**Korea (Article 33)**: AI operators must proactively review whether their AI qualifies as High-Impact AI before market deployment. They may request a formal determination from the Minister of Science and ICT, who may establish expert committees for consultation.

**EU (Articles 9-15)**: High-risk AI providers must implement a comprehensive risk management system, ensure data governance, maintain technical documentation, enable record-keeping, provide transparency to deployers, enable human oversight, and ensure accuracy, robustness, and cybersecurity.

### 4.3 Ethics and Principles

**Korea (Article 27)**: The government *shall* formulate and publish AI ethics principles covering safety, reliability, accessibility, and contribution to human welfare. The Minister of Science and ICT must develop action plans, disseminate them, and provide education. When other government agencies create AI ethics guidelines, the Minister may issue recommendations on consistency and coherence.

**EU (Article 95)**: Encourages voluntary codes of conduct for non-high-risk AI, but does not mandate government-led ethics principles.

---

## 5. Governance Architecture

### 5.1 Korea

- **Lead Agency**: Ministry of Science and ICT
- **Advisory Body**: AI Committee under the President
- **Extraterritorial scope**: The law applies to acts conducted outside Korea if they affect the domestic market or users (Article 4)
- **National defense exemption**: AI developed solely for national defense or national security purposes is excluded, as designated by Presidential Decree (Article 4.2)

### 5.2 EU

- **Lead Agency**: EU AI Office (under the European Commission) (Article 64)
- **Advisory Bodies**: European AI Board (Articles 65-66), Advisory Forum (Article 67), Scientific Panel of Independent Experts (Article 68)
- **Extraterritorial scope**: Applies to providers placing AI on the EU market regardless of establishment location

### 5.3 United States

No centralized AI governance structure at the federal level. The previous administration's executive orders on AI have been revoked. Individual agencies retain authority within their respective domains.

---

## 6. Penalties and Enforcement

The penalty structures reveal the regulatory intensity of each jurisdiction:

| **Violation Type** | **Korea** | **EU (Article 99)** | **US** |
|---|---|---|---|
| Prohibited AI practices | N/A | Up to EUR 35 million or 7% of global annual turnover | N/A |
| High-risk AI non-compliance | N/A | Up to EUR 15 million or 3% of global annual turnover | N/A |
| False information to authorities | N/A | Up to EUR 7.5 million or 1% of global annual turnover | N/A |
| SME provision | N/A | Lower of percentage or absolute amount applies | N/A |

Korea's AI Basic Act, as a framework law focused on promotion and trust-building, does not include penalty provisions. Enforcement will depend on sector-specific legislation and the development of subordinate regulations.

The EU's penalty regime is modeled on the GDPR's approach and represents the world's most stringent AI enforcement framework. Fines are calculated against global turnover, giving regulators significant leverage over multinational technology companies. Importantly, the regulation mandates consideration of mitigating factors including the operator's size, cooperation with authorities, and remedial actions taken (Article 99.7).

---

## 7. Legislative Dynamics: A Living Landscape

### 7.1 Korea: Rapid Amendment Activity

The AI Basic Act was passed with overwhelming support (260-1-3) on December 26, 2024, and a subsequent amendment bill was passed on December 30, 2025 (221-0-4). As of April 2026, **27 amendment bills** related to the AI Basic Act have been filed in the 22nd National Assembly, and a total of **65 AI-related bills** are under consideration. This demonstrates that the AI Basic Act functions as a living framework that the legislature actively updates.

Recent amendment proposals include:
- SME AI Adoption and Utilization Support Act (filed April 2, 2026)
- AI Data Center Construction and Operation Activation Act (filed March 24, 2026)
- Multiple amendments to the AI Basic Act addressing specific regulatory gaps

### 7.2 EU: Phased Implementation

The EU AI Act follows a staged implementation timeline:
- **August 2024**: Entry into force
- **February 2025**: Prohibition of banned AI practices
- **August 2025**: Obligations for general-purpose AI models
- **August 2026**: Most provisions applicable
- **August 2027**: Full application including high-risk AI in Annex III

### 7.3 United States: Fragmented Progress

The 119th US Congress has multiple AI-related bills pending, but no comprehensive federal legislation has been enacted. The regulatory approach remains sector-specific, with the Federal Trade Commission, Securities and Exchange Commission, and other agencies applying existing authority to AI-related issues. Meanwhile, US export control regulations (15 CFR 740.27) represent the most concrete federal AI policy, controlling the international transfer of advanced AI models and computing infrastructure.

---

## 8. Comparative Assessment

### 8.1 Regulatory Philosophy

The three jurisdictions embody distinct regulatory philosophies:

- **Korea** pursues a **developmental state model**: the government actively promotes AI industry development while establishing trust-building guardrails. The framework law creates a foundation that can be refined through Presidential Decrees and sector-specific legislation.

- **The EU** implements a **precautionary regulatory model**: comprehensive risk classification, mandatory compliance, and substantial penalties. The AI Act prioritizes preventing harm, even at the cost of potentially slowing innovation.

- **The US** follows a **market-led model**: minimal federal intervention, reliance on industry self-regulation, and sector-specific enforcement through existing agencies. This approach maximizes flexibility but creates regulatory uncertainty and fragmentation.

### 8.2 Definition Scope

Korea's capability-based definition ("electronic implementation of human intellectual capabilities") is the most anthropocentric. The EU's output-based definition ("machine-based system that infers outputs") is the most technically precise. The absence of a unified US federal definition creates interpretive ambiguity across agencies.

### 8.3 Risk Architecture

Korea's two-tier system (general vs. high-impact) is the simplest and most administration-friendly. The EU's four-tier pyramid (prohibited, high-risk, limited risk, minimal risk) is the most comprehensive. The US's sector-specific approach is the most fragmented.

### 8.4 Enforcement Gap

The most significant structural difference is in enforcement. The EU can impose fines up to 7% of global turnover, potentially billions of dollars for major technology companies. Korea's framework law contains no penalties, relying instead on soft governance and sector-specific enforcement. The US has no AI-specific federal enforcement mechanism.

---

## 9. Implications for International AI Governance

The three-country comparison reveals several critical dynamics:

**Regulatory convergence**: Despite different approaches, Korea and the EU share key concepts. Both distinguish "high-impact" or "high-risk" AI by application domain, both require some form of pre-market assessment, and both assert extraterritorial jurisdiction over AI affecting their markets.

**The Brussels Effect**: The EU AI Act's first-mover advantage and extraterritorial scope may establish de facto global standards, as companies serving the EU market must comply regardless of their home jurisdiction.

**Korea's middle path**: Korea's approach, lighter than the EU but more structured than the US, may offer a model for other Asian economies seeking to balance competitiveness with governance.

**The US regulatory vacuum**: The absence of comprehensive federal AI legislation leaves the world's largest AI ecosystem without unified governance, potentially creating friction with trading partners who have established frameworks.

---

## 10. Conclusion

This analysis demonstrates that AI governance is not a monolithic challenge but a multidimensional policy problem that different political systems address according to their institutional traditions, economic priorities, and risk tolerances.

Korea's AI Basic Act, the EU AI Act, and the US's fragmented approach represent three points on a spectrum from comprehensive regulation to market-led governance. As AI capabilities accelerate, the effectiveness of each approach will be tested by its ability to prevent harm while enabling beneficial innovation.

The legislative data infrastructure that enabled this analysis, real-time access to three national legislative systems through MCP, itself represents a new capability for comparative legal research, enabling researchers to track and compare regulatory developments across jurisdictions with unprecedented speed and precision.

---

*This report was produced using world-parliament-mcp and korean-law MCP servers, which provide AI (Claude) with direct access to legislative databases from the Korean Ministry of Government Legislation, the Korean National Assembly, EUR-Lex, the European Parliament, the US Congress, and the Electronic Code of Federal Regulations. All legislative data was retrieved in real time from official public APIs on April 5, 2026.*

</div>

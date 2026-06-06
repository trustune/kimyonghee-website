---
title: "The Right to Data Transfer: Social Problems and Response Plans"
title_ko: "개인정보 전송요구권: 사회적 문제와 대응 방안"
title_en: "The Right to Data Transfer: Social Problems and Response Plans"
subtitle: "Critical Analysis of Personal Information Protection Act Enforcement Decree Amendment"
subtitle_ko: "개인정보 보호법 시행령 개정안에 대한 비판적 분석"
subtitle_en: "Critical Analysis of Personal Information Protection Act Enforcement Decree Amendment"
date: "2025-11-21"
category: "Data Policy"
tags: ["MyData", "Data Privacy", "Regulation", "Policy Analysis", "Startup Ecosystem", "GDPR"]
keywords: ["MyData", "GDPR", "Data Portability", "Privacy Regulation", "Startup Policy"]
methodology: ["Policy Analysis", "Legal Review", "Comparative Study (GDPR)", "Stakeholder Analysis", "Cost-Benefit Analysis"]
data_period:
  start: "2023-03"
  end: "2025-11"
related_publications: []
related_projects: []
conference: "MyData Policy Startup Seminar"
venue: "Korea Startup Forum, D.CAMP, Gangnam, Seoul"
description: "In-depth analysis of the proposed expansion of the Right to Request Data Transfer, examining seven critical concerns including regulatory procedural violations, constitutional issues, GDPR non-compliance, and threats to the startup ecosystem."
description_ko: "개인정보 전송요구권 확대 개정안을 심층 분석한다. 규제 절차 위반, 위헌 소지, GDPR 기준 불일치, 스타트업 생태계 위협 등 일곱 가지 핵심 쟁점을 짚는다."
description_en: "In-depth analysis of the proposed expansion of the Right to Request Data Transfer, examining seven critical concerns including regulatory procedural violations, constitutional issues, GDPR non-compliance, and threats to the startup ecosystem."
summary: "The June 2025 amendment proposal ignores Regulatory Reform Committee recommendations (August 2024), violates constitutional principles, contradicts GDPR standards, and threatens to destroy Korea's startup ecosystem through unfair privileges to specialized agencies."
summary_ko: "2025년 6월 개정안은 규제개혁위원회의 권고(2024년 8월)를 무시하고, 헌법 원칙에 어긋나며, GDPR 기준과 충돌한다. 또한 전문기관에 부당한 특혜를 부여해 한국 스타트업 생태계를 무너뜨릴 우려가 있다."
summary_en: "The June 2025 amendment proposal ignores Regulatory Reform Committee recommendations (August 2024), violates constitutional principles, contradicts GDPR standards, and threatens to destroy Korea's startup ecosystem through unfair privileges to specialized agencies."
key_findings:
  - "Procedural violation: Re-proposing rejected content only 4 months after Regulatory Reform Committee decision"
  - "Constitutional issue: Unconstitutional delegation of proxy rights via enforcement decree"
  - "GDPR non-compliance: Lack of trade secret protection unlike EU standards"
  - "Market distortion: Exclusive privileges to specialized agencies creating unfair advantage"
  - "Security risk: Allowing screen scraping despite financial sector ban"
  - "Economic burden: Estimated billions in compliance costs for startups reaching 1M users"
  - "Policy inconsistency: Contradicting Financial Services Commission's scraping ban (2022)"
key_findings_ko:
  - "절차적 위반: 규제개혁위원회 결정 후 단 4개월 만에 부결된 내용을 다시 발의"
  - "위헌 소지: 시행령을 통한 대리권 위임은 위헌적 위임에 해당"
  - "GDPR 기준 불일치: 유럽연합 기준과 달리 영업비밀 보호 장치 부재"
  - "시장 왜곡: 전문기관에 배타적 특혜를 부여해 불공정한 우위를 형성"
  - "보안 위험: 금융권은 금지한 화면 스크래핑을 허용"
  - "경제적 부담: 이용자 100만 명에 도달한 스타트업의 준수 비용이 수십억 원으로 추정"
  - "정책 비일관성: 금융위원회의 스크래핑 금지 조치(2022년)와 모순"
policy_concerns:
  - "Expansion from 3 sectors (medical, telecom, energy) to ALL industries"
  - "Forcing core business data transfer without trade secret protection"
  - "Creating Single Point of Failure (SPOF) through data centralization"
  - "Imposing excessive costs on growing startups (Revenue 150B KRW & 1M users threshold)"
policy_concerns_ko:
  - "3개 분야(의료, 통신, 에너지)에서 전 산업으로 확대"
  - "영업비밀 보호 없이 핵심 사업 데이터의 전송을 강제"
  - "데이터 집중화로 단일 장애점(SPOF)을 형성"
  - "성장 중인 스타트업에 과도한 비용을 부과(매출 1,500억 원 및 이용자 100만 명 기준)"
featured: true
image: "/images/blog/PS25112100891.jpg"
---

<style>
.timeline-container {
  position: relative;
  max-width: 1000px;
  margin: 3rem auto;
  padding: 2rem;
}

.timeline-item {
  display: flex;
  margin-bottom: 2rem;
  position: relative;
}

.timeline-date {
  flex: 0 0 150px;
  font-weight: 700;
  color: #1e40af;
  font-size: 1.1rem;
}

.timeline-content {
  flex: 1;
  padding: 1.5rem;
  background: #f9fafb;
  border-left: 4px solid #2563eb;
  border-radius: 0.5rem;
}

.timeline-content.critical {
  background: #fef2f2;
  border-left-color: #ef4444;
}

.timeline-content.warning {
  background: #fffbeb;
  border-left-color: #f59e0b;
}

.comparison-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin: 2rem 0;
}

.comparison-card {
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.comparison-card.current {
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
  border-left: 4px solid #2563eb;
}

.comparison-card.proposed {
  background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
  border-left: 4px solid #ef4444;
}

.comparison-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #1f2937;
}

.metric-highlight {
  font-size: 3rem;
  font-weight: 900;
  margin: 1rem 0;
  font-family: 'Inter', sans-serif;
}

.current .metric-highlight {
  color: #1e40af;
}

.proposed .metric-highlight {
  color: #dc2626;
}

.concern-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.concern-card {
  padding: 2rem;
  background: white;
  border-radius: 1rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-left: 4px solid;
  transition: transform 0.3s, box-shadow 0.3s;
}

.concern-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}

.concern-card.procedural { border-left-color: #ef4444; }
.concern-card.legal { border-left-color: #f59e0b; }
.concern-card.gdpr { border-left-color: #3b82f6; }
.concern-card.market { border-left-color: #8b5cf6; }
.concern-card.security { border-left-color: #ec4899; }
.concern-card.economic { border-left-color: #10b981; }
.concern-card.consistency { border-left-color: #6366f1; }

.concern-number {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
  opacity: 0.3;
}

.data-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin: 2rem 0;
  background: white;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.data-table thead {
  background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
  color: white;
}

.data-table th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
}

.data-table tbody tr {
  border-bottom: 1px solid #e5e7eb;
  transition: background 0.2s;
}

.data-table tbody tr:hover {
  background: #f9fafb;
}

.data-table td {
  padding: 1rem;
  color: #374151;
}

.highlight-box {
  padding: 2rem;
  margin: 2rem 0;
  border-radius: 1rem;
  border-left: 4px solid;
}

.highlight-box.danger {
  background: #fef2f2;
  border-left-color: #ef4444;
}

.highlight-box.warning {
  background: #fffbeb;
  border-left-color: #f59e0b;
}

.highlight-box.info {
  background: #eff6ff;
  border-left-color: #3b82f6;
}

.chart-container {
  width: 100%;
  max-width: 800px;
  height: 400px;
  margin: 2rem auto;
  padding: 2rem;
  background: white;
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.solution-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  margin: 3rem 0;
}

.solution-card {
  padding: 2rem;
  background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
  border-radius: 1rem;
  border-left: 4px solid #2563eb;
}

.solution-card h3 {
  font-size: 1.5rem;
  color: #1e40af;
  margin-bottom: 1rem;
}

.vs-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 3rem 0;
}

.vs-badge {
  background: #ef4444;
  color: white;
  padding: 1rem 2rem;
  border-radius: 2rem;
  font-size: 2rem;
  font-weight: 900;
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}
</style>

<div data-lang="ko">

## 핵심 요약: 혁신을 위협하는 규제 과잉

**2025년 11월 21일**, 서울 강남 디캠프에서 한국스타트업포럼이 주최한 **마이데이터 정책 스타트업 세미나**에서 발표했다. 데이터 정책, 규제, 혁신이 만나는 지점을 연구하는 사람으로서, 2025년 6월에 발의된 **개인정보 보호법 시행령 개정안**에 대해 깊은 우려를 제기했다.

이 개정안은 "개인정보 전송요구권"을 전 산업으로 확대하려는 것으로, **데이터 활성화에서 데이터 통제로 향하는 근본적 전환**을 뜻한다. 이는 확립된 규제 원칙과 국제 규범을 어기면서 한국의 스타트업 생태계를 흔들 우려가 있다.

<div class="highlight-box danger">
<h3>중대한 경고</h3>
<strong>2025년 6월 개정안은 규제개혁위원회의 2024년 8월 결정을 어기고, 동일한 내용을 단 4개월 만에 다시 발의했다.</strong> 이런 절차적 위반은 행정의 신뢰성을 훼손하고, 보안, 비용, 영업비밀에 관한 업계의 정당한 우려를 외면한다.
</div>

</div>

<div data-lang="en">

## Executive Summary: A Regulatory Overreach Threatening Innovation

On **November 21, 2025**, I presented at the **MyData Policy Startup Seminar** hosted by the Korea Startup Forum at D.CAMP in Gangnam, Seoul. As a researcher examining the intersection of data policy, regulation, and innovation, I raised serious concerns about the **Personal Information Protection Act Enforcement Decree amendment** proposed in June 2025.

The amendment, which aims to expand the "Right to Request Data Transfer" to all industries, represents **a fundamental shift from data activation to data control**, one that threatens to undermine Korea's startup ecosystem while violating established regulatory principles and international norms.

<div class="highlight-box danger">
<h3>Critical Alert</h3>
<strong>The June 2025 amendment proposal violates the Regulatory Reform Committee's August 2024 decision by re-proposing identical content only 4 months later.</strong> This procedural violation undermines administrative integrity and ignores legitimate industry concerns about security, costs, and trade secrets.
</div>

</div>

---

<div data-lang="ko">

## 경과: 신중한 접근에서 규제 과잉으로

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-date">2023-03-14</div>
    <div class="timeline-content">
      <h4>법적 근거 마련</h4>
      <p>개인정보 보호법 2차 개정안이 국회를 통과하며 개인정보 전송요구권(제35조의2)이 신설</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2024-08-09</div>
    <div class="timeline-content warning">
      <h4>규제개혁위원회 결정</h4>
      <p><strong>주요 권고 사항:</strong></p>
      <ul>
        <li>3개 분야(의료, 통신, 에너지)로 제한</li>
        <li>본인 전송과 제3자 전송의 범위를 일치시켜 일관성 유지</li>
        <li>기술 인프라 준비를 위한 충분한 시간 부여</li>
        <li>시장 준비 정도에 따른 단계적 확대</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2025-02-25</div>
    <div class="timeline-content">
      <h4>시행령 제정(대통령령 제35343호)</h4>
      <p>규제개혁위원회 권고를 수용해 3개 분야(의료, 통신, 에너지)로 한정</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2025-03-13</div>
    <div class="timeline-content">
      <h4>제도 시행</h4>
      <p>지정된 3개 분야에서 개인정보 전송요구권 제도가 운영을 시작</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2025-06-23</div>
    <div class="timeline-content critical">
      <h4>논란의 개정안 발의</h4>
      <p><strong>개인정보보호위원회가 전 산업으로의 확대를 다시 발의</strong></p>
      <ul>
        <li>불과 4개월 전의 규제개혁위원회 결정을 무시</li>
        <li>전자상거래, 플랫폼, 게임, 교육, 숙박, 문화·여가로 범위를 확대</li>
        <li>기준: 매출 1,500억 원 + 이용자 100만 명</li>
        <li>전문기관 특혜를 신설</li>
      </ul>
    </div>
  </div>
</div>

</div>

<div data-lang="en">

## Timeline: From Cautious Approach to Regulatory Overreach

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-date">2023-03-14</div>
    <div class="timeline-content">
      <h4>Legal Framework Established</h4>
      <p>Personal Information Protection Act 2nd Amendment passes National Assembly, establishing Right to Request Data Transfer (Article 35-2)</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2024-08-09</div>
    <div class="timeline-content warning">
      <h4>Regulatory Reform Committee Decision</h4>
      <p><strong>Key Recommendations:</strong></p>
      <ul>
        <li>Limit to 3 sectors: Medical, Telecommunications, Energy</li>
        <li>Maintain consistency between self-transfer and third-party transfer scopes</li>
        <li>Allow sufficient preparation time for technical infrastructure</li>
        <li>Gradual expansion based on market readiness</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2025-02-25</div>
    <div class="timeline-content">
      <h4>Enforcement Decree Enacted (Presidential Decree No. 35343)</h4>
      <p>Adopted Regulatory Reform Committee recommendations: Limited to 3 sectors (Medical, Telecom, Energy)</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2025-03-13</div>
    <div class="timeline-content">
      <h4>System Launch</h4>
      <p>Right to Request Data Transfer system begins operation in 3 designated sectors</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2025-06-23</div>
    <div class="timeline-content critical">
      <h4>Controversial Amendment Proposed</h4>
      <p><strong>Personal Information Protection Commission re-proposes expansion to ALL industries</strong></p>
      <ul>
        <li>Ignores Regulatory Reform Committee decision from just 4 months prior</li>
        <li>Expands scope to: E-commerce, Platforms, Gaming, Education, Hospitality, Culture & Leisure</li>
        <li>Threshold: Revenue 150B KRW + 1M users</li>
        <li>Creates specialized agency privileges</li>
      </ul>
    </div>
  </div>
</div>

</div>

---

<div data-lang="ko">

## 확대의 함정: 현행법 대 개정안

<div class="comparison-grid">
  <div class="comparison-card current">
    <h3>현행 시행령(2025년 2월)</h3>
    <div class="metric-highlight">3개 분야</div>
    <h4>범위</h4>
    <ul>
      <li>의료기관</li>
      <li>통신사업자</li>
      <li>에너지 공급자</li>
    </ul>
    <h4>특징</h4>
    <ul>
      <li>본인 전송 = 제3자 전송 범위</li>
      <li>규제개혁위원회 권고를 준수</li>
      <li>단계적 확대 원칙</li>
      <li>충분한 시범 운영 기간</li>
    </ul>
  </div>

  <div class="comparison-card proposed">
    <h3>개정안(2025년 6월)</h3>
    <div class="metric-highlight">전 산업</div>
    <h4>범위</h4>
    <p><strong>다음을 충족하는 모든 사업자:</strong></p>
    <ul>
      <li>연 매출 1,500억 원 이상 <strong>그리고</strong></li>
      <li>이용자 100만 명 이상</li>
      <li>추가: 모든 초·중·고 및 고등 교육기관</li>
      <li>추가: 위원회가 지정하는 모든 사업자</li>
    </ul>
    <h4>문제점</h4>
    <ul>
      <li>본인 전송과 제3자 전송의 범위가 불일치</li>
      <li>규제개혁위원회 결정에 위반</li>
      <li>전 분야로 동시에 확대</li>
      <li>최초 시행 후 불과 4개월 만에 추진</li>
    </ul>
  </div>
</div>

<div class="highlight-box warning">
<h3>"매출 1,500억 원 및 이용자 100만 명"의 실제 의미</h3>
<p>이 기준에 포함되는 대상:</p>
<ul>
  <li><strong>주요 플랫폼:</strong> 네이버, 카카오, 쿠팡, 배민, 11번가, G마켓, 옥션</li>
  <li><strong>성장 중인 스타트업:</strong> 이용자 100만 명에 도달하면 자동으로 포함</li>
  <li><strong>영향받는 분야:</strong> 전자상거래, 배달, 게임, 교육, 숙박, 문화·여가</li>
</ul>
<p><strong>결과:</strong> 사실상 성공한 디지털 사업 대부분이 포함되어, 사실상 전 산업으로 확대되는 효과</p>
</div>

</div>

<div data-lang="en">

## The Expansion Trap: Current Law vs. Proposed Amendment

<div class="comparison-grid">
  <div class="comparison-card current">
    <h3>Current Enforcement Decree (Feb 2025)</h3>
    <div class="metric-highlight">3 Sectors</div>
    <h4>Scope</h4>
    <ul>
      <li>Medical institutions</li>
      <li>Telecommunications carriers</li>
      <li>Energy providers</li>
    </ul>
    <h4>Characteristics</h4>
    <ul>
      <li>Self-transfer = Third-party transfer scope</li>
      <li>Follows Regulatory Reform Committee guidance</li>
      <li>Gradual expansion principle</li>
      <li>Sufficient pilot period</li>
    </ul>
  </div>

  <div class="comparison-card proposed">
    <h3>Proposed Amendment (June 2025)</h3>
    <div class="metric-highlight">ALL Industries</div>
    <h4>Scope</h4>
    <p><strong>Any entity meeting:</strong></p>
    <ul>
      <li>Annual revenue ≥ 150B KRW <strong>AND</strong></li>
      <li>User base ≥ 1M persons</li>
      <li>Plus: All elementary/secondary/higher education institutions</li>
      <li>Plus: Any entity designated by Commission</li>
    </ul>
    <h4>Problems</h4>
    <ul>
      <li>Self-transfer and third-party transfer scope inconsistent</li>
      <li>Violates Regulatory Reform Committee decision</li>
      <li>Simultaneous expansion to all sectors</li>
      <li>Only 4 months after initial implementation</li>
    </ul>
  </div>
</div>

<div class="highlight-box warning">
<h3>What "Revenue 150B KRW & 1M Users" Really Means</h3>
<p>This threshold captures:</p>
<ul>
  <li><strong>Major platforms:</strong> Naver, Kakao, Coupang, Baemin, 11st, Gmarket, Auction</li>
  <li><strong>Growing startups:</strong> Any company reaching 1M users automatically included</li>
  <li><strong>Sectors affected:</strong> E-commerce, delivery, gaming, education, hospitality, culture & leisure</li>
</ul>
<p><strong>Result:</strong> Virtually all successful digital businesses are captured → De facto expansion to ALL industries</p>
</div>

</div>

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="scopeComparison"></canvas>
</div>

---

## Seven Critical Concerns

<div class="chart-container" style="height: 500px; margin-bottom: 3rem;"><canvas id="sevenConcernsRadar"></canvas></div>

<div data-lang="ko">

<div class="concern-grid">
  <div class="concern-card procedural">
    <div class="concern-number">1</div>
    <h3>절차적 위반</h3>
    <p><strong>쟁점:</strong> 규제개혁위원회 결정 후 단 4개월 만에 부결된 내용을 다시 발의</p>
    <p><strong>위험:</strong> 규제 심사 절차를 훼손하고 행정 신뢰를 약화</p>
  </div>

  <div class="concern-card legal">
    <div class="concern-number">2</div>
    <h3>위헌 소지</h3>
    <p><strong>쟁점:</strong> 본질적 사항(대리권)을 시행령에 위임하는 것은 법률유보 원칙에 위반</p>
    <p><strong>위험:</strong> 입법권 침해, 법체계 교란</p>
  </div>

  <div class="concern-card gdpr">
    <div class="concern-number">3</div>
    <h3>GDPR 기준 불일치</h3>
    <p><strong>쟁점:</strong> "타인의 권리와 자유"(영업비밀)를 보호하는 GDPR 제20조 4항에 해당하는 장치 부재</p>
    <p><strong>위험:</strong> 국제 규범 이탈, 재산권 침해</p>
  </div>

  <div class="concern-card market">
    <div class="concern-number">4</div>
    <h3>시장 왜곡</h3>
    <p><strong>쟁점:</strong> 전문기관에 대한 배타적 특혜가 데이터 무임승차를 가능하게 함</p>
    <p><strong>위험:</strong> 시장 조작, 생태계 파괴</p>
  </div>

  <div class="concern-card security">
    <div class="concern-number">5</div>
    <h3>보안 위험</h3>
    <p><strong>쟁점:</strong> 화면 스크래핑을 허용하고 단일 장애점(SPOF)을 형성</p>
    <p><strong>위험:</strong> 아이디·비밀번호 노출, 전국 동시 데이터 유출</p>
  </div>

  <div class="concern-card economic">
    <div class="concern-number">6</div>
    <h3>경제적 부담</h3>
    <p><strong>쟁점:</strong> 영업비밀 공개를 강제하고 과도한 준수 비용을 부과</p>
    <p><strong>위험:</strong> 경쟁력 약화, 성장 저해</p>
  </div>

  <div class="concern-card consistency">
    <div class="concern-number">7</div>
    <h3>정책 비일관성</h3>
    <p><strong>쟁점:</strong> 금융위원회의 스크래핑 금지 조치(2022년)와 모순</p>
    <p><strong>위험:</strong> 행정 일관성 상실</p>
  </div>
</div>

</div>

<div data-lang="en">

<div class="concern-grid">
  <div class="concern-card procedural">
    <div class="concern-number">1</div>
    <h3>Procedural Violation</h3>
    <p><strong>Issue:</strong> Re-proposing rejected content only 4 months after Regulatory Reform Committee decision</p>
    <p><strong>Risk:</strong> Undermines regulatory review process, erodes administrative credibility</p>
  </div>

  <div class="concern-card legal">
    <div class="concern-number">2</div>
    <h3>Constitutional Issues</h3>
    <p><strong>Issue:</strong> Delegation of essential matters (proxy rights) to enforcement decree violates legal reservation principle</p>
    <p><strong>Risk:</strong> Legislative power infringement, legal system disruption</p>
  </div>

  <div class="concern-card gdpr">
    <div class="concern-number">3</div>
    <h3>GDPR Non-Compliance</h3>
    <p><strong>Issue:</strong> Lacks GDPR Article 20(4) protection for "rights and freedoms of others" (trade secrets)</p>
    <p><strong>Risk:</strong> International norm deviation, property rights violation</p>
  </div>

  <div class="concern-card market">
    <div class="concern-number">4</div>
    <h3>Market Distortion</h3>
    <p><strong>Issue:</strong> Exclusive privileges to specialized agencies enable data free-riding</p>
    <p><strong>Risk:</strong> Market manipulation, ecosystem destruction</p>
  </div>

  <div class="concern-card security">
    <div class="concern-number">5</div>
    <h3>Security Risks</h3>
    <p><strong>Issue:</strong> Allows screen scraping, creates Single Point of Failure (SPOF)</p>
    <p><strong>Risk:</strong> ID/PW exposure, nationwide simultaneous data breach</p>
  </div>

  <div class="concern-card economic">
    <div class="concern-number">6</div>
    <h3>Economic Burden</h3>
    <p><strong>Issue:</strong> Forces trade secret disclosure, imposes excessive compliance costs</p>
    <p><strong>Risk:</strong> Competitiveness erosion, growth inhibition</p>
  </div>

  <div class="concern-card consistency">
    <div class="concern-number">7</div>
    <h3>Policy Inconsistency</h3>
    <p><strong>Issue:</strong> Contradicts Financial Services Commission's scraping ban (2022)</p>
    <p><strong>Risk:</strong> Administrative consistency loss</p>
  </div>
</div>

</div>

---

## Deep Dive: GDPR Compliance Gap

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="timelineChart"></canvas>
</div>

<div class="vs-divider">
  <div class="vs-badge">VS</div>
</div>

<div data-lang="ko">

<div class="comparison-grid">
  <div class="comparison-card current">
    <h3>GDPR 방식(균형)</h3>
    <ul style="line-height: 2;">
      <li>정보주체의 권리를 보호</li>
      <li>사업자의 재산권을 존중</li>
      <li>영업비밀을 명시적으로 보호</li>
      <li>기술적 실행 가능성을 고려</li>
      <li>균형 잡힌 접근</li>
    </ul>
    <div class="highlight-box info" style="margin-top: 1.5rem;">
      <strong>GDPR 제20조 4항:</strong><br>
      "제1항에 명시된 권리는 <strong>타인의 권리와 자유를 부당하게 침해해서는 안 된다.</strong>"
    </div>
  </div>

  <div class="comparison-card proposed">
    <h3>한국 개정안(불균형)</h3>
    <ul style="line-height: 2;">
      <li>정보주체의 권리를 보호</li>
      <li>사업자의 재산권을 무시</li>
      <li>영업비밀 보호 없음</li>
      <li>무조건적 전송 의무</li>
      <li>일방적 규제</li>
    </ul>
    <div class="highlight-box danger" style="margin-top: 1.5rem;">
      <strong>치명적 결함:</strong><br>
      구매 패턴, 가격 정책, 고객 세분화, 판매자 정보 등 수년간의 투자로 축적한 영업비밀임에도, "정당한 사유" 없이 핵심 사업 데이터의 전송을 강제
    </div>
  </div>
</div>

### 유럽연합 제29조 작업반 지침(WP242)

유럽연합의 권위 있는 해석은 명확한 경계를 제시한다.

<table class="data-table">
<thead>
<tr>
<th>원칙</th>
<th>유럽연합 해석</th>
<th>한국 개정안</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>정보주체가 "제공한" 데이터</strong></td>
<td>이용자가 직접 제공한 데이터로 한정하며, 기업이 생성한 분석 자료는 제외</td>
<td>그러한 제한 없음</td>
</tr>
<tr>
<td><strong>"가공 산물" 제외</strong></td>
<td>기업의 가공 산물(신용점수, 추천 알고리즘)을 명시적으로 제외</td>
<td>규정 없음</td>
</tr>
<tr>
<td><strong>타인의 권리와 자유</strong></td>
<td>영업비밀이나 데이터베이스 제작자의 권리를 침해할 수 없음</td>
<td><strong>보호 조항 없음</strong></td>
</tr>
<tr>
<td><strong>기술적 실행 가능성</strong></td>
<td>"기술적으로 가능한 경우"에만 직접 전송</td>
<td>무조건적 의무</td>
</tr>
</tbody>
</table>

</div>

<div data-lang="en">

<div class="comparison-grid">
  <div class="comparison-card current">
    <h3>GDPR Approach (Balanced)</h3>
    <ul style="line-height: 2;">
      <li>Protects data subject rights</li>
      <li>Respects business property rights</li>
      <li>Explicitly protects trade secrets</li>
      <li>Considers technical feasibility</li>
      <li>Balanced approach</li>
    </ul>
    <div class="highlight-box info" style="margin-top: 1.5rem;">
      <strong>GDPR Article 20(4):</strong><br>
      "The right referred to in paragraph 1 <strong>shall not adversely affect the rights and freedoms of others.</strong>"
    </div>
  </div>

  <div class="comparison-card proposed">
    <h3>Korean Amendment (Unbalanced)</h3>
    <ul style="line-height: 2;">
      <li>Protects data subject rights</li>
      <li>Ignores business property rights</li>
      <li>No trade secret protection</li>
      <li>Unconditional transfer obligation</li>
      <li>One-sided regulation</li>
    </ul>
    <div class="highlight-box danger" style="margin-top: 1.5rem;">
      <strong>Critical Flaw:</strong><br>
      Forces transfer of core business data (purchase patterns, pricing policies, customer segmentation, seller information) without "legitimate grounds" despite being trade secrets accumulated through years of investment
    </div>
  </div>
</div>

### EU Article 29 Working Party Guidelines (WP242)

The EU's authoritative interpretation provides clear boundaries:

<table class="data-table">
<thead>
<tr>
<th>Principle</th>
<th>EU Interpretation</th>
<th>Korean Amendment</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>"Provided by" data subject</strong></td>
<td>Limited to data directly provided by user; excludes company-generated analytics</td>
<td>No such limitation</td>
</tr>
<tr>
<td><strong>"Work product" exclusion</strong></td>
<td>Company work products (credit scores, recommendation algorithms) explicitly excluded</td>
<td>Not addressed</td>
</tr>
<tr>
<td><strong>Rights and freedoms of others</strong></td>
<td>Cannot violate trade secrets or database maker's rights</td>
<td><strong>No protection clause</strong></td>
</tr>
<tr>
<td><strong>Technical feasibility</strong></td>
<td>Direct transfer only "where technically feasible"</td>
<td>Unconditional obligation</td>
</tr>
</tbody>
</table>

</div>

<div class="chart-container" style="height: 450px; margin: 3rem 0;">
  <canvas id="gdprComplianceChart"></canvas>
</div>

---

<div data-lang="ko">

## 금융 분야의 역설: 규제의 자기모순

<div class="highlight-box danger">
<h3>금융위원회(2022년): 보안 위험을 이유로 화면 스크래핑 금지</h3>

**경과:**
- **2020년 8월 5일:** 신용정보법 개정으로 마이데이터 법적 근거 마련
- **2021년 12월 1일:** 마이데이터 시범 서비스 시작(17개 기관) - 스크래핑 한시 허용
- **2022년 1월 5일:** **화면 스크래핑 전면 금지, API 방식 의무화**

**공식 근거(금융위 보도자료, 2022년 1월 4일):**

> "2022년 1월 5일부터 화면 스크래핑은 전면 금지되며, 마이데이터 사업자는 모든 이용자에게 오직 API 방식으로만 서비스를 제공해야 한다."

**제기된 보안 우려:**
<table class="data-table">
<thead>
<tr>
<th>위험</th>
<th>내용</th>
</tr>
</thead>
<tbody>
<tr>
<td>아이디·비밀번호 직접 수집</td>
<td>마이데이터 사업자가 이용자의 아이디와 비밀번호를 직접 수집·저장해야 함</td>
</tr>
<tr>
<td>일방향 암호화 사용 불가</td>
<td>비밀번호를 평문 또는 복호화 가능한 방식으로 저장해야 하므로, 해킹 시 대량 유출 위험</td>
</tr>
<tr>
<td>2차 인증 우회</td>
<td>2차 인증, 일회용 비밀번호 등 추가 보안 수단을 우회해야 함</td>
</tr>
<tr>
<td>불분명한 책임 소재</td>
<td>유출 시 금융기관과 사업자 사이의 책임이 불분명</td>
</tr>
</tbody>
</table>

**API 방식의 장점:**
- 금융기관이 전송을 통제 → 책임 소재가 명확
- 토큰 기반 인증 → 비밀번호 노출 없음
- 전송 범위 한정 → 필요한 데이터만 전송
- 전송 이력 추적 가능 → 감사 가능
- 전송 계층 보안 암호화 → 안전한 전송
</div>

<div class="highlight-box warning">
<h3>개인정보보호위원회(2025년): 스크래핑을 "자동화 도구"로 허용</h3>

**근거:**
- "권리 행사의 편의성"
- "기술적 유연성"
- **명확한 보안 조치 없음**

**예상 결과:** 금융위원회가 금지한 위험의 재발

**범위:** 전자상거래, 플랫폼, 게임, 교육, 문화·여가 등 전 산업
</div>

<div class="highlight-box danger">
<h3>논리적 모순</h3>

<strong>규제 비일관성:</strong>
1. 금융 정보는 중요하다 → 스크래핑 금지
2. 의료, 쇼핑, 교육 정보는 중요하지 않다 → 스크래핑 허용?

<strong>개인정보 보호법 제29조 위반:</strong>

> **제29조(안전조치 의무):** 개인정보처리자는 개인정보가 분실·도난·유출·위조·변조 또는 훼손되지 않도록 내부 관리계획을 수립하고 접속기록을 보관하며, 대통령령으로 정하는 바에 따라 안전성 확보에 필요한 기술적·관리적·물리적 조치를 해야 한다.

→ **스크래핑 허용은 안전성 확보 의무와 정면으로 모순된다**

**결과:** 개인정보 보호 원칙의 일관성 상실
</div>

</div>

<div data-lang="en">

## The Financial Sector Paradox: Regulatory Self-Contradiction

<div class="highlight-box danger">
<h3>Financial Services Commission (2022): Screen Scraping Banned as Security Risk</h3>

**Timeline:**
- **August 5, 2020:** Credit Information Act amended - MyData legal framework established
- **December 1, 2021:** MyData pilot service launched (17 institutions) - Scraping temporarily allowed
- **January 5, 2022:** **Screen scraping completely banned, API-only mandate**

**Official Rationale (FSC Press Release, Jan 4, 2022):**

> "From January 5, 2022, screen scraping is completely prohibited and MyData operators must provide services exclusively through API methods to all users."

**Security Concerns Cited:**
<table class="data-table">
<thead>
<tr>
<th>Risk</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>ID/PW Direct Collection</td>
<td>MyData operators must directly collect and store user IDs and passwords</td>
</tr>
<tr>
<td>Inability to Use One-Way Encryption</td>
<td>Passwords must be stored in plaintext or reversible encryption → mass breach risk if hacked</td>
</tr>
<tr>
<td>2FA Bypass</td>
<td>Must circumvent additional security measures like 2FA, OTP</td>
</tr>
<tr>
<td>Unclear Liability</td>
<td>Responsibility unclear between financial institutions and operators in case of breach</td>
</tr>
</tbody>
</table>

**API Benefits:**
- Financial institution controls transfer → clear liability
- Token-based authentication → no password exposure
- Limited transfer scope → only necessary data
- Traceable transfer history → auditable
- TLS encryption → secure transmission
</div>

<div class="highlight-box warning">
<h3>Personal Information Protection Commission (2025): Allowing Scraping as "Automated Tool"</h3>

**Justification:**
- "Convenience for exercising rights"
- "Technical flexibility"
- **No clear security measures**

**Expected Result:** Revival of risks that FSC banned

**Scope:** E-commerce, platforms, gaming, education, culture & leisure - ALL industries
</div>

<div class="highlight-box danger">
<h3>The Logical Contradiction</h3>

<strong>Regulatory Inconsistency:</strong>
1. Financial information is important → scraping banned
2. Medical, shopping, education information is not important → scraping allowed?

<strong>Violation of Personal Information Protection Act Article 29:</strong>

> **Article 29 (Security Measures Obligation):** Personal information controllers must establish internal management plans, maintain access records, and take technical, administrative, and physical measures necessary to ensure safety as prescribed by Presidential Decree to prevent personal information from being lost, stolen, leaked, forged, altered, or damaged.

→ **Allowing scraping directly contradicts the obligation to ensure security**

**Result:** Loss of consistency in personal information protection principles
</div>

</div>

<!-- CHART:regulatoryContradiction -->

---

<div data-lang="ko">

## 전문기관 특혜 문제

<div class="highlight-box danger">
<h3>합법적 데이터 브로커의 탄생</h3>

**시행령 개정안 제42조의9(개인정보관리 전문기관의 업무):**

1. 정보주체로부터 받은 개인정보의 통합 조회
2. 정보주체를 위한 맞춤형 서비스 제공
3. 개인정보 활용 관련 연구 및 교육
4. **그 밖에 개인정보보호위원회가 정하는 업무** → 사실상 데이터 수집·분석·활용 사업

<strong>핵심 쟁점:</strong> 전문기관은 수집한 정보를 미끼(예: 커피 쿠폰)로 활용해 정보주체로부터 추가 동의를 받은 뒤, 이 정보를 제3자에게 판매하거나 상업적으로 이용할 수 있다. **이는 개인정보 거래와 유통의 합법적 통로를 열어 준다.**
</div>

**위원회가 밝힌 목표(2025년 6월 입법예고):**

> "새로운 사업 기회를 통한 데이터 경제 활성화"

→ 이는 정보주체 보호 조치가 아니라 **산업정책 목표**임을 자인한 것

### 무임승차 구조

<table class="data-table">
<thead>
<tr>
<th>주체</th>
<th>투자와 노력</th>
<th>결과</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>플랫폼 기업</strong></td>
<td>
<ul>
<li>수년간의 서비스 개발 투자</li>
<li>고객 확보를 위한 마케팅 비용</li>
<li>데이터 분석 인프라</li>
<li>개인정보 보호 체계</li>
</ul>
</td>
<td><strong>자산의 강제 전송</strong></td>
</tr>
<tr>
<td><strong>전문기관</strong></td>
<td>
<ul>
<li>투자나 혁신 없음</li>
<li>정부 인가만 취득</li>
<li>시행령의 의무 규정에 의존</li>
</ul>
</td>
<td><strong>무상으로 데이터 수집 → 자체 수익 사업</strong></td>
</tr>
</tbody>
</table>

</div>

<div data-lang="en">

## The Specialized Agency Privilege Problem

<div class="highlight-box danger">
<h3>Creating Legal Data Brokers</h3>

**Enforcement Decree Draft Article 42-9 (Duties of Personal Information Management Specialized Agencies):**

1. Integrated inquiry of personal information received from data subjects
2. Providing customized services for data subjects
3. Research and education related to personal information utilization
4. **Other duties determined by the Personal Information Protection Commission** → Effectively: data collection, analysis, and utilization business

<strong>Critical Issue:</strong> Specialized agencies can use collected information as bait (e.g., coffee coupons) to obtain additional consent from data subjects, then sell or commercially exploit this information to third parties. **This opens a legitimate channel for personal information trading and distribution.**
</div>

**Commission's Stated Objective (June 2025 Legislative Notice):**

> "Activate data economy through new business opportunities"

→ Admits this is an **industrial policy goal**, not a data subject protection measure

### The Free-Riding Structure

<table class="data-table">
<thead>
<tr>
<th>Actor</th>
<th>Investment & Effort</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Platform Companies</strong></td>
<td>
<ul>
<li>Years of service development investment</li>
<li>Customer acquisition marketing costs</li>
<li>Data analysis infrastructure</li>
<li>Personal information protection systems</li>
</ul>
</td>
<td><strong>Forced asset transfer</strong></td>
</tr>
<tr>
<td><strong>Specialized Agencies</strong></td>
<td>
<ul>
<li>No investment or innovation</li>
<li>Only government license acquired</li>
<li>Rely on enforcement decree mandate</li>
</ul>
</td>
<td><strong>Free data collection → Own revenue business</strong></td>
</tr>
</tbody>
</table>

</div>

---

<div data-lang="ko">

## 단일 장애점(SPOF): 국가 안보 위험

<div class="highlight-box danger">
<h3>분산된 위험에서 집중된 재앙으로</h3>

**현행 체계(분산형):**
- 쇼핑 사이트 유출 → 구매 이력만
- 병원 유출 → 진료 기록만
- **피해 범위가 한정됨**

**개정안 체계(집중형):**
- 전문기관 유출 → **삶의 이력 전체가 노출**
- **모든 국민이 동시에 피해**
- **국가적 재난**
</div>

### 전문기관 한 곳이 개인에 대해 알게 되는 정보:

<table class="data-table">
<thead>
<tr>
<th>분류</th>
<th>정보</th>
</tr>
</thead>
<tbody>
<tr>
<td>의료</td>
<td>진료 기록, 처방, 건강검진, 유전 정보</td>
</tr>
<tr>
<td>통신</td>
<td>통화 내역, 메시지, 위치 데이터, 인터넷 이용</td>
</tr>
<tr>
<td>금융</td>
<td>계좌 잔액, 거래 내역, 카드 사용, 대출</td>
</tr>
<tr>
<td>쇼핑</td>
<td>구매 이력, 찜 목록, 결제 수단, 배송지</td>
</tr>
<tr>
<td>교육</td>
<td>학습 기록, 성적, 수강 이력</td>
</tr>
<tr>
<td>민감</td>
<td>성인용품, 임신 정보, 개인적 취향</td>
</tr>
</tbody>
</table>

→ **삶의 전체 프로필이 한곳에 집중**

### 유출 시나리오:

**A씨:** 임신(산부인과) + 성인용품(쇼핑) + 특정 위치(위치정보) + 금융 거래 = **사생활 전면 노출**

**전문기관 유출 시:** A씨 같은 5,000만 명이 **동시에 피해**

</div>

<div data-lang="en">

## Single Point of Failure (SPOF): A National Security Risk

<div class="highlight-box danger">
<h3>From Distributed Risk to Concentrated Catastrophe</h3>

**Current System (Distributed):**
- Shopping site breach → Purchase history only
- Hospital breach → Medical records only
- **Limited damage scope**

**Amendment System (Centralized):**
- Specialized agency breach → **Entire life history exposed**
- **All citizens affected simultaneously**
- **National-level disaster**
</div>

### What One Specialized Agency Would Know About Each Person:

<table class="data-table">
<thead>
<tr>
<th>Category</th>
<th>Information</th>
</tr>
</thead>
<tbody>
<tr>
<td>Medical</td>
<td>Medical records, prescriptions, health checkups, genetic information</td>
</tr>
<tr>
<td>Telecom</td>
<td>Call history, messages, location data, internet usage</td>
</tr>
<tr>
<td>Financial</td>
<td>Account balances, transaction history, card usage, loans</td>
</tr>
<tr>
<td>Shopping</td>
<td>Purchase history, wish lists, payment methods, delivery addresses</td>
</tr>
<tr>
<td>Education</td>
<td>Learning records, grades, course history</td>
</tr>
<tr>
<td>Sensitive</td>
<td>Adult products, pregnancy info, personal preferences</td>
</tr>
</tbody>
</table>

→ **Complete life profile in one location**

### Breach Scenario:

**Person A:** Pregnancy (obstetrics) + Adult products (shopping) + Specific locations (GPS) + Financial transactions = **Complete privacy exposure**

**Specialized agency breach:** 50 million people like Person A **simultaneously affected**

</div>

<!-- CHART:spofRisk -->

---

<div data-lang="ko">

## 경제적 영향: 스타트업을 짓누르다

### 실제 금융 마이데이터 비용

<table class="data-table">
<thead>
<tr>
<th>항목</th>
<th>비용</th>
</tr>
</thead>
<tbody>
<tr>
<td>전체 시스템 구축(전 기관)</td>
<td>약 372억 원</td>
</tr>
<tr>
<td>연간 운영 비용(전 기관)</td>
<td>약 921억 원</td>
</tr>
<tr>
<td>연간 총비용</td>
<td>약 1,293억 원</td>
</tr>
<tr>
<td>기관당 평균 비용</td>
<td>수억 원에서 수십억 원(규모에 따라 상이)</td>
</tr>
</tbody>
</table>

*출처: 금융위원회 발표(2023년 1월 10일), 삼정KPMG 비용 분석*

</div>

<div data-lang="en">

## Economic Impact: Crushing Startups

### Actual Financial MyData Costs

<table class="data-table">
<thead>
<tr>
<th>Item</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Total System Construction (All institutions)</td>
<td>~37.2B KRW</td>
</tr>
<tr>
<td>Annual Operating Cost (All institutions)</td>
<td>~92.1B KRW</td>
</tr>
<tr>
<td>Annual Total Cost</td>
<td>~129.3B KRW</td>
</tr>
<tr>
<td>Average Cost Per Institution</td>
<td>Hundreds of millions to billions KRW (varies by size)</td>
</tr>
</tbody>
</table>

*Source: Financial Services Commission announcement (Jan 10, 2023), Samjong KPMG cost analysis*

</div>

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="costImpactChart"></canvas>
</div>

<div data-lang="ko">

### 전 산업 확대의 영향(추정)

- **대상 기업:** 매출 1,500억 원 이상 및 이용자 100만 명 이상
- **추정 기업 수:** 100~200개(전자상거래, 의료, 통신 등)
- **금융권과 달리:** 인프라를 처음부터 새로 구축해야 함
- **기업당 초기 비용:** 수천만 원에서 수억 원
- **총 추정 비용:** 최소 수천억 원에서 수조 원

<div class="highlight-box warning">
<h3>스타트업 성장의 함정</h3>

**딜레마:**

<strong>이용자 50만 명</strong> → 성장, 데이터 축적, 투자 유치

<strong>이용자 100만 명 도달</strong> → 전송 의무 발생 → API 구축에 수천만 원 비용

<strong>선택</strong> → 추가 성장 = 막대한 비용 + 핵심 데이터 노출

<strong>결과</strong> → 이용자 100만 명 직전에 성장을 멈춤 → 혁신 동력 상실

**역설:** "매출 1,500억 원 및 이용자 100만 명" 기준은 "대기업"을 겨냥한다고 홍보되지만, 실제로는 **성장 중인 기업에 가장 큰 타격**을 준다.
</div>

</div>

<div data-lang="en">

### All-Industry Expansion Impact (Estimated)

- **Target companies:** Revenue ≥150B KRW & ≥1M users
- **Estimated number:** 100-200 companies (e-commerce, medical, telecom, etc.)
- **Unlike financial sector:** Must build new infrastructure from scratch
- **Initial cost per company:** Tens to hundreds of millions KRW
- **Total estimated cost:** Minimum hundreds of billions to trillions of KRW

<div class="highlight-box warning">
<h3>The Startup Growth Trap</h3>

**The Dilemma:**

<strong>500K users</strong> → Growth, data accumulation, investment attraction

<strong>1M users milestone</strong> → Transfer obligation triggered → API construction costs tens of millions KRW

<strong>Choice</strong> → More growth = Massive costs + Core data exposure

<strong>Result</strong> → Stop growth just before 1M users → Loss of innovation momentum

**Irony:** The threshold "Revenue 150B KRW & 1M users" is marketed as targeting "large businesses" but actually hits **growing companies the hardest**.
</div>

</div>

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="startupGrowthTrap"></canvas>
</div>

<!-- CHART:startupGrowthTrap -->

---

<div data-lang="ko">

## 영업비밀 침해

<div class="highlight-box danger">
<h3>부정경쟁방지 및 영업비밀보호에 관한 법률 제2조 제2호</h3>

> "영업비밀"이란 공공연히 알려져 있지 않고 독립된 경제적 가치를 가지며, 상당한 노력으로 비밀로 유지·관리된 생산방법, 판매방법, 그 밖에 영업활동에 유용한 기술상 또는 경영상의 정보를 말한다.
</div>

### 위험에 처한 전자상거래 플랫폼의 영업비밀

<table class="data-table">
<thead>
<tr>
<th>정보 유형</th>
<th>영업비밀 해당성</th>
<th>전송 강제 여부</th>
</tr>
</thead>
<tbody>
<tr>
<td>구매 패턴</td>
<td>수년간의 분석 투자</td>
<td><strong>강제</strong></td>
</tr>
<tr>
<td>가격 정책</td>
<td>핵심 경쟁 우위</td>
<td><strong>강제</strong></td>
</tr>
<tr>
<td>고객 세분화</td>
<td>AI·머신러닝 투자</td>
<td><strong>강제</strong></td>
</tr>
<tr>
<td>판매자 정보</td>
<td>거래처 데이터</td>
<td><strong>강제</strong></td>
</tr>
</tbody>
</table>

### 데이터 유출 경로

**전문기관이 얻는 것:**
- 수백만 소비자의 구매 패턴
- 가격 민감도, 선호 상품, 구매 시점
- 이는 플랫폼이 수년간의 투자로 축적한 영업비밀과 같다

**결과:**
- 전문기관이 무상으로 취득
- 자체 서비스에 활용
- **한국 전자상거래의 경쟁 우위가 약화**

<div class="comparison-grid" style="margin-top: 2rem;">
  <div class="comparison-card current">
    <h3>GDPR 보호</h3>
    <p><strong>"타인의 권리와 자유를 부당하게 침해해서는 안 된다"</strong></p>
    <p>→ 영업비밀이 침해되면 거부 가능</p>
  </div>
  <div class="comparison-card proposed">
    <h3>한국 개정안</h3>
    <p><strong>영업비밀 보호 조항 없음</strong></p>
    <p>→ 무조건적 강제 전송</p>
  </div>
</div>

</div>

<div data-lang="en">

## Trade Secret Violation

<div class="highlight-box danger">
<h3>Unfair Competition Prevention Act Article 2, Paragraph 2</h3>

> "Trade secret" means production methods, sales methods, and other technical or business information useful for business activities that is not publicly known, has independent economic value, and has been maintained as confidential through considerable effort.
</div>

### E-Commerce Platform Trade Secrets at Risk

<table class="data-table">
<thead>
<tr>
<th>Information Type</th>
<th>Trade Secret Status</th>
<th>Transfer Mandate</th>
</tr>
</thead>
<tbody>
<tr>
<td>Purchase Patterns</td>
<td>Years of analysis investment</td>
<td><strong>Forced</strong></td>
</tr>
<tr>
<td>Pricing Policies</td>
<td>Core competitive advantage</td>
<td><strong>Forced</strong></td>
</tr>
<tr>
<td>Customer Segmentation</td>
<td>AI/ML investment</td>
<td><strong>Forced</strong></td>
</tr>
<tr>
<td>Seller Information</td>
<td>Business partner data</td>
<td><strong>Forced</strong></td>
</tr>
</tbody>
</table>

### The Data Leakage Path

**Specialized Agency Gains:**
- Purchase patterns of millions of consumers
- Price sensitivity, preferred products, purchase timing
- This equals trade secrets accumulated by platforms through years of investment

**Result:**
- Specialized agency acquires for free
- Uses for own services
- **Korean e-commerce competitive advantage eroded**

<div class="comparison-grid" style="margin-top: 2rem;">
  <div class="comparison-card current">
    <h3>GDPR Protection</h3>
    <p><strong>"shall not adversely affect the rights and freedoms of others"</strong></p>
    <p>→ Can refuse if trade secrets are infringed</p>
  </div>
  <div class="comparison-card proposed">
    <h3>Korean Amendment</h3>
    <p><strong>NO trade secret protection clause</strong></p>
    <p>→ Unconditional forced transfer</p>
  </div>
</div>

</div>

---

<div data-lang="ko">

## 네 가지 핵심 해법

<div class="solution-grid">
  <div class="solution-card">
    <h3>1. 개정안 철회 및 위원회 권고 준수</h3>
    <ul>
      <li>2025년 6월 개정안을 즉시 철회</li>
      <li>2024년 8월 규제개혁위원회 결정을 준수</li>
      <li>현행 시행령(3개 분야)을 유지</li>
      <li>재검토에 앞서 충분한 시범 운영</li>
    </ul>
  </div>

  <div class="solution-card">
    <h3>2. 법률유보: 국회 입법</h3>
    <ul>
      <li>시행령에서 대리권 조항을 삭제</li>
      <li>대리권의 본질적 사항은 법률로 규율</li>
      <li>국회 심의를 통한 사회적 합의</li>
    </ul>
  </div>

  <div class="solution-card">
    <h3>3. GDPR 방식 채택</h3>
    <ul>
      <li>전문기관 집중화를 폐지</li>
      <li>본인 내려받기 권리를 우선</li>
      <li>영업비밀과 데이터베이스 권리를 명시적으로 보호</li>
      <li>시장 자율을 장려</li>
    </ul>
  </div>

  <div class="solution-card">
    <h3>4. 보안 강화: 스크래핑 금지</h3>
    <ul>
      <li>금융위원회와 동일하게 스크래핑 금지</li>
      <li>표준 API만 허용</li>
      <li>분산 구조로 단일 장애점 방지</li>
    </ul>
  </div>
</div>

</div>

<div data-lang="en">

## Four Essential Solutions

<div class="solution-grid">
  <div class="solution-card">
    <h3>1. Withdraw Amendment & Follow Committee Guidance</h3>
    <ul>
      <li>Immediately withdraw June 2025 amendment</li>
      <li>Comply with August 2024 Regulatory Reform Committee decision</li>
      <li>Maintain current enforcement decree (3 sectors)</li>
      <li>Sufficient pilot operation before reconsidering</li>
    </ul>
  </div>

  <div class="solution-card">
    <h3>2. Legal Reservation - National Assembly Legislation</h3>
    <ul>
      <li>Delete proxy rights clause from enforcement decree</li>
      <li>Regulate essential proxy rights matters by law</li>
      <li>Social consensus through National Assembly deliberation</li>
    </ul>
  </div>

  <div class="solution-card">
    <h3>3. Adopt GDPR Approach</h3>
    <ul>
      <li>Abolish specialized agency centralization</li>
      <li>Prioritize self-download rights</li>
      <li>Explicitly protect trade secrets & database rights</li>
      <li>Encourage market autonomy</li>
    </ul>
  </div>

  <div class="solution-card">
    <h3>4. Security Enhancement - Ban Scraping</h3>
    <ul>
      <li>Ban scraping same as Financial Services Commission</li>
      <li>Allow only standard APIs</li>
      <li>Prevent SPOF through distributed structure</li>
    </ul>
  </div>
</div>

</div>

---

<div data-lang="ko">

## 권고하는 GDPR형 조항

<div class="highlight-box info">
<h3>개정안 제○조(전송요구의 제한)</h3>

**① 다음의 경우 전송을 거부할 수 있다:**

1. 영업비밀 또는 지식재산을 포함하는 경우
2. 데이터베이스 제작자의 권리를 침해하는 경우
3. 타인의 권리와 자유를 침해하는 경우
4. 기술적으로 곤란하거나 과도한 비용이 드는 경우

**② 거부 시 사유를 통지할 의무**
</div>

</div>

<div data-lang="en">

## Recommended GDPR-Style Provisions

<div class="highlight-box info">
<h3>Proposed Amendment Article ○ (Limitations on Transfer Requests)</h3>

**① Transfer may be refused in the following cases:**

1. Contains trade secrets or intellectual property
2. Infringes database maker's rights
3. Violates rights and freedoms of others
4. Technically difficult or excessively costly

**② Obligation to notify reasons when refusing**
</div>

</div>

---

<div data-lang="ko">

## 결론: 균형이 필수다

<div class="highlight-box warning">
<h3>일곱 가지 핵심 우려 요약</h3>

<table class="data-table">
<thead>
<tr>
<th>번호</th>
<th>영역</th>
<th>핵심 문제</th>
<th>사회적 위험</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>절차적 정당성</td>
<td>위원회 권고를 무시하고 4개월 만에 재발의</td>
<td>규제 절차 무력화, 행정 신뢰 훼손</td>
</tr>
<tr>
<td>2</td>
<td>법적 타당성</td>
<td>법률유보 원칙 위반, 위헌적 대리권</td>
<td>입법권 침해, 법체계 교란</td>
</tr>
<tr>
<td>3</td>
<td>국제 기준 부합</td>
<td>GDPR 모순, 영업비밀 보호 부재</td>
<td>국제 규범 이탈, 재산권 무시</td>
</tr>
<tr>
<td>4</td>
<td>정책 공정성</td>
<td>전문기관 특혜, 데이터 무임승차</td>
<td>시장 왜곡, 생태계 파괴</td>
</tr>
<tr>
<td>5</td>
<td>보안 안정성</td>
<td>스크래핑 허용, 단일 장애점 형성</td>
<td>아이디·비밀번호 노출, 전국 동시 유출</td>
</tr>
<tr>
<td>6</td>
<td>경제적 합리성</td>
<td>영업비밀 노출, 과도한 비용</td>
<td>경쟁력 약화, 성장 저해</td>
</tr>
<tr>
<td>7</td>
<td>정책 일관성</td>
<td>금융위 조치와 모순, 자기모순</td>
<td>행정 일관성 상실</td>
</tr>
</tbody>
</table>
</div>

**이것은 "개인정보 보호"가 아니라 "규제를 통한 시장 재편"이다**

**"데이터 활성화"가 아니라 "데이터 통제"**  
**"혁신 촉진"이 아니라 "성장 규제"**  
**"보호 강화"가 아니라 "위험 집중"**

→ **신중한 재검토와 충분한 사회적 합의가 필요하다**

</div>

<div data-lang="en">

## Conclusion: Balance is Essential

<div class="highlight-box warning">
<h3>Seven Critical Concerns Summary</h3>

<table class="data-table">
<thead>
<tr>
<th>No.</th>
<th>Area</th>
<th>Core Problem</th>
<th>Social Risk</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Procedural Legitimacy</td>
<td>Ignoring Committee guidance, re-proposing after 4 months</td>
<td>Regulatory process nullification, administrative trust damage</td>
</tr>
<tr>
<td>2</td>
<td>Legal Validity</td>
<td>Violating legal reservation principle, unconstitutional proxy rights</td>
<td>Legislative power infringement, legal system disruption</td>
</tr>
<tr>
<td>3</td>
<td>Global Compliance</td>
<td>GDPR contradiction, lack of trade secret protection</td>
<td>International norm deviation, property rights ignored</td>
</tr>
<tr>
<td>4</td>
<td>Policy Fairness</td>
<td>Specialized agency privileges, data free-riding</td>
<td>Market distortion, ecosystem destruction</td>
</tr>
<tr>
<td>5</td>
<td>Security Stability</td>
<td>Allowing scraping, SPOF formation</td>
<td>ID/PW exposure, nationwide simultaneous breach</td>
</tr>
<tr>
<td>6</td>
<td>Economic Rationality</td>
<td>Trade secret exposure, excessive costs</td>
<td>Competitiveness erosion, growth inhibition</td>
</tr>
<tr>
<td>7</td>
<td>Policy Consistency</td>
<td>Contradicting FSC measures, self-contradiction</td>
<td>Administrative consistency loss</td>
</tr>
</tbody>
</table>
</div>

**This is not "personal information protection" but "market restructuring through regulation"**

**Not "data activation" but "data control"**  
**Not "innovation promotion" but "growth regulation"**  
**Not "protection enhancement" but "risk centralization"**

→ **Careful reconsideration and sufficient social consensus required**

</div>

---

<div data-lang="ko">

## 연구 정보

**발표일:** 2025년 11월 21일  
**행사:** 마이데이터 정책 스타트업 세미나  
**주최:** 한국스타트업포럼  
**장소:** 디캠프, 서울 강남  
**발표자:** 김용희(Yonghee Kim, Ph.D.)

**연구 분야:**
- 데이터 정책과 거버넌스
- 디지털 플랫폼 규제
- 스타트업 생태계 보호
- 규제 영향 분석

**연락처:**
- 이메일: yhkim1981@sunmoon.ac.kr
- 소속: 선문대학교 경영학과
- ORCID: 0000-0002-5643-2748

</div>

<div data-lang="en">

## Research Information

**Presentation Date:** November 21, 2025  
**Event:** MyData Policy Startup Seminar  
**Host:** Korea Startup Forum  
**Venue:** D.CAMP, Gangnam, Seoul  
**Speaker:** Yonghee Kim, Ph.D.

**Research Focus:**
- Data policy and governance
- Digital platform regulation
- Startup ecosystem protection
- Regulatory impact analysis

**Contact:**
- Email: yhkim1981@sunmoon.ac.kr
- Institution: Sunmoon University, Department of Business Administration
- ORCID: 0000-0002-5643-2748

</div>

---

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
function initMyDataCharts() {

  // Destroy existing charts to prevent canvas reuse errors
  if (typeof Chart !== 'undefined' && Chart.instances) {
    Object.values(Chart.instances).forEach(function(instance) {
      if (instance && typeof instance.destroy === 'function') {
        instance.destroy();
      }
    });
  }

  // 1. Seven Concerns Radar Chart
  const radarCtx = document.getElementById('sevenConcernsRadar');
  if (radarCtx) {
    new Chart(radarCtx, {
      type: 'radar',
      data: {
        labels: ['Procedural\nLegitimacy', 'Legal\nValidity', 'GDPR\nCompliance', 'Market\nFairness', 'Security', 'Economic\nImpact', 'Policy\nConsistency'],
        datasets: [{
          label: 'Risk Level',
          data: [95, 90, 85, 88, 92, 87, 90],
          backgroundColor: 'rgba(239, 68, 68, 0.2)',
          borderColor: 'rgb(239, 68, 68)',
          borderWidth: 3,
          pointBackgroundColor: 'rgb(239, 68, 68)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgb(239, 68, 68)',
          pointRadius: 6,
          pointHoverRadius: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          r: {
            beginAtZero: true,
            max: 100,
            ticks: { stepSize: 20, font: { size: 12 } },
            pointLabels: { font: { size: 13, weight: 'bold' } }
          }
        },
        plugins: {
          title: {
            display: true,
            text: 'Seven Critical Concerns - Risk Assessment',
            font: { size: 20, weight: 'bold' },
            padding: 20
          },
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: function(context) {
                return 'Risk Level: ' + context.parsed.r + '/100';
              }
            }
          }
        }
      }
    });
  }

  // 2. Timeline Comparison Chart
  const timelineCtx = document.getElementById('timelineChart');
  if (timelineCtx) {
    new Chart(timelineCtx, {
      type: 'line',
      data: {
        labels: ['2023-03\nLaw Passed', '2024-08\nCommittee\nDecision', '2025-02\nEnforcement\nDecree', '2025-03\nSystem\nLaunch', '2025-06\nControversial\nAmendment'],
        datasets: [
          {
            label: 'Regulatory Compliance',
            data: [100, 100, 100, 100, 30],
            borderColor: 'rgb(37, 99, 235)',
            backgroundColor: 'rgba(37, 99, 235, 0.1)',
            borderWidth: 3,
            tension: 0.4,
            fill: true,
            pointRadius: 6,
            pointHoverRadius: 8
          },
          {
            label: 'Industry Preparedness',
            data: [20, 40, 60, 70, 25],
            borderColor: 'rgb(245, 158, 11)',
            backgroundColor: 'rgba(245, 158, 11, 0.1)',
            borderWidth: 3,
            tension: 0.4,
            fill: true,
            pointRadius: 6,
            pointHoverRadius: 8
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: {
            display: true,
            text: 'Regulatory Timeline: Compliance vs. Industry Preparedness',
            font: { size: 18, weight: 'bold' },
            padding: 20
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 100,
            title: { display: true, text: 'Score (%)', font: { size: 14, weight: 'bold' } },
            ticks: { callback: function(value) { return value + '%'; } }
          },
          x: { title: { display: true, text: 'Timeline', font: { size: 14, weight: 'bold' } } }
        }
      }
    });
  }

  // 3. Scope Comparison Chart
  const comparisonCtx = document.getElementById('scopeComparison');
  if (comparisonCtx) {
    new Chart(comparisonCtx, {
      type: 'bar',
      data: {
        labels: ['Medical', 'Telecom', 'Energy', 'E-commerce', 'Gaming', 'Education', 'Hospitality', 'Culture'],
        datasets: [
          { label: 'Current (Feb 2025)', data: [1, 1, 1, 0, 0, 0, 0, 0], backgroundColor: 'rgba(37, 99, 235, 0.7)', borderColor: 'rgb(37, 99, 235)', borderWidth: 2 },
          { label: 'Proposed (June 2025)', data: [1, 1, 1, 1, 1, 1, 1, 1], backgroundColor: 'rgba(239, 68, 68, 0.7)', borderColor: 'rgb(239, 68, 68)', borderWidth: 2 }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: { display: true, text: 'Sector Coverage: Current (3 Sectors) vs. Proposed (ALL Sectors)', font: { size: 18, weight: 'bold' }, padding: 20 }
        },
        scales: {
          y: { beginAtZero: true, max: 1.2, ticks: { stepSize: 1, callback: function(value) { return value === 1 ? 'Included' : ''; } } }
        }
      }
    });
  }

  // 4. GDPR Compliance Gap Chart
  const gdprCtx = document.getElementById('gdprComplianceChart');
  if (gdprCtx) {
    new Chart(gdprCtx, {
      type: 'radar',
      data: {
        labels: ['Data Subject\nRights', 'Business\nRights', 'Trade Secret\nProtection', 'Technical\nFeasibility', 'Balanced\nApproach'],
        datasets: [
          { label: 'GDPR Standard', data: [90, 85, 90, 80, 95], backgroundColor: 'rgba(37, 99, 235, 0.2)', borderColor: 'rgb(37, 99, 235)', borderWidth: 3, pointBackgroundColor: 'rgb(37, 99, 235)', pointRadius: 6 },
          { label: 'Korean Amendment', data: [95, 30, 20, 40, 35], backgroundColor: 'rgba(239, 68, 68, 0.2)', borderColor: 'rgb(239, 68, 68)', borderWidth: 3, pointBackgroundColor: 'rgb(239, 68, 68)', pointRadius: 6 }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: { r: { beginAtZero: true, max: 100, ticks: { stepSize: 20 } } },
        plugins: { title: { display: true, text: 'GDPR Compliance Gap: EU Standard vs. Korean Amendment', font: { size: 18, weight: 'bold' }, padding: 20 } }
      }
    });
  }

  // 5. Cost Impact Chart
  const costCtx = document.getElementById('costImpactChart');
  if (costCtx) {
    new Chart(costCtx, {
      type: 'bar',
      data: {
        labels: ['System\nConstruction', 'Annual\nOperations', 'Security\nMeasures', 'Compliance\nStaff', 'Total Annual\nCost'],
        datasets: [{
          label: 'Estimated Cost (Million KRW)',
          data: [500, 300, 200, 150, 650],
          backgroundColor: ['rgba(239, 68, 68, 0.7)', 'rgba(245, 158, 11, 0.7)', 'rgba(59, 130, 246, 0.7)', 'rgba(139, 92, 246, 0.7)', 'rgba(16, 185, 129, 0.7)'],
          borderColor: ['rgb(239, 68, 68)', 'rgb(245, 158, 11)', 'rgb(59, 130, 246)', 'rgb(139, 92, 246)', 'rgb(16, 185, 129)'],
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: { display: true, text: 'Estimated Compliance Costs per Startup (Revenue 150B & 1M Users)', font: { size: 18, weight: 'bold' }, padding: 20 },
          legend: { display: false }
        },
        scales: {
          y: { beginAtZero: true, title: { display: true, text: 'Cost (Million KRW)', font: { size: 14, weight: 'bold' } }, ticks: { callback: function(value) { return value.toLocaleString() + 'M'; } } }
        }
      }
    });
  }

  // 6. Startup Growth Trap Chart
  const growthCtx = document.getElementById('startupGrowthTrap');
  if (growthCtx) {
    new Chart(growthCtx, {
      type: 'line',
      data: {
        labels: ['0', '200K', '400K', '600K', '800K', '1M', '1.2M', '1.5M'],
        datasets: [
          { label: 'Natural Growth Path', data: [0, 15, 35, 60, 85, 110, 140, 175], borderColor: 'rgb(16, 185, 129)', backgroundColor: 'rgba(16, 185, 129, 0.1)', borderWidth: 3, tension: 0.4, borderDash: [10, 5], pointRadius: 6 },
          { label: 'Actual Growth (Under Amendment)', data: [0, 15, 35, 60, 85, 95, 98, 100], borderColor: 'rgb(239, 68, 68)', backgroundColor: 'rgba(239, 68, 68, 0.1)', borderWidth: 3, tension: 0.4, pointRadius: 6, pointHoverRadius: 8 }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { title: { display: true, text: 'The Startup Growth Trap: Innovation Ceiling at 1M Users', font: { size: 18, weight: 'bold' }, padding: 20 } },
        scales: {
          y: { beginAtZero: true, title: { display: true, text: 'Growth Index', font: { size: 14, weight: 'bold' } } },
          x: { title: { display: true, text: 'User Base', font: { size: 14, weight: 'bold' } } }
        }
      }
    });
  }

}
document.addEventListener('DOMContentLoaded', initMyDataCharts);
document.addEventListener('astro:page-load', initMyDataCharts);
</script>

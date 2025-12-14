---
title: "본인전송요구권 확대가 가져올 사회적 문제와 대응 방안"
title_en: "The Right to Data Transfer: Social Problems and Response Plans"
subtitle: "개인정보보호법 시행령 개정안의 법적·정책적 문제점 검토"
subtitle_en: "Critical Analysis of Personal Information Protection Act Enforcement Decree Amendment"
date: "2025-11-21"
category: "Data Policy"
tags: ["MyData", "Data Privacy", "Regulation", "Policy Analysis", "Startup Ecosystem", "GDPR"]
keywords: ["MyData", "본인전송요구권", "개인정보보호법", "GDPR", "스타트업", "규제개혁", "데이터이동권", "Data Portability", "Privacy Regulation", "Startup Policy"]
methodology: ["Policy Analysis", "Legal Review", "Comparative Study (GDPR)", "Stakeholder Analysis", "Cost-Benefit Analysis"]
data_period:
  start: "2023-03"
  end: "2025-11"
related_publications: []
related_projects: []
conference: "MyData Policy Startup Seminar"
venue: "Korea Startup Forum, D.CAMP, Gangnam, Seoul"
description: "본인전송요구권 확대 개정안의 7가지 핵심 문제점 분석: 절차적 정당성 위반, 헌법적 문제, GDPR 불일치, 스타트업 생태계 위협"
description_en: "In-depth analysis of the proposed expansion of the Right to Request Data Transfer, examining seven critical concerns including regulatory procedural violations, constitutional issues, GDPR non-compliance, and threats to the startup ecosystem."
summary: "2025년 6월 개정안은 규제개혁위원회 권고(2024년 8월)를 무시하고, 헌법 원칙을 위반하며, GDPR 기준에 부합하지 않고, 전문기관에 대한 불공정 특혜를 통해 한국 스타트업 생태계를 파괴할 위험이 있음."
summary_en: "The June 2025 amendment proposal ignores Regulatory Reform Committee recommendations (August 2024), violates constitutional principles, contradicts GDPR standards, and threatens to destroy Korea's startup ecosystem through unfair privileges to specialized agencies."
key_findings:
  - "Procedural violation: Re-proposing rejected content only 4 months after Regulatory Reform Committee decision"
  - "Constitutional issue: Unconstitutional delegation of proxy rights via enforcement decree"
  - "GDPR non-compliance: Lack of trade secret protection unlike EU standards"
  - "Market distortion: Exclusive privileges to specialized agencies creating unfair advantage"
  - "Security risk: Allowing screen scraping despite financial sector ban"
  - "Economic burden: Estimated billions in compliance costs for startups reaching 1M users"
  - "Policy inconsistency: Contradicting Financial Services Commission's scraping ban (2022)"
policy_concerns:
  - "Expansion from 3 sectors (medical, telecom, energy) to ALL industries"
  - "Forcing core business data transfer without trade secret protection"
  - "Creating Single Point of Failure (SPOF) through data centralization"
  - "Imposing excessive costs on growing startups (Revenue 150B KRW & 1M users threshold)"
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

<h2 data-lang="en">Executive Summary: A Regulatory Overreach Threatening Innovation</h2>
<h2 data-lang="ko">핵심 요약: 혁신을 위협하는 규제 과잉</h2>

<p data-lang="en">On <strong>November 21, 2025</strong>, I presented at the <strong>MyData Policy Startup Seminar</strong> hosted by the Korea Startup Forum at D.CAMP in Gangnam, Seoul. As a researcher examining the intersection of data policy, regulation, and innovation, I raised serious concerns about the <strong>Personal Information Protection Act Enforcement Decree amendment</strong> proposed in June 2025.</p>
<p data-lang="ko"><strong>2025년 11월 21일</strong>, 강남 D.CAMP에서 한국스타트업포럼이 주최한 <strong>마이데이터 정책 스타트업 세미나</strong>에서 발표했습니다. 데이터 정책, 규제, 혁신의 교차점을 연구하는 연구자로서, 2025년 6월 제안된 <strong>개인정보보호법 시행령 개정안</strong>에 대한 심각한 우려를 제기했습니다.</p>

<p data-lang="en">The amendment, which aims to expand the "Right to Request Data Transfer" to all industries, represents <strong>a fundamental shift from data activation to data control</strong>—one that threatens to undermine Korea's startup ecosystem while violating established regulatory principles and international norms.</p>
<p data-lang="ko">"본인전송요구권"을 모든 산업으로 확대하려는 이 개정안은 <strong>데이터 활성화에서 데이터 통제로의 근본적 전환</strong>을 나타내며, 확립된 규제 원칙과 국제 규범을 위반하면서 한국 스타트업 생태계를 약화시킬 위험이 있습니다.</p>

<div class="highlight-box danger">
<h3 data-lang="en">Critical Alert</h3>
<h3 data-lang="ko">긴급 경고</h3>
<p data-lang="en"><strong>The June 2025 amendment proposal violates the Regulatory Reform Committee's August 2024 decision by re-proposing identical content only 4 months later.</strong> This procedural violation undermines administrative integrity and ignores legitimate industry concerns about security, costs, and trade secrets.</p>
<p data-lang="ko"><strong>2025년 6월 개정안은 규제개혁위원회의 2024년 8월 결정에서 불과 4개월 후 동일한 내용을 재제안함으로써 위반하고 있습니다.</strong> 이러한 절차적 위반은 행정 무결성을 훼손하고 보안, 비용, 영업비밀에 대한 업계의 정당한 우려를 무시합니다.</p>
</div>

---

<h2 data-lang="en">Timeline: From Cautious Approach to Regulatory Overreach</h2>
<h2 data-lang="ko">타임라인: 신중한 접근에서 규제 과잉으로</h2>

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-date">2023-03-14</div>
    <div class="timeline-content">
      <h4><span data-lang="en">Legal Framework Established</span><span data-lang="ko">법적 체계 수립</span></h4>
      <p data-lang="en">Personal Information Protection Act 2nd Amendment passes National Assembly, establishing Right to Request Data Transfer (Article 35-2)</p>
      <p data-lang="ko">개인정보보호법 2차 개정안이 국회를 통과, 본인전송요구권 신설 (제35조의2)</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2024-08-09</div>
    <div class="timeline-content warning">
      <h4><span data-lang="en">Regulatory Reform Committee Decision</span><span data-lang="ko">규제개혁위원회 결정</span></h4>
      <p><strong data-lang="en">Key Recommendations:</strong><strong data-lang="ko">주요 권고사항:</strong></p>
      <ul data-lang="en">
        <li>Limit to 3 sectors: Medical, Telecommunications, Energy</li>
        <li>Maintain consistency between self-transfer and third-party transfer scopes</li>
        <li>Allow sufficient preparation time for technical infrastructure</li>
        <li>Gradual expansion based on market readiness</li>
      </ul>
      <ul data-lang="ko">
        <li>3개 분야로 제한: 의료, 통신, 에너지</li>
        <li>본인전송과 제3자 전송 범위 간 일관성 유지</li>
        <li>기술 인프라 준비를 위한 충분한 시간 허용</li>
        <li>시장 준비 상황에 따른 점진적 확대</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2025-02-25</div>
    <div class="timeline-content">
      <h4><span data-lang="en">Enforcement Decree Enacted (Presidential Decree No. 35343)</span><span data-lang="ko">시행령 제정 (대통령령 제35343호)</span></h4>
      <p data-lang="en">Adopted Regulatory Reform Committee recommendations: Limited to 3 sectors (Medical, Telecom, Energy)</p>
      <p data-lang="ko">규제개혁위원회 권고 수용: 3개 분야(의료, 통신, 에너지)로 제한</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2025-03-13</div>
    <div class="timeline-content">
      <h4><span data-lang="en">System Launch</span><span data-lang="ko">시스템 출범</span></h4>
      <p data-lang="en">Right to Request Data Transfer system begins operation in 3 designated sectors</p>
      <p data-lang="ko">본인전송요구권 시스템이 지정된 3개 분야에서 운영 시작</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2025-06-23</div>
    <div class="timeline-content critical">
      <h4><span data-lang="en">Controversial Amendment Proposed</span><span data-lang="ko">논란의 개정안 제안</span></h4>
      <p data-lang="en"><strong>Personal Information Protection Commission re-proposes expansion to ALL industries</strong></p>
      <p data-lang="ko"><strong>개인정보보호위원회가 전 산업으로의 확대를 재제안</strong></p>
      <ul data-lang="en">
        <li>Ignores Regulatory Reform Committee decision from just 4 months prior</li>
        <li>Expands scope to: E-commerce, Platforms, Gaming, Education, Hospitality, Culture & Leisure</li>
        <li>Threshold: Revenue 150B KRW + 1M users</li>
        <li>Creates specialized agency privileges</li>
      </ul>
      <ul data-lang="ko">
        <li>불과 4개월 전 규제개혁위원회 결정 무시</li>
        <li>범위 확대: 전자상거래, 플랫폼, 게임, 교육, 숙박, 문화·레저</li>
        <li>기준: 매출 1,500억원 + 이용자 100만명</li>
        <li>전문기관 특혜 신설</li>
      </ul>
    </div>
  </div>
</div>

---

<h2 data-lang="en">The Expansion Trap: Current Law vs. Proposed Amendment</h2>
<h2 data-lang="ko">확대의 함정: 현행법 vs. 개정안</h2>

<div class="comparison-grid">
  <div class="comparison-card current">
    <h3><span data-lang="en">Current Enforcement Decree (Feb 2025)</span><span data-lang="ko">현행 시행령 (2025년 2월)</span></h3>
    <div class="metric-highlight"><span data-lang="en">3 Sectors</span><span data-lang="ko">3개 분야</span></div>
    <h4><span data-lang="en">Scope</span><span data-lang="ko">범위</span></h4>
    <ul data-lang="en">
      <li>Medical institutions</li>
      <li>Telecommunications carriers</li>
      <li>Energy providers</li>
    </ul>
    <ul data-lang="ko">
      <li>의료기관</li>
      <li>통신사업자</li>
      <li>에너지 공급자</li>
    </ul>
    <h4><span data-lang="en">Characteristics</span><span data-lang="ko">특징</span></h4>
    <ul data-lang="en">
      <li>Self-transfer = Third-party transfer scope</li>
      <li>Follows Regulatory Reform Committee guidance</li>
      <li>Gradual expansion principle</li>
      <li>Sufficient pilot period</li>
    </ul>
    <ul data-lang="ko">
      <li>본인전송 = 제3자 전송 범위</li>
      <li>규제개혁위원회 지침 준수</li>
      <li>점진적 확대 원칙</li>
      <li>충분한 시범 기간</li>
    </ul>
  </div>

  <div class="comparison-card proposed">
    <h3><span data-lang="en">Proposed Amendment (June 2025)</span><span data-lang="ko">개정안 (2025년 6월)</span></h3>
    <div class="metric-highlight"><span data-lang="en">ALL Industries</span><span data-lang="ko">전 산업</span></div>
    <h4><span data-lang="en">Scope</span><span data-lang="ko">범위</span></h4>
    <p><strong data-lang="en">Any entity meeting:</strong><strong data-lang="ko">다음 요건을 충족하는 모든 사업자:</strong></p>
    <ul data-lang="en">
      <li>Annual revenue ≥ 150B KRW <strong>AND</strong></li>
      <li>User base ≥ 1M persons</li>
      <li>Plus: All elementary/secondary/higher education institutions</li>
      <li>Plus: Any entity designated by Commission</li>
    </ul>
    <ul data-lang="ko">
      <li>연매출 ≥ 1,500억원 <strong>AND</strong></li>
      <li>이용자 ≥ 100만명</li>
      <li>추가: 모든 초·중·고·대학 교육기관</li>
      <li>추가: 위원회가 지정하는 모든 사업자</li>
    </ul>
    <h4><span data-lang="en">Problems</span><span data-lang="ko">문제점</span></h4>
    <ul data-lang="en">
      <li>Self-transfer ≠ Third-party transfer (inconsistent)</li>
      <li>Violates Regulatory Reform Committee decision</li>
      <li>Simultaneous expansion to all sectors</li>
      <li>Only 4 months after initial implementation</li>
    </ul>
    <ul data-lang="ko">
      <li>본인전송 ≠ 제3자 전송 (불일치)</li>
      <li>규제개혁위원회 결정 위반</li>
      <li>전 분야 동시 확대</li>
      <li>최초 시행 후 불과 4개월</li>
    </ul>
  </div>
</div>

<div class="highlight-box warning">
<h3><span data-lang="en">What "Revenue 150B KRW & 1M Users" Really Means</span><span data-lang="ko">"매출 1,500억원 & 이용자 100만명"의 진정한 의미</span></h3>
<p data-lang="en">This threshold captures:</p>
<p data-lang="ko">이 기준에 해당하는 사업자:</p>
<ul data-lang="en">
  <li><strong>Major platforms:</strong> Naver, Kakao, Coupang, Baemin, 11st, Gmarket, Auction</li>
  <li><strong>Growing startups:</strong> Any company reaching 1M users automatically included</li>
  <li><strong>Sectors affected:</strong> E-commerce, delivery, gaming, education, hospitality, culture & leisure</li>
</ul>
<ul data-lang="ko">
  <li><strong>주요 플랫폼:</strong> 네이버, 카카오, 쿠팡, 배민, 11번가, 지마켓, 옥션</li>
  <li><strong>성장하는 스타트업:</strong> 100만 이용자 도달 시 자동 포함</li>
  <li><strong>영향 받는 분야:</strong> 전자상거래, 배달, 게임, 교육, 숙박, 문화·레저</li>
</ul>
<p data-lang="en"><strong>Result:</strong> Virtually all successful digital businesses are captured → De facto expansion to ALL industries</p>
<p data-lang="ko"><strong>결과:</strong> 사실상 모든 성공적인 디지털 비즈니스가 포함 → 실질적으로 전 산업 확대</p>
</div>

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="scopeComparison"></canvas>
</div>

---

<h2 data-lang="en">Seven Critical Concerns</h2>
<h2 data-lang="ko">7가지 핵심 문제점</h2>

<div class="chart-container" style="height: 500px; margin-bottom: 3rem;"><canvas id="sevenConcernsRadar"></canvas></div>

<div class="concern-grid">
  <div class="concern-card procedural">
    <div class="concern-number">1</div>
    <h3><span data-lang="en">Procedural Violation</span><span data-lang="ko">절차적 위반</span></h3>
    <p><strong data-lang="en">Issue:</strong><strong data-lang="ko">문제:</strong> <span data-lang="en">Re-proposing rejected content only 4 months after Regulatory Reform Committee decision</span><span data-lang="ko">규제개혁위원회 결정 후 불과 4개월 만에 거부된 내용 재제안</span></p>
    <p><strong data-lang="en">Risk:</strong><strong data-lang="ko">위험:</strong> <span data-lang="en">Undermines regulatory review process, erodes administrative credibility</span><span data-lang="ko">규제 심의 절차 훼손, 행정 신뢰도 하락</span></p>
  </div>

  <div class="concern-card legal">
    <div class="concern-number">2</div>
    <h3><span data-lang="en">Constitutional Issues</span><span data-lang="ko">헌법적 문제</span></h3>
    <p><strong data-lang="en">Issue:</strong><strong data-lang="ko">문제:</strong> <span data-lang="en">Delegation of essential matters (proxy rights) to enforcement decree violates legal reservation principle</span><span data-lang="ko">본질적 사항(대리권)을 시행령에 위임하여 법률유보원칙 위반</span></p>
    <p><strong data-lang="en">Risk:</strong><strong data-lang="ko">위험:</strong> <span data-lang="en">Legislative power infringement, legal system disruption</span><span data-lang="ko">입법권 침해, 법 체계 훼손</span></p>
  </div>

  <div class="concern-card gdpr">
    <div class="concern-number">3</div>
    <h3><span data-lang="en">GDPR Non-Compliance</span><span data-lang="ko">GDPR 불일치</span></h3>
    <p><strong data-lang="en">Issue:</strong><strong data-lang="ko">문제:</strong> <span data-lang="en">Lacks GDPR Article 20(4) protection for "rights and freedoms of others" (trade secrets)</span><span data-lang="ko">GDPR 제20조(4)의 "타인의 권리와 자유" (영업비밀) 보호 조항 부재</span></p>
    <p><strong data-lang="en">Risk:</strong><strong data-lang="ko">위험:</strong> <span data-lang="en">International norm deviation, property rights violation</span><span data-lang="ko">국제 규범 이탈, 재산권 침해</span></p>
  </div>

  <div class="concern-card market">
    <div class="concern-number">4</div>
    <h3><span data-lang="en">Market Distortion</span><span data-lang="ko">시장 왜곡</span></h3>
    <p><strong data-lang="en">Issue:</strong><strong data-lang="ko">문제:</strong> <span data-lang="en">Exclusive privileges to specialized agencies enable data free-riding</span><span data-lang="ko">전문기관에 대한 독점적 특혜로 데이터 무임승차 가능</span></p>
    <p><strong data-lang="en">Risk:</strong><strong data-lang="ko">위험:</strong> <span data-lang="en">Market manipulation, ecosystem destruction</span><span data-lang="ko">시장 조작, 생태계 파괴</span></p>
  </div>

  <div class="concern-card security">
    <div class="concern-number">5</div>
    <h3><span data-lang="en">Security Risks</span><span data-lang="ko">보안 위험</span></h3>
    <p><strong data-lang="en">Issue:</strong><strong data-lang="ko">문제:</strong> <span data-lang="en">Allows screen scraping, creates Single Point of Failure (SPOF)</span><span data-lang="ko">스크린 스크래핑 허용, 단일장애점(SPOF) 생성</span></p>
    <p><strong data-lang="en">Risk:</strong><strong data-lang="ko">위험:</strong> <span data-lang="en">ID/PW exposure, nationwide simultaneous data breach</span><span data-lang="ko">ID/PW 노출, 전국 동시 데이터 유출</span></p>
  </div>

  <div class="concern-card economic">
    <div class="concern-number">6</div>
    <h3><span data-lang="en">Economic Burden</span><span data-lang="ko">경제적 부담</span></h3>
    <p><strong data-lang="en">Issue:</strong><strong data-lang="ko">문제:</strong> <span data-lang="en">Forces trade secret disclosure, imposes excessive compliance costs</span><span data-lang="ko">영업비밀 공개 강제, 과도한 준수 비용 부과</span></p>
    <p><strong data-lang="en">Risk:</strong><strong data-lang="ko">위험:</strong> <span data-lang="en">Competitiveness erosion, growth inhibition</span><span data-lang="ko">경쟁력 약화, 성장 저해</span></p>
  </div>

  <div class="concern-card consistency">
    <div class="concern-number">7</div>
    <h3><span data-lang="en">Policy Inconsistency</span><span data-lang="ko">정책 불일치</span></h3>
    <p><strong data-lang="en">Issue:</strong><strong data-lang="ko">문제:</strong> <span data-lang="en">Contradicts Financial Services Commission's scraping ban (2022)</span><span data-lang="ko">금융위원회의 스크래핑 금지 조치(2022)와 모순</span></p>
    <p><strong data-lang="en">Risk:</strong><strong data-lang="ko">위험:</strong> <span data-lang="en">Administrative consistency loss</span><span data-lang="ko">행정 일관성 상실</span></p>
  </div>
</div>

---

<h2 data-lang="en">Deep Dive: GDPR Compliance Gap</h2>
<h2 data-lang="ko">심층 분석: GDPR 준수 격차</h2>

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="timelineChart"></canvas>
</div>

---

<div class="vs-divider">
  <div class="vs-badge">VS</div>
</div>

<div class="comparison-grid">
  <div class="comparison-card current">
    <h3><span data-lang="en">GDPR Approach (Balanced)</span><span data-lang="ko">GDPR 접근 (균형적)</span></h3>
    <ul data-lang="en" style="line-height: 2;">
      <li>Protects data subject rights</li>
      <li>Respects business property rights</li>
      <li>Explicitly protects trade secrets</li>
      <li>Considers technical feasibility</li>
      <li>Balanced approach</li>
    </ul>
    <ul data-lang="ko" style="line-height: 2;">
      <li>정보주체 권리 보호</li>
      <li>사업자 재산권 존중</li>
      <li>영업비밀 명시적 보호</li>
      <li>기술적 실현 가능성 고려</li>
      <li>균형 잡힌 접근</li>
    </ul>
    <div class="highlight-box info" style="margin-top: 1.5rem;">
      <strong>GDPR Article 20(4):</strong><br>
      <span data-lang="en">"The right referred to in paragraph 1 <strong>shall not adversely affect the rights and freedoms of others.</strong>"</span>
      <span data-lang="ko">"제1항에 언급된 권리는 <strong>타인의 권리와 자유에 부정적인 영향을 미쳐서는 안 된다.</strong>"</span>
    </div>
  </div>

  <div class="comparison-card proposed">
    <h3><span data-lang="en">Korean Amendment (Unbalanced)</span><span data-lang="ko">한국 개정안 (불균형)</span></h3>
    <ul data-lang="en" style="line-height: 2;">
      <li>Protects data subject rights</li>
      <li>Ignores business property rights</li>
      <li>No trade secret protection</li>
      <li>Unconditional transfer obligation</li>
      <li>One-sided regulation</li>
    </ul>
    <ul data-lang="ko" style="line-height: 2;">
      <li>정보주체 권리 보호</li>
      <li>사업자 재산권 무시</li>
      <li>영업비밀 보호 없음</li>
      <li>무조건적 전송 의무</li>
      <li>일방적 규제</li>
    </ul>
    <div class="highlight-box danger" style="margin-top: 1.5rem;">
      <strong data-lang="en">Critical Flaw:</strong><strong data-lang="ko">핵심 결함:</strong><br>
      <span data-lang="en">Forces transfer of core business data (purchase patterns, pricing policies, customer segmentation, seller information) without "legitimate grounds" despite being trade secrets accumulated through years of investment</span>
      <span data-lang="ko">수년간의 투자로 축적한 영업비밀임에도 불구하고 "정당한 사유" 없이 핵심 사업 데이터(구매 패턴, 가격 정책, 고객 세분화, 판매자 정보) 전송 강제</span>
    </div>
  </div>
</div>

<h3 data-lang="en">EU Article 29 Working Party Guidelines</h3>
<h3 data-lang="ko">EU 제29조 작업반 지침</h3>

<div class="chart-container" style="height: 450px; margin: 3rem 0;">
  <canvas id="gdprComplianceChart"></canvas>
</div>

<h3 data-lang="en">EU Article 29 Working Party Guidelines (WP242)</h3>
<h3 data-lang="ko">EU 제29조 작업반 지침 (WP242)</h3>

<p data-lang="en">The EU's authoritative interpretation provides clear boundaries:</p>
<p data-lang="ko">EU의 권위 있는 해석은 명확한 경계를 제공합니다:</p>

<table class="data-table">
<thead>
<tr>
<th><span data-lang="en">Principle</span><span data-lang="ko">원칙</span></th>
<th><span data-lang="en">EU Interpretation</span><span data-lang="ko">EU 해석</span></th>
<th><span data-lang="en">Korean Amendment</span><span data-lang="ko">한국 개정안</span></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong data-lang="en">"Provided by" data subject</strong><strong data-lang="ko">"정보주체가 제공한" 데이터</strong></td>
<td><span data-lang="en">Limited to data directly provided by user; excludes company-generated analytics</span><span data-lang="ko">이용자가 직접 제공한 데이터로 제한; 기업 생성 분석 제외</span></td>
<td><span data-lang="en">No such limitation</span><span data-lang="ko">그런 제한 없음</span></td>
</tr>
<tr>
<td><strong data-lang="en">"Work product" exclusion</strong><strong data-lang="ko">"작업 산출물" 제외</strong></td>
<td><span data-lang="en">Company work products (credit scores, recommendation algorithms) explicitly excluded</span><span data-lang="ko">기업의 작업 산출물(신용점수, 추천 알고리즘) 명시적 제외</span></td>
<td><span data-lang="en">Not addressed</span><span data-lang="ko">언급 없음</span></td>
</tr>
<tr>
<td><strong data-lang="en">Rights and freedoms of others</strong><strong data-lang="ko">타인의 권리와 자유</strong></td>
<td><span data-lang="en">Cannot violate trade secrets or database maker's rights</span><span data-lang="ko">영업비밀 또는 데이터베이스 제작자 권리 침해 불가</span></td>
<td><strong data-lang="en">No protection clause</strong><strong data-lang="ko">보호 조항 없음</strong></td>
</tr>
<tr>
<td><strong data-lang="en">Technical feasibility</strong><strong data-lang="ko">기술적 실현 가능성</strong></td>
<td><span data-lang="en">Direct transfer only "where technically feasible"</span><span data-lang="ko">"기술적으로 실현 가능한 경우에만" 직접 전송</span></td>
<td><span data-lang="en">Unconditional obligation</span><span data-lang="ko">무조건적 의무</span></td>
</tr>
</tbody>
</table>

---

<h2 data-lang="en">The Financial Sector Paradox: Regulatory Self-Contradiction</h2>
<h2 data-lang="ko">금융 분야 역설: 규제적 자기모순</h2>

<div class="highlight-box danger">
<h3 data-lang="en">🔴 Financial Services Commission (2022): Screen Scraping Banned as Security Risk</h3>
<h3 data-lang="ko">🔴 금융위원회 (2022): 스크린 스크래핑을 보안 위험으로 금지</h3>

<p><strong data-lang="en">Timeline:</strong><strong data-lang="ko">타임라인:</strong></p>
<ul data-lang="en">
<li><strong>August 5, 2020:</strong> Credit Information Act amended - MyData legal framework established</li>
<li><strong>December 1, 2021:</strong> MyData pilot service launched (17 institutions) - Scraping temporarily allowed</li>
<li><strong>January 5, 2022:</strong> <strong>Screen scraping completely banned, API-only mandate</strong></li>
</ul>
<ul data-lang="ko">
<li><strong>2020년 8월 5일:</strong> 신용정보법 개정 - 마이데이터 법적 체계 수립</li>
<li><strong>2021년 12월 1일:</strong> 마이데이터 시범서비스 출시 (17개 기관) - 스크래핑 임시 허용</li>
<li><strong>2022년 1월 5일:</strong> <strong>스크린 스크래핑 전면 금지, API 방식만 허용</strong></li>
</ul>

<p><strong data-lang="en">Official Rationale (FSC Press Release, Jan 4, 2022):</strong><strong data-lang="ko">공식 근거 (금융위원회 보도자료, 2022년 1월 4일):</strong></p>

<blockquote data-lang="en">"From January 5, 2022, screen scraping is completely prohibited and MyData operators must provide services exclusively through API methods to all users."</blockquote>
<blockquote data-lang="ko">"2022년 1월 5일부터 스크린 스크래핑은 완전히 금지되며, 마이데이터 사업자는 모든 이용자에게 API 방식으로만 서비스를 제공해야 합니다."</blockquote>

<p><strong data-lang="en">Security Concerns Cited:</strong><strong data-lang="ko">지적된 보안 우려:</strong></p>
<table class="data-table">
<thead>
<tr>
<th><span data-lang="en">Risk</span><span data-lang="ko">위험</span></th>
<th><span data-lang="en">Details</span><span data-lang="ko">세부사항</span></th>
</tr>
</thead>
<tbody>
<tr>
<td><span data-lang="en">ID/PW Direct Collection</span><span data-lang="ko">ID/PW 직접 수집</span></td>
<td><span data-lang="en">MyData operators must directly collect and store user IDs and passwords</span><span data-lang="ko">마이데이터 사업자가 이용자의 ID와 비밀번호를 직접 수집·저장해야 함</span></td>
</tr>
<tr>
<td><span data-lang="en">Inability to Use One-Way Encryption</span><span data-lang="ko">단방향 암호화 불가</span></td>
<td><span data-lang="en">Passwords must be stored in plaintext or reversible encryption → mass breach risk if hacked</span><span data-lang="ko">비밀번호를 평문 또는 복호화 가능한 암호화로 저장해야 함 → 해킹 시 대량 유출 위험</span></td>
</tr>
<tr>
<td><span data-lang="en">2FA Bypass</span><span data-lang="ko">2FA 우회</span></td>
<td><span data-lang="en">Must circumvent additional security measures like 2FA, OTP</span><span data-lang="ko">2FA, OTP 같은 추가 보안 조치를 우회해야 함</span></td>
</tr>
<tr>
<td><span data-lang="en">Unclear Liability</span><span data-lang="ko">불명확한 책임</span></td>
<td><span data-lang="en">Responsibility unclear between financial institutions and operators in case of breach</span><span data-lang="ko">유출 시 금융기관과 사업자 간 책임 불분명</span></td>
</tr>
</tbody>
</table>

<p><strong data-lang="en">API Benefits:</strong><strong data-lang="ko">API의 장점:</strong></p>
<ul data-lang="en">
<li>Financial institution controls transfer → clear liability</li>
<li>Token-based authentication → no password exposure</li>
<li>Limited transfer scope → only necessary data</li>
<li>Traceable transfer history → auditable</li>
<li>TLS encryption → secure transmission</li>
</ul>
<ul data-lang="ko">
<li>금융기관이 전송 통제 → 명확한 책임</li>
<li>토큰 기반 인증 → 비밀번호 노출 없음</li>
<li>제한된 전송 범위 → 필요한 데이터만</li>
<li>추적 가능한 전송 이력 → 감사 가능</li>
<li>TLS 암호화 → 안전한 전송</li>
</ul>
</div>

<div class="highlight-box warning">
<h3 data-lang="en">🟡 Personal Information Protection Commission (2025): Allowing Scraping as "Automated Tool"</h3>
<h3 data-lang="ko">🟡 개인정보보호위원회 (2025): 스크래핑을 "자동화 도구"로 허용</h3>

<p><strong data-lang="en">Justification:</strong><strong data-lang="ko">정당화 근거:</strong></p>
<ul data-lang="en">
<li>"Convenience for exercising rights"</li>
<li>"Technical flexibility"</li>
<li><strong>No clear security measures</strong></li>
</ul>
<ul data-lang="ko">
<li>"권리 행사의 편의성"</li>
<li>"기술적 유연성"</li>
<li><strong>명확한 보안 조치 없음</strong></li>
</ul>

<p><strong data-lang="en">Expected Result:</strong> <span data-lang="en">Revival of risks that FSC banned</span><span data-lang="ko">금융위원회가 금지한 위험 부활</span></p>

<p><strong data-lang="en">Scope:</strong><strong data-lang="ko">범위:</strong> <span data-lang="en">E-commerce, platforms, gaming, education, culture & leisure - ALL industries</span><span data-lang="ko">전자상거래, 플랫폼, 게임, 교육, 문화·레저 - 전 산업</span></p>
</div>

<div class="highlight-box danger">
<h3 data-lang="en">⚠️ The Logical Contradiction</h3>
<h3 data-lang="ko">⚠️ 논리적 모순</h3>

<p><strong data-lang="en">Regulatory Inconsistency:</strong><strong data-lang="ko">규제 불일치:</strong></p>
<ol data-lang="en">
<li>Financial information is important → scraping banned</li>
<li>Medical, shopping, education information is not important → scraping allowed?</li>
</ol>
<ol data-lang="ko">
<li>금융정보는 중요하다 → 스크래핑 금지</li>
<li>의료, 쇼핑, 교육 정보는 중요하지 않다 → 스크래핑 허용?</li>
</ol>

<p><strong data-lang="en">Violation of Personal Information Protection Act Article 29:</strong><strong data-lang="ko">개인정보보호법 제29조 위반:</strong></p>

<blockquote data-lang="en"><strong>Article 29 (Security Measures Obligation):</strong> Personal information controllers must establish internal management plans, maintain access records, and take technical, administrative, and physical measures necessary to ensure safety as prescribed by Presidential Decree to prevent personal information from being lost, stolen, leaked, forged, altered, or damaged.</blockquote>
<blockquote data-lang="ko"><strong>제29조 (안전조치 의무):</strong> 개인정보처리자는 개인정보가 분실·도난·유출·위조·변조 또는 훼손되지 아니하도록 대통령령으로 정하는 바에 따라 내부 관리계획을 수립하고, 접근기록을 보관하는 등 필요한 기술적·관리적 및 물리적 조치를 하여야 한다.</blockquote>

<p data-lang="en">→ <strong>Allowing scraping directly contradicts the obligation to ensure security</strong></p>
<p data-lang="ko">→ <strong>스크래핑 허용은 보안을 보장해야 할 의무와 직접적으로 모순됨</strong></p>

<p><strong data-lang="en">Result:</strong> <span data-lang="en">Loss of consistency in personal information protection principles</span><span data-lang="ko">개인정보 보호 원칙의 일관성 상실</span></p>
</div>

<!-- CHART:regulatoryContradiction -->

---

<h2 data-lang="en">The Specialized Agency Privilege Problem</h2>
<h2 data-lang="ko">전문기관 특혜 문제</h2>

<div class="highlight-box danger">
<h3 data-lang="en">Creating Legal Data Brokers</h3>
<h3 data-lang="ko">합법적 데이터 브로커 창출</h3>

<p><strong data-lang="en">Enforcement Decree Draft Article 42-9 (Duties of Personal Information Management Specialized Agencies):</strong><strong data-lang="ko">시행령 초안 제42조의9 (개인정보관리 전문기관의 업무):</strong></p>

<ol data-lang="en">
<li>Integrated inquiry of personal information received from data subjects</li>
<li>Providing customized services for data subjects</li>
<li>Research and education related to personal information utilization</li>
<li><strong>Other duties determined by the Personal Information Protection Commission</strong> → Effectively: data collection, analysis, and utilization business</li>
</ol>
<ol data-lang="ko">
<li>정보주체로부터 수령한 개인정보의 통합 조회</li>
<li>정보주체를 위한 맞춤형 서비스 제공</li>
<li>개인정보 활용 관련 연구 및 교육</li>
<li><strong>개인정보보호위원회가 정하는 기타 업무</strong> → 실질적으로: 데이터 수집, 분석 및 활용 사업</li>
</ol>

<p><strong data-lang="en">Critical Issue:</strong><strong data-lang="ko">핵심 문제:</strong> <span data-lang="en">Specialized agencies can use collected information as bait (e.g., coffee coupons) to obtain additional consent from data subjects, then sell or commercially exploit this information to third parties.</span><span data-lang="ko">전문기관은 수집한 정보를 미끼(예: 커피 쿠폰)로 사용하여 정보주체로부터 추가 동의를 받은 후, 이 정보를 제3자에게 판매하거나 상업적으로 이용할 수 있습니다.</span> <strong data-lang="en">This opens a legitimate channel for personal information trading and distribution.</strong><strong data-lang="ko">이는 개인정보 거래 및 유통의 합법적 채널을 열어줍니다.</strong></p>
</div>

<p><strong data-lang="en">Commission's Stated Objective (June 2025 Legislative Notice):</strong><strong data-lang="ko">위원회의 공식 목표 (2025년 6월 입법예고):</strong></p>

<blockquote data-lang="en">"Activate data economy through new business opportunities"</blockquote>
<blockquote data-lang="ko">"새로운 비즈니스 기회를 통한 데이터 경제 활성화"</blockquote>

<p data-lang="en">→ Admits this is an <strong>industrial policy goal</strong>, not a data subject protection measure</p>
<p data-lang="ko">→ 이것이 정보주체 보호 조치가 아닌 <strong>산업정책 목표</strong>임을 인정</p>

<h3 data-lang="en">The Free-Riding Structure</h3>
<h3 data-lang="ko">무임승차 구조</h3>

<table class="data-table">
<thead>
<tr>
<th><span data-lang="en">Actor</span><span data-lang="ko">주체</span></th>
<th><span data-lang="en">Investment & Effort</span><span data-lang="ko">투자 및 노력</span></th>
<th><span data-lang="en">Result</span><span data-lang="ko">결과</span></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong data-lang="en">Platform Companies</strong><strong data-lang="ko">플랫폼 기업</strong></td>
<td>
<ul data-lang="en">
<li>Years of service development investment</li>
<li>Customer acquisition marketing costs</li>
<li>Data analysis infrastructure</li>
<li>Personal information protection systems</li>
</ul>
<ul data-lang="ko">
<li>수년간의 서비스 개발 투자</li>
<li>고객 확보 마케팅 비용</li>
<li>데이터 분석 인프라</li>
<li>개인정보 보호 시스템</li>
</ul>
</td>
<td><strong data-lang="en">Forced asset transfer</strong><strong data-lang="ko">강제 자산 이전</strong></td>
</tr>
<tr>
<td><strong data-lang="en">Specialized Agencies</strong><strong data-lang="ko">전문기관</strong></td>
<td>
<ul data-lang="en">
<li>No investment or innovation</li>
<li>Only government license acquired</li>
<li>Rely on enforcement decree mandate</li>
</ul>
<ul data-lang="ko">
<li>투자나 혁신 없음</li>
<li>정부 라이선스만 취득</li>
<li>시행령 의무에 의존</li>
</ul>
</td>
<td><strong data-lang="en">Free data collection → Own revenue business</strong><strong data-lang="ko">무료 데이터 수집 → 자체 수익 사업</strong></td>
</tr>
</tbody>
</table>

---

<h2 data-lang="en">Single Point of Failure (SPOF): A National Security Risk</h2>
<h2 data-lang="ko">단일장애점(SPOF): 국가 안보 위험</h2>

<div class="highlight-box danger">
<h3 data-lang="en">🔴 From Distributed Risk to Concentrated Catastrophe</h3>
<h3 data-lang="ko">🔴 분산된 위험에서 집중된 재앙으로</h3>

<p><strong data-lang="en">Current System (Distributed):</strong><strong data-lang="ko">현행 시스템 (분산형):</strong></p>
<ul data-lang="en">
<li>Shopping site breach → Purchase history only</li>
<li>Hospital breach → Medical records only</li>
<li><strong>Limited damage scope</strong></li>
</ul>
<ul data-lang="ko">
<li>쇼핑 사이트 유출 → 구매 이력만</li>
<li>병원 유출 → 의료 기록만</li>
<li><strong>피해 범위 제한적</strong></li>
</ul>

<p><strong data-lang="en">Amendment System (Centralized):</strong><strong data-lang="ko">개정안 시스템 (중앙집중형):</strong></p>
<ul data-lang="en">
<li>Specialized agency breach → <strong>Entire life history exposed</strong></li>
<li><strong>All citizens affected simultaneously</strong></li>
<li><strong>National-level disaster</strong></li>
</ul>
<ul data-lang="ko">
<li>전문기관 유출 → <strong>전체 생애 이력 노출</strong></li>
<li><strong>모든 국민 동시 피해</strong></li>
<li><strong>국가적 재난</strong></li>
</ul>
</div>

<h3 data-lang="en">What One Specialized Agency Would Know About Each Person:</h3>
<h3 data-lang="ko">전문기관이 각 개인에 대해 알게 되는 정보:</h3>

<table class="data-table">
<thead>
<tr>
<th><span data-lang="en">Category</span><span data-lang="ko">분류</span></th>
<th><span data-lang="en">Information</span><span data-lang="ko">정보</span></th>
</tr>
</thead>
<tbody>
<tr>
<td><span data-lang="en">Medical</span><span data-lang="ko">의료</span></td>
<td><span data-lang="en">Medical records, prescriptions, health checkups, genetic information</span><span data-lang="ko">진료 기록, 처방전, 건강검진, 유전 정보</span></td>
</tr>
<tr>
<td><span data-lang="en">Telecom</span><span data-lang="ko">통신</span></td>
<td><span data-lang="en">Call history, messages, location data, internet usage</span><span data-lang="ko">통화 이력, 메시지, 위치 데이터, 인터넷 사용</span></td>
</tr>
<tr>
<td><span data-lang="en">Financial</span><span data-lang="ko">금융</span></td>
<td><span data-lang="en">Account balances, transaction history, card usage, loans</span><span data-lang="ko">계좌 잔액, 거래 내역, 카드 사용, 대출</span></td>
</tr>
<tr>
<td><span data-lang="en">Shopping</span><span data-lang="ko">쇼핑</span></td>
<td><span data-lang="en">Purchase history, wish lists, payment methods, delivery addresses</span><span data-lang="ko">구매 이력, 위시리스트, 결제 수단, 배송지</span></td>
</tr>
<tr>
<td><span data-lang="en">Education</span><span data-lang="ko">교육</span></td>
<td><span data-lang="en">Learning records, grades, course history</span><span data-lang="ko">학습 기록, 성적, 수강 이력</span></td>
</tr>
<tr>
<td><span data-lang="en">Sensitive</span><span data-lang="ko">민감정보</span></td>
<td><span data-lang="en">Adult products, pregnancy info, personal preferences</span><span data-lang="ko">성인용품, 임신 정보, 개인 취향</span></td>
</tr>
</tbody>
</table>

<p data-lang="en">→ <strong>Complete life profile in one location</strong></p>
<p data-lang="ko">→ <strong>한 곳에 완전한 생애 프로필</strong></p>

<h3 data-lang="en">Breach Scenario:</h3>
<h3 data-lang="ko">유출 시나리오:</h3>

<p data-lang="en"><strong>Person A:</strong> Pregnancy (obstetrics) + Adult products (shopping) + Specific locations (GPS) + Financial transactions = <strong>Complete privacy exposure</strong></p>
<p data-lang="ko"><strong>A씨:</strong> 임신 (산부인과) + 성인용품 (쇼핑) + 특정 위치 (GPS) + 금융 거래 = <strong>완전한 프라이버시 노출</strong></p>

<p data-lang="en"><strong>Specialized agency breach:</strong> 50 million people like Person A <strong>simultaneously affected</strong></p>
<p data-lang="ko"><strong>전문기관 유출:</strong> A씨와 같은 5,000만 명이 <strong>동시에 피해</strong></p>

<!-- CHART:spofRisk -->

---

<h2 data-lang="en">Economic Impact: Crushing Startups</h2>
<h2 data-lang="ko">경제적 영향: 스타트업 압박</h2>

<h3 data-lang="en">Actual Financial MyData Costs</h3>
<h3 data-lang="ko">실제 금융 마이데이터 비용</h3>

<table class="data-table">
<thead>
<tr>
<th><span data-lang="en">Item</span><span data-lang="ko">항목</span></th>
<th><span data-lang="en">Cost</span><span data-lang="ko">비용</span></th>
</tr>
</thead>
<tbody>
<tr>
<td><span data-lang="en">Total System Construction (All institutions)</span><span data-lang="ko">전체 시스템 구축 (전 기관)</span></td>
<td><span data-lang="en">~37.2B KRW</span><span data-lang="ko">약 372억원</span></td>
</tr>
<tr>
<td><span data-lang="en">Annual Operating Cost (All institutions)</span><span data-lang="ko">연간 운영 비용 (전 기관)</span></td>
<td><span data-lang="en">~92.1B KRW</span><span data-lang="ko">약 921억원</span></td>
</tr>
<tr>
<td><span data-lang="en">Annual Total Cost</span><span data-lang="ko">연간 총 비용</span></td>
<td><span data-lang="en">~129.3B KRW</span><span data-lang="ko">약 1,293억원</span></td>
</tr>
<tr>
<td><span data-lang="en">Average Cost Per Institution</span><span data-lang="ko">기관당 평균 비용</span></td>
<td><span data-lang="en">Hundreds of millions to billions KRW (varies by size)</span><span data-lang="ko">수억~수십억원 (규모별 상이)</span></td>
</tr>
</tbody>
</table>

<p data-lang="en"><em>Source: Financial Services Commission announcement (Jan 10, 2023), Samjong KPMG cost analysis</em></p>
<p data-lang="ko"><em>출처: 금융위원회 발표 (2023년 1월 10일), 삼정KPMG 비용 분석</em></p>

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="costImpactChart"></canvas>
</div>

<h3 data-lang="en">All-Industry Expansion Impact (Estimated)</h3>
<h3 data-lang="ko">전 산업 확대 영향 (추정)</h3>

<ul data-lang="en">
<li><strong>Target companies:</strong> Revenue ≥150B KRW & ≥1M users</li>
<li><strong>Estimated number:</strong> 100-200 companies (e-commerce, medical, telecom, etc.)</li>
<li><strong>Unlike financial sector:</strong> Must build new infrastructure from scratch</li>
<li><strong>Initial cost per company:</strong> Tens to hundreds of millions KRW</li>
<li><strong>Total estimated cost:</strong> Minimum hundreds of billions to trillions of KRW</li>
</ul>
<ul data-lang="ko">
<li><strong>대상 기업:</strong> 매출 1,500억원 이상 & 이용자 100만명 이상</li>
<li><strong>추정 기업 수:</strong> 100-200개 기업 (전자상거래, 의료, 통신 등)</li>
<li><strong>금융권과 다른 점:</strong> 새 인프라를 처음부터 구축해야 함</li>
<li><strong>기업당 초기 비용:</strong> 수천만~수억원</li>
<li><strong>총 추정 비용:</strong> 최소 수천억~수조원</li>
</ul>

<div class="highlight-box warning">
<h3 data-lang="en">The Startup Growth Trap</h3>
<h3 data-lang="ko">스타트업 성장의 덫</h3>

<p><strong data-lang="en">The Dilemma:</strong><strong data-lang="ko">딜레마:</strong></p>

<p data-lang="en"><strong>500K users</strong> → Growth, data accumulation, investment attraction</p>
<p data-lang="ko"><strong>50만 이용자</strong> → 성장, 데이터 축적, 투자 유치</p>

<p data-lang="en"><strong>1M users milestone</strong> → Transfer obligation triggered → API construction costs tens of millions KRW</p>
<p data-lang="ko"><strong>100만 이용자 도달</strong> → 전송 의무 발생 → API 구축 비용 수천만원</p>

<p data-lang="en"><strong>Choice</strong> → More growth = Massive costs + Core data exposure</p>
<p data-lang="ko"><strong>선택</strong> → 더 성장 = 막대한 비용 + 핵심 데이터 노출</p>

<p data-lang="en"><strong>Result</strong> → Stop growth just before 1M users → Loss of innovation momentum</p>
<p data-lang="ko"><strong>결과</strong> → 100만 직전에서 성장 중단 → 혁신 동력 상실</p>

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="startupGrowthTrap"></canvas>
</div>

<p data-lang="en"><strong>Irony:</strong> The threshold "Revenue 150B KRW & 1M users" is marketed as targeting "large businesses" but actually hits <strong>growing companies the hardest</strong>.</p>
<p data-lang="ko"><strong>아이러니:</strong> "매출 1,500억원 & 이용자 100만명" 기준은 "대기업 대상"으로 홍보되지만, 실제로는 <strong>성장하는 기업에게 가장 큰 타격</strong>을 줍니다.</p>
</div>

<!-- CHART:startupGrowthTrap -->

---

<h2 data-lang="en">Trade Secret Violation</h2>
<h2 data-lang="ko">영업비밀 침해</h2>

<div class="highlight-box danger">
<h3 data-lang="en">Unfair Competition Prevention Act Article 2, Paragraph 2</h3>
<h3 data-lang="ko">부정경쟁방지법 제2조 제2호</h3>

<blockquote data-lang="en">"Trade secret" means production methods, sales methods, and other technical or business information useful for business activities that is not publicly known, has independent economic value, and has been maintained as confidential through considerable effort.</blockquote>
<blockquote data-lang="ko">"영업비밀"이란 공공연히 알려져 있지 아니하고 독립된 경제적 가치를 가지는 것으로서, 상당한 노력에 의하여 비밀로 유지된 생산방법, 판매방법, 그 밖에 영업활동에 유용한 기술상 또는 경영상의 정보를 말한다.</blockquote>
</div>

<h3 data-lang="en">E-Commerce Platform Trade Secrets at Risk</h3>
<h3 data-lang="ko">위험에 처한 전자상거래 플랫폼 영업비밀</h3>

<table class="data-table">
<thead>
<tr>
<th><span data-lang="en">Information Type</span><span data-lang="ko">정보 유형</span></th>
<th><span data-lang="en">Trade Secret Status</span><span data-lang="ko">영업비밀 현황</span></th>
<th><span data-lang="en">Transfer Mandate</span><span data-lang="ko">전송 의무</span></th>
</tr>
</thead>
<tbody>
<tr>
<td><span data-lang="en">Purchase Patterns</span><span data-lang="ko">구매 패턴</span></td>
<td><span data-lang="en">Years of analysis investment</span><span data-lang="ko">수년간의 분석 투자</span></td>
<td><strong data-lang="en">Forced</strong><strong data-lang="ko">강제</strong></td>
</tr>
<tr>
<td><span data-lang="en">Pricing Policies</span><span data-lang="ko">가격 정책</span></td>
<td><span data-lang="en">Core competitive advantage</span><span data-lang="ko">핵심 경쟁 우위</span></td>
<td><strong data-lang="en">Forced</strong><strong data-lang="ko">강제</strong></td>
</tr>
<tr>
<td><span data-lang="en">Customer Segmentation</span><span data-lang="ko">고객 세분화</span></td>
<td><span data-lang="en">AI/ML investment</span><span data-lang="ko">AI/ML 투자</span></td>
<td><strong data-lang="en">Forced</strong><strong data-lang="ko">강제</strong></td>
</tr>
<tr>
<td><span data-lang="en">Seller Information</span><span data-lang="ko">판매자 정보</span></td>
<td><span data-lang="en">Business partner data</span><span data-lang="ko">사업 파트너 데이터</span></td>
<td><strong data-lang="en">Forced</strong><strong data-lang="ko">강제</strong></td>
</tr>
</tbody>
</table>

<h3 data-lang="en">The Data Leakage Path</h3>
<h3 data-lang="ko">데이터 유출 경로</h3>

<p><strong data-lang="en">Specialized Agency Gains:</strong><strong data-lang="ko">전문기관이 획득하는 것:</strong></p>
<ul data-lang="en">
<li>Purchase patterns of millions of consumers</li>
<li>Price sensitivity, preferred products, purchase timing</li>
<li>This equals trade secrets accumulated by platforms through years of investment</li>
</ul>
<ul data-lang="ko">
<li>수백만 소비자의 구매 패턴</li>
<li>가격 민감도, 선호 상품, 구매 시점</li>
<li>이는 플랫폼이 수년간의 투자로 축적한 영업비밀과 동일</li>
</ul>

<p><strong data-lang="en">Result:</strong><strong data-lang="ko">결과:</strong></p>
<ul data-lang="en">
<li>Specialized agency acquires for free</li>
<li>Uses for own services</li>
<li><strong>Korean e-commerce competitive advantage eroded</strong></li>
</ul>
<ul data-lang="ko">
<li>전문기관이 무료로 획득</li>
<li>자체 서비스에 활용</li>
<li><strong>한국 전자상거래 경쟁력 약화</strong></li>
</ul>

<div class="comparison-grid" style="margin-top: 2rem;">
  <div class="comparison-card current">
    <h3 data-lang="en">GDPR Protection</h3>
    <h3 data-lang="ko">GDPR 보호</h3>
    <p><strong data-lang="en">"shall not adversely affect the rights and freedoms of others"</strong><strong data-lang="ko">"타인의 권리와 자유에 부정적인 영향을 미쳐서는 안 된다"</strong></p>
    <p data-lang="en">→ Can refuse if trade secrets are infringed</p>
    <p data-lang="ko">→ 영업비밀이 침해되는 경우 거부 가능</p>
  </div>
  <div class="comparison-card proposed">
    <h3 data-lang="en">Korean Amendment</h3>
    <h3 data-lang="ko">한국 개정안</h3>
    <p><strong data-lang="en">NO trade secret protection clause</strong><strong data-lang="ko">영업비밀 보호 조항 없음</strong></p>
    <p data-lang="en">→ Unconditional forced transfer</p>
    <p data-lang="ko">→ 무조건적 강제 전송</p>
  </div>
</div>

---

<h2 data-lang="en">Four Essential Solutions</h2>
<h2 data-lang="ko">4가지 필수 해결책</h2>

<div class="solution-grid">
  <div class="solution-card">
    <h3><span data-lang="en">1. Withdraw Amendment & Follow Committee Guidance</span><span data-lang="ko">1. 개정안 철회 및 위원회 권고 준수</span></h3>
    <ul data-lang="en">
      <li>Immediately withdraw June 2025 amendment</li>
      <li>Comply with August 2024 Regulatory Reform Committee decision</li>
      <li>Maintain current enforcement decree (3 sectors)</li>
      <li>Sufficient pilot operation before reconsidering</li>
    </ul>
    <ul data-lang="ko">
      <li>2025년 6월 개정안 즉시 철회</li>
      <li>2024년 8월 규제개혁위원회 결정 준수</li>
      <li>현행 시행령(3개 분야) 유지</li>
      <li>재검토 전 충분한 시범 운영</li>
    </ul>
  </div>

  <div class="solution-card">
    <h3><span data-lang="en">2. Legal Reservation - National Assembly Legislation</span><span data-lang="ko">2. 법률유보 - 국회 입법</span></h3>
    <ul data-lang="en">
      <li>Delete proxy rights clause from enforcement decree</li>
      <li>Regulate essential proxy rights matters by law</li>
      <li>Social consensus through National Assembly deliberation</li>
    </ul>
    <ul data-lang="ko">
      <li>시행령에서 대리권 조항 삭제</li>
      <li>본질적인 대리권 사항은 법률로 규정</li>
      <li>국회 심의를 통한 사회적 합의</li>
    </ul>
  </div>

  <div class="solution-card">
    <h3><span data-lang="en">3. Adopt GDPR Approach</span><span data-lang="ko">3. GDPR 방식 채택</span></h3>
    <ul data-lang="en">
      <li>Abolish specialized agency centralization</li>
      <li>Prioritize self-download rights</li>
      <li>Explicitly protect trade secrets & database rights</li>
      <li>Encourage market autonomy</li>
    </ul>
    <ul data-lang="ko">
      <li>전문기관 중앙집중 폐지</li>
      <li>본인 다운로드 권리 우선</li>
      <li>영업비밀 및 데이터베이스권 명시적 보호</li>
      <li>시장 자율성 장려</li>
    </ul>
  </div>

  <div class="solution-card">
    <h3><span data-lang="en">4. Security Enhancement - Ban Scraping</span><span data-lang="ko">4. 보안 강화 - 스크래핑 금지</span></h3>
    <ul data-lang="en">
      <li>Ban scraping same as Financial Services Commission</li>
      <li>Allow only standard APIs</li>
      <li>Prevent SPOF through distributed structure</li>
    </ul>
    <ul data-lang="ko">
      <li>금융위원회와 동일하게 스크래핑 금지</li>
      <li>표준 API만 허용</li>
      <li>분산 구조를 통한 SPOF 방지</li>
    </ul>
  </div>
</div>

---

<h2 data-lang="en">Recommended GDPR-Style Provisions</h2>
<h2 data-lang="ko">권장 GDPR형 조항</h2>

<div class="highlight-box info">
<h3 data-lang="en">Proposed Amendment Article ○ (Limitations on Transfer Requests)</h3>
<h3 data-lang="ko">개정안 제○조 (전송요구의 제한)</h3>

<p><strong data-lang="en">① Transfer may be refused in the following cases:</strong><strong data-lang="ko">① 다음 각 호의 경우에는 전송을 거부할 수 있다:</strong></p>

<ol data-lang="en">
<li>Contains trade secrets or intellectual property</li>
<li>Infringes database maker's rights</li>
<li>Violates rights and freedoms of others</li>
<li>Technically difficult or excessively costly</li>
</ol>
<ol data-lang="ko">
<li>영업비밀 또는 지적재산권을 포함하는 경우</li>
<li>데이터베이스 제작자의 권리를 침해하는 경우</li>
<li>타인의 권리와 자유를 침해하는 경우</li>
<li>기술적으로 어렵거나 과도한 비용이 드는 경우</li>
</ol>

<p><strong data-lang="en">② Obligation to notify reasons when refusing</strong><strong data-lang="ko">② 거부 시 사유 통지 의무</strong></p>
</div>

---

<h2 data-lang="en">Conclusion: Balance is Essential</h2>
<h2 data-lang="ko">결론: 균형이 필수적</h2>

<div class="highlight-box warning">
<h3><span data-lang="en">Seven Critical Concerns Summary</span><span data-lang="ko">7가지 핵심 문제점 요약</span></h3>

<table class="data-table">
<thead>
<tr>
<th><span data-lang="en">No.</span><span data-lang="ko">순번</span></th>
<th><span data-lang="en">Area</span><span data-lang="ko">영역</span></th>
<th><span data-lang="en">Core Problem</span><span data-lang="ko">핵심 문제</span></th>
<th><span data-lang="en">Social Risk</span><span data-lang="ko">사회적 위험</span></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><span data-lang="en">Procedural Legitimacy</span><span data-lang="ko">절차적 정당성</span></td>
<td><span data-lang="en">Ignoring Committee guidance, re-proposing after 4 months</span><span data-lang="ko">위원회 권고 무시, 4개월 후 재제안</span></td>
<td><span data-lang="en">Regulatory process nullification, administrative trust damage</span><span data-lang="ko">규제 절차 무효화, 행정 신뢰 손상</span></td>
</tr>
<tr>
<td>2</td>
<td><span data-lang="en">Legal Validity</span><span data-lang="ko">법적 유효성</span></td>
<td><span data-lang="en">Violating legal reservation principle, unconstitutional proxy rights</span><span data-lang="ko">법률유보원칙 위반, 위헌적 대리권</span></td>
<td><span data-lang="en">Legislative power infringement, legal system disruption</span><span data-lang="ko">입법권 침해, 법 체계 훼손</span></td>
</tr>
<tr>
<td>3</td>
<td><span data-lang="en">Global Compliance</span><span data-lang="ko">국제 규범 준수</span></td>
<td><span data-lang="en">GDPR contradiction, lack of trade secret protection</span><span data-lang="ko">GDPR 모순, 영업비밀 보호 부재</span></td>
<td><span data-lang="en">International norm deviation, property rights ignored</span><span data-lang="ko">국제 규범 이탈, 재산권 무시</span></td>
</tr>
<tr>
<td>4</td>
<td><span data-lang="en">Policy Fairness</span><span data-lang="ko">정책 공정성</span></td>
<td><span data-lang="en">Specialized agency privileges, data free-riding</span><span data-lang="ko">전문기관 특혜, 데이터 무임승차</span></td>
<td><span data-lang="en">Market distortion, ecosystem destruction</span><span data-lang="ko">시장 왜곡, 생태계 파괴</span></td>
</tr>
<tr>
<td>5</td>
<td><span data-lang="en">Security Stability</span><span data-lang="ko">보안 안정성</span></td>
<td><span data-lang="en">Allowing scraping, SPOF formation</span><span data-lang="ko">스크래핑 허용, SPOF 형성</span></td>
<td><span data-lang="en">ID/PW exposure, nationwide simultaneous breach</span><span data-lang="ko">ID/PW 노출, 전국 동시 유출</span></td>
</tr>
<tr>
<td>6</td>
<td><span data-lang="en">Economic Rationality</span><span data-lang="ko">경제적 합리성</span></td>
<td><span data-lang="en">Trade secret exposure, excessive costs</span><span data-lang="ko">영업비밀 노출, 과도한 비용</span></td>
<td><span data-lang="en">Competitiveness erosion, growth inhibition</span><span data-lang="ko">경쟁력 약화, 성장 저해</span></td>
</tr>
<tr>
<td>7</td>
<td><span data-lang="en">Policy Consistency</span><span data-lang="ko">정책 일관성</span></td>
<td><span data-lang="en">Contradicting FSC measures, self-contradiction</span><span data-lang="ko">금융위원회 조치와 모순, 자기모순</span></td>
<td><span data-lang="en">Administrative consistency loss</span><span data-lang="ko">행정 일관성 상실</span></td>
</tr>
</tbody>
</table>
</div>

<p data-lang="en"><strong>This is not "personal information protection" but "market restructuring through regulation"</strong></p>
<p data-lang="ko"><strong>이것은 "개인정보 보호"가 아니라 "규제를 통한 시장 재편"입니다</strong></p>

<p data-lang="en"><strong>Not "data activation" but "data control"</strong><br>
<strong>Not "innovation promotion" but "growth regulation"</strong><br>
<strong>Not "protection enhancement" but "risk centralization"</strong></p>
<p data-lang="ko"><strong>"데이터 활성화"가 아니라 "데이터 통제"</strong><br>
<strong>"혁신 촉진"이 아니라 "성장 규제"</strong><br>
<strong>"보호 강화"가 아니라 "위험 집중"</strong></p>

<p data-lang="en">→ <strong>Careful reconsideration and sufficient social consensus required</strong></p>
<p data-lang="ko">→ <strong>신중한 재검토와 충분한 사회적 합의가 필요합니다</strong></p>

---

<h2 data-lang="en">Research Information</h2>
<h2 data-lang="ko">연구 정보</h2>

<p data-lang="en"><strong>Presentation Date:</strong> November 21, 2025<br>
<strong>Event:</strong> MyData Policy Startup Seminar<br>
<strong>Host:</strong> Korea Startup Forum<br>
<strong>Venue:</strong> D.CAMP, Gangnam, Seoul<br>
<strong>Speaker:</strong> Yonghee Kim, Ph.D.</p>
<p data-lang="ko"><strong>발표일:</strong> 2025년 11월 21일<br>
<strong>행사:</strong> 마이데이터 정책 스타트업 세미나<br>
<strong>주최:</strong> 한국스타트업포럼<br>
<strong>장소:</strong> D.CAMP, 강남, 서울<br>
<strong>발표자:</strong> 김용희 박사</p>

<p data-lang="en"><strong>Research Focus:</strong></p>
<p data-lang="ko"><strong>연구 분야:</strong></p>

<ul data-lang="en">
<li>Data policy and governance</li>
<li>Digital platform regulation</li>
<li>Startup ecosystem protection</li>
<li>Regulatory impact analysis</li>
</ul>
<ul data-lang="ko">
<li>데이터 정책 및 거버넌스</li>
<li>디지털 플랫폼 규제</li>
<li>스타트업 생태계 보호</li>
<li>규제 영향 분석</li>
</ul>

<p><strong data-lang="en">Contact:</strong><strong data-lang="ko">연락처:</strong></p>
<ul>
<li>Email: yhkim1981@sunmoon.ac.kr</li>
<li><span data-lang="en">Institution: Sunmoon University, Department of Business Administration</span><span data-lang="ko">소속: 선문대학교 경영학과</span></li>
<li>ORCID: 0000-0002-5643-2748</li>
</ul>

---

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
  
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
          y: { beginAtZero: true, max: 1.2, ticks: { stepSize: 1, callback: function(value) { return value === 1 ? '✓ Included' : ''; } } }
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
        labels: ['0', '200K', '400K', '600K', '800K', '1M ⚠', '1.2M', '1.5M'],
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

});
</script>

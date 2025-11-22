---
title: "본인전송요구권 확대가 가져올 사회적 문제와 대응 방안"
title_en: "The Right to Data Transfer: Social Problems and Response Plans"
subtitle: "개인정보보호법 시행령 개정안의 법적·정책적 문제점 검토"
subtitle_en: "Critical Analysis of Personal Information Protection Act Enforcement Decree Amendment"
date: "2025-11-21"
category: "Data Policy"
tags: ["MyData", "Data Privacy", "Regulation", "Policy Analysis", "Startup Ecosystem", "GDPR"]
conference: "MyData Policy Startup Seminar"
venue: "Korea Startup Forum, D.CAMP, Gangnam, Seoul"
description: "본인전송요구권 확대 개정안의 7가지 핵심 문제점 분석: 절차적 정당성 위반, 헌법적 문제, GDPR 불일치, 스타트업 생태계 위협"
description_en: "In-depth analysis of the proposed expansion of the Right to Request Data Transfer, examining seven critical concerns including regulatory procedural violations, constitutional issues, GDPR non-compliance, and threats to the startup ecosystem."
summary: "The June 2025 amendment proposal ignores Regulatory Reform Committee recommendations (August 2024), violates constitutional principles, contradicts GDPR standards, and threatens to destroy Korea's startup ecosystem through unfair privileges to specialized agencies."
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

## Executive Summary: A Regulatory Overreach Threatening Innovation

On **November 21, 2025**, I presented at the **MyData Policy Startup Seminar** hosted by the Korea Startup Forum at D.CAMP in Gangnam, Seoul. As a researcher examining the intersection of data policy, regulation, and innovation, I raised serious concerns about the **Personal Information Protection Act Enforcement Decree amendment** proposed in June 2025.

The amendment, which aims to expand the "Right to Request Data Transfer" to all industries, represents **a fundamental shift from data activation to data control**—one that threatens to undermine Korea's startup ecosystem while violating established regulatory principles and international norms.

<div class="highlight-box danger">
<h3>🚨 Critical Alert</h3>
<strong>The June 2025 amendment proposal violates the Regulatory Reform Committee's August 2024 decision by re-proposing identical content only 4 months later.</strong> This procedural violation undermines administrative integrity and ignores legitimate industry concerns about security, costs, and trade secrets.
</div>

---

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
      <h4>⚠️ Controversial Amendment Proposed</h4>
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

---

## The Expansion Trap: Current Law vs. Proposed Amendment

<div class="comparison-grid">
  <div class="comparison-card current">
    <h3>✅ Current Enforcement Decree (Feb 2025)</h3>
    <div class="metric-highlight">3 Sectors</div>
    <h4>Scope</h4>
    <ul>
      <li>Medical institutions</li>
      <li>Telecommunications carriers</li>
      <li>Energy providers</li>
    </ul>
    <h4>Characteristics</h4>
    <ul>
      <li>✓ Self-transfer = Third-party transfer scope</li>
      <li>✓ Follows Regulatory Reform Committee guidance</li>
      <li>✓ Gradual expansion principle</li>
      <li>✓ Sufficient pilot period</li>
    </ul>
  </div>

  <div class="comparison-card proposed">
    <h3>❌ Proposed Amendment (June 2025)</h3>
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
      <li>✗ Self-transfer ≠ Third-party transfer (inconsistent)</li>
      <li>✗ Violates Regulatory Reform Committee decision</li>
      <li>✗ Simultaneous expansion to all sectors</li>
      <li>✗ Only 4 months after initial implementation</li>
    </ul>
  </div>
</div>

<div class="highlight-box warning">
<h3>⚠️ What "Revenue 150B KRW & 1M Users" Really Means</h3>
<p>This threshold captures:</p>
<ul>
  <li><strong>Major platforms:</strong> Naver, Kakao, Coupang, Baemin, 11st, Gmarket, Auction</li>
  <li><strong>Growing startups:</strong> Any company reaching 1M users automatically included</li>
  <li><strong>Sectors affected:</strong> E-commerce, delivery, gaming, education, hospitality, culture & leisure</li>
</ul>
<p><strong>Result:</strong> Virtually all successful digital businesses are captured → De facto expansion to ALL industries</p>
</div>

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="scopeComparison"></canvas>
</div>

---

## Seven Critical Concerns

<div class="chart-container" style="height: 500px; margin-bottom: 3rem;"><canvas id="sevenConcernsRadar"></canvas></div>

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

---

## Deep Dive: GDPR Compliance Gap

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="timelineChart"></canvas>
</div>

---

## Deep Dive: GDPR Compliance Gap

<div class="vs-divider">
  <div class="vs-badge">VS</div>
</div>

<div class="comparison-grid">
  <div class="comparison-card current">
    <h3>GDPR Approach (Balanced)</h3>
    <ul style="line-height: 2;">
      <li>✓ Protects data subject rights</li>
      <li>✓ Respects business property rights</li>
      <li>✓ Explicitly protects trade secrets</li>
      <li>✓ Considers technical feasibility</li>
      <li>✓ Balanced approach</li>
    </ul>
    <div class="highlight-box info" style="margin-top: 1.5rem;">
      <strong>GDPR Article 20(4):</strong><br>
      "The right referred to in paragraph 1 <strong>shall not adversely affect the rights and freedoms of others.</strong>"
    </div>
  </div>

  <div class="comparison-card proposed">
    <h3>Korean Amendment (Unbalanced)</h3>
    <ul style="line-height: 2;">
      <li>✓ Protects data subject rights</li>
      <li>✗ Ignores business property rights</li>
      <li>✗ No trade secret protection</li>
      <li>✗ Unconditional transfer obligation</li>
      <li>✗ One-sided regulation</li>
    </ul>
    <div class="highlight-box danger" style="margin-top: 1.5rem;">
      <strong>Critical Flaw:</strong><br>
      Forces transfer of core business data (purchase patterns, pricing policies, customer segmentation, seller information) without "legitimate grounds" despite being trade secrets accumulated through years of investment
    </div>
  </div>
</div>

### EU Article 29 Working Party Guidelines

<div class="chart-container" style="height: 450px; margin: 3rem 0;">
  <canvas id="gdprComplianceChart"></canvas>
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

---

## The Financial Sector Paradox: Regulatory Self-Contradiction

<div class="highlight-box danger">
<h3>🔴 Financial Services Commission (2022): Screen Scraping Banned as Security Risk</h3>

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
<h3>🟡 Personal Information Protection Commission (2025): Allowing Scraping as "Automated Tool"</h3>

**Justification:**
- "Convenience for exercising rights"
- "Technical flexibility"
- **No clear security measures**

**Expected Result:** Revival of risks that FSC banned

**Scope:** E-commerce, platforms, gaming, education, culture & leisure - ALL industries
</div>

<div class="highlight-box danger">
<h3>⚠️ The Logical Contradiction</h3>

<strong>Regulatory Inconsistency:</strong>
1. Financial information is important → scraping banned
2. Medical, shopping, education information is not important → scraping allowed?

<strong>Violation of Personal Information Protection Act Article 29:</strong>

> **Article 29 (Security Measures Obligation):** Personal information controllers must establish internal management plans, maintain access records, and take technical, administrative, and physical measures necessary to ensure safety as prescribed by Presidential Decree to prevent personal information from being lost, stolen, leaked, forged, altered, or damaged.

→ **Allowing scraping directly contradicts the obligation to ensure security**

**Result:** Loss of consistency in personal information protection principles
</div>

<!-- CHART:regulatoryContradiction -->

---

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

---

## Single Point of Failure (SPOF): A National Security Risk

<div class="highlight-box danger">
<h3>🔴 From Distributed Risk to Concentrated Catastrophe</h3>

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

<!-- CHART:spofRisk -->

---

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

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="costImpactChart"></canvas>
</div>

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

<div class="chart-container" style="height: 400px; margin: 3rem 0;">
  <canvas id="startupGrowthTrap"></canvas>
</div>

**Irony:** The threshold "Revenue 150B KRW & 1M users" is marketed as targeting "large businesses" but actually hits **growing companies the hardest**.
</div>

<!-- CHART:startupGrowthTrap -->

---

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

---

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

---

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

---

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

---

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

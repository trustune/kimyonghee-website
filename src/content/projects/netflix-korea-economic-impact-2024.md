---
title: "The Hidden Investor: Netflix Korea's Economic Impact on K-Content Ecosystem"
title_en: "The Hidden Investor: Netflix Korea's Economic Impact on K-Content Ecosystem"
subtitle: "How 3.3 Trillion Won of 'Invisible FDI' Sustained Korea's Creative Industry Through Crisis"
subtitle_en: "How 3.3 Trillion Won of 'Invisible FDI' Sustained Korea's Creative Industry Through Crisis"
date: "2024-12-05"
category: "Media Economics"
tags: ["Netflix", "K-Content", "FDI", "Input-Output Analysis", "Economic Impact", "Employment", "COVID-19"]
keywords: ["Netflix Korea", "Economic Ripple Effect", "Hidden FDI", "Content Investment", "Employment Efficiency", "Counter-Cyclical Investment", "K-Content Ecosystem", "Production Inducement", "Value Added", "Human Capital Preservation"]
methodology: ["Input-Output Analysis", "Leontief Inverse Matrix", "Employment Inducement Coefficient", "Comparative Industry Analysis", "Gap Filling Analysis"]
data_period:
  start: "2020"
  end: "2023"
data_sources:
  - name: "Bank of Korea ECOS Input-Output Tables (New Series)"
    type: "primary"
  - name: "Netflix Korea Financial Statements (DART)"
    type: "primary"
  - name: "Netflix Inc. Content Investment Announcements"
    type: "primary"
  - name: "Broadcasting Industry Survey"
    type: "secondary"
related_publications: []
related_projects: ["broadcasting-revenue-2015-2024", "broadcasting-reapproval-2024"]
conference: ""
conference_en: ""
description: "Input-output analysis reveals Netflix Korea's true economic contribution: 3.3 trillion won in 'hidden FDI' generated 6.9 trillion won production and sustained 28,500 jobs during the pandemic crisis."
description_en: "Input-output analysis reveals Netflix Korea's true economic contribution: 3.3 trillion won in 'hidden FDI' generated 6.9 trillion won production and sustained 28,500 jobs during the pandemic crisis."
summary: "Financial statements show only 450 billion won, but actual investment including content production reached 3.3 trillion won (4-year cumulative). This 'hidden FDI' created 3.6x more jobs per billion won than semiconductor industry."
key_findings:
  - "Hidden FDI discovered: 3.3 trillion won total vs 450 billion won in financial statements"
  - "Production multiplier effect: 6.9 trillion won (2.07x) over 4 years"
  - "Employment efficiency: 3.6x higher job creation than semiconductor industry"
  - "Domestic retention rate: 93.3% of investment circulated within Korea"
  - "Counter-cyclical buffer: Filled 28.7% of legacy media investment gap during COVID-19"
  - "Human capital preservation: Sustained 8,777 jobs during 2020-2021 pandemic crisis"
policy_proposals:
  - "Recognize 'content FDI' employment efficiency in foreign investment policy"
  - "Account for hidden investment beyond financial statements in economic impact assessment"
  - "Acknowledge counter-cyclical investment's industry stabilization contribution"
featured: true
---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

<style>
.story-section {
  margin: 3rem 0;
  padding: 2rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.story-section h3 {
  color: #2d3748;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.story-section p {
  color: #4a5568;
  line-height: 1.8;
  font-size: 1.1rem;
}

.metric-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.metric-card {
  padding: 1.5rem;
  background: linear-gradient(135deg, #e50914 0%, #b81d24 100%);
  color: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(229, 9, 20, 0.3);
  text-align: center;
}

.metric-card.alt {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
}

.metric-card.green {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.metric-card.blue {
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

.metric-value {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.metric-label {
  font-size: 0.95rem;
  opacity: 0.9;
  line-height: 1.4;
}

.chart-container {
  margin: 2rem 0;
  padding: 1.5rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.chart-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 1rem;
  text-align: center;
}

.insight-box {
  margin: 2rem 0;
  padding: 1.5rem;
  background: #fef2f2;
  border-left: 4px solid #e50914;
  border-radius: 4px;
}

.insight-box.blue {
  background: #eff6ff;
  border-left-color: #3b82f6;
}

.insight-box.green {
  background: #ecfdf5;
  border-left-color: #10b981;
}

.insight-box h4 {
  color: #991b1b;
  margin-bottom: 0.5rem;
}

.insight-box.blue h4 {
  color: #1e40af;
}

.insight-box.green h4 {
  color: #065f46;
}

.data-source {
  font-size: 0.9rem;
  color: #718096;
  font-style: italic;
  margin-top: 1rem;
}

.data-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin: 2rem 0;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.data-table thead {
  background: linear-gradient(135deg, #e50914 0%, #b81d24 100%);
  color: white;
}

.data-table th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  font-size: 0.95rem;
}

.data-table tbody tr {
  border-bottom: 1px solid #e5e7eb;
  transition: background 0.2s;
}

.data-table tbody tr:hover {
  background: #fef2f2;
}

.data-table td {
  padding: 1rem;
  font-size: 0.95rem;
  color: #374151;
}

.data-table .number {
  text-align: right;
  font-weight: 500;
  font-family: 'Courier New', monospace;
}

.section-divider {
  height: 2px;
  background: linear-gradient(90deg, transparent, #e50914, transparent);
  margin: 3rem 0;
  border: none;
}

.comparison-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin: 2rem 0;
}

@media (max-width: 768px) {
  .comparison-grid {
    grid-template-columns: 1fr;
  }
}

.comparison-box {
  padding: 1.5rem;
  border-radius: 8px;
  text-align: center;
}

.comparison-box.legacy {
  background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
  border: 2px solid #ef4444;
}

.comparison-box.netflix {
  background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
  border: 2px solid #22c55e;
}

.comparison-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.comparison-value {
  font-size: 2rem;
  font-weight: 700;
  margin: 0.5rem 0;
}

.comparison-box.legacy .comparison-value {
  color: #dc2626;
}

.comparison-box.netflix .comparison-value {
  color: #16a34a;
}

.timeline-item {
  display: flex;
  margin: 1rem 0;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 8px;
  border-left: 4px solid #e50914;
}

.timeline-year {
  font-weight: 700;
  color: #e50914;
  width: 80px;
  flex-shrink: 0;
}

.timeline-content {
  flex: 1;
}

.highlight-number {
  color: #e50914;
  font-weight: 700;
}
</style>

## The Untold Story: What Financial Statements Don't Reveal

When we evaluate Netflix Korea's economic contribution, most analyses focus on the company's reported revenue and profits. But this approach misses a crucial piece of the puzzle: **the massive content production investments that flow directly from Netflix Inc. (US) to Korean production companies** - bypassing Korean financial statements entirely.

<div class="metric-cards">
  <div class="metric-card">
    <div class="metric-value">3.3 Trillion</div>
    <div class="metric-label">Total Investment (KRW)<br/>2020-2023 Cumulative</div>
  </div>
  <div class="metric-card alt">
    <div class="metric-value">6.9 Trillion</div>
    <div class="metric-label">Production Induced (KRW)<br/>2.07x Multiplier</div>
  </div>
  <div class="metric-card green">
    <div class="metric-value">28,501</div>
    <div class="metric-label">Jobs Created<br/>4-Year Total</div>
  </div>
  <div class="metric-card blue">
    <div class="metric-value">93.3%</div>
    <div class="metric-label">Domestic Retention<br/>Stayed in Korea</div>
  </div>
</div>

<div class="insight-box">
  <h4>The Hidden FDI Discovery</h4>
  <p><strong>Financial statements show:</strong> ~450 billion KRW (two subsidiaries' operating costs)<br/>
  <strong>Actual investment:</strong> ~3.3 trillion KRW (including content production)<br/>
  <strong>The gap:</strong> 2.9 trillion KRW of "invisible" foreign direct investment</p>
</div>

<hr class="section-divider">

## Part 1: The Investment Paradox - Where Does the Money Go?

Netflix Korea operates through two subsidiaries: **Netflix Services Korea** (subscription resale) and **Netflix Entertainment Korea** (content support). But here's the key insight: **content production investments flow directly from US headquarters to Korean production companies**.

<div class="chart-container">
  <div class="chart-title">Netflix Korea Investment Flow (2020-2023)</div>
  <canvas id="investmentFlow"></canvas>
</div>

### The Money Trail

<table class="data-table">
  <thead>
    <tr>
      <th>Year</th>
      <th>Operating Costs</th>
      <th>Content Investment</th>
      <th>Total Input</th>
      <th>YoY Growth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2020</td>
      <td class="number">611</td>
      <td class="number">3,300</td>
      <td class="number"><strong>3,911</strong></td>
      <td class="number">-</td>
    </tr>
    <tr>
      <td>2021</td>
      <td class="number">929</td>
      <td class="number">5,500</td>
      <td class="number"><strong>6,429</strong></td>
      <td class="number">+64.4%</td>
    </tr>
    <tr>
      <td>2022</td>
      <td class="number">1,040</td>
      <td class="number">8,000</td>
      <td class="number"><strong>9,040</strong></td>
      <td class="number">+40.6%</td>
    </tr>
    <tr>
      <td>2023</td>
      <td class="number">1,923</td>
      <td class="number">12,192</td>
      <td class="number"><strong>14,115</strong></td>
      <td class="number">+56.1%</td>
    </tr>
    <tr style="background: #fef2f2; font-weight: bold;">
      <td>Total</td>
      <td class="number">4,503</td>
      <td class="number">28,992</td>
      <td class="number"><strong>33,495</strong></td>
      <td class="number">-</td>
    </tr>
  </tbody>
</table>

<p class="data-source">Source: DART Financial Statements (Operating Costs), Netflix Official Announcements (Content Investment: USD 2.5B / 3 years for 2023-2025)</p>

<hr class="section-divider">

## Part 2: The Employment Efficiency Paradox

Here's where Netflix's investment model truly shines. When we compare job creation efficiency across industries, **content investment creates 3.6 times more jobs per billion won than semiconductor manufacturing**.

<div class="chart-container">
  <div class="chart-title">Employment Inducement Coefficient by Industry (Jobs per 1 Billion KRW)</div>
  <canvas id="employmentComparison"></canvas>
</div>

<table class="data-table">
  <thead>
    <tr>
      <th>Industry</th>
      <th>Employment Coefficient</th>
      <th>Import Coefficient</th>
      <th>Industry Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Accommodation & Food</td>
      <td class="number">1.62</td>
      <td class="number">0.053</td>
      <td>Key Industry</td>
    </tr>
    <tr style="background: #fef2f2;">
      <td><strong>Arts, Sports & Leisure</strong></td>
      <td class="number"><strong>0.84</strong></td>
      <td class="number"><strong>0.010</strong></td>
      <td>Independent</td>
    </tr>
    <tr style="background: #fef2f2;">
      <td><strong>ICT & Broadcasting</strong></td>
      <td class="number"><strong>0.83</strong></td>
      <td class="number"><strong>0.159</strong></td>
      <td>Platform</td>
    </tr>
    <tr>
      <td>Construction</td>
      <td class="number">0.65</td>
      <td class="number">0.000</td>
      <td>Final Goods</td>
    </tr>
    <tr>
      <td>Semiconductor/Electronics</td>
      <td class="number">0.23</td>
      <td class="number">0.621</td>
      <td>Platform</td>
    </tr>
    <tr>
      <td>Automobile</td>
      <td class="number">0.22</td>
      <td class="number">0.131</td>
      <td>Key Industry</td>
    </tr>
  </tbody>
</table>

<div class="insight-box blue">
  <h4>Why Content Investment Creates More Jobs</h4>
  <p><strong>Semiconductor:</strong> Capital-intensive, equipment-focused ("jobless growth")<br/>
  <strong>Content Production:</strong> Labor-intensive, people-focused (directors, writers, actors, crew, VFX artists)<br/>
  <strong>Result:</strong> Same 1 trillion KRW creates <span class="highlight-number">3.6x more jobs</span> in content than semiconductors</p>
</div>

<hr class="section-divider">

## Part 3: The Counter-Cyclical Safety Net

**This is the most critical finding.** When COVID-19 devastated the traditional media industry in 2020, Netflix didn't retreat - it **doubled down** on Korean content investment, effectively serving as a financial lifeline for the entire ecosystem.

<div class="comparison-grid">
  <div class="comparison-box legacy">
    <div class="comparison-title">Legacy Media (2020)</div>
    <div class="comparison-value">-37.1%</div>
    <div>Investment Collapse</div>
    <div style="margin-top: 0.5rem; font-size: 0.9rem;">Theaters closed, Ad revenue crashed</div>
  </div>
  <div class="comparison-box netflix">
    <div class="comparison-title">Netflix (2020-2021)</div>
    <div class="comparison-value">+66.7%</div>
    <div>Aggressive Expansion</div>
    <div style="margin-top: 0.5rem; font-size: 0.9rem;">880 billion KRW invested</div>
  </div>
</div>

<div class="chart-container">
  <div class="chart-title">Gap Filling Effect: Netflix vs Legacy Media Investment (Billion KRW)</div>
  <canvas id="gapFilling"></canvas>
</div>

### The Crisis Buffer Mechanism

<table class="data-table">
  <thead>
    <tr>
      <th>Year</th>
      <th>Netflix</th>
      <th>Terrestrial TV</th>
      <th>Film Investment</th>
      <th>Cable PP</th>
      <th>Legacy Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2019 (Pre-COVID)</td>
      <td class="number">-</td>
      <td class="number">18,000</td>
      <td class="number">5,000</td>
      <td class="number">8,000</td>
      <td class="number"><strong>31,000</strong></td>
    </tr>
    <tr style="background: #fef2f2;">
      <td>2020 (COVID Year 1)</td>
      <td class="number"><strong>3,300</strong></td>
      <td class="number">12,000</td>
      <td class="number">1,500</td>
      <td class="number">6,000</td>
      <td class="number">19,500</td>
    </tr>
    <tr style="background: #fef2f2;">
      <td>2021 (COVID Year 2)</td>
      <td class="number"><strong>5,500</strong></td>
      <td class="number">13,000</td>
      <td class="number">2,000</td>
      <td class="number">6,500</td>
      <td class="number">21,500</td>
    </tr>
    <tr>
      <td>2022 (Recovery)</td>
      <td class="number"><strong>8,000</strong></td>
      <td class="number">14,000</td>
      <td class="number">3,500</td>
      <td class="number">7,000</td>
      <td class="number">24,500</td>
    </tr>
    <tr>
      <td>2023 (Normalized)</td>
      <td class="number"><strong>12,192</strong></td>
      <td class="number">15,000</td>
      <td class="number">4,500</td>
      <td class="number">7,500</td>
      <td class="number">27,000</td>
    </tr>
  </tbody>
</table>

<div class="insight-box green">
  <h4>Lender of Last Resort</h4>
  <p><strong>2020 Legacy Media Drop:</strong> -11,500 billion KRW (-37.1% YoY)<br/>
  <strong>Netflix Investment:</strong> 3,300 billion KRW<br/>
  <strong>Gap Filled:</strong> 28.7% of legacy decline compensated<br/>
  <strong>Role:</strong> Netflix served as the industry's "lender of last resort" during the crisis</p>
</div>

<hr class="section-divider">

## Part 4: Human Capital Preservation

The content industry's workforce is predominantly **freelance and project-based** - directors, writers, cinematographers, lighting technicians, VFX artists. When projects stop, they immediately become unemployed. During COVID-19, Netflix's continued investment **prevented a mass exodus of skilled talent** from the industry.

<div class="chart-container">
  <div class="chart-title">Employment Induced by Netflix Investment (Persons)</div>
  <canvas id="employmentTimeline"></canvas>
</div>

### The Preservation Mechanism

<div class="timeline-item">
  <div class="timeline-year">2020</div>
  <div class="timeline-content">
    <strong>3,562 jobs sustained</strong> during theater closures and production shutdowns.<br/>
    Freelance crew received continuous project opportunities.
  </div>
</div>

<div class="timeline-item">
  <div class="timeline-year">2021</div>
  <div class="timeline-content">
    <strong>5,215 jobs sustained</strong> as Netflix expanded Korean original content.<br/>
    "Squid Game" production employed hundreds of skilled workers.
  </div>
</div>

<div class="timeline-item">
  <div class="timeline-year">2020-21</div>
  <div class="timeline-content">
    <strong>8,777 jobs total</strong> during the pandemic's worst years.<br/>
    Human capital preserved for post-pandemic industry recovery.
  </div>
</div>

<div class="insight-box">
  <h4>Why This Matters</h4>
  <p><strong>Skill Formation:</strong> Content industry skills take 7-10 years to develop<br/>
  <strong>Industry Exit Risk:</strong> Once workers leave for delivery/gig economy, they rarely return<br/>
  <strong>Netflix Effect:</strong> Provided "employment continuity" that preserved K-Content's competitive foundation<br/>
  <strong>Post-Pandemic Result:</strong> Industry could immediately scale up when demand returned</p>
</div>

<hr class="section-divider">

## Part 5: Vendor Ecosystem Safety Net

Netflix's investment model fundamentally differs from traditional Korean broadcasters in how it distributes financial risk and maintains cash flow stability for production companies.

<div class="comparison-grid">
  <div class="comparison-box legacy">
    <div class="comparison-title">Traditional Model</div>
    <div style="text-align: left; padding: 1rem;">
      <p><strong>Payment:</strong> Post-production settlement (2-6 months delay)</p>
      <p><strong>Risk:</strong> Box office failure = production company loss</p>
      <p><strong>Cash Flow:</strong> Unstable, requires bridge loans</p>
      <p><strong>Result:</strong> SME producers face "profitable bankruptcy" risk</p>
    </div>
  </div>
  <div class="comparison-box netflix">
    <div class="comparison-title">Netflix Model</div>
    <div style="text-align: left; padding: 1rem;">
      <p><strong>Payment:</strong> 100% upfront + milestone payments</p>
      <p><strong>Risk:</strong> Netflix HQ absorbs all box office risk</p>
      <p><strong>Cash Flow:</strong> Stable, no loans needed</p>
      <p><strong>Result:</strong> Producers focus on creation, not survival</p>
    </div>
  </div>
</div>

### Ecosystem Stabilization Effects

1. **Cash Flow Stability**: Upfront payment eliminates working capital crunch
2. **Risk Hedging**: Production companies protected from market volatility  
3. **Economies of Scale**: Large projects enable equipment/talent investment
4. **Technology Upgrade**: Netflix quality standards drove VFX/production capability improvements
5. **Supply Chain Protection**: Prevented K-Content production chain collapse during pandemic

<hr class="section-divider">

## Part 6: Four-Year Cumulative Impact Summary

<div class="chart-container">
  <div class="chart-title">Cumulative Economic Ripple Effects (2020-2023)</div>
  <canvas id="cumulativeEffects"></canvas>
</div>

<table class="data-table">
  <thead>
    <tr>
      <th>Indicator</th>
      <th>4-Year Cumulative</th>
      <th>Annual Average</th>
      <th>Unit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total Investment Input</td>
      <td class="number"><strong>33,495</strong></td>
      <td class="number">8,374</td>
      <td>Billion KRW</td>
    </tr>
    <tr>
      <td>Production Induced</td>
      <td class="number"><strong>69,422</strong></td>
      <td class="number">17,356</td>
      <td>Billion KRW</td>
    </tr>
    <tr>
      <td>Value Added (GDP Contribution)</td>
      <td class="number"><strong>36,534</strong></td>
      <td class="number">9,134</td>
      <td>Billion KRW</td>
    </tr>
    <tr>
      <td>Employment Induced</td>
      <td class="number"><strong>28,501</strong></td>
      <td class="number">7,125</td>
      <td>Persons</td>
    </tr>
    <tr>
      <td>Wage Employment Induced</td>
      <td class="number"><strong>25,913</strong></td>
      <td class="number">6,478</td>
      <td>Persons</td>
    </tr>
    <tr>
      <td>Income Induced (Household)</td>
      <td class="number"><strong>15,197</strong></td>
      <td class="number">3,799</td>
      <td>Billion KRW</td>
    </tr>
    <tr>
      <td>Production Tax Induced</td>
      <td class="number"><strong>2,091</strong></td>
      <td class="number">523</td>
      <td>Billion KRW</td>
    </tr>
  </tbody>
</table>

<div class="metric-cards">
  <div class="metric-card">
    <div class="metric-value">2.07x</div>
    <div class="metric-label">Average Production<br/>Multiplier</div>
  </div>
  <div class="metric-card green">
    <div class="metric-value">93.3%</div>
    <div class="metric-label">Domestic<br/>Retention Rate</div>
  </div>
  <div class="metric-card blue">
    <div class="metric-value">3.6x</div>
    <div class="metric-label">Job Creation vs<br/>Semiconductor</div>
  </div>
  <div class="metric-card alt">
    <div class="metric-value">28.7%</div>
    <div class="metric-label">COVID Gap<br/>Filled</div>
  </div>
</div>

<hr class="section-divider">

## Conclusion: Rethinking Netflix's Economic Contribution

The conventional view of Netflix Korea focuses on subscription revenue and local tax payments. But this analysis reveals a fundamentally different picture:

### The Three Pillars of Netflix's Contribution

1. **Employment-Efficient FDI**: Creates 3.6x more jobs per won than manufacturing FDI
2. **Counter-Cyclical Stabilizer**: Filled market gap during COVID-19 crisis
3. **Ecosystem Infrastructure**: Stabilized production company finances and preserved human capital

### Policy Implications

Future discussions about Netflix's role in Korea should move beyond simplistic debates about "network usage fees" or "profit repatriation" to recognize:

- **Hidden investment flows** that bypass financial statements but fuel the real economy
- **Employment efficiency** of content investment vs. traditional manufacturing FDI
- **Crisis buffer function** that stabilizes entire industry ecosystems
- **Human capital preservation** that maintains long-term competitive advantage

The data shows that Netflix is not just a "foreign company making money in Korea" - it's a **structural partner in Korea's creative economy** that provided critical support during the industry's most challenging period.

<hr class="section-divider">

## Methodology & Data Transparency

**Analysis Framework**: Input-Output Analysis using Bank of Korea ECOS Tables

**Key Coefficients Used**:
- Production Inducement Coefficient (Leontief Inverse)
- Value Added Inducement Coefficient
- Employment Inducement Coefficient (persons per billion KRW)
- Import Inducement Coefficient

**Data Sources**:
- Bank of Korea ECOS Input-Output Tables (New Series, 2020-2023)
- Netflix Korea Financial Statements via DART
- Netflix Inc. Official Investment Announcements
- Broadcasting Industry Survey (for legacy media comparison)

**Industry Classification**:
- Netflix Operations: J (ICT & Broadcasting Services)
- Content Production: J (Video Production/Distribution)

**Limitations**:
- Content investment breakdown by sub-sector not disclosed (business confidential)
- 2024 IO tables not yet available (analysis ends at 2023)
- Legacy media investment figures are estimates based on industry surveys

<hr class="section-divider">

## Project Information

**Research Period:** November 2024 - December 2024
**Last Updated:** December 5, 2024
**Version:** v1.0
**Analysis Tool:** Python (pandas, numpy) + Bank of Korea ECOS API

<hr class="section-divider">

## Researcher Information

**Yonghee Kim, Ph.D.**
Assistant Professor, Department of Business Administration
Sunmoon University

**Expertise:**
- Media policy and regulation
- Digital platform economics
- Input-Output economic analysis
- Media business strategy

**Contact:**
- Email: yhkim@sunmoon.ac.kr
- ORCID: 0000-0002-5643-2748
- Google Scholar: [View Profile](https://scholar.google.com/citations?user=semkeskAAAAJ)

---

<script>
// 1. Investment Flow Chart
const ctxInvestment = document.getElementById('investmentFlow');
if (ctxInvestment) {
  new Chart(ctxInvestment, {
    type: 'bar',
    data: {
      labels: ['2020', '2021', '2022', '2023'],
      datasets: [{
        label: 'Operating Costs (Billion KRW)',
        data: [611, 929, 1040, 1923],
        backgroundColor: 'rgba(26, 26, 46, 0.8)',
        borderColor: 'rgb(26, 26, 46)',
        borderWidth: 1
      }, {
        label: 'Content Investment (Billion KRW)',
        data: [3300, 5500, 8000, 12192],
        backgroundColor: 'rgba(229, 9, 20, 0.8)',
        borderColor: 'rgb(229, 9, 20)',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'bottom' }
      },
      scales: {
        x: { stacked: true },
        y: { 
          stacked: true,
          title: { display: true, text: 'Billion KRW' }
        }
      }
    }
  });
}

// 2. Employment Comparison Chart
const ctxEmployment = document.getElementById('employmentComparison');
if (ctxEmployment) {
  new Chart(ctxEmployment, {
    type: 'bar',
    data: {
      labels: ['Accommodation\n& Food', 'Arts/Sports\n(Content)', 'ICT &\nBroadcasting', 'Construction', 'Semiconductor', 'Automobile'],
      datasets: [{
        label: 'Jobs per Billion KRW',
        data: [1.62, 0.84, 0.83, 0.65, 0.23, 0.22],
        backgroundColor: [
          'rgba(156, 163, 175, 0.8)',
          'rgba(229, 9, 20, 0.8)',
          'rgba(229, 9, 20, 0.8)',
          'rgba(156, 163, 175, 0.8)',
          'rgba(59, 130, 246, 0.8)',
          'rgba(59, 130, 246, 0.8)'
        ],
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: 'Jobs per Billion KRW' }
        }
      }
    }
  });
}

// 3. Gap Filling Chart
const ctxGap = document.getElementById('gapFilling');
if (ctxGap) {
  new Chart(ctxGap, {
    type: 'line',
    data: {
      labels: ['2019', '2020', '2021', '2022', '2023'],
      datasets: [{
        label: 'Legacy Media (Terrestrial + Film + Cable)',
        data: [31000, 19500, 21500, 24500, 27000],
        borderColor: 'rgb(220, 38, 38)',
        backgroundColor: 'rgba(220, 38, 38, 0.1)',
        fill: true,
        tension: 0.3
      }, {
        label: 'Netflix Investment',
        data: [0, 3300, 5500, 8000, 12192],
        borderColor: 'rgb(229, 9, 20)',
        backgroundColor: 'rgba(229, 9, 20, 0.3)',
        fill: true,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'bottom' }
      },
      scales: {
        y: {
          title: { display: true, text: 'Billion KRW' }
        }
      }
    }
  });
}

// 4. Employment Timeline
const ctxEmpTimeline = document.getElementById('employmentTimeline');
if (ctxEmpTimeline) {
  new Chart(ctxEmpTimeline, {
    type: 'bar',
    data: {
      labels: ['2020', '2021', '2022', '2023'],
      datasets: [{
        label: 'Employment Induced (Persons)',
        data: [3562, 5215, 7290, 12434],
        backgroundColor: [
          'rgba(229, 9, 20, 0.9)',
          'rgba(229, 9, 20, 0.9)',
          'rgba(229, 9, 20, 0.7)',
          'rgba(229, 9, 20, 0.5)'
        ],
        borderColor: 'rgb(229, 9, 20)',
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            afterLabel: function(context) {
              const notes = [
                'COVID Year 1 - Theater closures',
                'COVID Year 2 - Squid Game production',
                'Recovery phase',
                'Full expansion'
              ];
              return notes[context.dataIndex];
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: 'Persons' }
        }
      }
    }
  });
}

// 5. Cumulative Effects Chart
const ctxCumulative = document.getElementById('cumulativeEffects');
if (ctxCumulative) {
  new Chart(ctxCumulative, {
    type: 'bar',
    data: {
      labels: ['Investment\nInput', 'Production\nInduced', 'Value Added\n(GDP)', 'Income\nInduced', 'Production\nTax'],
      datasets: [{
        label: 'Trillion KRW',
        data: [3.3, 6.9, 3.7, 1.5, 0.2],
        backgroundColor: [
          'rgba(26, 26, 46, 0.8)',
          'rgba(229, 9, 20, 0.8)',
          'rgba(16, 185, 129, 0.8)',
          'rgba(59, 130, 246, 0.8)',
          'rgba(245, 158, 11, 0.8)'
        ],
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: 'Trillion KRW' }
        }
      }
    }
  });
}
</script>

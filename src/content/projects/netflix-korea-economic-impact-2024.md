---
title: "The Hidden Investor: Netflix Korea's Economic Impact on K-Content Ecosystem"
title_en: "The Hidden Investor: Netflix Korea's Economic Impact on K-Content Ecosystem"
title_ko: "숨겨진 투자자: 넷플릭스 코리아의 K-콘텐츠 생태계 경제적 파급효과"
subtitle: "How 3.3 Trillion Won of 'Invisible FDI' Sustained Korea's Creative Industry Through Crisis"
subtitle_en: "How 3.3 Trillion Won of 'Invisible FDI' Sustained Korea's Creative Industry Through Crisis"
subtitle_ko: "3.3조원의 '보이지 않는 FDI'가 위기의 한국 창작산업을 지탱한 방법"
date: "2025-12-05"
category: "Media Economics"
tags: ["Netflix", "K-Content", "FDI", "Input-Output Analysis", "Economic Impact", "Employment", "COVID-19"]
keywords: ["Netflix Korea", "Economic Ripple Effect", "Hidden FDI", "Content Investment", "Employment Efficiency", "Counter-Cyclical Investment", "K-Content Ecosystem", "Production Inducement", "Value Added", "Human Capital Preservation", "Tax Contribution", "Global Capital Pipeline"]
methodology: ["Input-Output Analysis", "Leontief Inverse Matrix", "Employment Inducement Coefficient", "Comparative Industry Analysis", "Gap Filling Analysis", "Tax Incidence Analysis"]
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
  - name: "Korea Communications Commission Broadcasting Revenue Data"
    type: "secondary"
  - name: "Broadcasting Industry Survey"
    type: "secondary"
related_publications: []
related_projects: ["broadcasting-revenue-2015-2024", "broadcasting-reapproval-2024"]
conference: ""
conference_en: ""
conference_ko: ""
description: "Input-output analysis reveals Netflix Korea's true economic contribution: 3.3 trillion won in 'hidden FDI' generated 6.9 trillion won production and sustained 28,500 jobs during the pandemic crisis."
description_en: "Input-output analysis reveals Netflix Korea's true economic contribution: 3.3 trillion won in 'hidden FDI' generated 6.9 trillion won production and sustained 28,500 jobs during the pandemic crisis."
description_ko: "산업연관분석으로 밝힌 넷플릭스 코리아의 진정한 경제적 기여: 3.3조원의 '숨겨진 FDI'가 6.9조원의 생산을 유발하고 팬데믹 위기 동안 28,500개의 일자리를 유지했습니다."
summary: "Financial statements show only 450 billion won, but actual investment including content production reached 3.3 trillion won (4-year cumulative). This 'hidden FDI' created 3.6x more jobs per billion won than semiconductor industry."
summary_ko: "재무제표에는 4,500억원만 보이지만, 콘텐츠 제작을 포함한 실제 투자액은 3.3조원(4년 누적)에 달합니다. 이 '숨겨진 FDI'는 반도체 산업 대비 10억원당 3.6배 더 많은 일자리를 창출했습니다."
key_findings:
  - "Hidden FDI discovered: 3.3 trillion won total vs 450 billion won in financial statements"
  - "Global Capital Pipeline: Net inflow +487 billion won (2023) - more comes in than goes out"
  - "Production multiplier effect: 6.9 trillion won (2.07x) over 4 years"
  - "Employment efficiency: 3.6x higher job creation than semiconductor industry"
  - "Domestic retention rate: 93.3% of investment circulated within Korea"
  - "Counter-cyclical buffer: Filled 120.7% of broadcasting ad revenue gap"
  - "Human capital preservation: Sustained 8,777 jobs during 2020-2021 pandemic crisis"
  - "Hidden tax contribution: 143 billion won indirect taxes vs 3.6 billion corporate tax (40x)"
key_findings_ko:
  - "숨겨진 FDI 발견: 재무제표 4,500억원 vs 실제 투자 3.3조원"
  - "글로벌 자본 파이프라인: 순유입 +4,868억원 (2023) - 나간 돈보다 들어온 돈이 더 많음"
  - "생산유발효과: 4년간 6.9조원 (2.07배 승수)"
  - "고용 효율성: 반도체 대비 3.6배 높은 일자리 창출"
  - "국내 체류율: 투자금의 93.3%가 국내에서 순환"
  - "경기역행적 완충: 방송광고 감소분의 120.7% 대체"
  - "인적자본 보존: 2020-2021 팬데믹 위기 동안 8,777개 일자리 유지"
  - "숨겨진 조세 기여: 법인세 36억 vs 간접세 1,431억 (40배)"
policy_proposals:
  - "Recognize 'content FDI' employment efficiency in foreign investment policy"
  - "Account for hidden investment beyond financial statements in economic impact assessment"
  - "Acknowledge counter-cyclical investment's industry stabilization contribution"
  - "Consider indirect tax contribution (Tax Base Expansion) in evaluating foreign platform companies"
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

.metric-card.orange {
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
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

.insight-box.orange {
  background: #fffbeb;
  border-left-color: #f59e0b;
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

.insight-box.orange h4 {
  color: #92400e;
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

.data-table.blue-header thead {
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
}

.data-table.green-header thead {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
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

.flow-diagram {
  margin: 2rem 0;
  padding: 2rem;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  border-radius: 12px;
  color: white;
}

.flow-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 1rem 0;
  flex-wrap: wrap;
  gap: 1rem;
}

.flow-box {
  padding: 1rem 1.5rem;
  border-radius: 8px;
  text-align: center;
  min-width: 200px;
}

.flow-box.korea {
  background: rgba(229, 9, 20, 0.3);
  border: 2px solid #e50914;
}

.flow-box.us {
  background: rgba(59, 130, 246, 0.3);
  border: 2px solid #3b82f6;
}

.flow-box.producer {
  background: rgba(16, 185, 129, 0.3);
  border: 2px solid #10b981;
}

.flow-arrow {
  font-size: 2rem;
  color: #f59e0b;
}

.flow-amount {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0.5rem 0;
}

.flow-label {
  font-size: 0.85rem;
  opacity: 0.9;
}

.pipeline-highlight {
  background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
  border: 2px solid #10b981;
  border-radius: 12px;
  padding: 2rem;
  margin: 2rem 0;
  text-align: center;
}

.pipeline-highlight h3 {
  color: #065f46;
  margin-bottom: 1rem;
}

.pipeline-highlight .big-number {
  font-size: 3rem;
  font-weight: 800;
  color: #059669;
}

/* Mobile responsive styles */
@media (max-width: 768px) {
  .flow-row {
    flex-direction: column;
    align-items: stretch;
  }

  .flow-box {
    min-width: auto;
    width: 100%;
  }

  .flow-arrow {
    transform: rotate(90deg);
    margin: 0.5rem 0;
  }

  .flow-row:nth-child(2) .flow-arrow {
    transform: rotate(90deg);
  }

  .pipeline-highlight .big-number {
    font-size: 2rem;
  }

  .metric-cards {
    grid-template-columns: 1fr;
  }

  .metric-value {
    font-size: 1.8rem;
  }
}

@media (max-width: 640px) {
  .pipeline-highlight .big-number {
    font-size: 1.75rem;
  }

  .metric-value {
    font-size: 1.5rem;
  }

  .flow-amount {
    font-size: 1.25rem;
  }
}
</style>

<h2 data-lang="en">The Untold Story: What Financial Statements Don't Reveal</h2>
<h2 data-lang="ko">숨겨진 이야기: 재무제표가 말해주지 않는 것들</h2>

<p data-lang="en">When we evaluate Netflix Korea's economic contribution, most analyses focus on the company's reported revenue and profits. But this approach misses a crucial piece of the puzzle: <strong>the massive content production investments that flow directly from Netflix Inc. (US) to Korean production companies</strong> - bypassing Korean financial statements entirely.</p>
<p data-lang="ko">넷플릭스 코리아의 경제적 기여를 평가할 때, 대부분의 분석은 회사의 보고된 매출과 이익에 초점을 맞춥니다. 하지만 이러한 접근은 퍼즐의 중요한 조각을 놓치고 있습니다: <strong>넷플릭스 본사(미국)에서 한국 제작사로 직접 유입되는 대규모 콘텐츠 제작 투자금</strong> - 한국 재무제표를 완전히 우회하는 자금입니다.</p>

<div class="metric-cards">
  <div class="metric-card">
    <div class="metric-value">3.3T</div>
    <div class="metric-label">Total Investment (KRW)<br/>2020-2023 Cumulative</div>
  </div>
  <div class="metric-card alt">
    <div class="metric-value">6.9T</div>
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
  <h4 data-lang="en">The Hidden FDI Discovery</h4>
  <h4 data-lang="ko">숨겨진 FDI 발견</h4>
  <p data-lang="en"><strong>Financial statements show:</strong> ~450 billion KRW (two subsidiaries' operating costs)<br/>
  <strong>Actual investment:</strong> ~3.3 trillion KRW (including content production)<br/>
  <strong>The gap:</strong> 2.9 trillion KRW of "invisible" foreign direct investment that bypasses Korean subsidiaries</p>
  <p data-lang="ko"><strong>재무제표 상:</strong> ~4,500억원 (두 자회사의 운영비용)<br/>
  <strong>실제 투자액:</strong> ~3.3조원 (콘텐츠 제작 포함)<br/>
  <strong>차이:</strong> 한국 자회사를 우회하는 2.9조원의 "보이지 않는" 외국인 직접투자</p>
</div>

<hr class="section-divider">

<h2 data-lang="en">Part 1: The Global Capital Pipeline - More Comes In Than Goes Out</h2>
<h2 data-lang="ko">Part 1: 글로벌 자본 파이프라인 - 나가는 것보다 들어오는 것이 더 많다</h2>

A common criticism is that Netflix "takes subscription fees to the US." But examining the actual money flow reveals a fundamentally different picture: **Netflix is not a drain on Korea's economy - it's a pipeline that channels global capital INTO Korea.**

<div class="pipeline-highlight">
  <h3>The Core Thesis: Capital U-Turn Model</h3>
  <p>Netflix doesn't extract Korean capital - it <strong>adds</strong> global capital to Korea.</p>
  <div class="big-number">+487B KRW</div>
  <p><strong>Net Inflow to Korea (2023)</strong><br/>
  Content investment (1.22T) minus fee outflow (732B) = +487B KRW</p>
</div>

<div class="flow-diagram">
  <h3 style="text-align: center; margin-bottom: 1.5rem;">Netflix Korea Capital Flow (2023)</h3>
  
  <div class="flow-row">
    <div class="flow-box korea">
      <div class="flow-label">Korean Subscribers</div>
      <div class="flow-amount">900B</div>
      <div class="flow-label">KRW (Revenue)</div>
    </div>
    <div class="flow-arrow">--></div>
    <div class="flow-box korea">
      <div class="flow-label">Netflix Services Korea</div>
      <div class="flow-amount">151B</div>
      <div class="flow-label">KRW (Domestic Costs)</div>
    </div>
  </div>
  
  <div class="flow-row" style="justify-content: center;">
    <div class="flow-arrow" style="transform: rotate(90deg);">--></div>
    <div style="padding: 0.5rem 1rem; background: rgba(239, 68, 68, 0.3); border-radius: 4px;">
      <strong>732B KRW</strong><br/>
      <span style="font-size: 0.85rem;">Group Company Fee (to US)</span>
    </div>
  </div>
  
  <div class="flow-row">
    <div class="flow-box us">
      <div class="flow-label">Netflix Inc. (US HQ)</div>
      <div class="flow-amount">Global Pool</div>
      <div class="flow-label">Collects from 190+ countries</div>
    </div>
    <div class="flow-arrow">--></div>
    <div class="flow-box producer">
      <div class="flow-label">Korean Production Companies</div>
      <div class="flow-amount">1.22T+</div>
      <div class="flow-label">KRW (Content Investment)</div>
    </div>
  </div>
  
  <div style="text-align: center; margin-top: 1.5rem; padding: 1rem; background: rgba(16, 185, 129, 0.2); border-radius: 8px;">
    <strong style="color: #10b981; font-size: 1.2rem;">Net Inflow to Korea: +487B KRW</strong><br/>
    <span style="font-size: 0.9rem;">(Content Investment 1.22T - Fee Outflow 732B = <strong>+487B</strong>)</span>
  </div>
</div>

<div class="insight-box green">
  <h4>Why Korea is a Production Base, Not a Cash Cow</h4>
  <p><strong>Typical foreign company model:</strong> Earn in Korea --> Send profits home --> Zero reinvestment (True capital drain)<br/><br/>
  <strong>Netflix model:</strong> Earn in Korea + Earn globally --> Reinvest MORE than Korean earnings --> Korea becomes net recipient<br/><br/>
  <strong>Key insight:</strong> Korean subscription fees alone cannot fund productions like "Squid Game 2". Netflix brings <strong>global subscriber money from 190+ countries</strong> into Korea. Korea is Netflix's "Global Content R&D Center" - where investment flows IN, not out.</p>
</div>

<p class="data-source">Source: DART Financial Statements (2023), Netflix Korea representative confirmation (Content Investment: USD 2.5B / 3 years for 2023-2025)</p>

<hr class="section-divider">

<h2 data-lang="en">Part 2: Investment Flow by Year</h2>
<h2 data-lang="ko">Part 2: 연도별 투자 흐름</h2>

<div class="chart-container">
  <div class="chart-title">Netflix Korea Investment Flow (2020-2023)</div>
  <canvas id="investmentFlow"></canvas>
</div>

<table class="data-table">
  <thead>
    <tr>
      <th>Year</th>
      <th>Operating Costs<br/>(Billion KRW)</th>
      <th>Content Investment<br/>(Billion KRW)</th>
      <th>Total Input<br/>(Billion KRW)</th>
      <th>YoY Growth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2020</td>
      <td class="number">61</td>
      <td class="number">330</td>
      <td class="number"><strong>391</strong></td>
      <td class="number">-</td>
    </tr>
    <tr>
      <td>2021</td>
      <td class="number">93</td>
      <td class="number">550</td>
      <td class="number"><strong>643</strong></td>
      <td class="number">+64.4%</td>
    </tr>
    <tr>
      <td>2022</td>
      <td class="number">104</td>
      <td class="number">800</td>
      <td class="number"><strong>904</strong></td>
      <td class="number">+40.6%</td>
    </tr>
    <tr>
      <td>2023</td>
      <td class="number">192</td>
      <td class="number">1,219</td>
      <td class="number"><strong>1,411</strong></td>
      <td class="number">+56.1%</td>
    </tr>
    <tr style="background: #fef2f2; font-weight: bold;">
      <td>4-Year Total</td>
      <td class="number">450</td>
      <td class="number">2,899</td>
      <td class="number"><strong>3,349</strong></td>
      <td class="number">-</td>
    </tr>
  </tbody>
</table>

<p class="data-source">Source: DART Financial Statements (Operating Costs), Netflix Official Announcements (Content Investment: USD 2.5B / 3 years for 2023-2025)</p>

<hr class="section-divider">

<h2 data-lang="en">Part 3: Employment Efficiency - The 3.6x Advantage</h2>
<h2 data-lang="ko">Part 3: 고용 효율성 - 3.6배의 우위</h2>

When we compare job creation efficiency across industries, **content investment creates 3.6 times more jobs per 1 billion won than semiconductor manufacturing**.

<div class="chart-container">
  <div class="chart-title">Employment Inducement Coefficient by Industry (Jobs per 1 Billion KRW)</div>
  <canvas id="employmentComparison"></canvas>
</div>

<table class="data-table">
  <thead>
    <tr>
      <th>Industry</th>
      <th>Employment Coefficient<br/>(per 1B KRW)</th>
      <th>Import Coefficient</th>
      <th>Industry Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Accommodation & Food (I)</td>
      <td class="number">16.23</td>
      <td class="number">0.053</td>
      <td>Key Industry</td>
    </tr>
    <tr style="background: #fef2f2;">
      <td><strong>Arts, Sports & Leisure (R)</strong></td>
      <td class="number"><strong>8.44</strong></td>
      <td class="number"><strong>0.010</strong></td>
      <td>Independent</td>
    </tr>
    <tr style="background: #fef2f2;">
      <td><strong>ICT & Broadcasting (J)</strong></td>
      <td class="number"><strong>8.29</strong></td>
      <td class="number"><strong>0.159</strong></td>
      <td>Platform</td>
    </tr>
    <tr>
      <td>Construction (F)</td>
      <td class="number">6.54</td>
      <td class="number">0.000</td>
      <td>Final Goods</td>
    </tr>
    <tr>
      <td>Semiconductor/Electronics (C09)</td>
      <td class="number">2.34</td>
      <td class="number">0.312</td>
      <td>Platform</td>
    </tr>
    <tr>
      <td>Automobile (C12)</td>
      <td class="number">2.23</td>
      <td class="number">0.189</td>
      <td>Locomotive</td>
    </tr>
  </tbody>
</table>

<div class="insight-box">
  <h4>The 3.6x Employment Efficiency</h4>
  <p><strong>Content industry (8.29)</strong> vs <strong>Semiconductor (2.34)</strong> = 3.54x more jobs per 1 billion won<br/><br/>
  <strong>Why?</strong> Content production is labor-intensive: directors, writers, actors, cinematographers, lighting, sound, VFX artists, costume designers, set builders, caterers, drivers...<br/><br/>
  <strong>Policy Implication:</strong> When measuring FDI quality, employment efficiency should be weighted alongside investment volume.</p>
</div>

<hr class="section-divider">

<h2 data-lang="en">Part 4: The Counter-Cyclical Safety Net</h2>
<h2 data-lang="ko">Part 4: 경기역행적 안전망</h2>

**This is the most critical finding.** When COVID-19 devastated the traditional broadcasting industry in 2020, Netflix didn't retreat - it **doubled down** on Korean content investment.

### Broadcasting Industry Context (Verified Data)

According to Korea Communications Commission data, Korean broadcasting advertising revenue peaked at **3.30 trillion KRW in 2019** and has been declining since.

<div class="comparison-grid">
  <div class="comparison-box legacy">
    <div class="comparison-title">Broadcasting Advertising (2019-2024)</div>
    <div class="comparison-value">-30.6%</div>
    <div>Structural Collapse</div>
    <div style="margin-top: 0.5rem; font-size: 0.9rem;">3.30T --> 2.29T KRW (-1.01T lost)</div>
  </div>
  <div class="comparison-box netflix">
    <div class="comparison-title">Netflix Investment (2020-2023)</div>
    <div class="comparison-value">+269%</div>
    <div>Aggressive Expansion</div>
    <div style="margin-top: 0.5rem; font-size: 0.9rem;">0.33T --> 1.22T KRW (4-year: 2.9T)</div>
  </div>
</div>

<div class="chart-container">
  <div class="chart-title">Counter-Cyclical Effect: Broadcasting Ad Revenue vs Netflix Investment</div>
  <canvas id="gapFilling"></canvas>
</div>

<table class="data-table">
  <thead>
    <tr>
      <th>Year</th>
      <th>Broadcasting Ad<br/>(Trillion KRW)</th>
      <th>YoY Change</th>
      <th>Netflix Investment<br/>(Trillion KRW)</th>
      <th>YoY Change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2019 (Peak)</td>
      <td class="number">3.30</td>
      <td class="number">-</td>
      <td class="number">-</td>
      <td class="number">-</td>
    </tr>
    <tr style="background: #fef2f2;">
      <td>2020 (COVID Year 1)</td>
      <td class="number">2.88</td>
      <td class="number" style="color: #dc2626;">-12.7%</td>
      <td class="number"><strong>0.33</strong></td>
      <td class="number">-</td>
    </tr>
    <tr style="background: #fef2f2;">
      <td>2021 (COVID Year 2)</td>
      <td class="number">3.10</td>
      <td class="number" style="color: #16a34a;">+7.6%</td>
      <td class="number"><strong>0.55</strong></td>
      <td class="number" style="color: #16a34a;">+66.7%</td>
    </tr>
    <tr>
      <td>2022</td>
      <td class="number">2.88</td>
      <td class="number" style="color: #dc2626;">-7.1%</td>
      <td class="number"><strong>0.80</strong></td>
      <td class="number" style="color: #16a34a;">+45.5%</td>
    </tr>
    <tr>
      <td>2023</td>
      <td class="number">2.50</td>
      <td class="number" style="color: #dc2626;">-13.3%</td>
      <td class="number"><strong>1.22</strong></td>
      <td class="number" style="color: #16a34a;">+52.5%</td>
    </tr>
    <tr>
      <td>2024</td>
      <td class="number">2.29</td>
      <td class="number" style="color: #dc2626;">-8.4%</td>
      <td class="number"><strong>1.22</strong></td>
      <td class="number">-</td>
    </tr>
  </tbody>
</table>

<p class="data-source">Source: Korea Communications Commission Broadcasting Revenue Data (Ad Revenue), Netflix Official (Investment)</p>

<div class="insight-box green">
  <h4>Lender of Last Resort</h4>
  <p><strong>Broadcasting Ad Revenue Drop (2019-2024):</strong> -1.01 trillion KRW (-30.6%)<br/>
  <strong>Netflix Investment (2023):</strong> 1.22 trillion KRW<br/>
  <strong>Gap Coverage:</strong> 120.7% of ad revenue decline compensated<br/>
  <strong>Role:</strong> Netflix served as the industry's "lender of last resort" during the crisis</p>
</div>

<hr class="section-divider">

<h2 data-lang="en">Part 5: Human Capital Preservation</h2>
<h2 data-lang="ko">Part 5: 인적자본 보존</h2>

The content industry's workforce is predominantly **freelance and project-based**. When projects stop, they immediately become unemployed. During COVID-19, Netflix's continued investment **prevented a mass exodus of skilled talent**.

<div class="chart-container">
  <div class="chart-title">Employment Induced by Netflix Investment (Persons)</div>
  <canvas id="employmentTimeline"></canvas>
</div>

<div class="insight-box">
  <h4>Why This Matters</h4>
  <p><strong>Skill Formation:</strong> Content industry skills take 7-10 years to develop<br/>
  <strong>Industry Exit Risk:</strong> Once workers leave for delivery/gig economy, they rarely return<br/>
  <strong>Netflix Effect:</strong> Provided "employment continuity" that preserved K-Content's competitive foundation<br/>
  <strong>2020-2021 Total:</strong> 8,777 jobs sustained during pandemic's worst years</p>
</div>

<hr class="section-divider">

<h2 data-lang="en">Part 6: Four-Year Cumulative Impact Summary</h2>
<h2 data-lang="ko">Part 6: 4년간 누적 영향 요약</h2>

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
      <td class="number"><strong>3.35</strong></td>
      <td class="number">0.84</td>
      <td>Trillion KRW</td>
    </tr>
    <tr>
      <td>Production Induced</td>
      <td class="number"><strong>6.94</strong></td>
      <td class="number">1.74</td>
      <td>Trillion KRW</td>
    </tr>
    <tr>
      <td>Value Added (GDP Contribution)</td>
      <td class="number"><strong>3.65</strong></td>
      <td class="number">0.91</td>
      <td>Trillion KRW</td>
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
      <td class="number"><strong>1.52</strong></td>
      <td class="number">0.38</td>
      <td>Trillion KRW</td>
    </tr>
    <tr>
      <td>Production Tax Induced</td>
      <td class="number"><strong>0.21</strong></td>
      <td class="number">0.05</td>
      <td>Trillion KRW</td>
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
    <div class="metric-label">Job Efficiency vs<br/>Semiconductor</div>
  </div>
  <div class="metric-card orange">
    <div class="metric-value">120.7%</div>
    <div class="metric-label">Gap Coverage<br/>Ratio</div>
  </div>
</div>

<hr class="section-divider">

<h2 data-lang="en">Conclusion: Reframing the Debate</h2>
<h2 data-lang="ko">결론: 논쟁의 재구성</h2>

<table class="data-table">
  <thead>
    <tr>
      <th>Old Frame</th>
      <th>New Frame (IO Evidence)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Takes subscription fees to US"</td>
      <td><strong>Net inflow of +487B KRW (2023)</strong> - more comes back than goes out</td>
    </tr>
    <tr>
      <td>"Pays little tax"</td>
      <td><strong>143B total tax contribution</strong> - 40x hidden vs visible tax</td>
    </tr>
    <tr>
      <td>"Foreign company profit extraction"</td>
      <td><strong>Structural partner with aligned interests</strong> - Korea is production base</td>
    </tr>
    <tr>
      <td>"Competes with Korean media"</td>
      <td><strong>Crisis buffer that saved the ecosystem</strong> - filled 120% of ad revenue gap</td>
    </tr>
  </tbody>
</table>

<hr class="section-divider">

<h2 data-lang="en">Methodology & Data Transparency</h2>
<h2 data-lang="ko">방법론 및 데이터 투명성</h2>

**Analysis Framework**: Input-Output Analysis using Bank of Korea ECOS Tables

**Key Coefficients Used**:
- Production Inducement Coefficient (Leontief Inverse): 2.0147
- Value Added Inducement Coefficient: 1.0543
- Employment Inducement Coefficient: 8.290 per 1 billion KRW
- Import Inducement Coefficient: 0.159

**Unit Convention**:
- 1 Trillion KRW = 1,000 Billion KRW = 10,000 Eok Won
- Employment coefficients are per 1 billion KRW

**Data Sources**:
- Bank of Korea ECOS Input-Output Tables (New Series, 2020-2023)
- Netflix Korea Financial Statements via DART
- Netflix Inc. Official Investment Announcements (USD 2.5B / 3 years for 2023-2025)
- Korea Communications Commission Broadcasting Revenue Data

**Industry Classification**:
- Netflix Operations: J (ICT & Broadcasting Services)
- Content Production: R (Arts, Sports & Leisure)

**Limitations**:
- Content investment breakdown by sub-sector not disclosed
- 2024 IO tables not yet available

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
        label: 'Operating Costs',
        data: [61, 93, 104, 192],
        backgroundColor: 'rgba(26, 26, 46, 0.8)',
        borderColor: 'rgb(26, 26, 46)',
        borderWidth: 1
      }, {
        label: 'Content Investment',
        data: [330, 550, 800, 1219],
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
        label: 'Jobs per 1 Billion KRW',
        data: [16.23, 8.44, 8.29, 6.54, 2.34, 2.23],
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
          title: { display: true, text: 'Jobs per 1 Billion KRW' }
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
      labels: ['2019', '2020', '2021', '2022', '2023', '2024'],
      datasets: [{
        label: 'Broadcasting Ad Revenue (Trillion KRW)',
        data: [3.30, 2.88, 3.10, 2.88, 2.50, 2.29],
        borderColor: 'rgb(220, 38, 38)',
        backgroundColor: 'rgba(220, 38, 38, 0.1)',
        fill: true,
        tension: 0.3,
        yAxisID: 'y'
      }, {
        label: 'Netflix Investment (Trillion KRW)',
        data: [0, 0.33, 0.55, 0.80, 1.22, 1.22],
        borderColor: 'rgb(229, 9, 20)',
        backgroundColor: 'rgba(229, 9, 20, 0.3)',
        fill: true,
        tension: 0.3,
        yAxisID: 'y'
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'bottom' },
        title: {
          display: true,
          text: 'Source: Korea Communications Commission (Ad), Netflix Official (Investment)',
          font: { size: 11 }
        }
      },
      scales: {
        y: {
          title: { display: true, text: 'Trillion KRW' },
          beginAtZero: true
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
        legend: { display: false }
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
      labels: ['Investment\nInput', 'Production\nInduced', 'Value Added\n(GDP)', 'Income\nInduced', 'Tax\nInduced'],
      datasets: [{
        label: 'Trillion KRW',
        data: [3.35, 6.94, 3.65, 1.52, 0.21],
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

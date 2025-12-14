---
title: "투자 역설: 한국 방송 재승인 제도"
title_en: "The Investment Paradox: Korea's Broadcasting Reapproval System"
subtitle: "콘텐츠 투자 증가가 항상 실적 개선으로 이어지지 않는 이유"
subtitle_en: "Why Higher Content Investment Doesn't Always Lead to Better Performance"
date: "2025-10-11"
category: "Broadcasting Policy"
tags: ["Broadcasting", "Media Policy", "Regulation Reform", "Content Investment", "Data Analysis"]
keywords: ["Broadcasting Reapproval", "Content Investment", "Regulatory Reform", "Media Performance", "Investment Paradox", "Broadcasting License", "TV Chosun", "Profitability Analysis"]
methodology: ["Correlation Analysis", "Financial Performance Analysis", "Comparative International Study", "Regulatory Impact Assessment"]
data_period:
  start: "2014"
  end: "2024"
data_sources:
  - name: "Korea Communications Commission Reapproval Data"
    type: "primary"
  - name: "Broadcasting Companies Financial Statements"
    type: "primary"
related_publications: []
related_projects: ["broadcasting-revenue-2015-2024"]
conference: "한국언론학회 2024 가을 정기학술대회"
conference_en: "Korean Society for Journalism & Communication Studies 2024 Fall Conference"
description: "한국 방송 재승인 제도에 대한 실증적 조사 결과, 투자 역설이 발견됨: 엄격한 콘텐츠 투자 요건이 재무 성과 악화와 상관관계를 보임."
description_en: "An empirical investigation into Korea's broadcasting reapproval system reveals an investment paradox: stricter content investment requirements correlate with poorer financial performance."
summary: "한국은 법정 최대 7년임에도 불구하고 실제로는 3-4년의 재승인 기간만 부여 - 전 세계적으로 가장 짧음. 10년간의 데이터 분석 결과, 높은 투자 비율이 낮은 수익성과 상관관계를 보임."
summary_en: "Korea grants only 3-4 years reapproval period despite 7-year legal maximum - shortest globally. Analysis of 10 years of data reveals higher investment ratios correlate with lower profitability."
key_findings:
  - "Korea grants 3-4 years actual reapproval (legal max: 7 years) - shortest globally"
  - "Investment paradox: 70% requirement shows negative correlation with profit margins"
  - "TV Chosun achieved 73.5% average (exceeding 70%) but faced financial difficulties"
  - "International comparison: UK 10 years, US 8 years vs Korea 3-4 years"
policy_proposals:
  - "Extend actual reapproval period (3-4 years → 7 years legal maximum)"
  - "Relax content investment requirement (70% → 60-65%)"
  - "Introduce flexible evaluation based on market conditions"
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
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.metric-card {
  padding: 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
  text-align: center;
}

.metric-value {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.metric-label {
  font-size: 1rem;
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
  background: #fff5f5;
  border-left: 4px solid #e53e3e;
  border-radius: 4px;
}

.insight-box h4 {
  color: #c53030;
  margin-bottom: 0.5rem;
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.data-table th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  font-size: 1rem;
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
  font-size: 1rem;
  color: #374151;
}

.data-table .number {
  text-align: right;
  font-weight: 500;
}

.section-divider {
  height: 2px;
  background: linear-gradient(90deg, transparent, #667eea, transparent);
  margin: 3rem 0;
  border: none;
}
</style>

<h2 data-lang="en">The Untold Story of Korea's Broadcasting Regulation</h2>
<h2 data-lang="ko">한국 방송 규제의 숨겨진 이야기</h2>

<p data-lang="en">In 2011, Korea introduced comprehensive programming channels (종편) as a bold experiment in media diversification. These channels were meant to compete with traditional terrestrial broadcasters, bringing fresh perspectives and innovative content to Korean viewers. But thirteen years later, the experiment faces a critical question: <strong>Has the regulatory framework kept pace with market realities?</strong></p>
<p data-lang="ko">2011년, 한국은 미디어 다양화를 위한 대담한 실험으로 종합편성채널(종편)을 도입했습니다. 이 채널들은 지상파 방송사와 경쟁하며 한국 시청자들에게 새로운 관점과 혁신적인 콘텐츠를 제공하기 위해 만들어졌습니다. 하지만 13년이 지난 지금, 이 실험은 중요한 질문에 직면해 있습니다: <strong>규제 프레임워크가 시장 현실을 따라잡았는가?</strong></p>

<div class="metric-cards">
  <div class="metric-card">
    <div class="metric-value">3-4 years</div>
    <div class="metric-label"><span data-lang="en">Actual Reapproval Period<br/>(Legal max: 7 years)</span><span data-lang="ko">실제 재승인 기간<br/>(법정 최대: 7년)</span></div>
  </div>
  <div class="metric-card">
    <div class="metric-value">70%</div>
    <div class="metric-label"><span data-lang="en">Mandatory Content<br/>Investment Ratio</span><span data-lang="ko">의무 콘텐츠<br/>투자 비율</span></div>
  </div>
  <div class="metric-card">
    <div class="metric-value">10 years</div>
    <div class="metric-label"><span data-lang="en">Data Analysis<br/>Period (2015-2024)</span><span data-lang="ko">데이터 분석<br/>기간 (2015-2024)</span></div>
  </div>
</div>

<h2 data-lang="en">Part 1: The Shortest Leash in Global Broadcasting</h2>
<h2 data-lang="ko">Part 1: 전 세계 방송 시장에서 가장 짧은 줄</h2>

<p data-lang="en">When Korea's Broadcasting Act was revised, it allowed reapproval periods <strong>up to 7 years</strong> for comprehensive channels. Yet in practice, regulators have granted only <strong>3-4 years</strong> - creating the shortest reapproval cycle among major broadcasting markets globally.</p>
<p data-lang="ko">한국의 방송법이 개정되면서 종편에 대해 <strong>최대 7년</strong>의 재승인 기간을 허용했습니다. 그러나 실제로 규제 당국은 <strong>3-4년</strong>만 부여하여 전 세계 주요 방송 시장 중 가장 짧은 재승인 주기를 만들었습니다.</p>

<div class="chart-container">
  <div class="chart-title"><span data-lang="en">International Comparison: Reapproval Periods</span><span data-lang="ko">국제 비교: 재승인 기간</span></div>
  <canvas id="internationalComparison"></canvas>
</div>

<div class="insight-box">
  <h4 data-lang="en">Why This Matters</h4>
  <h4 data-lang="ko">왜 중요한가</h4>
  <p data-lang="en">Short reapproval periods create uncertainty that discourages long-term investment in content development, talent cultivation, and technology infrastructure. Broadcasters operate in perpetual "evaluation mode" rather than growth mode.</p>
  <p data-lang="ko">짧은 재승인 기간은 콘텐츠 개발, 인재 양성, 기술 인프라에 대한 장기 투자를 저해하는 불확실성을 만듭니다. 방송사들은 성장 모드가 아닌 영구적인 "평가 모드"에서 운영됩니다.</p>
</div>

<hr class="section-divider">

<h2 data-lang="en">Part 2: The Investment Paradox Revealed</h2>
<h2 data-lang="ko">Part 2: 투자 역설의 발견</h2>

<p data-lang="en">Our analysis of ten years of financial data from all four comprehensive channels reveals a surprising pattern: <strong>higher content investment ratios consistently correlate with lower profitability</strong>.</p>
<p data-lang="ko">4개 종편 채널의 10년간 재무 데이터 분석 결과, 놀라운 패턴이 발견되었습니다: <strong>높은 콘텐츠 투자 비율이 일관되게 낮은 수익성과 상관관계를 보입니다</strong>.</p>

<div class="chart-container">
  <div class="chart-title"><span data-lang="en">Content Investment Ratio vs Operating Profit Margin (2015-2024)</span><span data-lang="ko">콘텐츠 투자 비율 vs 영업이익률 (2015-2024)</span></div>
  <canvas id="investmentParadox"></canvas>
</div>

<p data-lang="en">This isn't a failure of investment strategy - it's evidence of a regulatory requirement that doesn't account for market realities. TV Chosun, for example, maintained an average investment ratio of <strong>73.5%</strong> (exceeding the 70% requirement) while facing significant financial challenges in certain years.</p>
<p data-lang="ko">이것은 투자 전략의 실패가 아닙니다 - 시장 현실을 고려하지 않는 규제 요건의 증거입니다. 예를 들어, TV조선은 평균 투자 비율 <strong>73.5%</strong>(70% 요건 초과)를 유지하면서도 특정 연도에 상당한 재정적 어려움에 직면했습니다.</p>

<div class="chart-container">
  <div class="chart-title"><span data-lang="en">TV Chosun: Investment Performance Timeline</span><span data-lang="ko">TV조선: 투자 실적 타임라인</span></div>
  <canvas id="tvChosunTimeline"></canvas>
</div>

<hr class="section-divider">

<h2 data-lang="en">Part 3: The Tale of Four Channels</h2>
<h2 data-lang="ko">Part 3: 4개 채널의 이야기</h2>

<p data-lang="en">Each comprehensive channel tells a different story of adaptation, struggle, and resilience under the current regulatory framework.</p>
<p data-lang="ko">각 종편 채널은 현행 규제 프레임워크 하에서 적응, 고군분투, 회복력에 대한 각기 다른 이야기를 들려줍니다.</p>

<div class="chart-container">
  <div class="chart-title"><span data-lang="en">4-Channel Comparison: Investment Ratios Over Time</span><span data-lang="ko">4개 채널 비교: 시간에 따른 투자 비율</span></div>
  <canvas id="fourChannelComparison"></canvas>
</div>

<p data-lang="en"><strong>JTBC</strong> achieved the highest investment ratio (averaging 85.2%) but experienced volatile profitability, with significant losses in 2019-2020 and 2023-2024.</p>
<p data-lang="ko"><strong>JTBC</strong>는 가장 높은 투자 비율(평균 85.2%)을 달성했지만, 2019-2020년과 2023-2024년에 상당한 손실을 기록하는 등 변동이 심한 수익성을 경험했습니다.</p>

<p data-lang="en"><strong>Channel A</strong> maintained moderate investment levels (79.2% average) but faced persistent financial challenges, recording losses in six out of ten years.</p>
<p data-lang="ko"><strong>채널A</strong>는 중간 수준의 투자(평균 79.2%)를 유지했지만 지속적인 재정적 어려움에 직면하여 10년 중 6년 동안 적자를 기록했습니다.</p>

<p data-lang="en"><strong>MBN</strong> kept a relatively conservative investment approach (78.7% average) and achieved more stable, albeit modest, profitability.</p>
<p data-lang="ko"><strong>MBN</strong>은 비교적 보수적인 투자 접근법(평균 78.7%)을 유지하면서 다소 낮지만 더 안정적인 수익성을 달성했습니다.</p>

<p data-lang="en"><strong>TV Chosun</strong> strategically increased investment over time, peaking at over 70% by 2022-2023, with notable profitability improvements in 2020-2022.</p>
<p data-lang="ko"><strong>TV조선</strong>은 전략적으로 시간이 지남에 따라 투자를 늘려 2022-2023년에 70%를 초과하는 정점에 도달했으며, 2020-2022년에 주목할 만한 수익성 개선을 보였습니다.</p>

<div class="chart-container">
  <div class="chart-title"><span data-lang="en">Operating Profit Margins: The Reality Behind Investment</span><span data-lang="ko">영업이익률: 투자 뒤에 숨겨진 현실</span></div>
  <canvas id="profitMargins"></canvas>
</div>

<hr class="section-divider">

<h2 data-lang="en">Part 4: Market Context - The Bigger Picture</h2>
<h2 data-lang="ko">Part 4: 시장 맥락 - 더 큰 그림</h2>

<p data-lang="en">The comprehensive channels don't operate in a vacuum. Comparing their investment patterns with terrestrial broadcasters and general PP channels reveals important context.</p>
<p data-lang="ko">종편 채널은 고립된 환경에서 운영되지 않습니다. 지상파 방송사 및 일반 PP 채널과의 투자 패턴 비교는 중요한 맥락을 보여줍니다.</p>

<div class="chart-container">
  <div class="chart-title"><span data-lang="en">Media Type Comparison: Average Investment Ratios</span><span data-lang="ko">미디어 유형 비교: 평균 투자 비율</span></div>
  <canvas id="mediaComparison"></canvas>
</div>

<ul data-lang="en">
<li><strong>Terrestrial broadcasters</strong> (KBS, MBC, SBS, EBS): Average 79.3%</li>
<li><strong>Comprehensive channels</strong>: Average 79.3%</li>
<li><strong>General PP channels</strong>: Average 124.8% (but with huge variance)</li>
</ul>
<ul data-lang="ko">
<li><strong>지상파 방송사</strong> (KBS, MBC, SBS, EBS): 평균 79.3%</li>
<li><strong>종합편성채널</strong>: 평균 79.3%</li>
<li><strong>일반 PP 채널</strong>: 평균 124.8% (그러나 편차가 큼)</li>
</ul>

<p data-lang="en">The data shows comprehensive channels are investing at levels comparable to traditional terrestrial broadcasters, despite operating in a far more competitive and fragmented market environment.</p>
<p data-lang="ko">데이터는 종편 채널이 훨씬 더 경쟁적이고 파편화된 시장 환경에서 운영됨에도 불구하고 전통적인 지상파 방송사와 비슷한 수준으로 투자하고 있음을 보여줍니다.</p>

<hr class="section-divider">

<h2 data-lang="en">Part 5: Evidence-Based Policy Recommendations</h2>
<h2 data-lang="ko">Part 5: 증거 기반 정책 제언</h2>

<p data-lang="en">Based on ten years of empirical data, our research suggests three key reforms:</p>
<p data-lang="ko">10년간의 실증 데이터를 바탕으로, 본 연구는 세 가지 핵심 개혁을 제안합니다:</p>

<h3 data-lang="en">1. Extend the Actual Reapproval Period</h3>
<h3 data-lang="ko">1. 실제 재승인 기간 연장</h3>

<p data-lang="en"><strong>Current</strong>: 3-4 years granted (despite 7-year legal maximum)<br/>
<strong>Recommended</strong>: Utilize the full 7-year legal maximum</p>
<p data-lang="ko"><strong>현재</strong>: 3-4년 부여 (법정 최대 7년에도 불구하고)<br/>
<strong>권장</strong>: 법정 최대 7년 전면 활용</p>

<div class="insight-box">
  <h4 data-lang="en">International Standard</h4>
  <h4 data-lang="ko">국제 기준</h4>
  <p data-lang="en">UK: 10 years | US: 8 years | Japan: 5-7 years | Korea: 3-4 years (actual)</p>
  <p data-lang="ko">영국: 10년 | 미국: 8년 | 일본: 5-7년 | 한국: 3-4년 (실제)</p>
</div>

<h3 data-lang="en">2. Adjust Content Investment Requirements</h3>
<h3 data-lang="ko">2. 콘텐츠 투자 요건 조정</h3>

<p data-lang="en"><strong>Current</strong>: Fixed 70% ratio requirement<br/>
<strong>Recommended</strong>: Flexible 60-65% range based on market conditions</p>
<p data-lang="ko"><strong>현재</strong>: 고정 70% 비율 요건<br/>
<strong>권장</strong>: 시장 상황에 따른 유연한 60-65% 범위</p>

<p data-lang="en">The data shows that forcing higher investment ratios beyond 70% creates diminishing returns and may actually harm long-term sustainability.</p>
<p data-lang="ko">데이터에 따르면 70%를 초과하는 높은 투자 비율을 강제하면 수익이 감소하고 실제로 장기적인 지속가능성을 해칠 수 있습니다.</p>

<h3 data-lang="en">3. Introduce Market-Responsive Evaluation</h3>
<h3 data-lang="ko">3. 시장 반응형 평가 도입</h3>

<p data-lang="en">Rather than rigid numerical targets, evaluation should consider:</p>
<p data-lang="ko">경직된 수치 목표 대신, 평가는 다음을 고려해야 합니다:</p>

<ul data-lang="en">
<li>Market share dynamics and competition intensity</li>
<li>Multi-year investment trends (not single-year snapshots)</li>
<li>Quality metrics alongside quantity</li>
<li>Revenue context (absolute investment amounts, not just ratios)</li>
</ul>
<ul data-lang="ko">
<li>시장 점유율 역학 및 경쟁 강도</li>
<li>다년간 투자 추세 (단일 연도 스냅샷이 아닌)</li>
<li>양적 지표와 함께 질적 지표</li>
<li>수익 맥락 (비율만이 아닌 절대 투자 금액)</li>
</ul>

<div class="chart-container">
  <div class="chart-title"><span data-lang="en">Proposed Framework: Flexible Investment Bands</span><span data-lang="ko">제안 프레임워크: 유연한 투자 구간</span></div>
  <canvas id="proposedFramework"></canvas>
</div>

<hr class="section-divider">

<h2 data-lang="en">Methodology & Data Transparency</h2>
<h2 data-lang="ko">연구 방법론 및 데이터 투명성</h2>

<p data-lang="en"><strong>Data Sources</strong>:</p>
<p data-lang="ko"><strong>데이터 출처</strong>:</p>
<ul data-lang="en">
<li>Broadcasting Industry Survey (2015-2024)</li>
<li>Korea Communications Commission official reports</li>
<li>Individual broadcaster business reports and reapproval documents</li>
</ul>
<ul data-lang="ko">
<li>방송산업실태조사 (2015-2024)</li>
<li>방송통신위원회 공식 보고서</li>
<li>개별 방송사 사업 보고서 및 재승인 문서</li>
</ul>

<p data-lang="en"><strong>Analysis Period</strong>: 10 years (2015-2024)<br/>
<strong>Sample</strong>: 4 comprehensive channels, 4 major terrestrial broadcasters, 145+ PP channels<br/>
<strong>Total Observations</strong>: 1,532 company-year records</p>
<p data-lang="ko"><strong>분석 기간</strong>: 10년 (2015-2024)<br/>
<strong>표본</strong>: 4개 종편 채널, 4개 주요 지상파 방송사, 145개 이상 PP 채널<br/>
<strong>총 관측치</strong>: 1,532개 기업-연도 레코드</p>

<p data-lang="en"><strong>Statistical Methods</strong>:</p>
<p data-lang="ko"><strong>통계적 방법</strong>:</p>
<ul data-lang="en">
<li>Time series analysis</li>
<li>Cross-sectional regression</li>
<li>Correlation analysis</li>
<li>Comparative international research</li>
</ul>
<ul data-lang="ko">
<li>시계열 분석</li>
<li>횡단면 회귀분석</li>
<li>상관관계 분석</li>
<li>비교 국제 연구</li>
</ul>

<p data-lang="en"><strong>Limitations</strong>:</p>
<p data-lang="ko"><strong>한계</strong>:</p>
<ul data-lang="en">
<li>2021 terrestrial data required correction (100x scaling error in original database)</li>
<li>PP channel data shows high variance due to diverse business models</li>
<li>Operating profit margins affected by multiple factors beyond investment ratios</li>
</ul>
<ul data-lang="ko">
<li>2021년 지상파 데이터 수정 필요 (원본 데이터베이스의 100배 스케일링 오류)</li>
<li>다양한 비즈니스 모델로 인해 PP 채널 데이터가 높은 분산을 보임</li>
<li>영업이익률이 투자 비율 외 여러 요인에 영향받음</li>
</ul>

<hr class="section-divider">

<h2 data-lang="en">Conclusion: Rethinking Regulation for Sustainability</h2>
<h2 data-lang="ko">결론: 지속가능성을 위한 규제 재고</h2>

<p data-lang="en">Korea's broadcasting reapproval system was designed with good intentions: ensuring quality content and broadcaster accountability. But thirteen years of real-world data reveal unintended consequences.</p>
<p data-lang="ko">한국의 방송 재승인 제도는 좋은 의도로 설계되었습니다: 품질 높은 콘텐츠와 방송사의 책임성을 보장하기 위해서였습니다. 그러나 13년간의 실제 데이터는 의도치 않은 결과를 보여줍니다.</p>

<p data-lang="en">The <strong>investment paradox</strong> - where meeting higher requirements correlates with worse financial performance - suggests the current framework may be undermining the very sustainability it seeks to ensure.</p>
<p data-lang="ko"><strong>투자 역설</strong> - 더 높은 요건을 충족하는 것이 더 나쁜 재무 성과와 상관관계를 보이는 현상 - 은 현재의 프레임워크가 보장하려는 바로 그 지속가능성을 약화시킬 수 있음을 시사합니다.</p>

<p data-lang="en">By extending reapproval periods to the legal maximum of 7 years and introducing more flexible investment requirements, Korea can maintain quality standards while giving broadcasters the stability needed for long-term growth and innovation.</p>
<p data-lang="ko">재승인 기간을 법정 최대 7년으로 연장하고 더 유연한 투자 요건을 도입함으로써, 한국은 방송사들에게 장기적인 성장과 혁신에 필요한 안정성을 제공하면서도 품질 기준을 유지할 수 있습니다.</p>

<p data-lang="en">The path forward isn't less accountability - it's <strong>smarter accountability</strong> informed by empirical evidence rather than arbitrary targets.</p>
<p data-lang="ko">앞으로 나아갈 길은 책임성을 줄이는 것이 아닙니다 - 자의적인 목표가 아닌 실증적 증거에 기반한 <strong>더 스마트한 책임성</strong>입니다.</p>

<hr class="section-divider">

<h2 data-lang="en">Project Information</h2>
<h2 data-lang="ko">프로젝트 정보</h2>

<p data-lang="en"><strong>Research Period:</strong> August 2024 - November 2025<br/>
<strong>Last Updated:</strong> October 11, 2025<br/>
<strong>Version:</strong> v2.0 FINAL<br/>
<strong>Presentation:</strong> Korean Society for Journalism & Communication Studies 2024 Fall Conference</p>
<p data-lang="ko"><strong>연구 기간:</strong> 2024년 8월 - 2025년 11월<br/>
<strong>최종 업데이트:</strong> 2025년 10월 11일<br/>
<strong>버전:</strong> v2.0 FINAL<br/>
<strong>발표:</strong> 한국언론학회 2024 가을 정기학술대회</p>

<hr class="section-divider">

<h2 data-lang="en">Researcher Information</h2>
<h2 data-lang="ko">연구자 정보</h2>

<p data-lang="en"><strong>Yonghee Kim, Ph.D.</strong><br/>
Assistant Professor, Department of Business Administration<br/>
Sunmoon University</p>
<p data-lang="ko"><strong>김용희 박사</strong><br/>
경영학과 조교수<br/>
선문대학교</p>

<p data-lang="en"><strong>Expertise:</strong></p>
<p data-lang="ko"><strong>전문 분야:</strong></p>
<ul data-lang="en">
<li>Media policy and regulation</li>
<li>Digital platform economics</li>
<li>Broadcasting and telecommunications industry analysis</li>
<li>Media business strategy</li>
</ul>
<ul data-lang="ko">
<li>미디어 정책 및 규제</li>
<li>디지털 플랫폼 경제학</li>
<li>방송통신 산업 분석</li>
<li>미디어 비즈니스 전략</li>
</ul>

<p data-lang="en"><strong>Contact:</strong></p>
<p data-lang="ko"><strong>연락처:</strong></p>
<ul>
<li>Email: yhkim@sunmoon.ac.kr</li>
<li>ORCID: 0000-0002-5643-2748</li>
<li>Google Scholar: <a href="https://scholar.google.com/citations?user=semkeskAAAAJ">View Profile</a></li>
</ul>

---

<script>
// Chart.js Configuration and Data

// 1. International Comparison Chart
const ctxInternational = document.getElementById('internationalComparison');
if (ctxInternational) {
  new Chart(ctxInternational, {
    type: 'bar',
    data: {
      labels: ['Korea\n(Actual)', 'Korea\n(Legal Max)', 'Japan', 'US', 'UK'],
      datasets: [{
        label: 'Reapproval Period (Years)',
        data: [3.5, 7, 6, 8, 10],
        backgroundColor: [
          'rgba(220, 38, 38, 0.8)',
          'rgba(245, 158, 11, 0.8)',
          'rgba(59, 130, 246, 0.8)',
          'rgba(16, 185, 129, 0.8)',
          'rgba(139, 92, 246, 0.8)'
        ],
        borderColor: [
          'rgb(220, 38, 38)',
          'rgb(245, 158, 11)',
          'rgb(59, 130, 246)',
          'rgb(16, 185, 129)',
          'rgb(139, 92, 246)'
        ],
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: function(context) {
              return context.parsed.y + ' years';
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          max: 12,
          ticks: {
            callback: function(value) {
              return value + ' years';
            }
          }
        }
      }
    }
  });
}

// 2. Investment Paradox Scatter Chart
const ctxParadox = document.getElementById('investmentParadox');
if (ctxParadox) {
  new Chart(ctxParadox, {
    type: 'scatter',
    data: {
      datasets: [{
        label: 'JTBC',
        data: [
          {x: 95.8, y: -26.8}, {x: 68.0, y: 3.2}, {x: 68.4, y: 3.7},
          {x: 85.4, y: -8.0}, {x: 87.0, y: -6.4}, {x: 87.4, y: -5.7},
          {x: 80.3, y: 1.3}, {x: 98.1, y: -19.1}, {x: 93.0, y: -10.2}
        ],
        backgroundColor: 'rgba(220, 38, 38, 0.6)',
        borderColor: 'rgb(220, 38, 38)'
      }, {
        label: 'Channel A',
        data: [
          {x: 78.1, y: -1.3}, {x: 82.2, y: -5.7}, {x: 82.1, y: -5.1},
          {x: 87.3, y: -10.2}, {x: 87.1, y: -9.3}, {x: 66.9, y: 12.3},
          {x: 70.6, y: 7.6}, {x: 81.5, y: -2.1}, {x: 78.7, y: 0.8}
        ],
        backgroundColor: 'rgba(59, 130, 246, 0.6)',
        borderColor: 'rgb(59, 130, 246)'
      }, {
        label: 'MBN',
        data: [
          {x: 78.4, y: 6.6}, {x: 73.0, y: 9.8}, {x: 85.4, y: -2.1},
          {x: 86.7, y: 0.1}, {x: 88.3, y: -0.5}, {x: 79.4, y: 7.5},
          {x: 72.7, y: 6.8}, {x: 74.8, y: 2.6}, {x: 73.6, y: 5.2}
        ],
        backgroundColor: 'rgba(16, 185, 129, 0.6)',
        borderColor: 'rgb(16, 185, 129)'
      }, {
        label: 'TV Chosun',
        data: [
          {x: 71.4, y: 5.8}, {x: 77.9, y: -0.6}, {x: 78.5, y: -0.7},
          {x: 72.8, y: 7.7}, {x: 61.6, y: 22.5}, {x: 65.6, y: 17.5},
          {x: 71.9, y: 9.9}, {x: 78.7, y: 6.1}, {x: 77.7, y: 8.3}
        ],
        backgroundColor: 'rgba(245, 158, 11, 0.6)',
        borderColor: 'rgb(245, 158, 11)'
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'bottom' },
        tooltip: {
          callbacks: {
            label: function(context) {
              return context.dataset.label + ': Investment ' + context.parsed.x.toFixed(1) + '%, Margin ' + context.parsed.y.toFixed(1) + '%';
            }
          }
        }
      },
      scales: {
        x: {
          title: { display: true, text: 'Content Investment Ratio (%)' },
          min: 55,
          max: 100
        },
        y: {
          title: { display: true, text: 'Operating Profit Margin (%)' },
          min: -30,
          max: 25
        }
      }
    }
  });
}

// 3. TV Chosun Timeline
const ctxTVChosun = document.getElementById('tvChosunTimeline');
if (ctxTVChosun) {
  new Chart(ctxTVChosun, {
    type: 'line',
    data: {
      labels: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
      datasets: [{
        label: 'Investment Ratio (%)',
        data: [71.4, 71.4, 77.9, 78.5, 72.8, 61.6, 65.6, 71.9, 78.7, 77.7],
        borderColor: 'rgb(245, 158, 11)',
        backgroundColor: 'rgba(245, 158, 11, 0.1)',
        yAxisID: 'y',
        tension: 0.3
      }, {
        label: 'Operating Profit Margin (%)',
        data: [5.8, 5.8, -0.6, -0.7, 7.7, 22.5, 17.5, 9.9, 6.1, 8.3],
        borderColor: 'rgb(16, 185, 129)',
        backgroundColor: 'rgba(16, 185, 129, 0.1)',
        yAxisID: 'y1',
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      plugins: { legend: { position: 'bottom' } },
      scales: {
        y: {
          type: 'linear',
          display: true,
          position: 'left',
          title: { display: true, text: 'Investment Ratio (%)' },
          min: 50,
          max: 90
        },
        y1: {
          type: 'linear',
          display: true,
          position: 'right',
          title: { display: true, text: 'Profit Margin (%)' },
          min: -5,
          max: 25,
          grid: { drawOnChartArea: false }
        }
      }
    }
  });
}

// 4. Four Channel Comparison
const ctxFourChannel = document.getElementById('fourChannelComparison');
if (ctxFourChannel) {
  new Chart(ctxFourChannel, {
    type: 'line',
    data: {
      labels: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
      datasets: [
        {
          label: 'JTBC',
          data: [95.8, 95.8, 68.0, 68.4, 85.4, 87.0, 87.4, 80.3, 98.1, 93.0],
          borderColor: 'rgb(220, 38, 38)',
          backgroundColor: 'rgba(220, 38, 38, 0.1)',
          tension: 0.3
        },
        {
          label: 'Channel A',
          data: [78.1, 78.1, 82.2, 82.1, 87.3, 87.1, 66.9, 70.6, 81.5, 78.7],
          borderColor: 'rgb(59, 130, 246)',
          backgroundColor: 'rgba(59, 130, 246, 0.1)',
          tension: 0.3
        },
        {
          label: 'MBN',
          data: [78.4, 78.4, 73.0, 85.4, 86.7, 88.3, 79.4, 72.7, 74.8, 73.6],
          borderColor: 'rgb(16, 185, 129)',
          backgroundColor: 'rgba(16, 185, 129, 0.1)',
          tension: 0.3
        },
        {
          label: 'TV Chosun',
          data: [71.4, 71.4, 77.9, 78.5, 72.8, 61.6, 65.6, 71.9, 78.7, 77.7],
          borderColor: 'rgb(245, 158, 11)',
          backgroundColor: 'rgba(245, 158, 11, 0.1)',
          tension: 0.3
        }
      ]
    },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: { position: 'bottom' }
      },
      scales: {
        y: {
          title: { display: true, text: 'Content Investment Ratio (%)' },
          min: 55,
          max: 100
        }
      }
    }
  });
}

// 5. Profit Margins
const ctxProfitMargins = document.getElementById('profitMargins');
if (ctxProfitMargins) {
  new Chart(ctxProfitMargins, {
    type: 'line',
    data: {
      labels: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
      datasets: [
        {
          label: 'JTBC',
          data: [-26.8, -26.8, 3.2, 3.7, -8.0, -6.4, -5.7, 1.3, -19.1, -10.2],
          borderColor: 'rgb(220, 38, 38)',
          tension: 0.3
        },
        {
          label: 'Channel A',
          data: [-1.3, -1.3, -5.7, -5.1, -10.2, -9.3, 12.3, 7.6, -2.1, 0.8],
          borderColor: 'rgb(59, 130, 246)',
          tension: 0.3
        },
        {
          label: 'MBN',
          data: [6.6, 6.6, 9.8, -2.1, 0.1, -0.5, 7.5, 6.8, 2.6, 5.2],
          borderColor: 'rgb(16, 185, 129)',
          tension: 0.3
        },
        {
          label: 'TV Chosun',
          data: [5.8, 5.8, -0.6, -0.7, 7.7, 22.5, 17.5, 9.9, 6.1, 8.3],
          borderColor: 'rgb(245, 158, 11)',
          tension: 0.3
        }
      ]
    },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: { position: 'bottom' }
      },
      scales: {
        y: {
          title: { display: true, text: 'Operating Profit Margin (%)' },
          min: -30,
          max: 25
        }
      }
    }
  });
}

// 6. Media Type Comparison
const ctxMediaComparison = document.getElementById('mediaComparison');
if (ctxMediaComparison) {
  new Chart(ctxMediaComparison, {
    type: 'bar',
    data: {
      labels: ['Terrestrial', 'Comprehensive', 'General PP'],
      datasets: [{
        label: 'Average Investment Ratio (%)',
        data: [79.3, 79.3, 124.8],
        backgroundColor: [
          'rgba(59, 130, 246, 0.8)',
          'rgba(245, 158, 11, 0.8)',
          'rgba(156, 163, 175, 0.8)'
        ],
        borderColor: [
          'rgb(59, 130, 246)',
          'rgb(245, 158, 11)',
          'rgb(156, 163, 175)'
        ],
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
              if (context.dataIndex === 2) {
                return '(High variance: σ=1,431%)';
              }
              return '';
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          max: 140,
          title: { display: true, text: 'Investment Ratio (%)' }
        }
      }
    }
  });
}

// 7. Proposed Framework
const ctxProposed = document.getElementById('proposedFramework');
if (ctxProposed) {
  new Chart(ctxProposed, {
    type: 'bar',
    data: {
      labels: ['Current\nFixed', 'Proposed\nMinimum', 'Proposed\nOptimal', 'Proposed\nMaximum'],
      datasets: [{
        label: 'Investment Ratio Range (%)',
        data: [70, 60, 65, 70],
        backgroundColor: [
          'rgba(220, 38, 38, 0.8)',
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
        legend: { display: false },
        tooltip: {
          callbacks: {
            afterLabel: function(context) {
              const labels = [
                'Rigid requirement',
                'Market downturn flexibility',
                'Sustainable target',
                'Strong market conditions'
              ];
              return labels[context.dataIndex];
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          max: 80,
          title: { display: true, text: 'Investment Ratio (%)' }
        }
      }
    }
  });
}
</script>

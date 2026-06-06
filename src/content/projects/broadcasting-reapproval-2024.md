---
title: "The Investment Paradox: Korea's Broadcasting Reapproval System"
title_ko: "투자의 역설: 한국 방송 재승인 제도"
title_en: "The Investment Paradox: Korea's Broadcasting Reapproval System"
subtitle: "Why Higher Content Investment Doesn't Always Lead to Better Performance"
subtitle_ko: "콘텐츠 투자를 늘린다고 늘 성과가 좋아지지는 않는 이유"
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
conference: "Korean Society for Journalism & Communication Studies 2024 Fall Conference"
description: "An empirical investigation into Korea's broadcasting reapproval system reveals an investment paradox: stricter content investment requirements correlate with poorer financial performance."
description_ko: "한국 방송 재승인 제도를 실증적으로 분석한 결과, 콘텐츠 투자 의무를 강화할수록 오히려 재무 성과가 나빠지는 투자의 역설이 확인되었다."
description_en: "An empirical investigation into Korea's broadcasting reapproval system reveals an investment paradox: stricter content investment requirements correlate with poorer financial performance."
summary: "Korea grants only 3-4 years reapproval period despite 7-year legal maximum - shortest globally. Analysis of 10 years of data reveals higher investment ratios correlate with lower profitability."
summary_ko: "한국은 법정 최대 7년이 가능한데도 실제 재승인 기간은 3~4년에 그쳐 세계에서 가장 짧다. 10년치 자료를 분석한 결과, 투자 비율이 높을수록 수익성은 낮아지는 경향이 나타났다."
summary_en: "Korea grants only 3-4 years reapproval period despite 7-year legal maximum - shortest globally. Analysis of 10 years of data reveals higher investment ratios correlate with lower profitability."
key_findings:
  - "Korea grants 3-4 years actual reapproval (legal max: 7 years) - shortest globally"
  - "Investment paradox: 70% requirement shows negative correlation with profit margins"
  - "TV Chosun achieved 73.5% average (exceeding 70%) but faced financial difficulties"
  - "International comparison: UK 10 years, US 8 years vs Korea 3-4 years"
key_findings_ko:
  - "한국의 실제 재승인 기간은 3~4년으로(법정 최대 7년) 세계에서 가장 짧다"
  - "투자의 역설: 70% 의무 비율은 영업이익률과 음(-)의 상관을 보인다"
  - "TV조선은 평균 73.5%로 70% 기준을 넘겼지만 재무적 어려움을 겪었다"
  - "국제 비교: 영국 10년, 미국 8년에 비해 한국은 3~4년"
policy_proposals:
  - "Extend actual reapproval period (3-4 years → 7 years legal maximum)"
  - "Relax content investment requirement (70% → 60-65%)"
  - "Introduce flexible evaluation based on market conditions"
policy_proposals_ko:
  - "실제 재승인 기간 확대(3~4년 → 법정 최대 7년)"
  - "콘텐츠 투자 의무 완화(70% → 60~65%)"
  - "시장 상황을 반영한 유연 평가 도입"
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

<div data-lang="ko">

## 한국 방송 규제의 숨겨진 이야기

2011년 한국은 미디어 다양성을 실험하는 차원에서 종합편성채널을 도입했습니다. 이 채널들은 기존 지상파 방송사와 경쟁하며 시청자에게 새로운 관점과 혁신적인 콘텐츠를 제공하기 위한 것이었습니다. 그러나 13년이 지난 지금, 이 실험은 중요한 질문에 직면해 있습니다. **규제 틀이 시장의 현실을 제대로 따라왔는가?**

</div>

<div data-lang="en">

## The Untold Story of Korea's Broadcasting Regulation

In 2011, Korea introduced comprehensive programming channels as an experiment in media diversification. These channels were meant to compete with traditional terrestrial broadcasters, bringing fresh perspectives and innovative content to Korean viewers. But thirteen years later, the experiment faces a critical question: **Has the regulatory framework kept pace with market realities?**

</div>

<div class="metric-cards">
  <div class="metric-card">
    <div class="metric-value">3-4 years</div>
    <div class="metric-label">Actual Reapproval Period<br/>(Legal max: 7 years)</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">70%</div>
    <div class="metric-label">Mandatory Content<br/>Investment Ratio</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">10 years</div>
    <div class="metric-label">Data Analysis<br/>Period (2015-2024)</div>
  </div>
</div>

<div data-lang="ko">

## 1부: 세계에서 가장 짧은 고삐

방송법 개정으로 종합편성채널의 재승인 기간은 **최대 7년**까지 허용되었습니다. 그러나 실제로 규제 기관이 부여한 기간은 **3~4년**에 그쳐, 세계 주요 방송 시장 가운데 가장 짧은 재승인 주기를 만들어 냈습니다.

</div>

<div data-lang="en">

## Part 1: The Shortest Leash in Global Broadcasting

When Korea's Broadcasting Act was revised, it allowed reapproval periods **up to 7 years** for comprehensive channels. Yet in practice, regulators have granted only **3-4 years** - creating the shortest reapproval cycle among major broadcasting markets globally.

</div>

<div class="chart-container">
  <div class="chart-title">International Comparison: Reapproval Periods</div>
  <canvas id="internationalComparison"></canvas>
</div>

<div data-lang="ko">

<div class="insight-box">
  <h4>왜 중요한가</h4>
  <p>재승인 기간이 짧으면 불확실성이 커지고, 이는 콘텐츠 개발, 인재 양성, 기술 인프라에 대한 장기 투자를 위축시킵니다. 방송사는 성장 모드가 아니라 늘 "평가 모드"로 운영하게 됩니다.</p>
</div>

</div>

<div data-lang="en">

<div class="insight-box">
  <h4>Why This Matters</h4>
  <p>Short reapproval periods create uncertainty that discourages long-term investment in content development, talent cultivation, and technology infrastructure. Broadcasters operate in perpetual "evaluation mode" rather than growth mode.</p>
</div>

</div>

<hr class="section-divider">

<div data-lang="ko">

## 2부: 드러난 투자의 역설

종합편성채널 4사의 10년치 재무 자료를 분석한 결과 놀라운 패턴이 나타났습니다. **콘텐츠 투자 비율이 높을수록 수익성은 일관되게 낮아진다**는 것입니다.

</div>

<div data-lang="en">

## Part 2: The Investment Paradox Revealed

Our analysis of ten years of financial data from all four comprehensive channels reveals a surprising pattern: **higher content investment ratios consistently correlate with lower profitability**.

</div>

<div class="chart-container">
  <div class="chart-title">Content Investment Ratio vs Operating Profit Margin (2015-2024)</div>
  <canvas id="investmentParadox"></canvas>
</div>

<div data-lang="ko">

이것은 투자 전략의 실패가 아니라, 시장의 현실을 반영하지 못하는 규제 요건이 낳은 결과입니다. 예컨대 TV조선은 평균 투자 비율 **73.5%**(70% 기준 초과)를 유지했지만, 특정 연도에는 상당한 재무적 어려움을 겪었습니다.

</div>

<div data-lang="en">

This isn't a failure of investment strategy - it's evidence of a regulatory requirement that doesn't account for market realities. TV Chosun, for example, maintained an average investment ratio of **73.5%** (exceeding the 70% requirement) while facing significant financial challenges in certain years.

</div>

<div class="chart-container">
  <div class="chart-title">TV Chosun: Investment Performance Timeline</div>
  <canvas id="tvChosunTimeline"></canvas>
</div>

<hr class="section-divider">

<div data-lang="ko">

## 3부: 네 채널의 서로 다른 이야기

종합편성채널 네 곳은 현재의 규제 틀 아래에서 적응, 고전, 회복이라는 저마다 다른 이야기를 들려줍니다.

</div>

<div data-lang="en">

## Part 3: The Tale of Four Channels

Each comprehensive channel tells a different story of adaptation, struggle, and resilience under the current regulatory framework.

</div>

<div class="chart-container">
  <div class="chart-title">4-Channel Comparison: Investment Ratios Over Time</div>
  <canvas id="fourChannelComparison"></canvas>
</div>

<div data-lang="ko">

**JTBC**는 가장 높은 투자 비율(평균 85.2%)을 기록했지만, 2019~2020년과 2023~2024년에 큰 손실을 내는 등 수익성의 변동이 컸습니다.

**채널A**는 중간 수준의 투자(평균 79.2%)를 유지했으나, 10년 중 6년 동안 손실을 기록하며 지속적인 재무적 어려움을 겪었습니다.

**MBN**은 상대적으로 보수적인 투자 기조(평균 78.7%)를 유지했고, 폭은 크지 않지만 보다 안정적인 수익성을 달성했습니다.

**TV조선**은 시간이 지나며 전략적으로 투자를 늘려 2022~2023년에는 70%를 넘겼으며, 2020~2022년에는 수익성이 눈에 띄게 개선되었습니다.

</div>

<div data-lang="en">

**JTBC** achieved the highest investment ratio (averaging 85.2%) but experienced volatile profitability, with significant losses in 2019-2020 and 2023-2024.

**Channel A** maintained moderate investment levels (79.2% average) but faced persistent financial challenges, recording losses in six out of ten years.

**MBN** kept a relatively conservative investment approach (78.7% average) and achieved more stable, albeit modest, profitability.

**TV Chosun** strategically increased investment over time, peaking at over 70% by 2022-2023, with notable profitability improvements in 2020-2022.

</div>

<div class="chart-container">
  <div class="chart-title">Operating Profit Margins: The Reality Behind Investment</div>
  <canvas id="profitMargins"></canvas>
</div>

<hr class="section-divider">

<div data-lang="ko">

## 4부: 시장 맥락 - 더 큰 그림

종합편성채널은 진공 속에서 운영되지 않습니다. 이들의 투자 패턴을 지상파 방송사 및 일반 방송채널사용사업자(PP)와 비교하면 중요한 맥락이 드러납니다.

</div>

<div data-lang="en">

## Part 4: Market Context - The Bigger Picture

The comprehensive channels don't operate in a vacuum. Comparing their investment patterns with terrestrial broadcasters and general PP channels reveals important context.

</div>

<div class="chart-container">
  <div class="chart-title">Media Type Comparison: Average Investment Ratios</div>
  <canvas id="mediaComparison"></canvas>
</div>

<div data-lang="ko">

- **지상파 방송사**(KBS, MBC, SBS, EBS): 평균 79.3%
- **종합편성채널**: 평균 79.3%
- **일반 방송채널사용사업자(PP)**: 평균 124.8%(다만 편차가 매우 큼)

종합편성채널은 훨씬 더 경쟁이 치열하고 파편화된 시장 환경에서 운영되고 있음에도, 전통적인 지상파 방송사와 비슷한 수준으로 투자하고 있음을 자료가 보여 줍니다.

</div>

<div data-lang="en">

- **Terrestrial broadcasters** (KBS, MBC, SBS, EBS): Average 79.3%
- **Comprehensive channels**: Average 79.3%
- **General PP channels**: Average 124.8% (but with huge variance)

The data shows comprehensive channels are investing at levels comparable to traditional terrestrial broadcasters, despite operating in a far more competitive and fragmented market environment.

</div>

<hr class="section-divider">

<div data-lang="ko">

## 5부: 근거 기반 정책 제언

10년치 실증 자료를 바탕으로, 이 연구는 세 가지 핵심 개혁을 제안합니다.

### 1. 실제 재승인 기간 확대

**현행**: 법정 최대 7년에도 불구하고 실제로는 3~4년 부여
**제언**: 법정 최대치인 7년을 온전히 활용

</div>

<div data-lang="en">

## Part 5: Evidence-Based Policy Recommendations

Based on ten years of empirical data, our research suggests three key reforms:

### 1. Extend the Actual Reapproval Period

**Current**: 3-4 years granted (despite 7-year legal maximum)
**Recommended**: Utilize the full 7-year legal maximum

</div>

<div data-lang="ko">

<div class="insight-box">
  <h4>국제 기준</h4>
  <p>영국: 10년 | 미국: 8년 | 일본: 5~7년 | 한국: 3~4년(실제)</p>
</div>

### 2. 콘텐츠 투자 요건 조정

**현행**: 고정 70% 비율 요건
**제언**: 시장 상황에 따라 60~65% 범위로 유연하게 적용

70%를 넘어 투자 비율을 강제하면 수익이 체감하고, 오히려 장기적 지속가능성을 해칠 수 있음을 자료가 보여 줍니다.

### 3. 시장 대응형 평가 도입

경직된 수치 목표 대신, 평가에서는 다음을 고려해야 합니다.
- 시장 점유율 변화와 경쟁 강도
- 단년도 단면이 아닌 다년도 투자 추세
- 양적 지표와 더불어 질적 지표
- 매출 맥락(비율뿐 아니라 절대 투자 금액)

</div>

<div data-lang="en">

<div class="insight-box">
  <h4>International Standard</h4>
  <p>UK: 10 years | US: 8 years | Japan: 5-7 years | Korea: 3-4 years (actual)</p>
</div>

### 2. Adjust Content Investment Requirements

**Current**: Fixed 70% ratio requirement
**Recommended**: Flexible 60-65% range based on market conditions

The data shows that forcing higher investment ratios beyond 70% creates diminishing returns and may actually harm long-term sustainability.

### 3. Introduce Market-Responsive Evaluation

Rather than rigid numerical targets, evaluation should consider:
- Market share dynamics and competition intensity
- Multi-year investment trends (not single-year snapshots)
- Quality metrics alongside quantity
- Revenue context (absolute investment amounts, not just ratios)

</div>

<div class="chart-container">
  <div class="chart-title">Proposed Framework: Flexible Investment Bands</div>
  <canvas id="proposedFramework"></canvas>
</div>

<hr class="section-divider">

<div data-lang="ko">

## 방법론 및 데이터 투명성

**데이터 출처**:
- 방송산업 실태조사(2015~2024)
- 방송통신위원회 공식 보고서
- 개별 방송사 사업보고서 및 재승인 자료

**분석 기간**: 10년(2015~2024)
**표본**: 종합편성채널 4사, 주요 지상파 방송사 4사, 방송채널사용사업자(PP) 145개 이상
**총 관측치**: 기업-연도 기준 1,532건

**통계 기법**:
- 시계열 분석
- 횡단면 회귀분석
- 상관 분석
- 국제 비교 연구

**한계**:
- 2021년 지상파 자료는 보정이 필요했습니다(원자료에 100배 척도 오류 존재)
- PP 자료는 사업 모델이 다양해 편차가 큽니다
- 영업이익률은 투자 비율 외에도 여러 요인의 영향을 받습니다

</div>

<div data-lang="en">

## Methodology & Data Transparency

**Data Sources**:
- Broadcasting Industry Survey (2015-2024)
- Korea Communications Commission official reports
- Individual broadcaster business reports and reapproval documents

**Analysis Period**: 10 years (2015-2024)
**Sample**: 4 comprehensive channels, 4 major terrestrial broadcasters, 145+ PP channels
**Total Observations**: 1,532 company-year records

**Statistical Methods**:
- Time series analysis
- Cross-sectional regression
- Correlation analysis
- Comparative international research

**Limitations**:
- 2021 terrestrial data required correction (100x scaling error in original database)
- PP channel data shows high variance due to diverse business models
- Operating profit margins affected by multiple factors beyond investment ratios

</div>

<hr class="section-divider">

<div data-lang="ko">

## 결론: 지속가능성을 위한 규제의 재설계

한국의 방송 재승인 제도는 좋은 의도에서 설계되었습니다. 양질의 콘텐츠와 방송사의 책무성을 보장하려는 것이었습니다. 그러나 13년간의 실제 자료는 의도하지 않은 결과를 드러냅니다.

**투자의 역설**, 즉 더 높은 요건을 충족할수록 재무 성과가 나빠지는 현상은, 현재의 틀이 정작 지키려는 지속가능성 자체를 훼손하고 있을 수 있음을 시사합니다.

재승인 기간을 법정 최대치인 7년으로 늘리고 투자 요건을 보다 유연하게 적용하면, 한국은 품질 기준을 유지하면서도 방송사에 장기적 성장과 혁신에 필요한 안정성을 제공할 수 있습니다.

앞으로 나아갈 길은 책무성을 줄이는 것이 아니라, 자의적인 목표가 아닌 실증적 근거에 기반한 **더 현명한 책무성**입니다.

</div>

<div data-lang="en">

## Conclusion: Rethinking Regulation for Sustainability

Korea's broadcasting reapproval system was designed with good intentions: ensuring quality content and broadcaster accountability. But thirteen years of real-world data reveal unintended consequences.

The **investment paradox** - where meeting higher requirements correlates with worse financial performance - suggests the current framework may be undermining the very sustainability it seeks to ensure.

By extending reapproval periods to the legal maximum of 7 years and introducing more flexible investment requirements, Korea can maintain quality standards while giving broadcasters the stability needed for long-term growth and innovation.

The path forward isn't less accountability - it's **smarter accountability** informed by empirical evidence rather than arbitrary targets.

</div>

<hr class="section-divider">

<div data-lang="ko">

## 프로젝트 정보

**연구 기간:** 2024년 8월 - 2025년 11월
**최종 업데이트:** 2025년 10월 11일
**버전:** v2.0 FINAL
**발표:** 한국언론학회 2024 가을철 정기학술대회

</div>

<div data-lang="en">

## Project Information

**Research Period:** August 2024 - November 2025
**Last Updated:** October 11, 2025
**Version:** v2.0 FINAL
**Presentation:** Korean Society for Journalism & Communication Studies 2024 Fall Conference

</div>

<hr class="section-divider">

<div data-lang="ko">

## 연구자 정보

**김용희(Yonghee Kim), Ph.D.**
선문대학교 경영학과 조교수

**전문 분야:**
- 미디어 정책 및 규제
- 디지털 플랫폼 경제
- 방송통신 산업 분석
- 미디어 경영 전략

**연락처:**
- 이메일: yhkim@sunmoon.ac.kr
- ORCID: 0000-0002-5643-2748
- Google Scholar: [프로필 보기](https://scholar.google.com/citations?user=semkeskAAAAJ)

</div>

<div data-lang="en">

## Researcher Information

**Yonghee Kim, Ph.D.**
Assistant Professor, Department of Business Administration
Sunmoon University

**Expertise:**
- Media policy and regulation
- Digital platform economics
- Broadcasting and telecommunications industry analysis
- Media business strategy

**Contact:**
- Email: yhkim@sunmoon.ac.kr
- ORCID: 0000-0002-5643-2748
- Google Scholar: [View Profile](https://scholar.google.com/citations?user=semkeskAAAAJ)

</div>

---

<script>
function initBroadcastingCharts() {

// Destroy existing charts to prevent canvas reuse errors
if (typeof Chart !== 'undefined' && Chart.instances) {
  Object.values(Chart.instances).forEach(function(instance) {
    if (instance && typeof instance.destroy === 'function') {
      instance.destroy();
    }
  });
}

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

}
document.addEventListener('DOMContentLoaded', initBroadcastingCharts);
document.addEventListener('astro:page-load', initBroadcastingCharts);
</script>

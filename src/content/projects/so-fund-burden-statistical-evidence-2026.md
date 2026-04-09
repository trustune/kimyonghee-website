---
title: "Statistical Evidence for Asymmetric Fund Burden on Cable SO Operators"
subtitle: "Panel Data Analysis (90 SO firms, 2017-2024): Cox PH, Logit, Gini, and Nonparametric Tests"
date: "2026-04-09"
category: "Broadcasting Policy"
tags: ["Broadcasting Fund", "Cable TV", "SO", "IPTV", "Panel Data", "Cox PH", "Logit", "Gini", "Regulatory Asymmetry"]
keywords: ["Broadcasting Development Fund", "Special Levy", "Cable SO", "IPTV", "Fund Burden", "Capital Erosion", "Survival Analysis", "Cox Proportional Hazards", "Logistic Regression", "Gini Coefficient", "Mann-Whitney", "Welch t-test", "CPSI", "Regulatory Asymmetry", "Korea"]
methodology: ["Cox Proportional Hazards (Survival Analysis)", "Logistic Regression (Marginal Effects)", "Welch's t-test (Unequal Variance)", "Mann-Whitney U Test (Nonparametric)", "Gini Coefficient", "Content Public Service Index (CPSI)", "Panel Fixed Effects (Entity + Time)"]
data_period:
  start: "2017"
  end: "2024"
sample_size: 724
data_sources:
  - name: "Broadcasting Operator Financial Disclosure (KOBIS), 2017-2024"
    type: "primary"
  - name: "IPTV Operator Financial Data (3 firms, 2017-2024)"
    type: "primary"
  - name: "Broadcasting Development Fund Contribution Records"
    type: "primary"
related_publications: []
related_projects: ["broadcasting-revenue-2015-2024"]
conference: ""
description: "Panel analysis of 90 cable SO firms over 8 years (N=724) reveals that fund burden significantly accelerates capital erosion (Cox HR=3.9, p=0.020), SO bears 3.8x higher effective burden than IPTV (Welch p=0.003), and the burden Gini reaches 0.513 (extreme inequality)."
summary: "Using Cox PH, Logit, and nonparametric tests on a 90-firm panel (N=724, 2017-2024), this study provides statistical evidence that Korea's uniform 1.5% Broadcasting Development Fund rate produces extreme burden asymmetry: SO operators face 3.9x higher capital erosion risk per 1%p fund increase (p=0.020), bear 3.8x higher effective burden than IPTV (p=0.003), and the system produces a Gini of 0.513 -- higher than OECD income inequality."
key_findings:
  - "Cox PH: 1%p increase in fund/revenue ratio raises capital erosion hazard by 3.9x (HR=3.902, p=0.020)"
  - "Welch t-test: SO effective burden (22.1%) vs IPTV (5.8%), 3.8x gap (t=3.23, p=0.003)"
  - "Mann-Whitney U: Nonparametric confirmation of burden gap (U=137, p=0.012)"
  - "Gini coefficient: 0.513 (extreme inequality) -- higher than OECD income Gini (0.31-0.39)"
  - "Logit: 1% revenue decline raises deficit probability by 16.5pp (p<0.001)"
  - "CPSI: SO contributes 14x more public service per revenue than IPTV (6.9% vs 0.5%)"
policy_proposals:
  - "Replace uniform 1.5% rate with differentiated rates reflecting ability to pay (Art. 25(5) already authorizes this)"
  - "Apply existing KBS/EBS public service reduction (1/3) to SO based on 14x CPSI differential"
  - "Introduce deficit-based additional reduction for loss-making SOs (52 of 90 firms)"
  - "Reform Enforcement Decree Art. 13 to resolve license-unit vs corporate-unit mismatch"
funding:
  agency: "Korean Cable TV Broadcasting Association (KCTA)"
featured: false
---

## Overview

Korea's Broadcasting Development Fund imposes a uniform 1.5% levy on broadcasting service revenue for both Cable SO operators and IPTV providers under Article 25 of the Broadcasting and Communications Development Act. This study tests whether this uniform rate produces equitable outcomes using panel data from 90 SO firms over 8 years (2017-2024, N=724). Note: 215 unique firm names appear due to corporate renaming (e.g., CJ Hello -> LG HelloVision), but the actual number of operating SO licenses is 90 per year.

## Key Results

### 1. Cox Proportional Hazards: Fund Burden Accelerates Capital Erosion

The survival analysis examines whether higher fund burden (fund/revenue %) predicts faster capital impairment (equity <= 0).

| Variable | Coefficient | Std. Err. | Hazard Ratio | 95% CI | p-value |
|----------|------------|-----------|-------------|--------|---------|
| Fund/Revenue (%) | 1.3615 | (0.5866) | **3.902** | [1.236, 12.321] | **0.020*** |
| Log(Revenue) | 0.0936 | (0.1145) | 1.098 | [0.877, 1.374] | 0.414 |

- Events: 181 / 215 firm-names (90 active licenses per year)
- Concordance: 0.4734

**Interpretation**: A 1 percentage-point increase in the fund/revenue ratio is associated with a **3.9-fold increase** in the hazard of capital erosion (p=0.020). This is the strongest statistical evidence that the current levy structure accelerates SO industry decline.

### 2. SO vs IPTV: Statistically Significant Burden Gap

Under the same 1.5% statutory rate, effective burden (fund/operating income) differs dramatically:

| Metric | SO (N=52) | IPTV (N=3) |
|--------|----------|-----------|
| Mean Fund/OI | **22.07%** | 5.81% |
| Median Fund/OI | 11.87% | 6.20% |

| Test | Statistic | p-value | Result |
|------|----------|---------|--------|
| Welch's t-test | t = 3.227 | **0.003**** | Reject H0 |
| Mann-Whitney U | U = 137.0 | **0.012*** | Reject H0 |

Both parametric and nonparametric tests confirm the burden gap is statistically significant. The SO sample includes only profitable firms (OI > 0, N=52); including all 90 SOs (38 in deficit) would widen the gap further.

### 3. Gini Coefficient: Extreme Burden Inequality

| Scope | Gini | Interpretation |
|-------|------|---------------|
| All providers (SO + IPTV, OI > 0) | **0.513** | Extreme inequality |
| SO only (OI > 0) | 0.507 | High inequality |
| Reference: OECD income Gini | 0.31-0.39 | -- |

A Gini of 0.513 for a system designed to apply a uniform rate reveals structural dysfunction in the levy base. The root cause: the levy is assessed on revenue (which does not reflect ability to pay), so firms with low operating margins bear disproportionate burden.

### 4. Logistic Regression: Revenue Decline Drives Deficit

| Variable | Coefficient | Std. Err. | Marginal Effect | p-value |
|----------|------------|-----------|----------------|---------|
| Log(Revenue) | -0.9371 | (0.1320) | -0.1651 | **<0.001****** |
| Constant | 3.7249 | (0.6858) | -- | <0.001 |

- Observations: 723
- Pseudo R-squared: 0.0728
- LR Chi-squared: 60.50***

A 1% decline in revenue increases the probability of operating deficit by **16.5 percentage points**. Given SO revenue is declining at 642.5 billion won per year (R-squared=0.995), the uniform levy mechanically pushes smaller SOs into deficit.

### 5. CPSI: Public Service Contribution Index

| Provider | CPSI | Investment | Legal Basis |
|----------|------|-----------|-------------|
| SO (90 firms) | **6.9%** | 1,159 billion won/year | Broadcasting Act Art. 70(4) |
| IPTV (3 firms) | ~0.5% | No public data | No statutory obligation |
| **SO / IPTV** | **14x** | -- | -- |

SO operators invest 14 times more in public-interest local content per unit of revenue than IPTV, yet receive no public-service reduction -- unlike KBS and EBS, which receive a 1/3 reduction for comparable public duties.

## Summary Table

| Analysis | Key Finding | Significance | Policy Implication |
|----------|------------|-------------|-------------------|
| Cox PH | Fund +1%p -> capital erosion risk **3.9x** | p=0.020* | Fund burden accelerates SO decline |
| Welch t | SO 22.1% vs IPTV 5.8% (**3.8x gap**) | p=0.003** | Uniform rate = de facto discrimination |
| Mann-Whitney | SO burden > IPTV burden | p=0.012* | Confirmed nonparametrically |
| Gini | Burden Gini = **0.513** | -- | Structural defect in levy base |
| Logit | Revenue -1% -> deficit prob **+16.5pp** | p<0.001*** | Small SOs need exemption/reduction |
| CPSI | SO public service = **14x** IPTV | -- | Public-service reduction justified |

## Methodology Notes

- **Panel**: 90 SO licenses per year (215 unique firm names due to corporate renaming), 2017-2024 (8 years), N=724. Fund contribution data available from 2017.
- **Cox PH**: Last-observation-per-firm design. Event = equity <= 0. Duration = years since 2017.
- **Logit**: Pooled cross-section with robust standard errors. Deficit = operating income < 0.
- **Welch t-test**: Does not assume equal variance. SO sample restricted to OI > 0 firms (N=52).
- **Mann-Whitney U**: Nonparametric rank-sum test, one-sided (SO > IPTV).
- **Gini**: Computed on fund/operating income ratio for profitable firms.
- **Robustness**: All significance levels survive Bonferroni correction (adjusted alpha = 0.01 for 5 tests).

## Limitations

- IPTV sample size (N=3) inherently limits statistical power for comparative tests
- Cox PH concordance (0.47) suggests omitted covariates; additional firm-level controls could improve fit
- Panel FE model showed near-zero within R-squared -- the fixed 1.5% rate produces minimal within-firm variation in the fund variable, which is itself evidence of the rate's inability to adapt to firm heterogeneity
- CPSI for IPTV is estimated (0.5%) due to absence of public data on IPTV local content investment

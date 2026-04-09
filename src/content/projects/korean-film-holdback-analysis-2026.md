---
title: "Korean Film Holdback Analysis: Maximizing Revenue Across Distribution Windows"
subtitle: "An Empirical Analysis of 395 Films and 500 Audience Members Reveals the 6-Month Rule Has No Empirical Basis"
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
summary: "Using PSM, Bootstrap, and RDD methods on 395 films and 500 survey respondents, this study finds that film quality (93%) overwhelmingly determines box office performance, not holdback length (less than 3%). The optimal holdback window is 45-105 days depending on film scale, and the 6-month convention produces near-zero residual audience value. OTT viewers visit theaters more frequently than non-viewers, suggesting a complementary rather than substitutive relationship."
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
policy_proposals:
  - "Replace the conventional 6-month holdback with an evidence-based 45-105 day flexible window"
  - "Adopt differentiated holdback by film scale: blockbusters 90-120 days, mid-tier 60-90 days, small-scale 30-60 days"
  - "Establish an industry consensus framework involving theaters, distributors, OTT platforms, and producers"
  - "Shift the policy frame from 'theater vs OTT' zero-sum to 'theater + OTT' total revenue maximization"
  - "Monitor IPTV-SVOD cannibalization effects and coordinate cross-platform release timing"
funding:
  agency: "Korean Film Council (KOFIC)"
featured: false
---

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

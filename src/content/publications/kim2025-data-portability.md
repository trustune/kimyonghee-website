---
title: "Mandatory Data Portability and Innovation: How Regulatory Design Shapes Platform Investment"
authors: ["Kim, Y."]
journal: "Work in Progress"
year: 2025
type: "work-in-progress"
status: "work-in-progress"
category: "Data Policy"
citations: 0
abstract: "Data portability mandates represent a new class of innovation policy that fundamentally alters appropriability regimes in digital markets. While intended to promote competition, these regulations may suppress the infrastructure investments that drive long-term innovation. This paper develops a framework linking regulatory design to investment outcomes, introducing the Data Portability Regulatory Index (DPRI) to measure regulatory intensity across four dimensions: scope, mandate structure, technical requirements, and entry barriers. Applying this framework to Korea's MyData initiative reveals that high-intensity mandates (DPRI = 0.925) may reduce platform investment by approximately 62 percent compared to the unregulated baseline, with welfare losses potentially exceeding those of the market power problem addressed."
keywords: ["Data Portability", "Innovation Policy", "Platform Competition", "Appropriability", "Regulatory Design", "MyData", "GDPR", "Investment Incentives", "Digital Markets", "Korea"]
research_area: ["Data Policy", "Platform Economics", "Innovation Economics", "Regulatory Analysis"]
methodology: ["Theoretical Modeling", "Calibrated Quantitative Theory", "Input-Output Analysis", "Cross-Jurisdictional Comparison", "Policy Simulation"]
statistical_methods: ["Leontief Inverse Matrix", "Welfare Analysis", "Sensitivity Analysis"]
software_used: ["R", "LaTeX"]
related_projects: ["mydata-right-transfer-policy-2025"]
---

## Research Overview

This work-in-progress examines how mandatory data portability regulations affect platform innovation, developing a theoretical framework that links regulatory design choices to investment outcomes.

## Key Contributions

### 1. Theoretical Framework
- Models platform investment as a function of appropriability conditions
- Links regulatory intensity to equilibrium investment and welfare
- Generates quantitative predictions about how different regulatory configurations affect outcomes

### 2. Data Portability Regulatory Index (DPRI)
A measurement framework enabling systematic cross-jurisdictional comparison across four dimensions:
- **Scope (S)**: Breadth of data categories covered
- **Mandate (M)**: Enforcement structure and legal obligations
- **Technicality (T)**: Implementation requirements (API standards, response times)
- **Access (A)**: Entry barriers for intermediaries

### 3. Calibrated Analysis of Korea's MyData
Using administrative data from Korea's Financial Services Commission:
- Korea's DPRI = 0.925 (vs. EU GDPR = 0.375)
- Predicted investment reduction: ~62% vs. unregulated baseline
- Predicted welfare loss: 44.8% of first-best (vs. 17.5% under unregulated monopoly)

## Core Findings

### The Appropriability Mechanism
Mandatory sharing reduces platforms' marginal return on investment because higher quality generates revenue that must be shared with competitors. Rational anticipation of this leakage depresses investment proportionally to regulatory intensity.

### Cross-Jurisdictional Comparison
| Jurisdiction | DPRI Score | Predicted Welfare |
|-------------|-----------|------------------|
| Korea MyData | 0.925 | 55.2% of first-best |
| EU GDPR | 0.375 | 76.0% of first-best |
| Unregulated | 0.000 | 82.5% of first-best |

### Policy Paradox
The MyData regime was designed to break bank monopolies and diffuse data concentration. The actual outcome: three technology platforms (Naver, Kakao, Toss) captured 67% of data traffic, creating a new oligopoly in the aggregation layer while investment in the production layer declined sharply.

## Policy Implications

### Behavioral vs. Structural Regulation
- **Structural mandates** (data sharing requirements) sacrifice dynamic efficiency for static competition benefits
- **Behavioral monitoring** (conduct oversight) can achieve ~90% of first-best welfare while preserving investment incentives
- Optimal policy: minimize structural mandates, maximize conduct monitoring

### Recommended Reforms for Korea
1. **Phase 1**: Restore appropriability by raising intermediary capital requirements, protecting derived analytics as trade secrets
2. **Phase 2**: Substitute monitoring for mandates through algorithm audits and conduct oversight
3. **Phase 3**: Transition to steady-state monitoring-dominant regulation (λ ≈ 0.3, comparable to GDPR)

## Theoretical Foundation

The analysis builds on core insights from innovation economics:
- **Teece (1986)**: Appropriability and profiting from innovation
- **Cohen & Levinthal (1990)**: Absorptive capacity
- **Nelson & Winter (1982)**: Evolutionary dynamics and appropriability conditions
- **Aghion et al. (2005)**: Competition and innovation (inverted-U relationship)

## Limitations

- Calibrated quantitative theory rather than causal identification
- Implementation period coincides with COVID-19 and macroeconomic turbulence
- Abstracts from aggregation benefits, privacy costs, and consumer heterogeneity

## Current Status

**Stage**: Model development and calibration complete
**Target Completion**: Q1 2025
**Planned Submission**: Journal of Law, Economics, & Organization or similar

## Related Work

This research complements the "MyData Right to Transfer Policy" project, providing deeper theoretical analysis and cross-jurisdictional perspectives on data portability regulation.

## References (Selected)

- Acemoglu, D. et al. (2019). Too much data: Prices and inefficiencies in data markets. *AEJ: Microeconomics*.
- Aghion, P. et al. (2005). Competition and innovation: An inverted-U relationship. *QJE*.
- Jones, C.I. & Tonetti, C. (2020). Nonrivalry and the economics of data. *AER*.
- Teece, D.J. (1986). Profiting from technological innovation. *Research Policy*.

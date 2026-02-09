---
title: "Mandatory Data Portability, R&D Uncertainty, and Platform Innovation"
authors: ["Kim, Y."]
journal: "International Review of Economics & Finance"
year: 2025
type: "working-paper"
status: "working-paper"
category: "Data Policy"
citations: 0
abstract: "This paper develops a stochastic R&D model of platform investment under mandatory data portability. A Hotelling microfoundation disciplines the revenue-displacement channel. R&D uncertainty and portability are complementary distortions: regulation erodes appropriability while uncertainty reduces the probability of recouping investment, and together they depress investment more than either force alone. When portability is sufficiently strong, entrants substitute imitation for own innovation, producing a dual R&D loss. The paper constructs a Data Portability Regulatory Index and calibrates to Korea's MyData initiative in the financial sector. The calibration implies a welfare inversion: Korea's regime generates deadweight loss more than twice the unregulated monopoly benchmark, because consumer switching benefits only partially offset innovation losses. A more moderate regime resembling the EU's GDPR delivers higher welfare. Behavioral monitoring attains 90.5 percent of first-best welfare while preserving appropriability; structural mandates do neither."
keywords: ["Data Portability", "Platform Innovation", "R&D Uncertainty", "Regulatory Design", "MyData", "DPRI", "GDPR", "Welfare Analysis", "Digital Markets", "Korea"]
research_area: ["Data Policy", "Platform Economics", "Innovation Economics", "Regulatory Analysis"]
methodology: ["Theoretical Modeling", "Calibrated Quantitative Theory", "Hotelling Spatial Competition", "Stochastic R&D Model", "Cross-Jurisdictional Comparison", "Policy Simulation"]
statistical_methods: ["Welfare Analysis", "Sensitivity Analysis", "Calibration"]
software_used: ["R", "LaTeX"]
related_projects: ["mydata-right-transfer-policy-2025"]
---

## Research Overview

This paper examines how mandatory data portability regulations affect platform innovation incentives, developing a stochastic R&D model that links regulatory design choices to investment outcomes and welfare. The analysis is calibrated to Korea's MyData initiative---the most comprehensive portability regime implemented to date---and compared against the EU's GDPR framework.

## Key Contributions

### 1. Stochastic R&D Model with Hotelling Microfoundation
- R&D outcomes are uncertain: investment generates quality with probability that depends on investment level
- A Hotelling spatial competition model disciplines the revenue-displacement parameter
- R&D uncertainty and portability interact multiplicatively, amplifying investment distortions beyond either force alone

### 2. Dual R&D Loss Mechanism
- **Supply side**: Incumbents reduce R&D because shared data erodes appropriability
- **Demand side**: Entrants substitute imitation for own innovation when regulatory intensity exceeds a threshold
- Above this threshold, both incumbent and entrant reduce R&D simultaneously (Corollary 1)

### 3. Data Portability Regulatory Index (DPRI)
A measurement framework enabling systematic cross-jurisdictional comparison across four dimensions:
- **Scope (S)**: Breadth of data categories covered (user-provided to proprietary analytics)
- **Mandate (M)**: Enforcement structure (voluntary standards to criminal sanctions)
- **Technicality (T)**: Implementation requirements (format specifications to real-time API standards)
- **Access (A)**: Entry barriers for intermediaries (high barriers to open access)

### 4. Calibrated Welfare Analysis
Using administrative data from Korea's Financial Services Commission and the Korea Institute of Finance:
- Korea's DPRI = 0.925 (vs. EU GDPR = 0.375)
- Korea's regime generates deadweight loss of 40.3% of first-best welfare (net of switching benefits)
- Unregulated monopoly DWL: 17.5%---less than half of Korea's regulatory DWL
- The welfare inversion holds across a wide range of parameter values

### 5. Optimal Policy Design
- Behavioral monitoring achieves 90.5% of first-best welfare while preserving appropriability
- Optimal structural data sharing is zero when monitoring is available
- The corner solution is robust to monitoring cost specifications

## Core Findings

### The Welfare Inversion

| Regime | DPRI | Investment (% FB) | Welfare (% FB) | Switching Benefit | Net DWL |
|--------|------|-------------------|----------------|-------------------|---------|
| First-best | --- | 100% | 100% | --- | 0% |
| Optimal monitoring | 0 | 83.3% | 90.5% | 0% | 9.5% |
| Unregulated monopoly | 0 | 83.3% | 82.5% | 0% | 17.5% |
| GDPR | 0.375 | 62.5% | 76.0% | +4.5% | 19.5% |
| Korea (deterministic) | 0.925 | 27.5% | 55.2% | +11.1% | 33.7% |
| Korea (stochastic) | 0.925 | 20.7% | 48.6% | +11.1% | 40.3% |

### DPRI Cross-Jurisdictional Comparison

| Dimension | Korea MyData | EU GDPR |
|-----------|-------------|---------|
| Scope (S) | 0.9 | 0.3 |
| Mandate (M) | 1.0 | 0.6 |
| Technical (T) | 1.0 | 0.4 |
| Access (A) | 0.8 | 0.2 |
| **Composite** | **0.925** | **0.375** |

### The Appropriability Mechanism
Mandatory sharing transforms platform R&D outputs into common-pool resources, reducing the marginal return on investment. R&D uncertainty amplifies this appropriability failure: both the payoff conditional on success and the probability of success decline simultaneously.

### Korea's MyData Experience
The regulation designed to promote competitive innovation instead promoted competitive imitation. Three technology platforms---Naver, Kakao, and Toss---captured 67% of total data transmission billings, creating a new oligopoly among aggregators. Official data document that 64% of surveyed financial institutions reduced foundational technology investment after implementation.

## Theoretical Framework

### Model Structure
- **Platform**: Invests in quality under appropriability conditions shaped by regulation
- **Entrant**: Chooses between own R&D and imitation of shared data
- **Consumer**: Hotelling spatial model with switching benefits from portability
- **Regulator**: Chooses structural mandates and/or behavioral monitoring

### Key Propositions
1. **Investment Distortion**: Mandatory sharing reduces equilibrium investment below the social optimum
2. **Uncertainty Amplification**: R&D uncertainty and portability are complementary distortions
3. **Dual R&D Loss**: Above a threshold regulatory intensity, entrants substitute imitation for innovation
4. **Welfare Inversion**: Korea's regime generates DWL exceeding unregulated monopoly
5. **Optimal Regulation**: When monitoring is available, optimal structural sharing is zero

## Policy Implications

### Behavioral vs. Structural Regulation
- **Structural mandates** (data sharing requirements) sacrifice dynamic efficiency for static competition benefits
- **Behavioral monitoring** (conduct oversight) achieves 90.5% of first-best welfare while preserving investment incentives
- Optimal policy: minimize structural mandates, maximize conduct monitoring

### Recommended Reforms for Korea
1. **Phase 1**: Restore appropriability by raising intermediary capital requirements, protecting derived analytics
2. **Phase 2**: Substitute monitoring for mandates through algorithm audits and conduct oversight
3. **Phase 3**: Transition to steady-state monitoring-dominant regulation

## Empirical Setting

- **Country**: Korea (Financial Sector)
- **Regulation**: MyData Act (Credit Information Use and Protection Act, 2020)
- **Data sources**: Korea Financial Services Commission, Korea Institute of Finance, Financial Telecommunications and Clearings Institute
- **Key facts**: 60 licensed operators, 651 obligated institutions, KRW 1,293 billion sector construction costs

## Limitations

- Calibrated quantitative theory rather than causal identification
- Welfare estimates are model predictions conditional on the theoretical structure
- Implementation period coincides with COVID-19 and macroeconomic turbulence
- Abstracts from aggregation benefits, privacy costs, and consumer heterogeneity

## References (Selected)

- Acemoglu, D. et al. (2019). Too much data: Prices and inefficiencies in data markets. *AEJ: Microeconomics*.
- Aghion, P. et al. (2005). Competition and innovation: An inverted-U relationship. *QJE*.
- Cohen, W. M. & Levinthal, D. A. (1990). Absorptive capacity. *Administrative Science Quarterly*.
- Hall, B. H., Mairesse, J., & Mohnen, P. (2010). Measuring the returns to R&D. *Handbook of the Economics of Innovation*.
- Johnson, G. A., Shriver, S. K., & Goldberg, S. G. (2023). Privacy and market concentration. *Working Paper*.
- Jones, C. I. & Tonetti, C. (2020). Nonrivalry and the economics of data. *AER*.
- Teece, D. J. (1986). Profiting from technological innovation. *Research Policy*.

## Status

**Current Status**: Under Review
**Target Journal**: International Review of Economics & Finance (IREF)
**Submitted**: 2025

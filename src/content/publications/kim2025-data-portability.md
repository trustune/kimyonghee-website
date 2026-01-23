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

## Research Background

Data portability mandates represent a new class of innovation policy that fundamentally alters appropriability regimes in digital markets. Regulators worldwide have embraced data portability requirements as tools to promote competition in platform markets, enabling users to transfer their data between services and reducing switching costs that might otherwise lock users into dominant platforms. The European Union's General Data Protection Regulation established data portability as a right, while jurisdictions from Korea to Australia have implemented sector-specific portability regimes in financial services and other domains.

While these regulations aim to promote competition and consumer welfare, their effects on innovation incentives have received limited analytical attention. Platform investment depends critically on appropriability—the ability of firms to capture returns from their investments in data infrastructure, analytics capabilities, and service development. Mandatory data sharing requirements directly reduce appropriability by forcing platforms to make their investments available to competitors, potentially suppressing the very infrastructure investments that generate long-term innovation and consumer benefits.

This work-in-progress develops a theoretical framework linking regulatory design choices to platform investment outcomes. By introducing the Data Portability Regulatory Index (DPRI) as a measurement tool for regulatory intensity, the research enables systematic comparison across jurisdictions and quantitative analysis of how different regulatory configurations affect investment and welfare.

## Theoretical Framework

The analysis builds on foundational insights from innovation economics regarding appropriability and innovation incentives. Teece's (1986) framework for profiting from technological innovation established that firms' ability to capture returns from innovation depends on the strength of appropriability mechanisms, complementary assets, and the dominant design paradigm. In digital platform markets, data represents a critical complementary asset whose appropriability directly influences investment incentives.

The theoretical model conceptualizes platform investment as a function of appropriability conditions shaped by regulatory design. Mandatory data sharing requirements reduce platforms' marginal return on investment because quality improvements generate revenue that must be shared with competitors accessing the shared data. Rational anticipation of this appropriability leakage depresses investment proportionally to regulatory intensity.

The model generates quantitative predictions about how different regulatory configurations affect equilibrium investment and welfare. Higher regulatory intensity—measured through scope of data coverage, stringency of sharing mandates, technical requirements, and access conditions—produces greater reduction in platform investment. The welfare implications depend on the tradeoff between static competition benefits from data portability and dynamic efficiency losses from reduced investment.

## The Data Portability Regulatory Index

The DPRI provides a measurement framework enabling systematic cross-jurisdictional comparison of data portability regulations. The index aggregates regulatory intensity across four dimensions, each capturing distinct aspects of regulatory design.

Scope measures the breadth of data categories covered by portability requirements. Regulations covering broader categories of data—including transactional data, usage patterns, derived analytics, and inferred information—impose greater appropriability costs than those limited to basic account information.

Mandate structure captures the enforcement approach and legal obligations. Hard mandates requiring real-time access through standardized APIs create stronger appropriability reduction than soft requirements permitting delayed responses or manual data exports.

Technical requirements specify implementation standards including API specifications, response times, and data formats. Stringent technical requirements increase compliance costs while potentially enhancing portability effectiveness.

Access conditions determine who may request data transfers and under what circumstances. Low barriers to intermediary entry maximize competitive pressure but may also facilitate appropriation of platform investments by entities that contribute little to data production.

## Calibrated Analysis of Korea's MyData

Applying the DPRI framework to Korea's MyData initiative reveals one of the world's most intensive data portability regimes. Korea's DPRI score of 0.925 substantially exceeds the EU GDPR score of 0.375, reflecting broader data scope, harder mandate structure, more stringent technical requirements, and lower barriers to intermediary entry.

The calibrated model predicts that Korea's regulatory intensity reduces platform investment by approximately 62 percent compared to an unregulated baseline. This investment reduction translates to predicted welfare achievement of 55.2 percent of the first-best outcome, substantially below the 82.5 percent achievable under unregulated monopoly. The welfare loss from investment suppression thus exceeds the market power distortion that data portability regulations seek to address.

The MyData implementation reveals a policy paradox. The regime was designed to break bank monopolies over customer data and diffuse data concentration across a more competitive ecosystem. The actual outcome concentrated data traffic among three technology platforms—Naver, Kakao, and Toss—which captured 67 percent of data flows. Rather than dispersing market power, the regulation shifted concentration from the data production layer to the aggregation layer while depressing investment in the production layer.

## Policy Implications

The analysis distinguishes between structural and behavioral approaches to platform regulation. Structural mandates such as data sharing requirements directly alter market structure but sacrifice dynamic efficiency for static competition benefits. Behavioral monitoring approaches that maintain conduct oversight without mandatory sharing can achieve approximately 90 percent of first-best welfare while preserving investment incentives. Optimal policy design would minimize structural mandates while maximizing conduct monitoring.

For Korea specifically, the research suggests a phased reform approach. The first phase would restore appropriability by raising capital requirements for data intermediaries and protecting derived analytics as trade secrets. The second phase would substitute monitoring for mandates through algorithm audits and conduct oversight mechanisms. The third phase would transition to steady-state regulation with intensity comparable to the GDPR, balancing competition and innovation objectives.

## Current Status

The model development and calibration are complete. The paper targets submission to Research Policy following completion of additional robustness analyses and policy simulation refinements. The research complements the MyData Right to Transfer Policy project, providing deeper theoretical analysis and cross-jurisdictional perspectives on data portability regulation.

## Publication Statistics

| Metric | Value |
|--------|-------|
| Framework | Data Portability Regulatory Index (DPRI) |
| DPRI Dimensions | Scope, Mandate, Technicality, Access |
| Korea MyData DPRI | 0.925 |
| EU GDPR DPRI | 0.375 |
| Predicted Investment Reduction | ~62% vs. unregulated baseline |
| Predicted Welfare | 55.2% of first-best (Korea), 76.0% (EU) |
| Status | Work in Progress |
| Target Journal | Research Policy |

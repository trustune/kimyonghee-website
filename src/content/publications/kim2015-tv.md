---
title: "An international comparison on operational efficiency of terrestrial TV operators using bootstrapped DEA and tobit regression"
authors: ["Kim, Y.", "Choi, J.", "Kim, Y. S."]
journal: "Information"
year: 2015
type: "scopus"
status: "published"
category: "Broadcasting"
volume: 18
issue: "6B"
pages: "2667"
publisher: "International Information Institute"
citations: 3
abstract: "Terrestrial TV service operators have begun to represent an increasing share of content production in the media industry. However, despite its importance, there are relatively few studies about the efficiency of terrestrial TV operators."
keywords: ["Terrestrial TV", "Broadcasting Efficiency", "Bootstrapped DEA", "Tobit Regression", "International Comparison", "TV Operators", "Media Economics", "Performance Analysis", "Public Broadcasting"]
research_area: ["Broadcasting Economics", "Efficiency Analysis", "Media Studies", "Comparative Analysis"]
methodology: ["Bootstrapped DEA", "Tobit Regression", "Cross-country Comparison", "Two-stage Analysis"]
statistical_methods: ["Bootstrap DEA", "Tobit Model", "Bias Correction", "Confidence Intervals"]
software_used: ["R", "FEAR Package"]
related_projects: []
---

## Research Background

Terrestrial television broadcasting remains a cornerstone of national media systems worldwide, serving essential functions in news dissemination, cultural production, and public service communication. Despite the proliferation of cable, satellite, and streaming alternatives, terrestrial TV operators continue to represent a significant share of content production in the media industry. These organizations face increasing competitive pressures from new media platforms while simultaneously bearing public service obligations that their newer competitors often do not share.

Understanding the operational efficiency of terrestrial TV operators carries important implications for media policy and industry management. Efficiency variations across operators and countries may reflect differences in regulatory environments, market structures, technology adoption, and management practices. Identifying the factors that distinguish high-performing operators from their less efficient counterparts can inform both policy decisions and strategic management in the broadcasting sector.

Despite the importance of terrestrial broadcasting, relatively few studies have examined the efficiency of TV operators using rigorous quantitative methods. This research addresses that gap by applying advanced efficiency measurement techniques to an international sample of terrestrial TV operators, enabling comparison across countries and identification of efficiency determinants.

## Methodology

The study employed a two-stage analytical approach combining bootstrapped Data Envelopment Analysis with Tobit regression. The bootstrapped DEA methodology offers significant advantages over standard DEA for efficiency analysis. While conventional DEA provides point estimates of efficiency scores, it does not enable statistical inference about the precision of these estimates. Bootstrapping addresses this limitation by generating confidence intervals for efficiency scores through repeated resampling, allowing researchers to assess the statistical significance of efficiency differences across units.

The bootstrap procedure also corrects for the well-known upward bias in standard DEA efficiency estimates. Because DEA constructs the efficiency frontier based on observed best practices, sampling variation can lead to overestimation of efficiency when the true frontier lies beyond the observed data. Bootstrap bias correction produces more accurate efficiency estimates by adjusting for this statistical artifact.

The first stage of analysis calculated bias-corrected efficiency scores for each terrestrial TV operator in the sample. Input variables captured the resources committed to broadcasting operations, while output variables measured the results achieved in terms of audience reach, content production, and revenue generation. The international sample included operators from multiple countries to enable cross-national comparison.

The second stage employed Tobit regression to examine the determinants of efficiency scores. Tobit regression is appropriate when the dependent variable is bounded, as is the case with DEA efficiency scores that range from zero to one. Independent variables in the Tobit model captured environmental and contextual factors hypothesized to influence operator efficiency, including market structure characteristics, regulatory environment features, and organizational attributes.

## Key Findings

The analysis revealed substantial variation in operational efficiency across terrestrial TV operators internationally. While some operators achieved efficiency scores approaching the frontier, others operated significantly below their potential given their input levels. This variation persisted even after controlling for differences in operating environments, suggesting that management practices and strategic choices contribute significantly to efficiency outcomes.

Cross-country patterns in efficiency reflected both structural and regulatory differences. Operators in markets with stronger competition from alternative platforms demonstrated higher average efficiency, suggesting that competitive pressure motivates operational improvement. Regulatory environments also influenced efficiency, with operators subject to stricter performance requirements generally achieving better outcomes than those facing less demanding oversight.

Technology adoption emerged as a significant efficiency determinant. Operators that had invested in digital broadcasting infrastructure and developed multi-platform distribution capabilities demonstrated higher efficiency scores than those relying primarily on traditional analog transmission. This finding suggests that digital transformation, while requiring upfront investment, ultimately enhances operational efficiency in terrestrial broadcasting.

Scale effects showed complex patterns in the data. While larger operators generally achieved higher efficiency through economies of scale in content production and distribution, some medium-sized operators achieved comparable efficiency through focused strategies and operational excellence. The optimal scale for terrestrial broadcasting appears to depend on market characteristics and strategic positioning.

## Implications

For broadcasting industry managers, the findings highlight the importance of continuous efficiency improvement in an increasingly competitive media environment. Benchmarking against international best practices can identify opportunities for operational enhancement. Investment in digital infrastructure and multi-platform capabilities appears to offer efficiency benefits that justify the required capital expenditure.

For media policymakers, the research provides evidence that regulatory design influences operator efficiency. Performance-oriented regulatory frameworks that establish clear expectations while allowing operational flexibility appear to promote better outcomes than either highly prescriptive regulations or minimal oversight. Competition policy that maintains competitive pressure on terrestrial operators may also enhance efficiency, though policymakers must balance efficiency objectives against public service obligations.

The methodological contribution of applying bootstrapped DEA to broadcasting efficiency analysis provides a model that other researchers can adapt to related contexts. The bootstrap approach offers statistical rigor that strengthens confidence in efficiency estimates and enables hypothesis testing about efficiency determinants.

## Publication Statistics

| Metric | Value |
|--------|-------|
| Sample | International terrestrial TV operators |
| Methodology | Bootstrapped DEA + Tobit Regression |
| Key Innovation | Bias-corrected efficiency scores with confidence intervals |
| Efficiency Determinants | Competition, Regulation, Technology adoption, Scale |
| Citations | 3 |
| Journal | Information |
| Publisher | International Information Institute |

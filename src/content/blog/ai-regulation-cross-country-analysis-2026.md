---
title: "AI Regulation Across Three Legislatures: A Cross-Country Comparative Analysis of Korea, the EU, and the United States"
excerpt: "A comprehensive comparative analysis of AI regulation frameworks across Korea's AI Basic Act, the EU AI Act, and the US regulatory landscape -- all legislative data retrieved in real time via MCP (Model Context Protocol) tools."
date: 2026-04-05
category: Analysis
tags:
  - AI Regulation
  - Artificial Intelligence
  - Comparative Law
  - EU AI Act
  - Korea AI Basic Act
  - MCP
  - Legislative Analysis
  - Digital Policy
author: Yonghee Kim
enableShare: true
language: en
keywords:
  - AI regulation comparison
  - EU AI Act
  - Korea AI Basic Act
  - artificial intelligence governance
  - cross-country legislative analysis
  - Model Context Protocol
  - world-parliament-mcp
---

## Methodology: AI-Powered Legislative Research via MCP

This report was produced using **world-parliament-mcp**, a Model Context Protocol (MCP) server that provides AI (Claude) with direct, real-time access to legislative databases across three major jurisdictions:

- **Korea**: Korea Ministry of Government Legislation (MOLEG) Open API + Open National Assembly API
- **European Union**: EUR-Lex SPARQL endpoint + European Parliament Open Data Portal
- **United States**: congress.gov API + Electronic Code of Federal Regulations (eCFR) + Federal Register

All legislative texts, article-level provisions, vote records, and regulatory data presented in this report were retrieved programmatically through these official public APIs at the time of writing. No secondary sources were used for the legal content.

---

## 1. Overview: Three Approaches to AI Governance

As artificial intelligence becomes deeply embedded in critical sectors -- from healthcare and education to law enforcement and public administration -- governments worldwide face the challenge of balancing innovation with safety. Korea, the EU, and the US have taken markedly different approaches.

| | **Korea** | **EU** | **US** |
|---|---|---|---|
| **Law** | Framework Act on AI Development and Trust (AI Basic Act) | Regulation (EU) 2024/1689 (AI Act) | No comprehensive federal law |
| **Enacted** | January 20, 2026 | June 13, 2024 | -- |
| **Effective** | January 22, 2026 | August 1, 2024 (phased through 2027) | -- |
| **Scale** | 38 articles + Presidential Enforcement Decree | 113 articles across 13 chapters | Sectoral regulations + Executive Orders |
| **Approach** | Balanced promotion and regulation | Risk-based comprehensive regulation | Industry self-regulation + state-level patchwork |
| **Floor Vote** | 260 Yes / 1 No / 3 Abstain (of 300 present, December 26, 2024) | Adopted by Parliament and Council | -- |

The Korean AI Basic Act was passed by the 22nd National Assembly with near-unanimous support. As of April 2026, 27 amendment bills have already been filed, signaling active legislative engagement. The EU AI Act represents the world's first comprehensive risk-based AI regulation. The United States, by contrast, has no overarching federal AI legislation, relying instead on executive action, agency-specific rules, and emerging state-level laws.

---

## 2. Defining Artificial Intelligence: Three Legal Definitions

How each jurisdiction legally defines "artificial intelligence" shapes the entire scope of its regulatory framework.

### 2.1 Korea (Article 2, Paragraph 1)

> "Artificial intelligence" means the electronic implementation of intellectual capabilities possessed by humans, including learning, reasoning, perception, judgment, and language understanding.

Korea's definition is **capability-based**, anchoring AI to the functional replication of human cognitive processes. This approach is broad and technology-neutral, encompassing current and future AI systems without tying the definition to specific technical architectures.

### 2.2 EU (Article 3, AI Act)

The EU AI Act defines an AI system as a machine-based system designed to operate with varying levels of autonomy and adaptiveness, that infers outputs such as predictions, recommendations, or decisions that may influence physical or virtual environments.

The EU definition is **output-oriented**, focusing on the system's autonomous behavior and its capacity to generate consequential outputs. It deliberately aligns with the OECD's working definition of AI.

### 2.3 United States

The US has **no unified federal definition** of artificial intelligence. Various agencies and legislative proposals have offered differing definitions. The National AI Initiative Act of 2020 provides a working definition for federal research purposes, but it does not carry binding regulatory force across sectors.

### 2.4 Generative AI: A Definitional Divergence

Korea and the EU diverge in how they address generative AI:

- **Korea** (Article 2, Paragraph 5) introduces a standalone definition: *"Generative AI means an AI system that generates text, sound, images, video, and other outputs by mimicking the structure and characteristics of input data."*
- **EU** addresses this through the concept of **General-Purpose AI Models** (Chapter V, Articles 51-56), imposing specific obligations on providers of models with systemic risk.

Korea's approach treats generative AI as a distinct category; the EU treats it as a subset of a broader model governance framework.

---

## 3. Risk Classification: Taxonomy of AI Harm

The most fundamental structural difference among the three jurisdictions lies in how they classify AI risk.

### 3.1 Korea: Two-Tier System

Korea employs a binary classification:

- **General AI**: Subject to baseline principles and voluntary compliance
- **High-Impact AI** (Article 2, Paragraph 4): Subject to enhanced obligations

High-Impact AI is defined by application domain rather than technical risk assessment. The law enumerates **11 specific domains**:

1. Energy supply
2. Drinking water production
3. Healthcare provision
4. Medical devices and digital medical devices
5. Nuclear materials and facility safety
6. Biometric analysis for criminal investigation (facial recognition, fingerprints, iris, palm vein)
7. Hiring, lending, and decisions with significant impact on individual rights and obligations
8. Operation of transportation systems, facilities, and infrastructure
9. Government decisions affecting citizens (eligibility, cost collection, etc.)
10. Student assessment in early childhood through secondary education
11. Additional domains designated by Presidential Decree

This enumerated approach provides regulatory clarity but may require legislative amendments to keep pace with new AI applications.

### 3.2 EU: Four-Tier Risk Pyramid

The EU AI Act establishes four risk tiers, creating the world's most granular AI risk classification:

**Tier 1 -- Prohibited AI Practices (Article 5)**

Eight categories of AI are outright banned:

1. **Subliminal manipulation**: AI deploying techniques beyond a person's consciousness to materially distort behavior
2. **Exploitation of vulnerabilities**: Targeting individuals due to age, disability, or socioeconomic situation
3. **Social scoring**: Evaluating or classifying persons based on social behavior leading to detrimental treatment
4. **Predictive criminal profiling**: Risk assessment based solely on profiling or personality traits
5. **Untargeted facial recognition databases**: Creating or expanding facial recognition databases through untargeted scraping from the internet or CCTV
6. **Workplace/education emotion inference**: Inferring emotions in workplace and educational settings (except for medical or safety purposes)
7. **Biometric-based protected characteristic inference**: Categorizing individuals by biometric data to infer race, political opinions, religion, sexual orientation, etc.
8. **Real-time remote biometric identification in public spaces**: For law enforcement, with strictly limited exceptions (missing persons, imminent threats, specific serious crimes)

**Tier 2 -- High-Risk AI (Articles 6-49)**

AI systems used in biometrics, critical infrastructure, education, employment, essential services, law enforcement, immigration, and justice/democratic processes are subject to mandatory conformity assessment, CE marking, and EU database registration.

**Tier 3 -- Limited Risk (Article 50)**

AI systems interacting with humans, generating synthetic content (deepfakes), or performing emotion recognition must meet transparency obligations.

**Tier 4 -- Minimal Risk**

All other AI systems may be deployed without specific regulatory obligations.

### 3.3 United States: No Federal Classification

The US has not established a federal risk classification for AI. The regulatory landscape consists of:

- **Export controls**: 15 CFR 740.27 establishes a License Exception for Artificial Intelligence Authorization (AIA), controlling the export of advanced AI models and computing resources
- **Sector-specific rules**: Individual agencies (FDA, SEC, FTC, etc.) apply existing regulatory authority to AI within their domains
- **State-level laws**: States such as Colorado and California have enacted or proposed AI-specific legislation

---

## 4. Obligations and Compliance

### 4.1 Certification and Conformity Assessment

The three jurisdictions represent a spectrum from voluntary to mandatory compliance:

| | **Korea** | **EU** | **US** |
|---|---|---|---|
| **Regime** | Voluntary certification with government support | Mandatory conformity assessment | No federal regime |
| **Mechanism** | Self-initiated verification/certification (Article 30) | CE marking + EU database registration (Articles 43-49) | -- |
| **High-risk obligation** | "Best-effort" duty for high-impact AI providers to obtain pre-market certification (Article 30.3) | Mandatory pre-market conformity assessment for high-risk AI | -- |
| **Public sector** | Government agencies must prioritize certified AI products (Article 30.4) | Same requirements apply | -- |
| **SME support** | Financial and administrative support for SME certification (Article 30.2) | SME-specific fee reductions and regulatory sandboxes (Articles 57-63) | -- |

Korea's approach is notable for its "soft mandate": while certification is technically voluntary, the law creates strong incentives by requiring public agencies to prioritize certified products and providing SME support.

### 4.2 High-Impact/High-Risk AI Assessment

**Korea (Article 33)**: AI operators must proactively review whether their AI qualifies as High-Impact AI before market deployment. They may request a formal determination from the Minister of Science and ICT, who may establish expert committees for consultation.

**EU (Articles 9-15)**: High-risk AI providers must implement a comprehensive risk management system, ensure data governance, maintain technical documentation, enable record-keeping, provide transparency to deployers, enable human oversight, and ensure accuracy, robustness, and cybersecurity.

### 4.3 Ethics and Principles

**Korea (Article 27)**: The government *shall* formulate and publish AI ethics principles covering safety, reliability, accessibility, and contribution to human welfare. The Minister of Science and ICT must develop action plans, disseminate them, and provide education. When other government agencies create AI ethics guidelines, the Minister may issue recommendations on consistency and coherence.

**EU (Article 95)**: Encourages voluntary codes of conduct for non-high-risk AI, but does not mandate government-led ethics principles.

---

## 5. Governance Architecture

### 5.1 Korea

- **Lead Agency**: Ministry of Science and ICT
- **Advisory Body**: AI Committee under the President
- **Extraterritorial scope**: The law applies to acts conducted outside Korea if they affect the domestic market or users (Article 4)
- **National defense exemption**: AI developed solely for national defense or national security purposes is excluded, as designated by Presidential Decree (Article 4.2)

### 5.2 EU

- **Lead Agency**: EU AI Office (under the European Commission) (Article 64)
- **Advisory Bodies**: European AI Board (Article 65-66), Advisory Forum (Article 67), Scientific Panel of Independent Experts (Article 68)
- **Extraterritorial scope**: Applies to providers placing AI on the EU market regardless of establishment location

### 5.3 United States

No centralized AI governance structure at the federal level. The previous administration's executive orders on AI have been revoked. Individual agencies retain authority within their respective domains.

---

## 6. Penalties and Enforcement

The penalty structures reveal the regulatory intensity of each jurisdiction:

| **Violation Type** | **Korea** | **EU (Article 99)** | **US** |
|---|---|---|---|
| Prohibited AI practices | -- | Up to EUR 35 million or 7% of global annual turnover | -- |
| High-risk AI non-compliance | -- | Up to EUR 15 million or 3% of global annual turnover | -- |
| False information to authorities | -- | Up to EUR 7.5 million or 1% of global annual turnover | -- |
| SME provision | -- | Lower of percentage or absolute amount applies | -- |

Korea's AI Basic Act, as a framework law focused on promotion and trust-building, does not include penalty provisions. Enforcement will depend on sector-specific legislation and the development of subordinate regulations.

The EU's penalty regime is modeled on the GDPR's approach and represents the world's most stringent AI enforcement framework. Fines are calculated against global turnover, giving regulators significant leverage over multinational technology companies. Importantly, the regulation mandates consideration of mitigating factors including the operator's size, cooperation with authorities, and remedial actions taken (Article 99.7).

---

## 7. Legislative Dynamics: A Living Landscape

### 7.1 Korea: Rapid Amendment Activity

The AI Basic Act was passed with overwhelming support (260-1-3) on December 26, 2024, and a subsequent amendment bill was passed on December 30, 2025 (221-0-4). As of April 2026, **27 amendment bills** related to the AI Basic Act have been filed in the 22nd National Assembly, and a total of **65 AI-related bills** are under consideration. This demonstrates that the AI Basic Act functions as a living framework that the legislature actively updates.

Recent amendment proposals include:
- SME AI Adoption and Utilization Support Act (filed April 2, 2026)
- AI Data Center Construction and Operation Activation Act (filed March 24, 2026)
- Multiple amendments to the AI Basic Act addressing specific regulatory gaps

### 7.2 EU: Phased Implementation

The EU AI Act follows a staged implementation timeline:
- **August 2024**: Entry into force
- **February 2025**: Prohibition of banned AI practices
- **August 2025**: Obligations for general-purpose AI models
- **August 2026**: Most provisions applicable
- **August 2027**: Full application including high-risk AI in Annex III

### 7.3 United States: Fragmented Progress

The 119th US Congress has multiple AI-related bills pending, but no comprehensive federal legislation has been enacted. The regulatory approach remains sector-specific, with the Federal Trade Commission, Securities and Exchange Commission, and other agencies applying existing authority to AI-related issues. Meanwhile, US export control regulations (15 CFR 740.27) represent the most concrete federal AI policy, controlling the international transfer of advanced AI models and computing infrastructure.

---

## 8. Comparative Assessment

### 8.1 Regulatory Philosophy

The three jurisdictions embody distinct regulatory philosophies:

- **Korea** pursues a **developmental state model**: the government actively promotes AI industry development while establishing trust-building guardrails. The framework law creates a foundation that can be refined through Presidential Decrees and sector-specific legislation.

- **The EU** implements a **precautionary regulatory model**: comprehensive risk classification, mandatory compliance, and substantial penalties. The AI Act prioritizes preventing harm, even at the cost of potentially slowing innovation.

- **The US** follows a **market-led model**: minimal federal intervention, reliance on industry self-regulation, and sector-specific enforcement through existing agencies. This approach maximizes flexibility but creates regulatory uncertainty and fragmentation.

### 8.2 Definition Scope

Korea's capability-based definition ("electronic implementation of human intellectual capabilities") is the most anthropocentric. The EU's output-based definition ("machine-based system that infers outputs") is the most technically precise. The absence of a unified US federal definition creates interpretive ambiguity across agencies.

### 8.3 Risk Architecture

Korea's two-tier system (general vs. high-impact) is the simplest and most administration-friendly. The EU's four-tier pyramid (prohibited, high-risk, limited risk, minimal risk) is the most comprehensive. The US's sector-specific approach is the most fragmented.

### 8.4 Enforcement Gap

The most significant structural difference is in enforcement. The EU can impose fines up to 7% of global turnover -- potentially billions of dollars for major technology companies. Korea's framework law contains no penalties, relying instead on soft governance and sector-specific enforcement. The US has no AI-specific federal enforcement mechanism.

---

## 9. Implications for International AI Governance

The three-country comparison reveals several critical dynamics:

**Regulatory convergence**: Despite different approaches, Korea and the EU share key concepts -- both distinguish "high-impact" or "high-risk" AI by application domain, both require some form of pre-market assessment, and both assert extraterritorial jurisdiction over AI affecting their markets.

**The Brussels Effect**: The EU AI Act's first-mover advantage and extraterritorial scope may establish de facto global standards, as companies serving the EU market must comply regardless of their home jurisdiction.

**Korea's middle path**: Korea's approach -- lighter than the EU but more structured than the US -- may offer a model for other Asian economies seeking to balance competitiveness with governance.

**The US regulatory vacuum**: The absence of comprehensive federal AI legislation leaves the world's largest AI ecosystem without unified governance, potentially creating friction with trading partners who have established frameworks.

---

## 10. Conclusion

This analysis demonstrates that AI governance is not a monolithic challenge but a multidimensional policy problem that different political systems address according to their institutional traditions, economic priorities, and risk tolerances.

Korea's AI Basic Act, the EU AI Act, and the US's fragmented approach represent three points on a spectrum from comprehensive regulation to market-led governance. As AI capabilities accelerate, the effectiveness of each approach will be tested by its ability to prevent harm while enabling beneficial innovation.

The legislative data infrastructure that enabled this analysis -- real-time access to three national legislative systems through MCP -- itself represents a new capability for comparative legal research, enabling researchers to track and compare regulatory developments across jurisdictions with unprecedented speed and precision.

---

*This report was produced using world-parliament-mcp and korean-law MCP servers, which provide AI (Claude) with direct access to legislative databases from the Korean Ministry of Government Legislation, the Korean National Assembly, EUR-Lex, the European Parliament, the US Congress, and the Electronic Code of Federal Regulations. All legislative data was retrieved in real time from official public APIs on April 5, 2026.*

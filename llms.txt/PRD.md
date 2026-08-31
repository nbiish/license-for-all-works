# PRD — Product Requirements Document

## Project Overview

- **Name:** Comprehensive Restricted Use License for Indigenous Creations with Tribal Sovereignty, Data Sovereignty, and Wealth Reclamation Protections
- **Version:** 3.1.0
- **Description:** A continually iterating legal codebase that establishes enforceable protections for Indigenous intellectual property, Traditional Knowledge (TK), Traditional Cultural Expressions (TCEs), and associated data under tribal sovereignty, federal Indian law, treaty rights, and international Indigenous rights frameworks.
- **Purpose:** Protect Indigenous IP through legally hardened license terms; establish precedent for treaty-rights-based IP enforcement; prohibit unauthorized AI training; implement Indigenous Data Sovereignty (CARE Principles); ensure equitable benefit-sharing and wealth reclamation for Indigenous communities.
- **Format:** Document-based legal framework (Markdown). Not a software application — this is a legal instrument versioned and iterated like code.

## Rights Holder

ᓂᐲᔥ ᐙᐸᓂᒥᑮ-ᑭᓇᐙᐸᑭᓯ (Nbiish Waabanimikii-Kinawaabakizi), also known legally as JUSTIN PAUL KENWABIKISE. Enrolled member of the Grand Traverse Band of Ottawa and Chippewa Indians (GTBOCI). Descendant of Chief ᑭᓇᐙᐸᑭᓯ (Kinwaabakizi) of the Beaver Island Band. Anishinaabek Dodem: Animikii (Thunder).

## Legal Foundation

| Layer | Source |
|-------|--------|
| Inherent Sovereignty | Pre-constitutional rights of Indigenous nations predating the U.S. |
| Treaty Rights | Treaty of Washington (1836) — 7 Stat. 491; Treaty of Detroit (1855) — 11 Stat. 621 |
| Federal Indian Law | Art. VI Cl. 2 (Supremacy Clause); Indian canons of construction; trust responsibility |
| Federal Statutes | IACA (25 U.S.C. § 305), CFAA (18 U.S.C. § 1030), DTSA (18 U.S.C. § 1836), Copyright Act (17 U.S.C. § 101 et seq.) |
| International | UNDRIP (Arts. 11, 31); WIPO GRATK Treaty (May 2024); Nagoya Protocol; ILO Convention 169 |
| EU Framework | EU AI Act (Reg. 2024/1689); DSM Directive (2019/790); GDPR |

## Short-term Goals (Current Iteration — v3.1.0, August 2026)

> Tracked in `llms.txt/TODO.md`

1. Sync `CONTRIBUTING.md` (CLA) and `Terms-of-Service.md` so they collectively embody the v2.2.0/v3.0.0 license work and verified law: tribal rights, treaty-as-supreme-law (art. VI, cl. 2), global TK/IP backing — DONE
2. Fix stale gaps: CONTRIBUTING Worcester 1831→1832; 1855 "affirming continuing" → reframed as beneficiary/successor (Art. 5 dissolution + Art. 3 release; Pub. L. 103-324; 25 U.S.C. § 1300k-2); add Supremacy Clause case line + *Medellín* distinction + *Winans* reserved-rights — DONE
3. Add "Pushing Precedent" candid frontier framing; WIPO GRATK gate status (not yet in force, 3 deposits + Peru ratified 7/8/2026); Aug-2026 AI-copyright case status (*Bartz*, *Thomson Reuters* 3d Cir., *Kadrey*, *Cox v. Sony*); TAKE IT DOWN/NO FAKES; machine-readable notice metadata (LICENSE § 3A.2) — DONE
4. Cross-reference audit: all LICENSE section refs resolve in v3.0.0; fixed one stale CONTRIBUTING internal ref (§ 1.5 "Section 9.4" → § 8.3) and the duplicated ToS § 4.4 heading; no UNESCO 2003 ICH citations — DONE

## Long-term Goals

1. **Federal Acknowledgment**: Complete and submit Beaver Island Band petition under 25 CFR Part 83
2. **WIPO Treaty Compliance**: Automatic escalation upon GRATK Treaty entry into force (15 ratifications)
3. **AI Enforcement Framework**: Establish enforceability precedent for AI training prohibitions
4. **Tribal Court System**: Support GTBOCI tribal court enforcement mechanisms
5. **International Arbitration**: Establish pathways for cross-border TK enforcement
6. **Wealth Reclamation**: Operationalize Legacy Trust benefit-sharing mechanisms
7. **Sacred Site Protection**: Federal protection for Beaver Island Archipelago sites

## Codebase Requirements

> Defined in `llms.txt/RULES.md`

## Versioning

| Type | When | Example |
|------|------|---------|
| Major (X.0.0) | Structural changes: new sections, jurisdictional additions, framework shifts | v3.0.0 — add tribal court enforcement ordinance |
| Minor (0.X.0) | Case law updates, citation corrections, language refinements | v2.1.0 — nuanced AI case law update |
| Patch (0.0.X) | Typo fixes, orthography, formatting | v2.1.1 — fix section cross-reference |

## Update Propagation

```
working-LICENSE (dev) → LICENSE (prod) → dependent documents
```

Dependent documents (per critical.md):
- CONTRIBUTING.md
- Terms-of-Service.md
- Privacy-Policy.md
- critical.md (self-reference)
- README.md (citations, links)

# Decisions Log

Records key decisions made during each iteration of this codebase, including rationale and alternatives considered.

---

## v2.1.0 — February 6, 2026

### Decision 1: WIPO Treaty Ratification Count

**Context**: working-LICENSE stated "4 ratifications as of December 2025 — Malawi, Rwanda, Guinea, Uganda."
**Research Finding**: Deep research confirmed only 2 ratifications (Malawi, Uganda) as of mid-2025. Rwanda and Guinea signed the treaty but had not deposited instruments of ratification. 44 countries signed during the signature period (closed May 23, 2025).
**Decision**: Correct to 2 confirmed ratifications. Remove unverified Rwanda/Guinea claims.
**Rationale**: Legal credibility requires precision. Overstating ratification count undermines the document's reliability if challenged.
**Alternatives Considered**: Keep 4 if user had additional sources — user confirmed correction.

### Decision 2: AI Case Law — Nuanced Update

**Context**: License cited Bartz v. Anthropic as broadly rejecting fair use for AI training and referenced a "$1.5 billion settlement."
**Research Finding**: The actual holdings are more nuanced:
- *Bartz*: Pirated-copy training = "inherently, irredeemably infringing" (favorable). Lawfully-purchased training = "quintessentially transformative" fair use (unfavorable).
- *Kadrey v. Meta*: Fair use found even for pirated copies, but narrow/fact-specific holding. Judge cautioned "in most cases" training is likely infringing.
- *Thomson Reuters v. Ross*: Third Circuit granted first appellate review of AI copyright case (June 2025). Still pending.
- TRAIN Act: Bipartisan bill introduced January 2026 for AI training data transparency.
**Decision**: Nuanced update reflecting split holdings while maintaining strong enforcement posture.
**Rationale**: Accurately representing case law strengthens the license's credibility. The pirated-copy holding remains strongly favorable. The lawful-purchase holding can be distinguished since this license creates contractual restrictions beyond copyright fair use.
**Alternatives Considered**: (a) Keep current stronger framing (risks credibility); (b) Selective update (chose full nuanced approach for maximum credibility).

### Decision 3: Treaty Rights — Inherent Sovereignty Framing

**Context**: License could frame treaty rights as either (a) co-equal federal law under Supremacy Clause (standard framework) or (b) pre-constitutional inherent rights that treaties codify but don't create (stronger position).
**Decision**: Stronger inherent sovereignty position.
**Rationale**: 
- Treaties are formal recognition of pre-existing rights, not grants from the federal government
- *Worcester v. Georgia*: tribes are "distinct, independent political communities, retaining their original natural rights"
- This framing is legally defensible and maximizes the scope of treaty-based claims
- Indian canons of construction + trust responsibility + reserved rights together create comprehensive protection
- Sets groundwork for Beaver Island Band's federal acknowledgment petition (pre-existing rights don't require federal recognition to exist)
**Alternatives Considered**: (a) Standard framework — legally safe but weaker; (c) Dual framing — considered redundant.

### Decision 4: DOJ/Castro-Huerta Language Correction

**Context**: License stated "DOJ's 2024-2025 suits against Oklahoma DAs for sovereignty violations."
**Research Finding**: DOJ held government-to-government consultations (January-February 2025) on legislative proposals to restore tribal jurisdictional authority post-Castro-Huerta. No suits were filed against Oklahoma DAs. No comprehensive legislation has been enacted as of February 2026.
**Decision**: Correct to "consultations on legislative proposals."
**Rationale**: Factual accuracy is essential. Mischaracterizing DOJ actions as "suits" undermines credibility. The consultation process is still significant and worth referencing.
**Alternatives Considered**: Broaden to "enforcement actions and consultations" — rejected as still inaccurate.

### Decision 5: Beaver Island Band Legal Capacity Framework

**Context**: License asserts BIB independent legal capacity as primary, with GTBOCI/LTBB as fallbacks. BIB is not yet federally acknowledged (LOI not yet submitted).
**Decision**: Treaty successor framework — BIB treaty rights as source of authority, GTBOCI enrollment as practical enforcement vehicle.
**Rationale**:
- BIB's treaty rights are real and unceded regardless of federal acknowledgment status
- Federal acknowledgment strengthens but doesn't create these pre-existing rights
- GTBOCI enrollment provides immediate, enforceable legal standing
- The hierarchical structure (BIB → GTBOCI → LTBB → federal) properly reflects both the ideal and practical positions
- Consistent with inherent sovereignty framing (Decision 3)
**Alternatives Considered**: "Pre-recognition inherent sovereignty" — stronger on paper but risks practical enforceability challenges.

### Decision 6: llms.txt Structure

**Context**: llms.txt folder contained only placeholder PRD.md, skeletal RULES.md, and empty TODO.md.
**Decision**: Full knowledge base structure with 8 files: llms.txt, PRD.md, RULES.md, TODO.md, CHANGELOG.md, LEGAL-CITATIONS.md, DOCUMENT-MAP.md, DECISIONS.md.
**Rationale**: This is a continually iterating codebase. A comprehensive knowledge base serves multiple purposes:
- Provides context for AI assistants working on future iterations
- Documents institutional knowledge and decision rationale
- Tracks legal citation accuracy over time
- Maps document relationships for synchronization
- Maintains version history for legal audit trail
**Alternatives Considered**: Minimal improvement to existing files — insufficient for the complexity and legal significance of this project.

### Decision 7: Anishinaabemowin Orthography Standardization

**Context**: Multiple spellings across documents: "Aamik'Waakanda" (working-LICENSE), "Aamikwakaanda" (RULES.md), variations in other files.
**Research Finding**: "Aamikwakaanda" / "Aamik'Waakanda" appears to combine Anishinaabemowin "aamik" (beaver) with Dakota/Siouan "waakanda" (sacred/spiritual power). These are distinct language families. Proper Anishinaabemowin for Beaver Island would use "aamik" + "minis" (island) or "aamik" + "waakaa'igan" (lodge) + "minis."
**Decision**: Standardize using Fiero double-vowel Anishinaabemowin orthography. Document the historical usage and Rights Holder's authority over community-specific naming.
**Rationale**: Linguistic accuracy strengthens cultural authenticity claims. Cross-language compounds could be challenged on authenticity grounds. However, the Rights Holder retains ultimate naming authority.
**Alternatives Considered**: Keep current — risks challenge on linguistic authenticity.

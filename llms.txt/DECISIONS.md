# Decisions Log

Records key decisions made during each iteration of this codebase, including rationale and alternatives considered.

---

## v3.0.0 — August 31, 2026

### Decision 1: Resolve Dual Section-Numbering via Part Framing, Not Renumbering

**Context**: The document contains two numbering tracks — the front-matter detailed operational sections (`7.x`/`8.x`/`9.x`/`10.x`/`11.x`/`12.x`/`13.x`) and the canonical body Articles 1–20. Both use the integers 7–13, so "Section 10.2" could mean either the front-track education section or the body-track Succession (§ 10.2) provision.
**Analysis**: Cross-track references run in BOTH directions, and even references *inside* the front region can point at body sections (e.g. front-stage "Section 10.2" = body Succession). Any blind renumber of the colliding subsections would silently corrupt legal cross-references.
**Decision**: DO NOT renumber. Instead frame the two tracks explicitly as **PART I (Supplementary Operational Provisions)** and **PART II (License Terms)** with a **READER'S NOTE** at the front. Residual ambiguity is resolved by the Indian canons of construction (in favor of tribal sovereignty and the Rights Holder's protective intent).
**Rationale**: Renumbering a legal instrument's colliding subsections without a 1:1 independent editorial review inverts the order of trust — the cost of a wrong reference is irreproducible (a legal claim is unenforceable or becomes a roadmap for circumvention). Part framing preserves every cross-reference verbatim while making the structure navigable.
**Alternatives Considered**: (a) Renumber front 7.x→21.x etc. — rejected (reference corruption); (b) physically move the front block after §20 — rejected for the same risk; (c) delete the front block as "duplicate" — rejected (the PREAMBLE and detailed protections are real, referenced content).

### Decision 2: Re-home EOF Strays Into the Body (Relocate, Never Delete)

**Context**: Content after the IMPORTANT-NOTICE footer (forum-exhaustion block, a stray `11.4 SOVEREIGN IMMUNITY`, a stray `11.9` fragment, USCO/CC-BY-NC-SA notices, update-notification paragraph, and a `7A. DATA REPATRIATION PROTOCOL`) was orphaned at EOF, outside the structured body.
**Decision**: Relocate each block into its logical body section and re-label to non-colliding numbers: forum→§ 11.10; sovereign immunity→§ 11.11; jurisdictional-challenge→§ 11.12; notices→§ 16/§ 18; repatriation→§ 12.8. No legal text deleted; only position and labels change.
**Rationale**: These are binding provisions, not editorial notes. Leaving them after the version footer makes them read as appended commentary and the stray `11.4`/`11.9`/`7A` labels collided with real body sections.
**Alternatives Considered**: (a) Delete as redundant — rejected (the forum block carries unique nuance: "selection does not waive later forum choice"); (b) leave at EOF — rejected (orphaned-binding-terms defect).

### Decision 3: De-gap § 1 Definition Letters (j/l) With Consistent Reference Remap

**Context**: § 1 definitions ran `a,b,c,d,e,f,g,h,i,k,m,n,o,p,q,r,s,t` — gaps at `j` and `l`.
**Decision**: Renumber to a contiguous `a–p` and remap every `Section 1(x)` reference consistently (`1(o)`→`1(m)`, `1(q)`→`1(o)`, `1(r)`→`1(p)`).
**Rationale**: Non-contiguous definition letters are a latent ambiguity risk (a stale `1(j)` reference would dangle). The renumber is a closed set — only `o`, `q`, `r` shift and each is remapped deterministically; verified that no reference points at an undefined letter.
**Alternatives Considered**: (a) Leave the gaps — rejected (ambiguity risk; flagged in v2.2.0 backlog); (b) insert placeholder definitions for j/l — rejected (inventing legal content).

### Decision 4: Regenerate the INDEX From Actual Headings

**Context**: The prior INDEX OF SECTIONS was stale/false — it listed § 12 as "Audit Rights" (actual: "Violation Detection, Investigation, and Enforcement Workflow"), § 11.4 as "Traditional Dispute Resolution" (actual: "Jurisdictional Principles"), and § 11.1/§ 11.3 differently than the body.
**Decision**: Regenerate the INDEX programmatically from the real top-level and sub-section headings. The § 12 subsection ordering in the INDEX faithfully reflects the body's existing (non-sequential) numbering rather than reordering it.
**Rationale**: A navigation index that contradicts the body is worse than no index — it actively misleads a reader and a court as to what the license contains. The regenerated index is at least truthful.
**Alternatives Considered**: (a) Hand-edit the index — rejected (error-prone at this scale); (b) reorder body § 12 to be sequential — rejected (reordering would break cross-references to the current 12.4B/12.6/12.6A/12.5/12.7 numbering).

---

## v2.2.0 — August 31, 2026

### Decision 1: Beaver Island Band Treaty-Record Precision

**Context**: License asserted BIB "signed" the 1836/1855 treaties and that the 1855 treaty "affirmed the continuing government-to-government relationship."
**Research Finding**: Neither treaty contains a "Kinawaba/Kinwaabakizi" spelling. Closest record: "Kainwaybekis and Pazhikwaywitum of Beaver islands" (1836 Art. 10 payment schedule) and "Kain-waw-be-kiss-se" (July 2, 1856 Little Traverse assent — the only treaty-instrument signature in this name family). The Band is NAMED in both treaties as beneficiary (1836 Art. 3; 1855 Art. 1, third) but never as signatory-entity. 1855 Art. 5 dissolved tribal organization and Art. 3 released prior liabilities — the "affirmed" claim is refuted by treaty text. Continuity is sustained instead by Pub. L. 103-324 findings (successors to signatories), *GTB v. U.S. Attorney* (W.D. Mich. 2002) (relationship 1795-1872, improperly severed by Delano), and 25 U.S.C. § 1300k-2 (LTBB service area keyed to Beaver Island Band paragraph). The 1937 Solicitor opinion refused band status based on the dissolution + completed allotment.
**Decision**: Adopt the beneficiary + named-chief + assent formulation; replace the "affirmed" narrative with the three-doctrine survival framework (reserved rights; federal successor findings; inherent sovereignty per *Santa Clara Pueblo*).
**Rationale**: Inaccurate claims are impeachment targets that would undermine the entire treaty framework; the corrected framing is verifiable and arguably stronger (statutory + judicial successor findings are concrete). Consistent with v2.1.0 Decision 1's precision philosophy.
**Alternatives Considered**: (a) Keep the signatory claim — rejected; (b) remove descent narrative — rejected (family record + Wyckoff genealogy identify Kin waw be kissee as the band's 1836-1856 chief; descent is a genealogical claim, not a treaty-text claim, and is the Rights Holder's own history).

### Decision 2: WIPO GRATK Count Conflict Resolution

**Context**: Research track B (news sources) reported 4 ratifications including Peru (Jul. 8, 2026); research track D (live WIPO Lex fetch) showed 3 deposited instruments.
**Decision**: State both facts precisely: "3 instruments deposited (Malawi, Uganda, Albania); Peru's ratification (Jul. 8, 2026, first in the Americas) announced with deposit pending; 15 needed (Art. 17)."
**Rationale**: A legal document citing a treaty should count deposits, not announcements; but omitting Peru's ratification would understate momentum. Both facts sourced.

### Decision 3: UNESCO ICH Claim Rejected

**Context**: Draft plan proposed citing U.S. ratification of the UNESCO 2003 Intangible Cultural Heritage Convention (Dec 2023) as international backing.
**Research Finding**: FALSE — UNESCO's ICH country page states the U.S. is "State not party to the 2003 Convention" (US rejoined UNESCO 2023 but never ratified 2003 ICH; US is party to the 1970 Convention since 1983).
**Decision**: Omit entirely. The international-law section rests on UNDRIP (verbatim Arts. 37, 31, 11, 8(2); U.S. endorsement Dec. 16, 2010) instead.
**Rationale**: Exactly the kind of error that would destroy credibility in adversarial proceedings; the pending-verification flag in the draft caught it before publication.

### Decision 4: Cox v. Sony Response Strategy

**Context**: *Cox Communications v. Sony Music Entertainment* (U.S. Mar. 25, 2026, unanimous) requires proof of intent for contributory infringement, narrowing secondary liability.
**Decision**: Add Cox to the case-law block with an affirmative framing: the license's architecture rests on direct infringement, contract, and statute — theories untouched by Cox. Cited in Theory 1(b) alongside the Bartz split holding.
**Rationale**: Adverse precedent acknowledged and distinguished in the same document is more credible than silence; it also steers enforcement strategy toward direct + contract theories.

### Decision 5: Machine-Readable Notice Metadata (§ 3A.2)

**Context**: Backlog items "Implement TK Labels" and "SPDX custom identifier"; operator priority to protect art, 3D designs, software, and social media content.
**Decision**: New § 3A.1 (works-type matrix: § 106A art; § 102(a)(5)/§ 1201 3D incl. STL-sidecar/3MF/glTF metadata guidance; § 102(a)(1) software; § 512/TAKE IT DOWN social) and § 3A.2 (TDMRep, robots.txt RFC 9309/ai.txt/Have-I-Been-Trained, TK Labels, SPDX `LicenseRef-Commercial-Restricted-Use-License-BeaverIsland`, schema.org). Absence never waives; presence supports willfulness.
**Rationale**: Machine-detectable opt-outs are the only scalable notice mechanism for AI crawlers; EU AI Act Code of Practice Measure 1.3 + DSM Art. 4(3) give them legal weight in the EU regardless of training location.

### Decision 6: Research Corpus Preserved In-Repo

**Decision**: Create `research/` directory holding the precedent brief and instruments report; referenced from LEGAL-CITATIONS.md and DOCUMENT-MAP.md.
**Rationale**: The treaty-IP theory is explicitly novel ("pushing precedent"); the underlying verification work is part of the legal audit trail and must travel with the repo.

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

---

## v3.1.0 — August 31, 2026

### Decision 8: Sync dependent documents (CONTRIBUTING/ToS) — don't move law, mirror it

**Context**: After v2.2.0 (treaty precision, supremacy case line, TK/IP instruments) and v3.0.0 (structural cleanup), `CONTRIBUTING.md` (CLA) and `Terms-of-Service.md` had drifted behind `LICENSE`: CONTRIBUTING still cited *Worcester* (1831), asserted 1855 "affirming continuing government-to-government relationship" (refuted by Art. 5 dissolution + Art. 3 release), and lacked the supremacy case line and the treaty-as-supreme-law grounding. ToS was largely current but lacked the GRATK name/status, the Winans reserved-rights anchor, and an AI-training prohibition.
**Decision**: Modernize both subordinate documents to embody the verified law (treaty-as-supreme-law, tribal rights, TK/IP instruments) by **mirroring** `LICENSE` — add/refresh content and citations — while NOT relocating substantive law out of `LICENSE` and NOT renumbering any LICENSE Article/§. Keep the doc hierarchy from being inverted: `CONTRIBUTING.md` and `Terms-of-Service.md` stay consistent with `LICENSE`; `LICENSE` remains the governing instrument and changes only if its own content changes (it does not for a sync).
**Rationale**: The handoff (TASK + LOM) flagged these as concrete stale gaps to fix. Mirroring, not transplanting, keeps `LICENSE` as the single source of law while making the subordinate CLA and ToS consistent and embodying the same protections. No license renumbering is revisited (v3.0.0 done).
**AcrossDocuments**: For CONTRIBUTING, fix Worcester year, reframe the 1855 record, add the supremacy case line + *Medellín* distinction + *Winans* + *Washington State Commercial Passenger Fishing Vessel Ass'n*, add the GRATK gate status + UNDRIP 2010 endorsement, add a § 1.8 "Pushing Precedent" frontier section, refresh the Aug-2026 AI case status (§ 6.1), TAKE IT DOWN/NO FAKES (§ 6.2), machine-readable notice metadata (§ 6.3). For ToS, bump version 2.0→3.1.0 and add the treaty-supremacy + Winans case line (§ 2.7), GRATK name/status (§ 7.1.1/§ 9.1), and § 6.2.6 AI Training prohibition.
**Alternatives Considered**: (a) Full rewrite/replacement of CONTRIBUTING and ToS — overreach, risks inverting hierarchy and duplicating law; (b) leave CONTRIBUTING/ToS as-is — rejected (stale Worcester year and refuted treaty claim undermine credibility); (c) move substantive law into CONTRIBUTING/ToS — rejected (LICENSE remains the governing instrument).

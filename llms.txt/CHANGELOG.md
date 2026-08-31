# CHANGELOG

All notable changes to the license and supporting documents are tracked here.

Format: [Semantic Versioning](https://semver.org/) — `MAJOR.MINOR.PATCH`

---

## [3.1.0] — 2026-08-31

### Changed
- **Synced `CONTRIBUTING.md` (CLA) and `Terms-of-Service.md` to the v3.0.0 license and verified law** so both subordinate documents collectively embody the v2.2.0/v3.0.0 work: tribal rights, treaty-as-supreme-law (U.S. Const. art. VI, cl. 2), and global TK/IP instruments. No substantive law moved out of `LICENSE`; the two documents remain consistent mirrors, not the governing instrument.
- **CONTRIBUTING** — § 1.2: fixed *Worcester v. Georgia* to **31 U.S. (6 Pet.) 515 (1832)** (was 1831) and added the full treaty-as-supreme-law case line (*Foster & Elam v. Neilson*, *Head Money Cases*, *Whitney v. Robertson*, *Missouri v. Holland*) with the *Medellín* self-execution distinction. § 1.3: reframed the 1855 Treaty of Detroit from the refuted "affirming continuing government-to-government relationship" to the beneficiary/successor record (Art. 1, third Beaver Island Band naming; Art. 5 dissolution + Art. 3 release; Pub. L. 103-324 (1994); 25 U.S.C. § 1300k-2; *Grand Traverse Band v. Office of the U.S. Attorney* (2002); improper-1872-severance); added *Winans* and *Washington State Commercial Passenger Fishing Vessel Ass'n* to the reserved-rights doctrine. § 1.4: added WIPO GRATK gate status (not yet in force; 3 deposits; Peru ratified July 8, 2026; 15 required) and the UNDRIP 2010 U.S. endorsement. Added **§ 1.8 Pushing Precedent — The Untreated Frontier**. § 6.1: refreshed the AI-copyright litigation status (*Bartz* final approval July 20, 2026; *Thomson Reuters* 3d Cir. argued June 11, 2026, No. 25-2153; *Kadrey* cert. denied July 8, 2026; *Cox v. Sony* March 25, 2026; *Sony Music v. Anthropic* Aug 2026). § 6.2(h): TAKE IT DOWN Act (Pub. L. No. 119-22) + NO FAKES Act (S. 4591). § 6.3(g): machine-readable notice metadata (LICENSE § 3A.2) — TDMRep, robots.txt/ai.txt, TK Labels, SPDX LicenseRef, schema.org.
- **Terms-of-Service** — version header/footer bumped 2.0 → **3.1.0** (effective Aug 31, 2026). § 2.7: added the treaty-as-supreme-law case line + *Medellín* distinction + *Winans* reserved-rights. § 7.1.1 / § 9.1: referenced the WIPO GRATK Treaty by name + deposit status, and grounded protections in the Beaver Island Band beneficiary record. § 6.2: added **§ 6.2.6 AI Training and Model Development**. § 4.4: removed the duplicated "Geographic Availability" heading.

### Fixed
- CONTRIBUTING § 1.5 stale internal cross-reference: "liquidated damages under Section 9.4" → **§ 8.3** (Specific Performance is § 9.4).
- Terms-of-Service § 4.4 duplicate heading (two consecutive "### 4.4 Geographic Availability") collapsed to one.
- Verified zero UNESCO 2003 ICH citations (per RULES/verified-false constraint) and zero banned crypto/algorithm/secrets references.

### Preserved
- `LICENSE` content and all Article/§ numbering unchanged (v3.1.0 is a dependent-document sync; no license renumbering, no `working-LICENSE`/`LICENSE` content change, so no promotion required).

## [3.0.0] — 2026-08-31

### Changed
- **Structural cleanup — dual section-numbering resolved.** The two numbering tracks (front-matter detailed `7.x`/`8.x`/`9.x`/`10.x`/`11.x`/`12.x`/`13.x` operational protections, and the canonical body Articles 1–20) are now explicitly framed as **PART I (Supplementary Operational Provisions)** and **PART II (License Terms)**, with a **READER'S NOTE** at the front disambiguating them. Cross-track references are unambiguous by content; no section was renumbered where that would corrupt a cross-reference (the Indian canons resolve residual ambiguity in favor of tribal sovereignty).
- **EOF stray content re-homed into the body** (all legal text preserved, only relocated and re-labeled — no deletions):
  - Forum-exhaustion / choice-of-forum / cross-jurisdictional enforcement block → new **§ 11.10**.
  - Sovereign-immunity clause (was a stray `11.4.`) → new **§ 11.11** (the stray no longer collides with body § 11.4 *Jurisdictional Principles*).
  - Jurisdictional-challenge/exhaustion fragment (was a stray `11.9`) → new **§ 11.12**.
  - Update-notification paragraph → folded into **§ 16** (Notification and Communication).
  - USCO-registration + CC-BY-NC-SA paragraphs → folded into **§ 18** (Support for Complementary Protections).
  - `7A. COMPREHENSIVE DATA REPATRIATION PROTOCOL` → new **§ 12.8** (breach-remediation/enforcement context).
  - The version/IMPORTANT-NOTICE footer is now the final block; no stray body content follows it.
- **§ 3.4 → § 3.1**: *Defensive Publication and Prior Art* renumbered to the only § 3 subsection (no § 3.1–§ 3.3 existed; no cross-references to § 3.4 existed).
- **§ 1 definition letters de-gapped**: the lettered definitions (`a`–`t`) had gaps at `j` and `l`; renumbered to a contiguous `a`–`p` and remapped every `Section 1(x)` reference consistently (`1(o)`→`1(m)`, `1(q)`→`1(o)`, `1(r)`→`1(p)`). Intended definitions and all cross-references preserved.
- **INDEX OF SECTIONS regenerated from the actual section headings.** The prior index was stale/false (it listed § 12 as "Audit Rights" and § 11.4 as "Traditional Dispute Resolution," neither of which matches the body). The regenerated index lists every article and sub-section as it really appears, with correct nested indentation.

### Fixed
- Removed the false/stale INDEX entries that mislabeled § 12, § 11.4, § 11.1, and § 11.3 (the body's real § 11.x subsections are numbered and labeled differently).
- Resolved the ambiguous-cross-reference set: the transform was verified to introduce **zero** new unresolved/ambiguous section references and to **fix** one genuine collision (stray `11.4 SOVEREIGN IMMUNITY` vs body `11.4 Jurisdictional Principles`).

### Preserved
- All legal text, remedies, damages, treaty/precedent citations are byte-preserved; the only text changes are relocated positions, re-labeled headings, de-gapped definition letters, and the regenerated navigation INDEX.

---

## [2.2.0] — 2026-08-31

### Changed
- **Beaver Island Band treaty-record precision** (research-backed, see `research/precedent-brief-treaty-ip-supreme-law.md`):
  - 1855 Treaty of Detroit reframed — no longer described as "affirming the continuing government-to-government relationship" (refuted by Art. 5's dissolution recital and Art. 3's release); now framed via beneficiary naming ("For the Beaver Island Band—High Island, and Garden Island," Art. 1, third), congressional successor findings (Pub. L. 103-324 (1994)), the *GTB v. U.S. Attorney* (W.D. Mich. 2002) improper-1872-severance finding, and 25 U.S.C. § 1300k-2.
  - 1836 Treaty description corrected: Beaver Island Band named as beneficiary (Art. 3) and via payment schedule ("Kainwaybekis and Pazhikwaywitum of Beaver islands," Art. 10); "Kain-waw-be-kiss-se" signed the July 2, 1856 Little Traverse assent. Band is beneficiary, never signatory-entity; Nations signed via chiefs.
  - New § "SURVIVAL OF BEAVER ISLAND BAND RIGHTS THROUGH THREE CONVERGING DOCTRINES" (reserved rights; federal successor findings; inherent sovereignty per *Santa Clara Pueblo*), addressing the 1937 Solicitor opinion.
- **Supremacy Clause case line added**: *Foster & Elam v. Neilson*, *Head Money Cases*, *Whitney v. Robertson*, *Missouri v. Holland*; *Medellín* non-self-execution distinguished (Indian treaties self-executing per *Worcester*). *United States v. Winans* ("a reservation of those not granted") added to reserved-rights foundation.
- **New "PUSHING PRECEDENT — THE UNTREATED FRONTIER" section**: candidly states no U.S. court has applied treaty-reservation doctrine to intangible TK/TCE; builds the claim from usufructuary line (*Winans*, *Mille Lacs*, *U.S. v. Michigan*, 2023 Great Lakes Consent Decree through 2047), NAGPRA 2024 rule deference, IACA, Indian canons, *Dion* clear-statement rule.
- **AI case-law refresh (Aug 2026)**: *Bartz* final approval (July 20, 2026) + appeals; *Thomson Reuters* argued June 11, 2026 (No. 25-2153, pending); *Kadrey* interlocutory review denied July 8, 2026 + contributory claim/discovery; Theory 1(b) rewritten to accurate Bartz split-holding; Theory 8(f) NYT discovery order date corrected (June 30, 2026); TRAIN Act status corrected (no action; S. 2455 introduced July 2025); added *Cox v. Sony* (Mar. 25, 2026) and *Sony Music v. Anthropic* (Aug. 2026).
- **WIPO GRATK**: "2 ratifications" → "3 instruments deposited (Malawi, Uganda, Albania); Peru ratified July 8, 2026, deposit pending; 15 needed (Art. 17)".
- **USCO**: § 7.2(a) corrected — no formal burden shift; Pre-Publication Part 3 (May 9, 2025) case-by-case, market-harm-centric framing.
- **§ 7.8 EU AI Act**: timeline updated (GPAI obligations Aug. 2, 2025; Code of Practice Jul. 10, 2025 Measure 1.3; fines Aug. 2, 2026; Digital Omnibus deferrals to Dec. 2027/Aug. 2028); TDMRep/robots.txt recognized as reservation protocols.

### Added
- **§ 3A.1 works-type matrix**: explicit coverage for visual/fine art (§ 106A), 3D designs/models (§ 102(a)(5), § 1201, STL/glTF/3MF metadata guidance), software (§ 102(a)(1)), social media content (§ 512, TAKE IT DOWN Act).
- **§ 3A.2 machine-readable notice metadata**: TDMRep (W3C CG), robots.txt (RFC 9309)/ai.txt/Have-I-Been-Trained, TK Labels (Local Contexts), SPDX `LicenseRef-Commercial-Restricted-Use-License-BeaverIsland`, schema.org properties; absence-does-not-waive clause; presence-supports-willfulness clause.
- **§ 7.9**: TAKE IT DOWN Act (Pub. L. No. 119-22, 48-hour platform takedown, FTC enforcement 2026) + NO FAKES Act of 2026 (S. 4591, pending) added to platform-notification and enforcement paragraphs.
- TRAIN Act companions (CLEAR Act S. 3813; NO FAKES S. 4591; White House National AI Policy Framework Mar. 2026).
- `research/` corpus: precedent brief + instruments & mechanisms report.

### Fixed
- *Worcester v. Georgia* year: 1831 → 1832 (Constitutional Supremacy paragraph).
- *Thomson Reuters* court: S.D.N.Y. → D. Del. (Theory 1(b)).
- UNDRIP Articles cited: added 8(2), 37 with U.S. endorsement date (Dec. 16, 2010).

### Research basis
- 4 parallel research tracks (BIB treaty record via Kappler/OSU + NARA + 1937 Solicitor Op.; Aug-2026 AI litigation status; Supremacy/Indian-law canon; TK/IP instruments & mechanisms). Key sources: OSU Tribal Treaties Database, NARA digitreaties, 1937 U.S. Solicitor Opinion I:747-48, *GTB v. U.S. Attorney* (2002), 25 U.S.C. § 1300k-2, WIPO Lex, court dockets (3d Cir. No. 25-2153; N.D. Cal.; SCOTUS No. 24-291), Michigan DNR (2023 Consent Decree), Federal Register 88 FR 86,452.

---

## [2.1.0] — 2026-02-06

### Changed
- **WIPO Treaty ratification count**: Corrected from "4 ratifications (Malawi, Rwanda, Guinea, Uganda)" to "2 confirmed ratifications (Malawi, Uganda)" with 44 signatories. Rwanda and Guinea were signatories only, not ratified. 13 ratifications still needed for entry into force.
- **AI case law section**: Nuanced update reflecting split holdings:
  - *Bartz v. Anthropic*: Pirated-copy training = "inherently, irredeemably infringing"; lawfully-purchased training = fair use. $1.5B settlement pending final approval (April 2026 fairness hearing).
  - *Thomson Reuters v. Ross*: Third Circuit granted review (June 2025) — first appellate AI copyright case, pending as of Feb 2026.
  - *Kadrey v. Meta*: Narrow fair use finding even for pirated copies (weak plaintiff evidence); Judge Chhabria cautioned "in most cases" training is likely infringing.
  - Added reference to TRAIN Act (bipartisan, introduced January 2026).
- **DOJ/Castro-Huerta language**: Corrected "DOJ's 2024-2025 suits against Oklahoma DAs for sovereignty violations" to "DOJ's 2024-2025 government-to-government consultations on legislative proposals to restore tribal jurisdictional authority." No comprehensive legislation enacted as of Feb 2026.
- **Treaty rights framing**: Strengthened to pre-constitutional inherent sovereignty position. Treaties codify pre-existing rights, not grants.
- **Beaver Island Band framework**: Refined to treaty successor model — BIB treaty rights as source of authority, GTBOCI enrollment as practical enforcement vehicle.
- **Anishinaabemowin orthography**: Standardized across all documents per Fiero double-vowel system. "Aamik'Waakanda" / "Aamikwakaanda" replaced with proper Anishinaabemowin compound.

### Added
- *Flying T Ranch, Inc. v. Stillaguamish Tribe* (Wash. 2025) — tribal sovereign immunity bars in rem proceedings
- *Martorello v. Williams* (cert petition 25-829) — Indian Commerce Clause preemption pending
- TRAIN Act reference (Transparency and Responsibility for AI Networks Act, January 2026)
- llms.txt knowledge base: llms.txt, PRD.md, RULES.md, TODO.md, CHANGELOG.md, LEGAL-CITATIONS.md, DOCUMENT-MAP.md, DECISIONS.md

### Fixed
- README.md reference to nonexistent LICENSE_IMPROVEMENT_PLAN.md
- 25 CFR Part 83 effective date (delayed from Feb 14 to March 21, 2025)
- Section cross-reference audit

---

## [2.0.0] — 2026-01-13

### Added
- Terms-of-Service.md v2.0
- Privacy-Policy.md v2.0
- Comprehensive AI Training Data Restrictions with graduated liquidated damages (5 tiers)
- Multi-theory legal basis for AI prohibition (9 independent theories)
- EU AI Act compliance section (Section 7.8)
- Synthetic media / deepfake protections (Section 7.9)
- Cognitive sovereignty and neuro-rights (Section 7.7)
- Biometric data protections (aligned with Illinois BIPA)
- Emerging technology restrictions with beneficial use exceptions (Section 7.5)
- State-specific preemption analysis (MI, CA, NY, DE, TX, WA, IL)
- Enhanced WIPO Treaty compliance section
- Beaver Island Band recognition, unceded treaty rights, and legal capacity framework
- Treaty territory boundaries and geographic scope
- Hierarchical legal capacity and enforcement structure
- Cultural harm methodology and damages framework
- Revenue-based scaling multipliers for AI violations
- Cultural harm multipliers for sacred content

### Changed
- Major structural overhaul of license framework
- Expanded from basic license to comprehensive treaty-rights-based IP protection instrument

---

## [1.0.0] — 2025-10-28

### Added
- Initial working-LICENSE draft
- Basic copyright and attribution provisions
- Initial AI training prohibition
- CONTRIBUTING.md (CLA)
- README.md with citation block

### Notes
- Backup preserved as `working-LICENSE.10282025.backup`

---

## [1.0.1] — 2025-10-29

### Changed
- Minor corrections to initial draft

### Notes
- Backup preserved as `working-LICENSE.10292025.backup`

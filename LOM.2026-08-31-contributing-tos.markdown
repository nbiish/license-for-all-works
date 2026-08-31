# LOM — Log of Messages: License v3.0.0 → CONTRIBUTING.md / Terms-of-Service.md handoff

> **Purpose.** This is the **log of messages** / context-handoff note for the NEXT conversation.
> It captures (a) the final state of this session's license work (v3.0.0, merged + promoted),
> (b) the **verified law** from the research tracks so nothing needs re-deriving, and (c) the
> concrete, stale gaps in `CONTRIBUTING.md` and `Terms-of-Service.md` that the next agent must fix.
> The companion **agent TASK file** is `.agents/tasks/TASK.2026-08-31-contributing-tos.md`; this
> note is the *knowledge* layer, that file is the *work* layer.

## 1. Session outcome (what is now true in the repo)

- **`main`** is at `e562ba1`. `LICENSE` = `working-LICENSE` = **v3.0.0** (byte-identical, checksum
  verified), back up of prior v2.2.0 at `LICENSE.08312026.backup` (gitignored, local only).
- **v3.0.0** (`75831db`) merged from `docs/license-v3-structure`; then promoted
  (`9cf4eb5`); then COMMS `checkout` logged (`e562ba1`). Worktree + branch cleaned up.
- Prior **v2.2.0** (`04d32ef`) contained the treaty-record precision + AI case-law + international
  instruments work. That made the LICENSE; v3.0.0 restructured its numbering/index.

## 2. The doc hierarchy (must not be inverted)

```
LICENSE (governing instrument — v3.0.0)
├── CONTRIBUTING.md  (CLA — subordinate to LICENSE)   ← STALE, needs sync
├── Terms-of-Service.md (implements LICENSE for services) ← mostly current, verify
├── Privacy-Policy.md (implements LICENSE for data)
├── Tribal-Consulting-Agreement.md (template)
└── critical.md (sync standards)
```

`CONTRIBUTING.md` and `Terms-of-Service.md` are **subordinate mirrors**. Do NOT move substantive
law out of `LICENSE` into them; they must stay consistent *with* LICENSE, not replace it.

## 3. VERIFIED LAW — carry these, cite them, do not re-derive

### Constitutional supremacy + treaty-as-supreme-law
- **U.S. Const. art. VI, cl. 2** (Supremacy Clause) — federal law (incl. federal Indian law) = "supreme Law of the Land."
- Indian treaties are **self-executing** (cf. *Worcester*), which distinguishes them from the
  non-self-executing treaty in *Medellín v. Texas* (552 U.S. 491 (2007)). Do NOT conflate.
- **Reserved-rights doctrine:** *United States v. Winans*, 198 U.S. 371 (1905) ("a reservation of
  those not granted"); *Winters v. United States*, 207 U.S. 564 (1908).
- **Supremacy line added in v2.2.0:** *Foster & Elam v. Neilson*, 27 U.S. (2 Pet.) 253 (1829);
  *Head Money Cases*, 112 U.S. 580 (1884); *Whitney v. Robertson*, 124 U.S. 190 (1888);
  *Missouri v. Holland*, 252 U.S. 416 (1920).
- **Foundational:** *Worcester v. Georgia*, **31 U.S. (6 Pet.) 515 (1832)** — state law inapplicable
  to tribal matters. **The year is 1832 — NOT 1831.** (CONTRIBUTING.md:35 still says 1831 — fix.)

### Beaver Island Band (Kinawaba descendant line) — treaty record
- **1836 Treaty of Washington** = 7 Stat. 491. BIB named **beneficiary** (Art. 3) + payment schedule
  "Kainwaybekis and Pazhikwaywitum of Beaver islands" (Art. 10).
- **1855 Treaty of Detroit** = 11 Stat. 621. BIB named beneficiary "For the Beaver Island Band—High
  Island, and Garden Island" (Art. 1, third).
- **"Kain-waw-be-kiss-se"** signed the **July 2, 1856 Little Traverse assent** — the only
  treaty-instrument signature in the Kinawaba name family.
- **Rights Holder** = ᓂᐲᔥ ᐙᐸᓂᒥᑮ-ᑭᓇᐙᐸᑭᓯ (Nbiish Waabanimikii-Kinawaabakizi) = JUSTIN PAUL
  KENWABIKISE, Anishinaabek Dodem Animikii (Thunder), enrolled GTBOCI, descendant of Chief
  Kinwaabakizi.
- **CRITICAL reframe:** the Band is a **named beneficiary and a descendant line** — it was NEVER a
  signatory-entity to either treaty (the Nations signed via chiefs). The 1855 treaty did NOT "affirm
  the continuing government-to-government relationship": Art. 5 **dissolved** tribal organization and
  Art. 3 released prior liabilities. Continuity rests instead on:
  - congressional successor findings: **Pub. L. 103-324 (1994)**;
  - **25 U.S.C. § 1300k-2** (LTBB service area keyed to the Beaver Island Band paragraph);
  - **GTB v. U.S. Attorney** (W.D. Mich. 2002) (relationship 1795–1872, improperly severed by Delano);
  - **inherent sovereignty** per *Santa Clara Pueblo v. Martinez*, 436 U.S. 49 (1978);
  - and the 1937 U.S. Solicitor Opinion refused band status on dissolution + completed allotment —
    that negative must be **addressed, not hidden**.

### Federal Indian law / canons / statutes
- **Indian canons of construction** — treaties construed liberally in favor of the tribe; ambiguities
  resolved in favor of tribal sovereignty (*Dion*, 476 U.S. 734 (1986) clear-statement rule).
- **Indian Arts and Crafts Act (IACA)**, 25 U.S.C. § 305 (and IACA § 305e).
- **NAGPRA 2024 rule** — 88 FR 86,452 (deference to tribal/Indigenous meaning).
- **Civil jurisdiction preserved post-Castro-Huerta:** *Oklahoma v. Castro-Huerta*, 597 U.S. 629 (2022)
  addressed **criminal** jurisdiction only; the license governs **civil** IP and stays under
  *Montana v. United States* (450 U.S. 544 (1981)) / *Williams v. Lee* (358 U.S. 217 (1959)).
- **Federal jurisdiction / removal:** 28 U.S.C. § 1441; tribal sovereign immunity
  (*Michigan v. Bay Mills*, 572 U.S. 782 (2014); *Flying T Ranch v. Stillaguamish* (Wash. 2025)).

### Pushing-precedent honesty (the "untreated frontier")
No U.S. court has yet applied treaty-reservation doctrine to **intangible** TK/TCE. The license builds
the claim from the **usufructuary** line — *Winans*, *Minnesota v. Mille Lacs Band of Chippewa Indians*
(526 U.S. 172 (1999)), *United States v. Michigan*, and the **2023 Great Lakes Consent Decree**
(through 2047) — plus NAGPRA 2024 deference, IACA, Indian canons, *Dion*. **Keep this candid framing**;
do not overstate that a court has already accepted the treaty-reservation-for-intangibles theory.

### AI-copyright status (Aug-2026) — for the IP + technology sections
- *Bartz v. Anthropic* — final approval **July 20, 2026** + appeals pending. Split holding: pirated-copy
  training = "inherently, irredeemably infringing"; lawfully-purchased training = fair use.
- *Thomson Reuters v. Ross* — argued **June 11, 2026**, 3d Cir. **No. 25-2153**; **D. Del.** at trial.
- *Kadrey v. Meta* — interlocutory review denied **July 8, 2026**; narrow fair-use finding.
- *Cox Communications v. Sony Music* — **U.S., Mar. 25, 2026** (unanimous): contributory infringement
  requires proof of intent → license architecture rests on **direct infringement + contract + statute**.
- *Sony Music v. Anthropic* — Aug. 2026.
- TRAIN Act — **no action** (S. 2455 introduced July 2025). TAKE IT DOWN Act Pub. L. No. 119-22
  (48-hour platform takedown; FTC enforcement 2026); NO FAKES Act S. 4591 (pending).

### Works-type coverage (protect ALL works per operator priority)
- **Art / visual** — 17 U.S.C. § 106A (VARA).
- **3D designs/models** — 17 U.S.C. § 102(a)(5), § 1201 (DMCA) for model files; STL-sidecar/3MF/glTF metadata.
- **Software** — 17 U.S.C. § 102(a)(1).
- **Social-media content** — 17 U.S.C. § 512; TAKE IT DOWN Act.

### Machine-readable notice / opt-outs (scalable enforcement)
- TDMRep (W3C CG); robots.txt (RFC 9309); ai.txt; Have-I-Been-Trained.
- **TK Labels** (Local Contexts). SPDX `LicenseRef-Commercial-Restricted-Use-License-BeaverIsland`;
  schema.org properties. Absence-does-not-waive + presence-supports-willfulness (LICENSE §3A.2).

### International instruments (backing)
- **UNDRIP** Arts. 11, 31, 37, 8(2) — U.S. endorsed **Dec. 16, 2010**.
- **WIPO GRATK Treaty** (adopted May 2024): 3 deposited (Malawi, Uganda, Albania); **Peru ratified
  Jul. 8, 2026** (deposit pending); 15 needed (Art. 17). Arts. 3, 5, 7.
- **ILO Convention 169** Arts. 2, 15, 23. **Nagoya Protocol** Arts. 5, 7, 12 (CBD).
- **⚠ DO NOT cite UNESCO 2003 Intangible Cultural Heritage Convention as a U.S. obligation.** Verified
  FALSE: the U.S. is NOT a party to the 2003 ICH Convention (it rejoined UNESCO 2023 but only ratified
  the 1970 Convention). This was removed from LICENSE; leave it out.

## 4. CONCRETE STALE GAPS to fix (the actual next-work slate)

### CONTRIBUTING.md (STALE — must change)
| Line | Current (stale) | Fix to (verified) |
|------|-----------------|-------------------|
| ~~35~~ | *Worcester* 31 U.S. 515 **(1831)** | **(1832)** |
| ~~47~~ | 1855 "affirming continuing government-to-government relationship" | **Reframe** to beneficiary/named-chief/successor; add Art. 5 dissolution recital + Art. 3 release; Pub. L. 103-324; 25 U.S.C. § 1300k-2; *GTB v. U.S. Attorney* |
| §1.2 case list | missing *Foster/Head Money/Whitney/Holland* | add supremacy line + *Medellín* distinguished + *Winans* |
| §1.4 international | — | add WIPO GRATK deposit status; UNDRIP 37/8(2); **ensure UNESCO 2003 ICH absent** |
| §6/§7 IP + tech | — | mirror v3.0.0 re-homed §11.x/§12.8 refs + §3A works-type matrix + §3A.2 notice opt-outs |
| cross-refs | — | audit every "LICENSE § N[.X]" against v3.0.0 (use `tools/v3_verify.py`) |

### Terms-of-Service.md (verify; mostly current — several already correct)
- §2.2 Governing Law / §2.7 Applicable Case Law — *Worcester* already **(1832)** ✓; *Williams v. Lee* ✓;
  add supremacy line + treaty-reservation + candid "untreated frontier" framing (do not overstate).
- §7 IP Rights — mirror works-type coverage (art/3D/software/social) + machine-readable opt-outs.
- §8 Indigenous Data Sovereignty / CARE — align with LICENSE §4.x (CARE + data governance + breach
  protocol); add NAGPRA 2024 + IACA if absent.
- Cross-reference audit against v3.0.0.

## 5. Versioning / next-step target
Per `llms.txt/PRD.md` versioning (Minor = case-law/citation correction, language refinement),
target **v3.1.0** for this sync. Update `llms.txt/PRD.md` (version → 3.1.0), `llms.txt/TODO.md`,
`llms.txt/CHANGELOG.md` (+v3.1.0 entry), `llms.txt/DECISIONS.md`, `llms.txt/LEGAL-CITATIONS.md`,
`llms.txt/DOCUMENT-MAP.md` (version rows for CONTRIBUTING.md/Terms-of-Service.md).

## 6. Workflow / gates (do not skip)
- Worktree gate first — never edit on `main`. Branch `docs/contributing-tos-sync`, worktree
  `../license-contrib-tos`.
- Read `AGENTS/{date}.COMMS.md` + `.agents/tasks/` + `llms.txt/llms.txt` (PRD anchor) at start.
- One task = one worktree. Verify, then **ask before merging** to main.
- Post-merge cleanup mandatory (remove worktree, delete branch, verify clean).
- `LICENSE` content should NOT change for a sync; CONTRIBUTING.md + ToS are subordinate mirrors.
- No renumbering of LICENSE Article/§ numbers.

## 7. Sources consulted (this session)
Research tracks: Kappler/OSU Tribal Treaties Database + NARA digi-treaties + 1937 U.S. Solicitor
Opinion I:747-48 + *GTB v. U.S. Attorney* (2002) + 25 U.S.C. § 1300k-2 + Pub. L. 103-324; Aug-2026
AI litigation dockets (3d Cir. No. 25-2153; N.D. Cal.; SCOTUS No. 24-291; *Cox* U.S. 2026);
WIPO Lex (GRATK); Michigan DNR 2023 Great Lakes Consent Decree; Federal Register 88 FR 86,452;
UNDRIP / ILO 169 / Nagoya Protocol texts.

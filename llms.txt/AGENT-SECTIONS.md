# Agent Sections — Sectioned Work Breakdown and Verification Protocol

> DOX child of `llms.txt/llms.txt`. Defines how agent work on this repository is split into
> sections (lanes), what each lane owns, and how online/factual content is verified.
> Created 2026-11-22 (v3.2.0 planning). One writer per lane at a time; lanes may run in
> parallel only where their file scopes do not overlap.

## Purpose

The corpus (LICENSE 459K + subordinate instruments) is too large for one agent pass and its
factual claims drift stale. This document (1) splits the work into numbered sections with
owning agent lanes so any agent can pick up exactly one section, and (2) mandates online
fact verification so no unverified legal claim ships.

## Ownership

- Steward: Rights Holder (operator). Agents draft; the operator merges and signs.
- Verification ledger: `research/` (dated reports) + `llms.txt/LEGAL-CITATIONS.md` (index).

## Local Contracts

1. **One lane per mutation.** A lane may edit only the file scopes listed for its section.
   Cross-lane needs go through the sectioned plan (`.agents/plans/`).
2. **No unverified claim ships.** Every factual/legal assertion added or edited must carry a
   source (URL or primary cite) and a retrieval date in the section's verification entry, or
   be explicitly marked `UNVERIFIED` in `research/` and the text must say so.
3. **Verification statuses** (used in the table below and in every research report):
   - `VERIFIED-YYYY-MM-DD` — claim checked against a live source on that date.
   - `STALE` — verified earlier than 90 days and the claim is time-sensitive (case status,
     ratification counts, effective dates, pending legislation).
   - `UNVERIFIED` — no live source; must not be presented as fact in operative text.
4. **Time-sensitive claims re-verify at least quarterly** and before every version bump.
   Automation (`tools/trigger_enforcement.py` monitors + Hermes cron `license-fact-monitor`)
   watches the watch-list in `research/2026-11-22-factual-verification.md` and reports drift.
5. **Promotion gate:** `working-LICENSE` → `LICENSE` only after (a) `python3 tools/v3_verify.py
   working-LICENSE` passes, (b) the verification ledger is updated, (c) the operator reviews.

## Work Sections and Lanes

| Section | Scope (files / license areas) | Owning lane | Verification requirement | Status |
|---|---|---|---|---|
| S1 Legal Foundation | working-LICENSE treaty/supremacy/federal-Indian-law blocks (preamble; § 5A; supremacy case line; 1836/1855 treaty record); `research/precedent-brief-treaty-ip-supreme-law.md` | Lane Treaty | Every case/statute cite checked against court/USCode source; treaty text against Kappler/NARA | VERIFIED-2026-08-31 → re-verify 2026-11-22 (report `research/2026-11-22-factual-verification.md`) |
| S2 License Terms | working-LICENSE definitions (§ 1), grants/restrictions (§ 3/3A), notices/metadata (§ 3A.2), works matrix | Lane License | Cross-ref integrity via `tools/v3_verify.py`; cite checks for statutes referenced (VARA, § 113, DMCA, § 512) | structural VERIFIED-2026-08-31 |
| S3 Trust & Financial Architecture | § 6A benefit-sharing, § 9A financial institution/living trust, § 10.2/10.2A/10.3 Legacy Trust + lifetime-trust amendments, § 13.7 | Lane Trust-Wealth | Every trust/tax mechanism carries verified legal basis (statute/rev-proc/ruling/case + URL); treaty-trust analogues verified | AMENDING 2026-11-22 (research/2026-11-22-trust-mechanisms.md) |
| S4 Enforcement & Dispute Resolution | § 11 jurisdiction/forum/exhaustion, § 12 enforcement incl. § 12.3 UNCITRAL, § 12.4, § 13 violations & damages; `tools/trigger_enforcement.py`, `templates/` | Lane Enforcement | Arbitration/immunity/jurisdiction cites verified (cases + rules pages); trigger clocks match § 13 cure tiers | AMENDING 2026-11-22 (research/2026-11-22-arbitration-architecture.md) |
| S5 Data Sovereignty & AI | § 4 data governance, § 7 AI prohibitions/damages, § 7.8/7.9, TK Labels/TDMRep/ai.txt/SPDX metadata | Lane Data-AI | AI-litigation and statute status (Bartz, Thomson Reuters, Kadrey, NO FAKES, TAKE IT DOWN) re-verified each version bump | VERIFIED-2026-08-31 → STALE, refreshed 2026-11-22 |
| S6 Subordinate Instruments | CONTRIBUTING.md (CLA), Terms-of-Service.md, Privacy-Policy.md, Tribal-Consulting-Agreement.md | Lane Sync | Any cite changed in working-LICENSE must be mirrored per `critical.md` sync chain; verified by diff of citation lists | synced 2026-08-31 |
| S7 Research & Fact Verification | `research/*`, `llms.txt/LEGAL-CITATIONS.md`, this protocol | Lane Verify | Owns the verification ledger; every report dated and source-linked; watch-list maintained | active 2026-11-22 |
| S8 Automation & Tooling | `tools/*`, `templates/*`, Hermes cron monitors (`license-fact-monitor`, `uhnw-wealth-intel`) | Lane Automation | Tools deterministic (no network, no LLM in decision path); golden-run output inspected each change | built 2026-11-22 |
| S9 Sovereignty & Governance | Beaver-Island-Band-Founding-Charter.md, LETTER OF INTENT (25 CFR 83), `roadmap/tribal-roadmap.md` | Lane Sovereignty | Regulatory cites checked against eCFR/BIA; acknowledgment criteria tracked against 25 CFR 83 status | petition pending |
| S10 Wealth Intelligence Ops | `~/.hermes/profiles/too-wealthy-financial-expert/` (SOUL.md panel, skills, cron), its research brief | Lane Wealth | Persona claims grounded in verified wealth-preservation research (`research/2026-11-22-uhnw-wealth-brief.md`); cron keeps briefs current | built 2026-11-22 |

### Lane definitions

- **Lane Treaty** — treaty record, federal Indian law, supremacy. Never edits financial or
  tooling scopes.
- **Lane License** — operative license terms, definitions, cross-references.
- **Lane Trust-Wealth** — trust instruments, benefit-sharing, secured-income architecture.
- **Lane Enforcement** — disputes, arbitration, damages, trigger automation.
- **Lane Data-AI** — data sovereignty, AI restrictions, machine-readable notices.
- **Lane Sync** — subordinate instruments and the critical.md synchronization chain.
- **Lane Verify** — online fact verification and the citation ledger. Read on every lane's
  behalf; write only in `research/` and `LEGAL-CITATIONS.md`.
- **Lane Automation** — deterministic tooling and monitors.
- **Lane Sovereignty** — tribal governance documents and federal acknowledgment track.
- **Lane Wealth** — the `too-wealthy-financial-expert` Hermes profile and UHNW intel.

## Work Guidance

- Pick ONE section per task record; state the lane in the plan frontmatter.
- A section task ends with: (1) edits, (2) verification entries added/updated, (3) DOX sync
  for touched docs, (4) `v3_verify.py` run when working-LICENSE changed.
- When a lane needs another lane's scope, record a suggestion in
  `.agents/suggestions/{date}-{HH}-{slug}.md` instead of editing across the boundary.

## Verification

- `python3 tools/v3_verify.py working-LICENSE [--strict]` — reference integrity (S2 gate).
- `python3 tools/trigger_enforcement.py tests/sample-trigger.json` — golden packet run (S4 gate).
- Hermes probe for the wealth profile (S10 gate), per `hermes-profile-personas` skill.
- Verification ledger freshness: no `STALE` row at promotion time.

## Child DOX Index

None — this is a leaf document. Domain detail lives in the research reports it references.

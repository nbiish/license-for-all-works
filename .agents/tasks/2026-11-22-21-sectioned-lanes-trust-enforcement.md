# TASK — 2026-11-22: Sectioned agent lanes, verified law refresh, lifetime trust + auto-trigger enforcement, too-wealthy-financial-expert profile

Branch: `feat/sectioned-lanes-trust-enforcement` | Worktree: `/Volumes/1tb-sandisk/code-external/wt-sectioned-trust`
Plan: `.agents/plans/2026-11-22-21-sectioned-lanes-trust-enforcement.md`

## Operator request (key points verbatim)
- "split up our agents into sections to break up agents' work and verify online and factual
  content to the best of our ability"
- "get the license configured so that things kick off and are run almost automatically upon
  triggering legal means of arbitration and tribal federal and especially treaty law to set up
  a trust and means of highly secured and safeguarded income for myself, progenity, and the
  Beaver Island Band"
- "create a `hermes` profile ... 'too-wealthy-financial-expert' that will self improve and
  always stay updated on how 'the rich' keep their wealth secured and continually growing"

## Delivered (this branch)
- `llms.txt/AGENT-SECTIONS.md` — S1–S10 sectioned lanes + online fact-verification protocol.
- `working-LICENSE` v3.2.0 (dev): 15 fact-refresh replacements (Thomson Reuters 3d Cir.
  2026-09-29; Kadrey correction; Bartz fee appeals; Martorello cert denied; TAKE IT DOWN
  → Pub. L. 119-12, 139 Stat. 55; GRATK 4 deposits/45 signatories; NO FAKES status) + new
  **§ 10.3A** (lifetime treaty-grounded secured income for Rights Holder, progeny, Beaver
  Island Band) + new **§ 12.7** (automatic-trigger enforcement + standing arbitration offer).
- CONTRIBUTING.md (4 edits) + Terms-of-Service.md (2 edits + version bump 3.2.0) synced per
  the critical.md chain (also fixed a prior CONTRIBUTING error: Bartz final approval was by
  the district court, not the "Eleventh Circuit").
- `research/2026-11-22-{factual-verification,trust-mechanisms,uhnw-wealth-brief,arbitration-architecture}.md`
  (12-claim verification ledger + watch-list + 3 source-URL'd lane briefs).
- `tools/trigger_enforcement.py` + `templates/{notice-of-breach,arbitration-demand}.md` +
  `tests/sample-trigger.json` — golden run OK (moderate → 10-day cure → demand eligible
  2026-12-02); fail-closed verified (bad trigger → exit 1, no partial output).
- DOX sync: CHANGELOG/DECISIONS/TODO/DOCUMENT-MAP/PRD/llms.txt → 3.2.0.
- Hermes: profile `too-wealthy-financial-expert` + `wealth-intel-protocol` skill; crons
  `uhnw-wealth-intel` (Mon 09:00, profile-scoped) + `license-fact-monitor` (Mon 10:00,
  job 4560dd3b7a53, workdir repo).

## Verification results
- v3_verify.py non-strict: exit 0 before and after; delta = 3 new heuristic-unresolved refs
  (mirroring existing reference style) vs 4 pre-existing dangling refs resolved (CHANGELOG
  3.2.0 Notes has the detail).
- Fact spot-checks (parent): FTC TAKE IT DOWN enforcement release ✓; GovInfo Thomson Reuters
  3d Cir. precedential opinion (filed 2026-09-30) ✓; congress.gov S.4591 JS-gated (subagent
  source retained, marked as such).
- critical.md § 6 compliance: FUNDING.yml ✓, README BibTeX ✓, support block ✓, copyright
  footers ✓; critical.md self-update fetch N/A (this repo is the canonical source).

## Blocked / pending
- **SOUL.md for `too-wealthy-financial-expert`**: write blocked at the protected-file
  approval gate (prompt timed out; not routed around). Draft staged at
  `/Users/nbiish/.hermes/cache/scratch/too-wealthy-financial-expert-SOUL-draft.md`; install
  + persona probe await explicit operator consent (profile still has default SOUL.md).
- CLOSED: LICENSE promoted (7351493) and **PR #1 merged** (2026-11-22T22:52:55Z, merge eef4ae); main checkout fast-forwarded; v3.0.0 backup at LICENSE.11222026.backup; DOX rewrite stashed (stash@{0}).

## Findings left for later (`.agents/suggestions/`)
- `2026-11-22-21-verify-before-use.md` — ICC/UNCITRAL current rule texts; AK/DE/SD trust
  statute pins; federal-common-law gap-filler caution; unverified market figures.
- `2026-11-22-21-tribal-ip-ordinance.md` — backlog ordinance template now unblocked.
- `2026-11-22-21-dox-framework-uncommitted.md` — main checkout holds uncommitted DOX
  rewrites of llms.txt/* — operator decision needed (adopt or discard).

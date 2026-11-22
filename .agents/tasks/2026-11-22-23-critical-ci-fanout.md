# TASK — 2026-11-22-23: critical.md 2.1.0, license CI, and OFSL/OCA fan-out deployment

Branch: `feat/critical-2.1.0-ci` | Worktree: `/Volumes/1tb-sandisk/code-external/wt-critical-ci`
Plan: `.agents/plans/2026-11-22-22-open-fair-share-license.md` (recommendations executed) +
this record.

## Operator direction (2026-11-22, second wave)
- Retry SOUL.md install (popup missed) — gate timed out again; operator to run the staged
  `cp` himself; panel probe follows.
- "update the critical.md that I copy from other repos to fully integrate everything we've
  updated so far"
- "Proceed with any recommendations you've made for the next call and merge all the content
  to main" → Exhibit A rate stays at draft default 10%; OFSL/OCA deployed to target repos;
  DOX stash stays dropped (archived at stash@{0} in main checkout).
- "update my CI workflow so that when I merge new PRs we do an automation to check for and
  integrate the latest license content"

## Delivered (this branch)
- critical.md **2.1.0**: OFSL/OCA in § 1.3 canonical fetch set + § 1.4 hierarchy; new § 7
  License Content Sync (CI) contract; § 6 compliance gains the workflow item.
- `.github/workflows/license-ci.yml`: on every PR/merge — v3_verify regression ceiling
  (AMBIGUOUS ≤ 60, DANGLING ≤ 96), trigger_enforcement golden + fail-closed negative,
  stale-fact guard (Pub. L. 119-22 / Kadrey mischaracterization / 3 deposits / 25 CFR 24 /
  Rev. Rul. 2005-44 must not reappear), OFSL incorporated-section checks, critical.md § 2–4
  compliance surface.
- `.github/workflows/license-sync.yml`: canonical template for consuming repos — on PR
  merge to main + weekly, fetches canonical critical.md/OFSL/OCA, opens integration PR on
  drift (repo-local GITHUB_TOKEN only; no cross-repo secrets).

## Fan-out deployment (separate commits per repo)
- nbiish-dot-me, ggufy-dot-com (off develop→main per its flow), in-digi-nous,
  learnsyllabics-dot-com, betterbrowsermcp: OFSL + OCA + license-sync.yml + README
  licensing pointer + critical.md refresh where already present — branch + PR + merge
  (operator pre-authorization: "merge all the content to main").
- goal-first-trillion: **local commit to main only** (GitHub remote intentionally empty —
  never push; private financial project).
- NOT done (flagged): critical.md § 2–4 README compliance surface (BibTeX citation,
  support block, FUNDING.yml) is unchanged in repos that lacked it — follow-up pass.

## Verification
- Workflow YAML lint clean (write_file lint); stale-fact patterns verified absent from
  working-LICENSE/CONTRIBUTING/ToS before guard thresholds set; per-repo read-back after
  fan-out (file presence + README pointer).

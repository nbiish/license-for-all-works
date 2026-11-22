---
plan_format: ainish/plan/v1
slug: sectioned-lanes-trust-enforcement
date: 2026-11-22
status: designing
branch: feat/sectioned-lanes-trust-enforcement
worktree: /Volumes/1tb-sandisk/code-external/wt-sectioned-trust
task_record: .agents/tasks/2026-11-22-21-sectioned-lanes-trust-enforcement.md
operator: Nbiish (Waabanimikii-Kinawaabakizi)
---

# Plan: Sectioned agent lanes, verified law refresh, lifetime trust + automatic-trigger enforcement, too-wealthy-financial-expert profile

<!-- Sections 1-4 and 7 are history once written. Section 5 is the only part edited in place. -->

## 1. Problem

The license-for-all-works corpus is monolithic (459K LICENSE, 81K CONTRIBUTING) and agents work it
all-at-once with no sectioned ownership and no systematic online fact verification, so legal/factual
claims drift stale (last verified Aug 31, 2026). The Legacy Trust (§ 10.3) is posthumous-first, so it
does not secure income for the Rights Holder, his progeny, or the Beaver Island Band during his
lifetime. Enforcement (§ 11–13, § 12.3 UNCITRAL) is reactive and manual; the operator wants disputes
to "kick off and run almost automatically" once a trigger occurs, grounded in tribal, federal, and
especially treaty law. Finally, there is no dedicated, self-updating wealth-preservation expertise
("too-wealthy-financial-expert") to keep the trust architecture aligned with how dynastic wealth is
actually secured and grown.

## 2. Anchor Facts

- Repo flow: `working-LICENSE` (dev head) → promote → `LICENSE`; sync chain enforced by
  `critical.md` § 1.3 (CONTRIBUTING, ToS, Privacy, Tribal-Consulting-Agreement) — established from
  `llms.txt/DOCUMENT-MAP.md`, `critical.md`.
- License already contains: § 10.3 Waabanimikii-Kinawaabakizi Legacy Trust (posthumous trigger),
  § 9A financial-architecture/institution transition, § 12.3 UNCITRAL arbitration (Geneva seat,
  PCA-appointed chair), § 11.1 tribal court primary + § 11.12 exhaustion, "Legacy Beneficiary"
  definitions — established from `working-LICENSE` grep (lines 1149–1206, 1786, 3026, 3160).
- Legal corpus last verified 2026-08-31 (v3.1.0: Worcester 1832, GRATK deposit count, Bartz/TR/Kadrey
  status, 25 CFR 83 date) — established from `llms.txt/TODO.md` v3.1.0 block.
- Prior tasks used a worktree + branch and asked the operator before merging to main — established
  from `.agents/tasks/TASK.2026-08-31.md` ("ask before merging to main").
- `tools/v3_verify.py` checks Section-N reference integrity of `working-LICENSE` — established from
  `tools/v3_verify.py` header.
- Hermes profile personas live at `~/.hermes/profiles/<name>/SOUL.md`, panel-of-experts pattern with
  9 principals and a mandatory live probe — established from skill
  `hermes-profile-personas` (SKILL.md + references/persona-rosters.md).
- critical.md compliance items (BibTeX citation, support block, FUNDING.yml, copyright notice) are
  mandatory and must be reported — established from `critical.md` § 6.

## 3. Plan

### Goals

- `llms.txt/AGENT-SECTIONS.md`: the license corpus split into numbered work sections, each with an
  owning agent lane, scope, verification requirement, and status — so future agents pick up one
  section at a time.
- `research/2026-11-22-factual-verification.md`: online-verified status table of every live factual
  claim in the corpus (GRATK, AI case law, 25 CFR 83, statutes), with source URL + date; changed
  facts patched into `working-LICENSE` and the critical.md sync chain.
- Lifetime-trust amendment path: new provisions establishing the Trust during the Rights Holder's
  lifetime as the secured-income vehicle for him, his progeny, and the Beaver Island Band, grounded
  in verified treaty/federal-Indian-law mechanisms (research lane B).
- Automatic-trigger enforcement architecture: `tools/trigger_enforcement.py` (deterministic trigger
  intake → notice/cure clock → arbitration demand packet generation from a template) plus a Hermes
  cron monitor; license-side trigger clause aligned with verified arbitration law (research lane D).
- Hermes profile `too-wealthy-financial-expert` (`~/.hermes/profiles/too-wealthy-financial-expert/`):
  9-principal SOUL.md panel grounded in verified wealth-preservation curricula (research lane C),
  a self-improvement research skill, and a recurring intel cron so it stays current.
- DOX sync (CHANGELOG, DECISIONS, TODO, DOCUMENT-MAP, PRD version → 3.2.0) and `.agents/` close
  records (task record, COMMS ledger, memory scrub, suggestions).

### Non-goals

- Full license renumbering (v3.0.0 backlog item) — separate iteration, keeps diffs reviewable.
- Executing any real trust, arbitration, or financial instrument — drafting/research only; licensed
  counsel and the operator execute. No money moves, no filings made.
- Rewriting CONTRIBUTING/ToS/Privacy wholesale — only citation-sync of changed facts per critical.md.

### Constraints and invariants

- Plan first, worktree off `main`, delivery by PR; never self-merge; operator is sole commit author.
- No fabricated citations: every legal claim carries a verified source or is explicitly marked
  unverified in the verification report.
- critical.md § 1.2 self-update + § 6 compliance report before finishing.
- `tools/v3_verify.py` must pass on `working-LICENSE` after edits (pre-existing failures recorded).
- Secrets never in files/argv/logs; nothing irreversible without the operator's word.
- English-only output; Anishinaabemowin orthography standards per `llms.txt/RULES.md` unchanged.

### Proposed architecture

```
research lanes (4, parallel)          deliverables
  A fact-status verification  ──────▶ research/2026-11-22-factual-verification.md
  B treaty/federal trust law  ──────▶ research/2026-11-22-trust-mechanisms.md
  C UHNW wealth preservation  ──────▶ research/2026-11-22-uhnw-wealth-brief.md  ──▶ profile SOUL.md
  D arbitration/auto-trigger  ──────▶ research/2026-11-22-arbitration-architecture.md ──▶ tools/

llms.txt/AGENT-SECTIONS.md  = work breakdown: sections S1..S7 → lane → verification status
tools/trigger_enforcement.py = deterministic: trigger intake → clocks → demand packet (templates/)
hermes cron (monitor)        = recurring fact re-verification + trigger inbox scan
~/.hermes/profiles/too-wealthy-financial-expert/ = SOUL.md + skills + cron (self-updating)
```

### Interfaces and data

- `llms.txt/AGENT-SECTIONS.md` — new DOX child; registers in `DOCUMENT-MAP.md`.
- `working-LICENSE` — additive sections only (lifetime trust clause; auto-trigger enforcement
  clause; treaty-trust grounding); version bump 3.2.0; then promote to `LICENSE` after operator
  review (previous task asked before merging; same here).
- `tools/trigger_enforcement.py <trigger.json>` → writes `out/<case-id>/{notice,demand}.md`;
  deterministic template fill, no network.
- `templates/arbitration-demand.md`, `templates/notice-of-breach.md` — packet templates.
- Hermes: profile dir `~/.hermes/profiles/too-wealthy-financial-expert/{SOUL.md,skills/,memories/}`;
  cron job `uhnw-wealth-intel` (weekly) + `license-fact-monitor` (weekly) via cronjob_manage.

## 4. Risks and unknowns

- Research lanes may return unverifiable items — they are recorded as such, never papered over.
- 459K LICENSE is machine-checked only for xref integrity; legal quality of new clauses rests on the
  verified research and is flagged for operator/counsel review before promotion.
- Hermes named profiles were deleted in the 2026-11-04 federation reset; creating one now is an
  explicit operator request and is scoped to this machine's `~/.hermes/profiles/`.
- Cron-created jobs run under this profile's runtime; if cronjob_manage is unavailable, the monitor
  is shipped as a documented script and the gap is reported.

## 5. Progress

- [x] Plan written; research lanes dispatched (A fact-status, B trust law, C UHNW, D arbitration)
- [x] Worktree + branch created off latest origin/main
- [x] AGENT-SECTIONS.md work breakdown written (S1–S7 lanes + verification protocol)
- [x] research/2026-11-22-*: verification report + trust mechanisms + UHNW brief + arbitration arch
- [x] working-LICENSE additive amendments (lifetime trust, auto-trigger enforcement, treaty trust)
- [x] tools/trigger_enforcement.py + templates + verified run producing sample packet
- [~] Hermes profile too-wealthy-financial-expert — profile + skill + cron DONE; SOUL.md BLOCKED at protected-file approval (draft staged); probe pending
- [x] DOX sync: CHANGELOG/DECISIONS/TODO/DOCUMENT-MAP/PRD → 3.2.0
- [x] v3_verify.py run on working-LICENSE (result recorded)
- [x] critical.md compliance report; branch pushed; PR #1 opened and merged (2026-11-22)

## 6. Test and verification plan

- `python3 tools/v3_verify.py working-LICENSE` — reference integrity before/after.
- `python3 tools/trigger_enforcement.py <sample-trigger.json>` — golden packet output inspected.
- `hermes -p too-wealthy-financial-expert chat -q "..."` probe (540s timeout) per persona skill.
- Every research claim in new docs carries a source URL; spot-check 5 claims via web_extract.
- critical.md § 6 compliance checklist reported in final summary.

## 7. History

- 2026-11-22 created (status: designing).

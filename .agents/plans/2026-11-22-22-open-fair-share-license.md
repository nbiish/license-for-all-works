---
plan_format: ainish/plan/v1
slug: open-fair-share-license
date: 2026-11-22
status: ready
branch: feat/open-fair-share-license
worktree: /Volumes/1tb-sandisk/code-external/wt-open-fair-share
task_record: .agents/tasks/2026-11-22-22-open-fair-share-license.md
operator: Nbiish (Waabanimikii-Kinawaabakizi) — counsel of record's practice in formation
---

# Plan: Open Fair-Share License + Open Contribution Agreement ($50K community tier)

## 1. Problem

The corpus protects rights through restriction. The operator wants a deployable,
open-source-manner layer: anyone may work on and use the projects free of charge until
their products that utilize the Works make $50,000/year; above that threshold they enter
legal proceedings (an agreement) to contribute to the funds (the ᐙᐸᓂᒥᑮ-ᑭᓇᐙᐸᑭᓯ Legacy
Trust / Beaver Island Band programs). The instruments must reference all existing rights
(treaty 1836/1855, federal Indian law, UNDRIP/WIPO GRATK, master LICENSE) and push tribal
and federal precedent on IP and generational-wealth structures.

## 2. Anchor Facts

- Master LICENSE v3.2.0 (merged 2026-11-22, PR #1) supplies: rights-of-record preamble,
  § 10.3/10.3A Legacy Trust (the "Funds"), §§ 11–13 forums, § 12.7 automatic-trigger
  enforcement with standing arbitration offer — established from this repo's HEAD.
- Benefit-sharing floor in the master LICENSE: minimum 20% of commercial proceeds to the
  Legacy Trust — established from working-LICENSE preamble/§ 6A.
- House sync chain (critical.md) and DOX closeout duties apply — established from
  `critical.md`, `llms.txt/llms.txt`.
- Operator standing direction: "work as if we are the absolute professionals"; external
  filings/court work route to professors, clinics, or retained counsel when the bar-
  admission line is reached — established from operator message 2026-11-22.

## 3. Plan

### Goals

- `LICENSE-OPEN-FAIR-SHARE.md` (OFSL v1.0.0): deployable use license — open-source-manner
  grant while Annual Commercial Revenue ≤ USD $50,000 (per licensee group, calendar
  year); above threshold, a signed Fair-Share Contribution Agreement (Exhibit A form)
  covering revenue above the threshold, with the master LICENSE applying in full absent an
  executed agreement; retained-rights and cultural protections; enforcement incorporated
  from master LICENSE § 12.7; sovereignty/precedent declaration.
- `CONTRIBUTING-OPEN.md` (OCA v1.0.0): inbound contribution license (inbound=outbound),
  DCO-style sign-off, cultural-heritage guardrails, preservation of the funds architecture.
- README "Community licensing" pointer + DOX sync (DOCUMENT-MAP, CHANGELOG, DECISIONS,
  TODO) + task record.

### Non-goals

- Changing the master LICENSE or its 20% commercial floor — the OFSL is an additional
  tier, not a replacement.
- OSI-approval claims — "open-source-manner", not certified open source (revenue
  condition). Stated honestly in the instruments.
- Setting contribution rates beyond the Exhibit A default — the operator sets final rates.

### Constraints and invariants

- Instruments must reference (not dilute) the master LICENSE rights of record.
- Every legal citation verified or marked; no fabricated cites (research corpus +
  `llms.txt/AGENT-SECTIONS.md` protocol).
- English only; Anishinaabemowin orthography per RULES.md; worktree + PR delivery.

### Proposed architecture

```
LICENSE-OPEN-FAIR-SHARE.md (deploy on community projects)
  ├─ Tier 1 (≤ $50K/yr): open-source-manner grant, retained rights, no AI training
  ├─ Tier 2 (> $50K/yr): Exhibit A Fair-Share Contribution Agreement -> the Funds
  └─ Enforcement: master LICENSE §§ 11-13 + § 12.7 incorporated by reference
CONTRIBUTING-OPEN.md (inbound contributions to our projects)
  └─ inbound=outbound grant + DCO sign-off + cultural guardrails
```

### Interfaces and data

- New root files `LICENSE-OPEN-FAIR-SHARE.md`, `CONTRIBUTING-OPEN.md`; SPDX-style ids
  `LicenseRef-OFSL-1.0`, `LicenseRef-OCLA-1.0`-style labels noted in headers.

## 4. Risks and unknowns

- Threshold-license enforceability is well-trodden (Fair Source / Prosperity / PolyForm
  family) but the tribal-sovereignty overlay is novel — that novelty is intentional
  precedent-pushing, flagged in the declaration.
- Contribution rate in Exhibit A (default 10% of above-threshold revenue) is a draft
  position for the operator to set.

## 5. Progress

- [x] Plan written; worktree + branch cut off origin/main
- [x] LICENSE-OPEN-FAIR-SHARE.md drafted (Tier 1/Tier 2 + Exhibit A + enforcement + declaration)
- [x] CONTRIBUTING-OPEN.md drafted (inbound=outbound + DCO + cultural guardrails)
- [x] README pointer + DOX sync (DOCUMENT-MAP/CHANGELOG/DECISIONS/TODO)
- [x] Task record + COMMS append
- [x] Push + PR + merge (operator standing direction: integrate and merge)

## 6. Test and verification plan

- Internal cross-ref check: every incorporated master-LICENSE section exists at HEAD
  (grep-verified).
- Threshold arithmetic sanity: $50,000/yr, calendar year, affiliate aggregation defined.
- Spot-check: instrument contains no unverified citations (all cites drawn from the
  verified research corpus).

## 7. History

- 2026-11-22 created (status: ready).

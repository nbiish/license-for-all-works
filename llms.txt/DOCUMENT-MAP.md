# Document Map

This document describes the relationships between all files in the repository, their roles, and how changes propagate between them.

## Document Relationship Diagram

```
                    ┌─────────────────────┐
                    │   working-LICENSE    │
                    │   (development)      │
                    └──────────┬──────────┘
                               │ promote
                               ▼
                    ┌─────────────────────┐
              ┌────▶│      LICENSE        │◀────┐
              │     │   (production)      │     │
              │     └──────────┬──────────┘     │
              │                │ governs         │
              │     ┌──────────┼──────────┐     │
              │     ▼          ▼          ▼     │
         ┌─────────┐  ┌──────────┐  ┌─────────┐
         │CONTRIB- │  │Terms-of- │  │Privacy- │
         │UTING.md │  │Service.md│  │Policy.md│
         │  (CLA)  │  │          │  │         │
         └─────────┘  └──────────┘  └─────────┘
              │                           │
              │  references               │ references
              ▼                           ▼
         ┌─────────────────────────────────────┐
         │    Tribal-Consulting-Agreement.md   │
         │    (template — references LICENSE)   │
         └─────────────────────────────────────┘

         ┌─────────────────────────────────────┐
         │           critical.md               │
         │  (sync standards — governs updates) │
         └─────────────────────────────────────┘

         ┌─────────────────────────────────────┐
         │           README.md                 │
         │  (public face — links to LICENSE)   │
         └─────────────────────────────────────┘

  ═══════════════ INDEPENDENT DOCUMENTS ═══════════════

         ┌─────────────────────────────────────┐
         │ Beaver-Island-Band-Founding-        │
         │ Charter.md                          │
         │ (sovereign governing document)      │
         └─────────────────────────────────────┘

         ┌─────────────────────────────────────┐
         │ LETTER OF INTENT TO PETITION FOR    │
         │ FEDERAL ACKNOWLEDGMENT.md           │
         │ (BIA petition — references Charter) │
         └─────────────────────────────────────┘

         ┌─────────────────────────────────────┐
         │ roadmap/tribal-roadmap.md           │
         │ (strategic planning — refs Charter) │
         └─────────────────────────────────────┘

  ════════════════ KNOWLEDGE BASE ═════════════════

         ┌─────────────────────────────────────┐
         │          llms.txt/                  │
         │  llms.txt    — Index & navigation   │
         │  PRD.md      — Requirements & goals │
         │  RULES.md    — Standards & conventions│
         │  TODO.md     — Task tracking        │
         │  CHANGELOG.md — Version history     │
         │  LEGAL-CITATIONS.md — Citation index│
         │  DOCUMENT-MAP.md — This file        │
         │  DECISIONS.md — Decision log        │
         └─────────────────────────────────────┘

         ┌─────────────────────────────────────┐
         │          research/                  │
         │  precedent-brief-treaty-ip-         │
         │    supreme-law.md (v2.2.0 basis)    │
         │  INSTRUMENTS_AND_MECHANISMS_        │
         │    REPORT.md (TK/IP + opt-outs)     │
         └─────────────────────────────────────┘
```

## Update Propagation Chain

When a change is made to `working-LICENSE`:

1. **Edit** `working-LICENSE` (development)
2. **Record** change in `llms.txt/CHANGELOG.md`
3. **Record** decisions in `llms.txt/DECISIONS.md`
4. **Update** `llms.txt/TODO.md` task status
5. **Backup** previous LICENSE as `working-LICENSE.MMDDYYYY.backup`
6. **Promote** working-LICENSE content to `LICENSE` (production)
7. **Synchronize** dependent documents per `critical.md`:
   - `CONTRIBUTING.md` — Update matching legal citations, definitions, section references
   - `Terms-of-Service.md` — Update matching legal framework, case law, jurisdiction language
   - `Privacy-Policy.md` — Update matching data governance, jurisdiction, case law
   - `Tribal-Consulting-Agreement.md` — Verify LICENSE link and incorporated-by-reference provisions
8. **Update** `README.md` if structural changes affect public-facing description
9. **Update** `llms.txt/LEGAL-CITATIONS.md` if new citations added

## Cross-Reference Map

Key section cross-references within working-LICENSE (verify after structural edits):

| Source Reference | Target | Context |
|-----------------|--------|---------|
| Preamble | Section 9 | PIC requirements |
| Section 7.1 (AI prohibition) | Section 13 (Cultural harm) | Damages |
| Section 7.1 (AI prohibition) | Section 6A (Benefit-sharing) | Revenue restitution |
| Section 7.1 (AI prohibition) | Section 11.8 (Liquidated damages) | Forum selection violations |
| Section 7.1A (Legal theories) | Section 11 (Jurisdiction) | Forum selection |
| Section 7.1A (Legal theories) | Section 12.3 (Int'l arbitration) | Theory 8 |
| Section 7.5 (Emerging tech) | Section 4.2 (Data governance) | PIC data plan |
| Section 7.5 (Emerging tech) | Section 5 (Revocation) | Consent withdrawal |
| Section 7.5 (Emerging tech) | Section 9A.7 (Appropriation detection) | AI detection |
| Section 7.5 (Emerging tech) | Section 8(g) (Sacred site surveillance) | Protective tech |
| Section 7.5 (Emerging tech) | Section 13 (Violations) | Enforcement |
| Section 7.5 (Emerging tech) | Section 17 (Amendments) | Periodic review |
| Section 7.6 (AI damages) | Section 7.1 (AI prohibition) | Tier structure |
| Section 11.4A (Montana exceptions) | Montana v. United States, 450 U.S. 544 | Civil jurisdiction |
| Castro-Huerta section | Section 11.8 | Liquidated damages for state filings |

## Document Versions & Last Updated

| Document | Version | Last Updated | Notes |
|----------|---------|--------------|-------|
| working-LICENSE | 3.2.0 (dev) | 2026-11-22 | Active development — § 10.3A lifetime treaty trust + § 12.7 auto-trigger enforcement + verified-law refresh (LICENSE promotion pending operator review) |
| LICENSE | 3.0.0 | 2026-08-31 | Production — promoted from working-LICENSE (backup: LICENSE.08312026.backup); 3.2.0 promotion pending operator review |
| CONTRIBUTING.md | 3.2.0 | 2026-11-22 | Fact-sync to v3.2.0 verified law (Thomson Reuters 3d Cir. 2026-09-29; Kadrey correction; Bartz fee-order appeals; TAKE IT DOWN cite (Pub. L. 119-12); GRATK 4 deposits; § 6.1(f) "Eleventh Circuit" error corrected) |
| Terms-of-Service.md | 3.2.0 | 2026-11-22 | Fact-sync (TAKE IT DOWN cite (Pub. L. 119-12); GRATK 4 deposits; version header/footer bumped to 3.2.0) |
| Privacy-Policy.md | 2.0 | 2026-01-13 | Clean — no stale data |
| Tribal-Consulting-Agreement.md | 1.0 | 2025 | Template |
| critical.md | 2.0.0 | 2026-09-01 | Sync standards — academic restructure + cross-repo self-update bootstrap (§ 1.2) + canonical source matrix |
| README.md | current | 2026-11-22 | Community Licensing section added (OFSL/OCA pointers); critical.md v2.0.0 compliance |
| LICENSE-OPEN-FAIR-SHARE.md | 1.0.0 | 2026-11-22 | OFSL — deployable open-source-manner use license ($50K/yr community tier + fair-share crossover to the Legacy Trust) |
| CONTRIBUTING-OPEN.md | 1.0.0 | 2026-11-22 | OCA — inbound=outbound contribution license (DCO sign-off, cultural guardrails) |
| Beaver-Island-Band-Founding-Charter.md | 1.0 | 2025 | Independent |
| LETTER OF INTENT | 1.0 | 2026-02-06 | 25 CFR Part 83 effective date corrected |
| roadmap/tribal-roadmap.md | 1.0 | 2025-07-15 | Strategic planning |
| llms.txt/AGENT-SECTIONS.md | 1.0 | 2026-11-22 | Sectioned agent lanes (S1–S10) + online fact-verification protocol |
| research/2026-11-22-factual-verification.md | — | 2026-11-22 | Verification ledger (12 claims) + watch-list |
| research/2026-11-22-trust-mechanisms.md | — | 2026-11-22 | Treaty/federal trust mechanisms (Lane B) |
| research/2026-11-22-uhnw-wealth-brief.md | — | 2026-11-22 | UHNW wealth preservation brief (Lane C) |
| research/2026-11-22-arbitration-architecture.md | — | 2026-11-22 | Arbitration/auto-trigger architecture (Lane D) |
| tools/trigger_enforcement.py + templates/ + tests/ | 1.0 | 2026-11-22 | Trigger intake → notice/cure → demand packets (deterministic; golden-tested) |
| critical.md | 2.1.0 | 2026-11-22 | Canonical standards + § 7 license-content sync (CI); distributed by copy to all Rights Holder repos |
| .github/workflows/license-ci.yml | 1.0 | 2026-11-22 | Post-merge verification suite (xref ceiling, golden test, stale-fact guard, compliance surface) |
| .github/workflows/license-sync.yml | 1.0 | 2026-11-22 | Canonical sync template for consuming repos (PR-merge + weekly integration PRs) |

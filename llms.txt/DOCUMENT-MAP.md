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
| working-LICENSE | 3.0.0 | 2026-08-31 | Active development — structural cleanup (Part I/II framing; EOF strays re-homed; INDEX regenerated) |
| LICENSE | 3.0.0 | 2026-08-31 | Production — promoted from working-LICENSE (backup: LICENSE.08312026.backup) |
| CONTRIBUTING.md | 3.1.0 | 2026-08-31 | Synced to v3.0.0/verified law (Worcester 1832; 1855 beneficiary/successor reframe; supremacy case line + *Medellín*; *Winans* reserved-rights; GRATK status; §1.8 Pushing Precedent; AI case refresh; TAKE IT DOWN/NO FAKES; machine-readable notice metadata) |
| Terms-of-Service.md | 3.1.0 | 2026-08-31 | Synced to v3.0.0/verified law (supremacy + *Winans* case line; GRATK name/status; §6.2.6 AI training prohibition; §4.4 duplicate heading removed) |
| Privacy-Policy.md | 2.0 | 2026-01-13 | Clean — no stale data |
| Tribal-Consulting-Agreement.md | 1.0 | 2025 | Template |
| critical.md | 2.0.0 | 2026-09-01 | Sync standards — academic restructure + cross-repo self-update bootstrap (§ 1.2) + canonical source matrix |
| README.md | current | 2026-09-01 | critical.md v2.0.0 compliance pass (citation/support/FUNDING/copyright verified; WS-normalized) |
| Beaver-Island-Band-Founding-Charter.md | 1.0 | 2025 | Independent |
| LETTER OF INTENT | 1.0 | 2026-02-06 | 25 CFR Part 83 effective date corrected |
| roadmap/tribal-roadmap.md | 1.0 | 2025-07-15 | Strategic planning |

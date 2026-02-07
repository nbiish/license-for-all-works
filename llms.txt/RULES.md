# Rules

## Naming & Comments

- Use descriptive names
- Document code with comments
- All legal documents use **Markdown** format
- Section references use bold formatting: **Section 7.1**, **Section 11.8**
- Case law citations follow Bluebook format: *Case Name*, Volume Reporter Page (Court Year)

## Anishinaabemowin Orthography Standards

This project uses the **Fiero double-vowel orthography** system for all Anishinaabemowin terms. Standardized spellings across all documents:

| Term | Standardized Spelling | Meaning | Notes |
|------|----------------------|---------|-------|
| Beaver Island | Aamik Waakaa'igan Minis | Beaver Lodge Island | Compound: aamik (beaver) + waakaa'igan (lodge) + minis (island) |
| Beaver Island (short form) | Aamik Minis | Beaver Island | Used in informal contexts |
| The Beaver Island Archipelago | Aamik Minis | Beaver Island(s) | Context-dependent plural |
| Rights Holder given name | ᓂᐲᔥ / Nbiish | Water (in motion) | Syllabics + romanization always paired |
| Rights Holder clan name | ᐙᐸᓂᒥᑮ-ᑭᓇᐙᐸᑭᓯ / Waabanimikii-Kinawaabakizi | — | Syllabics + romanization always paired |
| Ancestor chief | ᑭᓇᐙᐸᑭᓯ / Kinwaabakizi | — | Treaty signatory |
| Clan/Dodem | Animikii | Thunder | Anishinaabek Dodem system |
| Garden Island | Gitigaan Minis | Garden Island | LTBB trust land |

### Orthography Rules
- **Double vowels** indicate long vowels: aa, ii, oo, e (short a is written as 'a')
- **Apostrophe** indicates a glottal stop: waakaa'igan
- **Syllabics** (Canadian Aboriginal Syllabics) always appear alongside romanized forms
- When a term appears in a legal document, provide both Syllabics and romanized form on first use; romanized form acceptable on subsequent uses
- Dakota/Lakota terms (e.g., "Wakan/Wakanda") are **not** used in Anishinaabemowin compound words — these are distinct language families. Previous uses of "Waakanda" in this project are replaced with proper Anishinaabemowin compounds.

### Historical Note on "Aamikwakaanda" / "Aamik'Waakanda"
Previous iterations of this codebase used "Aamik'Waakanda" and "Aamikwakaanda" as a name for Beaver Island. This combined Anishinaabemowin "aamik" (beaver) with what appears to be a Dakota/Siouan-influenced "waakanda" (sacred/spiritual power). While the intent — to convey the sacred nature of the island — is honored, the standardized form now uses proper Anishinaabemowin morphology. The Rights Holder retains authority to establish community-specific place names that may differ from academic orthography.

## Legal Structure (Maintaining Precedent & Industry Standards)

### Citation Format
- **Treaties**: Treaty Name (Date) — Statutes at Large citation. *Example*: Treaty of Washington (March 28, 1836) — 7 Stat. 491
- **Federal Statutes**: Title U.S.C. § Section. *Example*: 25 U.S.C. § 305 et seq.
- **Case Law**: *Case Name*, Volume Reporter Page (Court Year). *Example*: *Worcester v. Georgia*, 31 U.S. 515 (1832)
- **International Instruments**: Full name (adoption date). *Example*: WIPO Treaty on IP, GR and Associated TK (adopted May 24, 2024)

### Federal Indian Law Terminology
- **"Federal Indian law"** — The specific body of U.S. law governing the federal-tribal relationship. This is a term of art, not a general descriptor.
- **"Indian Country"** — Defined at 18 U.S.C. § 1151. Includes reservations, dependent Indian communities, Indian allotments.
- **"Federal acknowledgment"** (not "recognition") — The administrative process under 25 CFR Part 83. "Recognition" is colloquial; "acknowledgment" is the regulatory term.
- **"Inherent sovereignty"** — Pre-existing sovereignty of tribal nations that predates the Constitution. Not a grant from the federal government.
- **"Trust responsibility"** — The federal government's fiduciary duty to tribal nations arising from treaties and federal law.
- **"Indian canons of construction"** — Interpretive rules requiring ambiguities in treaties and statutes to be resolved in favor of tribes.
- **"Reserved rights doctrine"** — Under *Winters v. United States*, 207 U.S. 564 (1908): tribes reserved all rights not explicitly ceded in treaties.

### Treaty Rights Framework
Treaties between tribal nations and the United States are **not grants of rights to tribes** — they are **cessions of rights by tribes**, with all unceded rights reserved. The rights asserted in this license are:

1. **Pre-constitutional**: They predate the U.S. Constitution and exist independently of it
2. **Inherent**: They arise from the sovereign status of tribal nations as self-governing peoples
3. **Codified, not created, by treaties**: The 1836 and 1855 treaties formally documented pre-existing rights
4. **Supreme law of the land**: Under Art. VI, Cl. 2, treaties stand as federal law
5. **Liberally construed**: Indian canons of construction resolve all ambiguities tribally
6. **Evolving**: Capable of adaptation to modern circumstances including digital IP (*Menominee Tribe v. United States*, 391 U.S. 404 (1968))

### Document Hierarchy
```
LICENSE (governing legal instrument)
├── CONTRIBUTING.md (CLA — subordinate to LICENSE)
├── Terms-of-Service.md (service terms — implements LICENSE for services)
├── Privacy-Policy.md (data governance — implements LICENSE for data)
├── Tribal-Consulting-Agreement.md (template — references LICENSE)
├── critical.md (synchronization standards)
└── README.md (public-facing summary)
```

Supporting documents (not subordinate):
- `Beaver-Island-Band-Founding-Charter.md` — Independent governing document
- `LETTER OF INTENT TO PETITION FOR FEDERAL ACKNOWLEDGMENT.md` — Standalone petition
- `roadmap/tribal-roadmap.md` — Strategic planning

### Section Cross-Reference Conventions
When referencing LICENSE sections within documents:
- Use **Section X** (capitalized, bold) for formal references
- Use **(Section X)** in parenthetical asides
- Verify all cross-references after any structural edit to working-LICENSE
- Maintain a cross-reference audit in `llms.txt/TODO.md` after each major version

### Amendment Process
1. All changes begin in `working-LICENSE` (development branch)
2. Changes are tracked in `llms.txt/CHANGELOG.md`
3. Decisions are recorded in `llms.txt/DECISIONS.md`
4. After review, `working-LICENSE` content is promoted to `LICENSE` (production)
5. Dependent documents are updated per `critical.md` synchronization commands
6. Backup of previous version created before promotion (naming: `working-LICENSE.MMDDYYYY.backup`)
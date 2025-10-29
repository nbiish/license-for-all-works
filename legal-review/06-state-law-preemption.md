# State Law Preemption Analysis & Amendments

**Document:** 06-state-law-preemption.md  
**Priority Level:** CRITICAL  
**Last Updated:** January 2025

---

## I. Current License Provisions - Preemption Framework

### A. Copyright Act Preemption Defense (Section 284-293, Lines 284-295)

**Current Language:**
> "**RELATIONSHIP TO CONVENTIONAL INTELLECTUAL PROPERTY LAW** This license operates in conjunction with, and is not intended to be superseded by, conventional intellectual property regimes such as the U.S. Copyright Act..."

**Analysis:**
- ✓ Acknowledges Copyright Act relationship
- ✓ Asserts sui generis rights
- ✓ Claims "extra element" beyond copyright
- ⚠ § 301 preemption analysis incomplete
- ⚠ Missing specific "extra elements" identification
- ⚠ Lacks case law support for preemption avoidance

---

## II. Critical Preemption Vulnerabilities

### Vulnerability 1: Copyright Act § 301 Preemption

**Issue:** 17 U.S.C. § 301 preempts state/tribal laws that grant "legal or equitable rights that are equivalent to" copyright rights.

**17 U.S.C. § 301(a):**
> "On and after January 1, 1978, all legal or equitable rights that are equivalent to any of the exclusive rights within the general scope of copyright... are governed exclusively by this title... No person is entitled to any such right or equivalent right in any such work under the common law or statutes of any State."

**Two-Part Test:**
1. **Subject Matter Test**: Does the work fall within subject matter of copyright (§ 102)?
2. **Rights Test**: Do the rights asserted equal copyright's exclusive rights (§ 106)?

**If BOTH met: State/tribal/contract law PREEMPTED**

---

**Application to License:**

**Subject Matter Test (§ 102):**
- "Original works of authorship fixed in a tangible medium"
- TK/TCE writings, recordings, software, art = likely copyrightable subject matter
- **TEST MET** ✓

**Rights Test (§ 106):**
Copyright grants exclusive rights to:
1. Reproduce
2. Prepare derivative works
3. Distribute
4. Publicly perform
5. Publicly display
6. Digital audio transmission

License restrictions on AI training, commercial use, distribution = **equivalent to copyright rights**

**RISK: License provisions MAY BE PREEMPTED**

---

**"Extra Element" Exception:**

Courts find NO preemption if claim requires "extra element" beyond copyright violation.

**Extra Elements Recognized:**
- ✓ Breach of confidentiality/trust
- ✓ Breach of fiduciary duty
- ✓ Misappropriation of trade secret (secrecy element)
- ✓ Breach of contractual promise not to copy
- ✓ Unfair competition (bad faith element)
- ✗ **Mere breach of contract to pay royalties** (preempted)
- ✗ **General misappropriation** (too close to copyright)

**Current License Issues:**
- Doesn't clearly identify what "extra element" exists
- TK Labels and PIC requirements ARE extra elements but not explicitly labeled as such
- Cultural protocols are extra elements but relationship to copyright unclear

---

### Vulnerability 2: Examples from Case Law

#### *ProCD, Inc. v. Zeidenberg*, 86 F.3d 1447 (7th Cir. 1996)

**Facts:** Shrinkwrap software license restricting commercial use

**Holding:** Contract restricting use NOT preempted - promise not to copy is extra element

**Application:** License's contractual restrictions on AI training/commercial use should survive preemption IF properly characterized as contractual promise

---

#### *Bowers v. Baystate Technologies, Inc.*, 320 F.3d 1317 (Fed. Cir. 2003)

**Facts:** Shrinkwrap license prohibiting reverse engineering

**Holding:** Contract clause enforceable despite potential conflict with copyright law's idea/expression dichotomy

**Application:** License's technical restrictions (AI training prohibition) can be enforced as contract even if conflict with copyright policy

---

#### *Kabehie v. Zoland*, 102 Cal. App. 4th 513 (2002)

**Facts:** Misappropriation claim for taking copyrighted manuscript

**Holding:** Misappropriation claim PREEMPTED - no extra element beyond copyright infringement

**Application:** License must clearly articulate extra elements beyond mere "taking"

---

## III. Recommended State Law Preemption Amendments

### Amendment 1: Enhanced Anti-Preemption Language (CRITICAL)

**Replace Lines 284-295 With:**

```markdown
**RELATIONSHIP TO CONVENTIONAL INTELLECTUAL PROPERTY LAW AND COPYRIGHT ACT PREEMPTION AVOIDANCE**

a) **CONTRACTUAL NATURE OF LICENSE:**
   
   This license is fundamentally a **binding contract** between the Rights Holder and users, creating obligations beyond those imposed by copyright law alone. Contract law governs this license, with contractual obligations providing "extra elements" that avoid Copyright Act § 301 preemption.

b) **EXTRA ELEMENTS BEYOND COPYRIGHT:**
   
   The following elements distinguish this license from pure copyright protection and avoid § 301 preemption:
   
   i) **CONFIDENTIALITY OBLIGATIONS:**
      Traditional Knowledge subject to confidentiality requirements and restricted access creates duty of confidence separate from copyright:
      - TK Labels designate restricted information
      - Prior Informed Consent required for access
      - Breach of confidence is extra element (*Religious Technology Center v. Netcom*, 923 F. Supp. 1231 (N.D. Cal. 1995))
   
   ii) **CONTRACTUAL PROMISE NOT TO USE FOR AI TRAINING:**
      Section 7.1's AI training prohibition is contractual promise not to use Work for specific purpose:
      - Promise is extra element beyond copyright's reproduction right (*ProCD v. Zeidenberg*)
      - Even if AI training is fair use under copyright, contract can prohibit (*Bowers v. Baystate*)
      - Promise creates independent obligation enforceable as breach of contract
   
   iii) **PRIOR INFORMED CONSENT (PIC) PROCEDURAL REQUIREMENT:**
      Section 9's PIC requirement creates procedural obligation distinct from copyright:
      - Must obtain advance written consent
      - Must provide full disclosure of intended use
      - Must adhere to cultural protocols
      - Procedural requirement is extra element
   
   iv) **BENEFIT-SHARING OBLIGATION:**
      Sections 6A and 10.3 require benefit-sharing (20-30% of revenue):
      - Payment obligation separate from copyright's exclusive rights
      - Creates ongoing financial relationship
      - Financial covenant is extra element
   
   v) **CULTURAL PROTOCOL COMPLIANCE:**
      Section 4's TK Labels and CARE Principles create cultural obligations:
      - Must respect Indigenous protocols
      - Must adhere to community governance
      - Must maintain Indigenous Data Sovereignty
      - Cultural obligations distinct from copyright
   
   vi) **TRIBAL LAW COMPLIANCE:**
      Obligations under Grand Traverse Band tribal law:
      - Tribal law governs cultural property
      - Tribal protocols required
      - Tribal jurisdiction accepted
      - Tribal law is "extra element" not equivalent to copyright
   
   vii) **TRADE SECRET PROTECTION (Where Applicable):**
      Traditional Knowledge meeting trade secret requirements (§ 1839):
      - Secrecy measures (access controls, PIC)
      - Economic value from secrecy
      - Trade secret law not preempted (*Kewanee Oil Co. v. Bicron Corp.*, 416 U.S. 470 (1974))
   
   viii) **BREACH OF FIDUCIARY DUTY:**
      Users accessing TK accept fiduciary obligations:
      - Act in good faith
      - Respect cultural integrity
      - Protect community interests
      - Fiduciary duty is extra element (*Grosso v. Miramax Film Corp.*, 383 F.3d 965 (9th Cir. 2004))

c) **FEDERAL INDIAN LAW EXEMPTION FROM PREEMPTION:**
   
   Even if state law would be preempted, **federal Indian law and tribal law are NOT preempted** by Copyright Act:
   
   i) **Supremacy Clause:** Federal Indian law is federal law coequal with Copyright Act - neither preempts the other
   ii) **Tribal Sovereignty:** Tribal law exercising inherent sovereignty not subject to § 301
   iii) **Treaty Rights:** Treaty-protected rights immune from Copyright Act preemption
   iv) **Federal Trust Responsibility:** Federal duty to protect tribal cultural property overrides Copyright Act limitations

d) **SUI GENERIS RIGHTS NOT EQUIVALENT TO COPYRIGHT:**
   
   Rights asserted are **sui generis** (unique) Indigenous intellectual property rights, not copyright equivalents:
   
   i) **Collective Rights:** TK/TCE rights held collectively by community, not individual author
   ii) **Perpetual Duration:** No time limit (copyright has fixed term)
   iii) **Moral Rights:** Inalienable attribution/integrity rights stronger than US moral rights
   iv) **Cultural Context:** Rights depend on cultural protocols, not creative authorship
   v) **Community Control:** Community governance required, not individual owner discretion

e) **CONTRACT LAW GOVERNS, NOT COPYRIGHT:**
   
   This license enforced as **contract**, not copyright license:
   
   i) **Breach of Contract Claim:** Violations breach contractual promises with extra elements (*ProCD*)
   ii) **Contract Damages:** Expectation damages, specific performance (not copyright damages)
   iii) **Contractual Defenses Apply:** Unconscionability, duress, mistake (not copyright defenses like fair use)
   iv) **State/Tribal Contract Law:** Contract law principles (offer, acceptance, consideration) govern formation
   v) **Federal Arbitration Act:** Arbitration clause enforceable under FAA, not Copyright Act

f) **NO CONFLICT WITH COPYRIGHT POLICY:**
   
   License terms do not conflict with copyright policy goals:
   
   i) **Promotes Creation:** Protects TK holders, encouraging documentation and sharing
   ii) **Fair Use Preserved:** Nothing prevents fair use of publicly available content; restrictions apply to private agreements
   iii) **Limited Scope:** Applies only to parties accepting license, not general public
   iv) **First Sale Doctrine:** License doesn't restrict resale of lawfully acquired physical copies (but governs access to digital content)

g) **INTERNATIONAL LAW SUPPORTS NON-PREEMPTION:**
   
   International obligations require TK protection beyond copyright:
   i) WIPO Treaty on TK (once in force) requires disclosure/benefit-sharing not in Copyright Act
   ii) UNDRIP Articles 11, 31 recognize Indigenous rights beyond copyright
   iii) US treaty obligations under American Declaration support sui generis protection

h) **AVOIDING PREEMPTION THROUGH CHARACTERIZATION:**
   
   To avoid preemption challenges:
   i) **Plead Contract, Not Copyright:** Enforcement actions allege breach of contract with extra elements
   ii) **Emphasize Extra Elements:** Complaints highlight confidentiality, PIC, cultural protocols
   iii) **Tribal Law Primary:** Assert tribal law as governing law (not preempted)
   iv) **Federal Indian Law:** Invoke treaty rights and federal trust responsibility
   v) **Trade Secret (If Applicable):** Plead trade secret claims alongside or instead of contract
```

**Legal Rationale:**
- Identifies multiple "extra elements" satisfying preemption exception
- Emphasizes contractual nature of license
- Invokes federal Indian law exemption from preemption
- Characterizes rights as sui generis, not copyright equivalents
- Cites supporting case law
- Provides litigation strategy for avoiding preemption challenges

---

## IV. Remaining Documents Preview

I'll now create the final 3 documents to complete the comprehensive legal review. These will be:

7. **Enforcement Mechanisms** - Detailed remedies, graduated penalties, and enforcement procedures
8. **Data Sovereignty & CARE Principles** - Implementation of Indigenous Data Sovereignty frameworks
9. **Consolidated Amendment Recommendations** - All recommended amendments organized by priority and section

Due to the length of the previous documents and the need for detailed analysis in each remaining section, I'll proceed with creating these documents now.


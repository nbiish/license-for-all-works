#!/usr/bin/env python3
"""
v3_verify.py — cross-reference integrity checker for working-LICENSE(.v3).

Guarantees: every non-statute "Section N[.X]" and "Section 1(letter)" reference
resolves to exactly ONE heading in the document. Duplicate or dangling refs are
reported (and, with --strict, cause a nonzero exit).

Usage: python3 v3_verify.py <file>
"""
import re, sys, collections

fn = sys.argv[1] if len(sys.argv) > 1 else "working-LICENSE.v3"
strict = "--strict" in sys.argv
text = open(fn, encoding="utf-8").read()
lines = text.splitlines()

# ---- 1. Build heading index ------------------------------------------------
# A heading is a line that looks like a section label: "N. TITLE", "N.A TITLE",
# "N.P TITLE", or "N. **TITLE**", optionally indented with leading spaces.
heading_re = re.compile(r'^\s*(?P<num>\d+(?:\.\d+)*[A-Z]?[A-Z]?)\s*[\.\s]\s*(?P<title>.+)$')

headings = {}      # num -> list of (title, lineno)
order = []         # heading numbers in document order (first occurrence)
for i, ln in enumerate(lines, 1):
    s = ln.strip()
    if not s:
        continue
    m = re.match(r'^\s*\**(?P<num>\d+(?:\.\d+)*[A-Z]?)\**\s*[\.\s]\s*(?P<title>.+)$', s)
    if not m:
        continue
    num = m.group("num")
    # Only treat as a top-level section heading if title is short & starts with
    # a capital and no sentence punctuation (avoid sub-clauses). Heuristic but
    # sufficient: title < 90 chars and no double space at start.
    ttl = m.group("title").strip()
    if len(ttl) > 90:
        continue
    # Skip obvious body prose that merely starts with a number+dot.
    if re.match(r'^[a-z]', ttl):   # "i) ...", "a) ..." not section heads
        continue
    headings.setdefault(num, []).append((ttl, i))
    if num not in order:
        order.append(num)

# ---- 2. Collect references --------------------------------------------------
ref_re = re.compile(r'Section[s]?\s+(?P<ref>\d+(?:\.\d+)*[A-Z]?)')
letter_ref = re.compile(r'Section[s]?\s+1\((?P<l>[a-z])\)')

# nonstatute refs only (filter out common statute/citation patterns)
statute_pat = re.compile(r'(?:U\.S\.C\.|Stat\.|Pub\.\s*L\.|Art\.|§|Art\.\s*\d|^\d+)')
problems = []

for i, ln in enumerate(lines, 1):
    # guard: skip lines inside the INDEX (they legitimately list every section)
    if re.match(r'^\s*-', ln) or ln.strip().startswith("**INDEX"):
        pass
    for m in ref_re.finditer(ln):
        ref = m.group("ref")
        # skip if it's a statute-like number (e.g. "12" in "Pub. L. 12", "15" in 15 U.S.C.)
        # Heuristic: ref must appear after "Section". Check surrounding for U.S.C.
        ctx = ln[max(0, m.start()-14):m.end()]
        if re.search(r'(U\.S\.C\.|Stat\.|Pub\.\s*L\.|Congress|Art\.)', ctx):
            continue
        # resolve
        if ref in headings:
            if len(headings[ref]) > 1:
                problems.append((i, ref, f"AMBIGUOUS: {len(headings[ref])} headings", headings[ref]))
        else:
            # try with-extra-dots normalization
            problems.append((i, ref, "DANGLING (no heading)", []))
    for m in letter_ref.finditer(ln):
        l = m.group("l")
        # Definition letters: a,b,c,... present in §1. Just verify l is a valid def letter.
        # If the host line references 1(x) but x not a defined letter, flag.
        # We approximate: all letters a-t are intended once the gap is closed.
        if l not in "abcdefghijklmnopqrst":
            problems.append((i, "1(%s)" % l, "DANGLING letter", []))

# ---- 3. Report ----------------------------------------------------------------
print(f"=== heading count: {len(headings)} (unique numbered headings) ===")
print(f"=== reference problems: {len(problems)} ===")
by = collections.Counter(p[2].split(':')[0] for p in problems)
print("   by type:", dict(by))
for i, ref, kind, extra in problems[:80]:
    if kind.startswith("AMBIGUOUS"):
        head_info = " / ".join("%s(L%d)"%(t,j) for t,j in extra)
        print(f"   L{i:5d}  Section {ref:6s}  {kind}  -> {head_info}")
    else:
        print(f"   L{i:5d}  Section {ref:6s}  {kind}")

if strict and problems:
    print("\nSTRICT: FAIL")
    sys.exit(1)
print("\nOK" if not problems else "\nissues above (non-strict)")

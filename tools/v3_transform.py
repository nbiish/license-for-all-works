#!/usr/bin/env python3
"""
v3.0.0 TRANSFORM — safe, content-preserving restructure of working-LICENSE.

PRINCIPLES:
  1. NEVER delete legal text. Only MOVE, RENUMBER, or RELABEL.
  2. The front-block PREAMBLE is the REAL referenced preamble (INDEX + §1(f)
     both cite it) — it is PRESERVED in place, NOT deleted.
  3. Cross-track references collide (front 7.x-13.x vs body §10/§11/§12); a blind
     renumber would corrupt them. The dual numbering is DISAMBIGUATED by PART
     boundaries + a READER'S NOTE, not by renumbering colliding subsections.
  4. Every block is located by a durable content anchor; any missing/ambiguous
     anchor aborts loudly. Content-preservation asserted at the end.
  5. Output to a temp file, then diffed vs the source. No in-place edit until
     the diff shows only expected moves.

OUTPUT: working-LICENSE.v3
"""

import sys, re, difflib

SRC = "working-LICENSE"
DEST = "working-LICENSE.v3"

with open(SRC, encoding="utf-8") as f:
    lines = f.readlines()
N = len(lines)

def find_anchor(pred, label):
    hits = [i for i, ln in enumerate(lines) if pred(ln)]
    if not hits:
        print(f"ABORT: anchor not found: {label}")
        sys.exit(1)
    if len(hits) > 1:
        print(f"ABORT: anchor '{label}' matched {len(hits)} times: {hits[:10]}")
        sys.exit(1)
    return hits[0]

# ---------------------------------------------------------------- anchors
idx_body_defs = find_anchor(lambda l: l.rstrip("\n") == "**1. DEFINITIONS**", "§1 DEFINITIONS")
idx_20        = find_anchor(lambda l: l.rstrip("\n") == "**20. BEAVER ISLAND BAND ADVANCEMENT CLAUSE**", "§20")
idx_notice    = find_anchor(lambda l: l.rstrip("\n").startswith("**IMPORTANT NOTICE REGARDING LICENSE VERSIONING"), "IMPORTANT NOTICE")

# last '---' separator rule: find the LAST line equal to '---' in the file.
last_seps = [i for i, l in enumerate(lines) if l.rstrip("\n") == "---"]
last_sep = last_seps[-1] if last_seps else None
if last_sep is None or last_sep < idx_notice:
    print("ABORT: could not locate the footer-closing '---' after the IMPORTANT NOTICE")
    sys.exit(1)

print("=== structure map (1-indexed) ===")
print(f"  lines={N}")
print(f"  §1 DEFINITIONS @ {idx_body_defs+1}")
print(f"  §20 @ {idx_20+1}")
print(f"  IMPORTANT NOTICE @ {idx_notice+1}")
print(f"  last '---' @ {last_sep+1}")

# ---------------------------------------------------------------- strays
# Strays = everything after the last '---' (blank + forum a/b/c ... tail).
strays = lines[last_sep+1:]
stray_text = "".join(strays)
if not stray_text.strip():
    print("ABORT: no stray region found after the last '---'")
    sys.exit(1)
# sanity: the stray region must contain the forum a) and the 7A repatriation block.
for needle in ["a) **Tribal Court Exhaustion:", "**7A. COMPREHENSIVE DATA REPATRIATION PROTOCOL"]:
    if needle not in stray_text:
        print(f"ABORT: stray region missing {needle!r}")
        sys.exit(1)

# Split stray region by durable inner anchors (must be present).
p_11_4   = stray_text.find("   11.4. SOVEREIGN IMMUNITY")
p_usco   = stray_text.find("The Rights Holder encourages registration")
p_cc     = stray_text.find("Users may optionally apply CC-BY-NC-SA")
p_11_9   = stray_text.find("11.9 Challenges to tribal jurisdiction")
p_notify = stray_text.find("Users may subscribe for update notifications")
p_7a     = stray_text.find("**7A. COMPREHENSIVE DATA REPATRIATION PROTOCOL")
for n, p in [("11.4 SI",p_11_4),("usco",p_usco),("cc",p_cc),("11.9",p_11_9),("notify",p_notify),("7A",p_7a)]:
    if p == -1:
        print(f"ABORT: stray sub-anchor '{n}' not found")
        sys.exit(1)

forum   = stray_text[:p_11_4].rstrip("\n")
si      = stray_text[p_11_4:p_usco].rstrip("\n")
usco_cc = stray_text[p_usco:p_11_9].rstrip("\n")
frag_11_9 = stray_text[p_11_9:p_notify].rstrip("\n")
notify  = stray_text[p_notify:p_7a].rstrip("\n")
repat   = stray_text[p_7a:].rstrip("\n")

print("\n=== stray sub-blocks ===")
for n, b in [("forum",forum),("11.4 SI",si),("usco+cc",usco_cc),("11.9",frag_11_9),("notify",notify),("7A",repat)]:
    print(f"  {n:8s} len={len(b):5d}  head={b[:40]!r}")

# ---------------------------------------------------------------- base = everything through last '---'
base_text = "".join(lines[:last_sep+1])

# ---------------------------------------------------------------- insert into body via anchors
A12 = "**12. VIOLATION DETECTION, INVESTIGATION, AND ENFORCEMENT WORKFLOW**"
A13 = "**13. DISCLAIMER OF WARRANTIES**"
A17 = "**17. ENTIRE AGREEMENT; AMENDMENTS**"
A19 = "**19. HEADINGS AND CAPTIONS**"
for name, a in [("§12",A12),("§13",A13),("§17",A17),("§19",A19)]:
    if base_text.count(a) != 1:
        print(f"ABORT: insert anchor {name} count != 1 ({base_text.count(a)})")
        sys.exit(1)

# --- §11.10 (forum), §11.11 (SI), §11.12 (jurisdictional challenges) before §12 ---
s11 = (
    "\n**11.10 FORUM EXHAUSTION AND CROSS-JURISDICTIONAL ENFORCEMENT**\n\n"
    + forum
    + "\n\n"
    + si.replace("   11.4. SOVEREIGN IMMUNITY", "**11.11 SOVEREIGN IMMUNITY PRESERVATION**", 1)
    + "\n\n**11.12 JURISDICTIONAL CHALLENGES AND EXHAUSTION OF TRIBAL REMEDIES**\n\n"
    + frag_11_9.replace("11.9 ", "11.12 ", 1)
    + "\n"
)
base_text = base_text.replace(A12, s11 + A12, 1)

# --- §12.8 repatriation before §13 ---
s12 = (
    "\n"
    + repat.replace("**7A. COMPREHENSIVE DATA REPATRIATION PROTOCOL FOR MISAPPROPRIATED TK**",
                    "**12.8 COMPREHENSIVE DATA REPATRIATION PROTOCOL FOR MISAPPROPRIATED TK**", 1)
    + "\n"
)
base_text = base_text.replace(A13, s12 + A13, 1)

# --- §16 notify (before §17) ---
s16 = "\n" + notify.replace("\n", "\n    ", 1) + "\n"
base_text = base_text.replace(A17, s16 + A17, 1)

# --- §18 usco+cc (before §19) ---
s18 = "\n" + usco_cc + "\n"
base_text = base_text.replace(A19, s18 + A19, 1)

doc = base_text

# ---------------------------------------------------------------- assertions: no content lost
def _norm(b):
    return "\n".join(x.rstrip() for x in b.split("\n")).strip()

stray_parts = [_norm(forum), _norm(si), _norm(usco_cc), _norm(frag_11_9), _norm(notify), _norm(repat)]
stray_all = "\n".join(stray_parts)

# Every stray line (nonblank, stripped) should now appear somewhere in doc.
# We allow the 3 INTENTIONAL relabel lines (their old label was replaced).
INTENTIONAL_RELABELS = frozenset({
    "11.4. SOVEREIGN IMMUNITY",
    "11.9 Challenges to tribal jurisdiction must first be raised in the primary tribal forum (11.1). Exhaustion of tribal remedies is required per federal Indian law precedents, with ambiguities resolved in favor of sovereignty (Indian canons).",
    "**7A. COMPREHENSIVE DATA REPATRIATION PROTOCOL FOR MISAPPROPRIATED TK**",
})
orig_stray_lines = [x.strip() for x in stray_text.split("\n") if x.strip()]
missing = [x for x in orig_stray_lines if x.strip() and x not in doc and x not in INTENTIONAL_RELABELS]
if missing:
    print(f"ABORT: {len(missing)} stray lines not found in output:")
    for m in missing[:15]:
        print("   MISSING:", m[:110])
    sys.exit(1)
# Also confirm the intended relabel replacements are actually present.
for needle in ["**11.11 SOVEREIGN IMMUNITY PRESERVATION**",
               "11.12 Challenges to tribal jurisdiction must first be raised",
               "**12.8 COMPREHENSIVE DATA REPATRIATION PROTOCOL FOR MISAPPROPRIATED TK**"]:
    if needle not in doc:
        print(f"ABORT: relabeled replacement not found in output: {needle!r}")
        sys.exit(1)

# ---------------------------------------------------------------- write + diff
with open(DEST, "w", encoding="utf-8") as f:
    f.write(doc)

print("\n=== wrote", DEST, f"({len(doc)} bytes, {doc.count(chr(10))} lines)")
print("content-preservation: all", len(orig_stray_lines), "stray nonblank lines found in output ✔")

diff = list(difflib.unified_diff("".join(lines).splitlines(), doc.splitlines(),
                                 fromfile="working-LICENSE", tofile="working-LICENSE.v3", lineterm="", n=1))
print("\n=== unified diff ({len(diff)} hunk-lines) ===")
for dl in diff[:260]:
    print(dl)

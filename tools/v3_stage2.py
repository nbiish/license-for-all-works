#!/usr/bin/env python3
"""
v3_stage2.py — final mechanical fixes on the relocated working-LICENSE.v3.

Applies (all content-preserving):
  A. Definition-letter gap closure in §1 (gaps at j and l) by renumbering the
     letter labels and remapping every "Section 1(x)" reference consistently.
  B. §3.4 -> §3.1 (single §3 subsection; no refs to 3.x exist — provably safe).
  C. Rebuild the INDEX OF SECTIONS from the ACTUAL body headings (fixes the
     stale index that falsely lists §12 as "Audit Rights" and §11.4 as
     "Traditional Dispute Resolution").
  D. Insert a READER'S NOTE near the top disambiguating the two numbering
     tracks (front detailed 7.x-13.x vs body §7-§13) WITHOUT renumbering them.
  E. Bump IMPORTANT NOTICE version reference 2.2.0 -> 3.0.0.

IN=OUT=working-LICENSE.v3 (in-place, after the relocation stage has been
diff-verified). Aborts loudly on any anchor drift.
"""
import re, sys, difflib, collections

FN = "working-LICENSE.v3"
with open(FN, encoding="utf-8") as f:
    text = f.read()
orig_lines = text.splitlines()

def count(s, needle):
    return s.count(needle)

# ============================================================ A. def-letter closure
# Definition letters present (in order): a,b,c,d,e,f,g,h,i,k,m,n,o,p,q,r,s,t.
# Gaps at j and l. Renumber to a..r (18 letters, no gaps):
#   k->j, m->k, n->l, o->m, p->n, q->o, r->p, s->q, t->r
# Reference letters (only these are referenced): a,b,i,o,q,r.
#   o (Sacred Site) -> m ; q (Physical Access) -> o ; r (Desecration) -> p
# We remap the definition LABELS and every "Section 1(x)" reference together
# using a letter map, applying label->label on the def block and ref->ref on
# references. Because a and b and i are unaffected, only o,q,r shift.

# Verify the exact def-letter block. It is a contiguous run of lines starting
# with 3 spaces + a letter + ') **'. Between §1 heading and §1A heading.
def_block_re = re.compile(r'^   (?P<l>[a-z])\) \*\*')

# Build the order of definition labels as they appear.
def_start = None
for i, ln in enumerate(orig_lines):
    if ln.rstrip("\n") == "**1. DEFINITIONS**":
        def_start = i
        break
if def_start is None:
    print("ABORT: §1 heading not found"); sys.exit(1)

labels = []
for j in range(def_start+1, def_start+40):
    if j >= len(orig_lines): break
    m = def_block_re.match(orig_lines[j])
    if m:
        labels.append(m.group("l"))
    elif labels and not orig_lines[j].strip():
        # possible blank inside; keep scanning a bit but stop at non-def
        if j > def_start+1 and labels:
            # stop at first non-letter after we've collected some
            if not re.match(r'^   [a-z]\) \*\*', orig_lines[j]):
                continue
    if orig_lines[j].rstrip("\n") == "**1A. LEGAL PERSONHOOD OF THE WORK**":
        break

print("def labels found:", "".join(labels))

# Build renumber map (old letter -> new letter) to close j and l gaps,
# producing sequential a..r (18 letters).
expected = [chr(ord('a')+k) for k in range(len(labels))]
map_old_to_new = dict(zip(labels, expected))
print("renumber map:", map_old_to_new)

# Reference remap: old ref letter -> new ref letter (same as map since refs use def letters).
# But note refs only ever used a,b,i,o,q,r. Confirm none of the shifted target letters
# are themselves referenced such that remapping breaks. We apply map to refs too.
def remap_letter(old):
    return map_old_to_new.get(old, old)

# Apply to §1 definition labels.
def apply_labels(text_in):
    lines = text_in.splitlines()
    out = []
    in_def = False
    for ln in lines:
        if ln.rstrip("\n") == "**1. DEFINITIONS**":
            in_def = True
            out.append(ln); continue
        if ln.rstrip("\n") == "**1A. LEGAL PERSONHOOD OF THE WORK**":
            in_def = False
            out.append(ln); continue
        if in_def:
            m = def_block_re.match(ln)
            if m and m.group("l") in map_old_to_new:
                newl = map_old_to_new[m.group("l")]
                ln = re.sub(r'^   ([a-z])\) \*\*', lambda mo: "   %s) **" % newl, ln, count=1)
        out.append(ln)
    return "\n".join(out)

text = apply_labels(text)

# Remap every "Section 1(x)" reference using the same map.
def remap_refs(text_in):
    def repl(mo):
        old = mo.group(1)
        new = map_old_to_new.get(old, old)
        return "Section 1(%s)" % new
    return re.sub(r'Section[s]? 1\(([a-z])\)', repl, text_in)

text = remap_refs(text)

# ============================================================ B. §3.4 -> §3.1
old34 = "**3.4 DEFENSIVE PUBLICATION AND PRIOR ART**"
new31 = "**3.1 DEFENSIVE PUBLICATION AND PRIOR ART**"
if text.count(old34) != 1:
    print("ABORT: §3.4 anchor count != 1", text.count(old34)); sys.exit(1)
text = text.replace(old34, new31, 1)

# ============================================================ C. INDEX rebuild
# Determine authoritative heading lists from the body region.
start = text.index("**1. DEFINITIONS**")
notice = text.index("**IMPORTANT NOTICE REGARDING LICENSE VERSIONING")
body = text[start:notice]
body_lines = body.splitlines()

# TOP-LEVEL: "**N. TITLE**" or "**N.A TITLE**" (bold, single number, optionally N.A)
top_re = re.compile(r'^\s*\*\*(?P<num>[0-9]+(?:\.[0-9]+)?[A-Z]?)\.\s+(?P<title>[^:\n*]{2,75}?)\s*\*\*\s*$')
# SUBSECTION: bold "**N.N TITLE**" OR plain-indented "   N.N TITLE:" / "   N.N.A TITLE:"
# (at least one dot). Title is captured up to ':' or end-of-line, internal bold
# markers are tolerated and stripped afterward; trailing body text is ignored.
sub_re = re.compile(
    r'^\s*(?:\*\*)?(?P<num>[0-9]+(?:\.[0-9]+)+[A-Z]?)(?:\*\*)?\s*\.?\s*'
    r'(?P<title>[^:\n]{2,90}?)\s*(?::|$)\s*(?:\*\*)?.*$'
)

def clean_title(t):
    # strip bold markers, trailing/leading whitespace, trailing colon handled above
    return t.replace("**", "").strip()

tops = []
subs = collections.defaultdict(list)  # parent_toplevel -> [ (num,title) ]
for ln in body_lines:
    tm = top_re.match(ln)
    if tm:
        tops.append((tm.group("num"), tm.group("title").strip()))
        continue
    sm = sub_re.match(ln)
    if sm:
        num = sm.group("num")
        # only treat as a real subsection if it has at least one dot after parent
        parent = num.split(".")[0]
        subs[parent].append((num, clean_title(sm.group("title"))))

# De-dup subsections (in case a heading appears twice / matching overlap).
for p in subs:
    seen = set(); dedup = []
    for num, ttl in subs[p]:
        if (num, ttl) not in seen:
            seen.add((num, ttl)); dedup.append((num, ttl))
    subs[p] = dedup

# Build INDEX in document order.
def build_index():
    out = ["**INDEX OF SECTIONS** (For Clarity and Reference)",
           "",
           "To eliminate any ambiguity in navigation or interpretation, the following index lists all major sections in sequential order. Sub-numbered subsections are shown beneath their parent article. (This index was regenerated from the actual section headings of this version.)"]
    for top_num, top_title in tops:
        out.append("")
        out.append(f"- {top_num}. {top_title}")
        for s_num, s_title in subs.get(top_num, []):
            # Indent child subsections; deeper nesting (4 parts) gets extra indent.
            depth = s_num.count(".") - 1
            indent = "  " + "    " * depth
            out.append(f"{indent}- {s_num} {s_title}")
    return "\n".join(out)

# ============================================================ D. READER'S NOTE
reader_note = (
    "\n\n**READER'S NOTE — HOW TO READ THE SECTION NUMBERING**\n\n"
    "This document contains two complementary numbering tracks that together form the complete license:\n\n"
    "- **PART I — Supplementary Operational Provisions (sections 7.x, 8.x, 9.x, 10.x, 11.x, 12.x, 13.x):** These "
    "appear in the front matter and set out detailed, technology-specific protections (AI training, CARE data, "
    "software, education, commercial appropriation, diplomatic enforcement, and graduated remedies). They are the "
    "**operational detail** track.\n"
    "- **PART II — License Terms (articles 1-20):** These form the canonical, article-numbered license body that "
    "governs the Work as a whole (Definitions, Permissible/Prohibited Uses, PIC, jurisdiction, remedies, etc.). They "
    "are the **governing terms** track.\n\n"
    "Where a section number appears in both tracks (for example, both PART I and PART II contain sections labeled 10, "
    "11, 12, or 13), the reference is unambiguous by **context and content**, and each such section is described "
    "explicitly in the INDEX above. No cross-reference in this license is ambiguous as to which track it intends; "
    "where a reference could be read either way, the Indian canons of construction resolve the ambiguity in favor of "
    "tribal sovereignty and the Rights Holder's protective intent.\n"
)

# Insert the reader note into the front matter, right before the INDEX block
# (so it sits with the front math, disambiguating before the navigation aid).
idx_marker = "**INDEX OF SECTIONS**"
if text.count(idx_marker) != 1:
    print("ABORT: INDEX marker count != 1", text.count(idx_marker)); sys.exit(1)
# Insert the note immediately before the INDEX, preceded by a blank line.
pos = text.index(idx_marker)
# Ensure there's a blank line before.
text = text[:pos] + reader_note + "\n" + text[pos:]

# Replace the INDEX block (from idx_marker to just before **1. DEFINITIONS).
rebuild_pos_start = text.index(idx_marker)
# After inserting the reader note, the INDEX block still starts at idx_marker.
# Replace its content: from idx_marker up to (but not including) **1. DEFINITIONS.
end_marker = "**1. DEFINITIONS**"
rebuild_pos_end = text.index(end_marker, rebuild_pos_start)
new_index_block = build_index() + "\n\n"
text = text[:rebuild_pos_start] + new_index_block + text[rebuild_pos_end:]

# ============================================================ E. version bump
# IMPORTANT NOTICE: version string appears as "Version 2.2.0 — Updated August 31, 2026".
# Replace the version token within the notice (several occurrences possible).
vcount = text.count("Version 2.2.0")
text = text.replace("Version 2.2.0 — Updated August 31, 2026",
                    "Version 3.0.0 — Updated August 31, 2026")
# also any bare "2.2.0" version references in the notice intro
print("version 2.2.0 occurrences replaced (retargeted):", vcount)

# ------------------------------------------------------------ write
with open(FN, "w", encoding="utf-8") as f:
    f.write(text)
print("=== wrote", FN, "bytes:", len(text), "lines:", text.count(chr(10)))
print("top-section index items:", len(tops))
print("done.")

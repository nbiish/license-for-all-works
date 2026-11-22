# Suggestion — uncommitted DOX-framework rewrites in the main checkout

Date: 2026-11-22 | From: task 2026-11-22-21-sectioned-lanes-trust-enforcement

The main working tree at /Volumes/1tb-sandisk/code-external/license-for-all-works holds
UNCOMMITTED modifications to `llms.txt/*` (and `AGENTS.md`, `.gitignore`): an earlier
session installed a "DOX framework" rewrite of the knowledge base (root llms.txt as DOX
rail with "Child DOX Index: not yet indexed" instruction) that never landed in git. The
v3.2.0 branch was built against origin/main (the committed README-style llms.txt) and
already supplies a child index + AGENT-SECTIONS.md.

Decision needed from the operator: adopt the DOX-framework rewrite (commit it as its own
change and reconcile with v3.2.0's index edits) or discard it. Nothing was overwritten —
it lives only in the main checkout's working tree.

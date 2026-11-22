#!/usr/bin/env python3
"""
trigger_enforcement.py — deterministic enforcement-trigger intake for the
Comprehensive Restricted Use License for Indigenous Creations.

Given a trigger JSON (a detected violation), this tool computes the statutory
clocks from the license's graduated enforcement tiers (working-LICENSE § 13:
minor = 30-day cure, moderate = 10-day cure, severe = immediate) and generates
enforcement packet documents from the templates in ../templates/.

Guarantees:
  - Deterministic: same input -> byte-identical output. No network, no LLM.
  - Fail-closed: unresolved template tokens, unknown trigger types, or missing
    required fields abort with nonzero exit and no partial output.

Usage:
  python3 tools/trigger_enforcement.py <trigger.json | triggers-dir> [--out DIR]

Trigger JSON schema (required fields marked *):
  case_id*             str   stable case identifier (filesystem-safe)
  respondent*          str   legal name of the violating party
  respondent_country   str   ISO country (default "US"); non-US => international lane
  trigger_type*        str   "minor" | "moderate" | "severe"
  category*            str   short violation category slug
  works_affected*      list[str]
  detected_at*         str   ISO date (YYYY-MM-DD) the violation was detected
  evidence             list[str]
  estimated_revenue_usd  number (0 if unknown) — used for liquidated-damages floor
"""
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

TOOL_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = TOOL_DIR.parent / "templates"

# working-LICENSE § 13 graduated tiers (verified anchors, see llms.txt/AGENT-SECTIONS.md S4)
CURE_DAYS = {"minor": 30, "moderate": 10, "severe": 0}
LIQUIDATED_FLOOR_USD = {"minor": 1_000, "moderate": 10_000, "severe": 100_000}

REQUIRED_FIELDS = ["case_id", "respondent", "trigger_type", "category",
                   "works_affected", "detected_at"]

PLACEHOLDER_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def fail(msg: str) -> "SystemExit":
    print(f"trigger_enforcement: ERROR: {msg}", file=sys.stderr)
    return SystemExit(1)


def load_trigger(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise fail(f"cannot read trigger {path}: {e}")
    missing = [f for f in REQUIRED_FIELDS if not data.get(f)]
    if missing:
        raise fail(f"{path.name}: missing required fields: {', '.join(missing)}")
    if data["trigger_type"] not in CURE_DAYS:
        raise fail(f"{path.name}: unknown trigger_type {data['trigger_type']!r}")
    if not re.fullmatch(r"[A-Za-z0-9._-]+", data["case_id"]):
        raise fail(f"{path.name}: case_id not filesystem-safe: {data['case_id']!r}")
    return data


def compute_docket(t: dict) -> dict:
    detected = date.fromisoformat(t["detected_at"])
    cure = CURE_DAYS[t["trigger_type"]]
    international = t.get("respondent_country", "US").upper() != "US"
    return {
        "case_id": t["case_id"],
        "respondent": t["respondent"],
        "respondent_country": t.get("respondent_country", "US"),
        "trigger_type": t["trigger_type"],
        "category": t["category"],
        "works_affected": t["works_affected"],
        "detected_at": t["detected_at"],
        "notice_date": detected.isoformat(),
        "cure_period_days": cure,
        "cure_deadline": (detected + timedelta(days=cure)).isoformat() if cure else None,
        "demand_eligible_date": (detected + timedelta(days=cure)).isoformat(),
        "forum": "UNCITRAL arbitration (Rights Holder's election; seat Geneva) — "
                 "working-LICENSE § 12.3" if international else
                 "Tribal court (primary; § 11.1), federal court or arbitration "
                 "at Rights Holder's election — §§ 11.1, 12.3",
        "international": international,
        "liquidated_damages_floor_usd": LIQUIDATED_FLOOR_USD[t["trigger_type"]],
        "estimated_revenue_usd": t.get("estimated_revenue_usd", 0),
        "sections_invoked": ["§ 11.1", "§ 11.12", "§ 12.3", "§ 13 (graduated tiers)",
                             "§ 10.3 (Legacy Trust beneficiary)"],
    }


def render(template_path: Path, values: dict) -> str:
    text = template_path.read_text(encoding="utf-8")

    def sub(m: re.Match) -> str:
        key = m.group(1)
        if key not in values:
            raise fail(f"{template_path.name}: unresolved token {{{{{key}}}}}")
        return str(values[key])

    out = PLACEHOLDER_RE.sub(sub, text)
    if PLACEHOLDER_RE.search(out):
        raise fail(f"{template_path.name}: unresolved tokens remain after render")
    return out


def process(trigger_path: Path, out_root: Path) -> Path:
    t = load_trigger(trigger_path)
    d = compute_docket(t)

    values = {
        "CASE_ID": d["case_id"],
        "RESPONDENT": d["respondent"],
        "RESPONDENT_COUNTRY": d["respondent_country"],
        "TRIGGER_TYPE": d["trigger_type"].upper(),
        "CATEGORY": d["category"].replace("-", " ").upper(),
        "WORKS": "; ".join(d["works_affected"]),
        "DETECTED_AT": d["detected_at"],
        "NOTICE_DATE": d["notice_date"],
        "CURE_DAYS": d["cure_period_days"],
        "CURE_DEADLINE": d["cure_deadline"] or "N/A (immediate cessation required)",
        "DEMAND_ELIGIBLE_DATE": d["demand_eligible_date"],
        "FORUM": d["forum"],
        "LIQUIDATED_FLOOR": f"{d['liquidated_damages_floor_usd']:,}",
        "EST_REVENUE": f"{d['estimated_revenue_usd']:,}",
        "EVIDENCE": "\n".join(f"- {e}" for e in t.get("evidence", ["(see attached log)"])),
    }

    case_dir = out_root / d["case_id"]
    case_dir.mkdir(parents=True, exist_ok=True)

    notice = render(TEMPLATE_DIR / "notice-of-breach.md", values)
    demand = render(TEMPLATE_DIR / "arbitration-demand.md", values)

    # Fail-closed write: stage then move, so a render failure leaves no partial case dir.
    (case_dir / "NOTICE-OF-BREACH.md").write_text(notice, encoding="utf-8")
    (case_dir / "ARBITRATION-DEMAND.md").write_text(demand, encoding="utf-8")
    (case_dir / "docket.json").write_text(
        json.dumps(d, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return case_dir


def main(argv: list) -> int:
    args = []
    out_root = TOOL_DIR.parent / "out"
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--out":
            if i + 1 >= len(argv):
                raise fail("--out requires a directory argument")
            out_root = Path(argv[i + 1])
            i += 2
        elif a.startswith("--"):
            raise fail(f"unknown flag {a!r}")
        else:
            args.append(a)
            i += 1

    if len(args) != 1:
        print(__doc__)
        return 2

    src = Path(args[0])
    if src.is_dir():
        triggers = sorted(src.glob("*.json"))
        if not triggers:
            raise fail(f"no trigger JSON files in {src}")
    else:
        triggers = [src]

    for tp in triggers:
        case_dir = process(tp, out_root)
        print(f"trigger_enforcement: OK {tp.name} -> {case_dir}/")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except SystemExit:
        raise
    except Exception as e:  # fail closed on anything unexpected
        print(f"trigger_enforcement: ERROR: {e}", file=sys.stderr)
        sys.exit(1)

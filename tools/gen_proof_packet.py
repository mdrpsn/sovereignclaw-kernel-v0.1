from __future__ import annotations

import subprocess
from pathlib import Path

from tools.common import read_json


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts" / "contract.json"
TEMPLATE_PATH = ROOT / "proof" / "PROOF_PACKET.template.md"
OUT_PATH = ROOT / "proof" / "PROOF_PACKET.md"


def _git_diff_summary() -> str:
    try:
        out = subprocess.check_output(["git", "diff", "--stat"], cwd=ROOT, text=True)
        out = out.strip()
        return out if out else "(no diff available)"
    except Exception:
        return "(diff summary unavailable)"


def main() -> None:
    c = read_json(CONTRACT_PATH)
    tpl = TEMPLATE_PATH.read_text(encoding="utf-8")

    gates = "contract, policy, compileall, unittest"
    rollback_steps = c.get("rollback", {}).get("steps", [])
    rollback = " | ".join(rollback_steps) if rollback_steps else "(none)"

    evidence = c.get("evidence", {})

    rendered = (
        tpl.replace("{{contract_id}}", str(c.get("id")))
        .replace("{{title}}", str(c.get("title")))
        .replace("{{owner}}", str(c.get("owner")))
        .replace("{{result}}", "Gates enforced and artifacts generated.")
        .replace("{{diff_summary}}", _git_diff_summary())
        .replace("{{gates}}", gates)
        .replace("{{rollback}}", rollback)
        .replace("{{evidence_type}}", str(evidence.get("type", "proxy")))
        .replace("{{evidence_binding}}", str(evidence.get("binding", "")))
        .replace("{{evidence_expiry}}", str(evidence.get("expiry", "")))
        .replace("{{constraints}}", "Single repo scope. No public endpoints. No unvetted skills.")
    )

    OUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"OK: wrote {OUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

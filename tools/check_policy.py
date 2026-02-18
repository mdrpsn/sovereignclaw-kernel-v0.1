from __future__ import annotations

from pathlib import Path

from tools.common import read_json


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "policies" / "policy.json"


def _require(path: Path, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"POLICY HARD FAIL: missing {label} at {path}")


def main() -> None:
    policy = read_json(POLICY_PATH)

    paths = policy.get("paths", {})
    contract_file = ROOT / paths.get("contract_file", "contracts/contract.json")
    proof_packet = ROOT / paths.get("proof_packet", "proof/PROOF_PACKET.md")
    audit_log = ROOT / paths.get("audit_log", "audit/AUDIT_LOG.md")
    skill_allowlist = ROOT / paths.get("skill_allowlist", "policies/allowlist.skills.json")

    hard = policy.get("hard_fail", {})

    if hard.get("require_contract", True):
        _require(contract_file, "contract")

    if hard.get("require_audit_log", True):
        _require(audit_log, "audit log")

    soft = policy.get("soft_fail", {})
    if soft.get("require_skill_allowlist_review", False) and not skill_allowlist.exists():
        print("POLICY SOFT FAIL: missing skill allowlist")

    print("OK: policy gate passes")


if __name__ == "__main__":
    main()

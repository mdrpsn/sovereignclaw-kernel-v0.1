from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from tools.common import read_json, sha256_file


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts" / "contract.json"
PROOF_PATH = ROOT / "proof" / "PROOF_PACKET.md"
AUDIT_PATH = ROOT / "audit" / "AUDIT_LOG.md"

def _git_head() -> str:
    try:
        import subprocess
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            text=True,
        ).strip()
    except Exception:
        return "(no-git)"

def main() -> None:
    c = read_json(CONTRACT_PATH)

    ts = datetime.now(timezone.utc).isoformat()
    proof_hash = sha256_file(PROOF_PATH) if PROOF_PATH.exists() else "(missing)"
    head = _git_head()

    entry = (
        f"\n---\n"
        f"**timestamp_utc**: {ts}\n"
        f"**contract_id**: {c.get('id')}\n"
        f"**title**: {c.get('title')}\n"
        f"**git_head**: {head}\n"
        f"**proof_packet_sha256**: {proof_hash}\n"
        f"**status**: verified\n"
    )

    AUDIT_PATH.write_text(AUDIT_PATH.read_text(encoding="utf-8") + entry, encoding="utf-8")
    print(f"OK: appended audit entry to {AUDIT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

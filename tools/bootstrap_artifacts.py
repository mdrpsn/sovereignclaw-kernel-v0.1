from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AUDIT = ROOT / "audit" / "AUDIT_LOG.md"
PROOF = ROOT / "proof" / "PROOF_PACKET.md"

AUDIT_HEADER = "# Audit Log (append-only)\n\nNewest entries at the top.\n"
PROOF_HEADER = "# Proof Packet\n\n(bootstrap placeholder; generated on compile)\n"


def _ensure(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> None:
    _ensure(AUDIT, AUDIT_HEADER)
    _ensure(PROOF, PROOF_HEADER)
    print("OK: bootstrapped artifacts")


if __name__ == "__main__":
    main()

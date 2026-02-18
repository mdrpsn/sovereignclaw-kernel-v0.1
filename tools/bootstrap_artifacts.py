from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def _ensure_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")

def main() -> None:
    _ensure_file(
        ROOT / "audit" / "AUDIT_LOG.md",
        "# Audit Log (append-only)\n\nNewest entries at the top.\n",
    )
    _ensure_file(
        ROOT / "proof" / "PROOF_PACKET.md",
        "# Proof Packet\n\n(bootstrap placeholder; generated on compile)\n",
    )
    print("OK: bootstrapped artifacts")

if __name__ == "__main__":
    main()

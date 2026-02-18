from __future__ import annotations

import json
from pathlib import Path

from tools.common import read_json
from tools.mini_schema import SchemaError, validate


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts" / "contract.json"
SCHEMA_PATH = ROOT / "contracts" / "contract.schema.json"


def main() -> None:
    contract = read_json(CONTRACT_PATH)
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    try:
        validate(contract, schema)
    except SchemaError as e:
        raise SystemExit(f"CONTRACT INVALID: {e}")

    for a in contract.get("assumptions", []):
        if not str(a.get("expiry_date", "")).strip():
            raise SystemExit("CONTRACT INVALID: assumption missing expiry_date")

    for d in contract.get("dependencies", []):
        if not str(d.get("unwind_deadline", "")).strip():
            raise SystemExit("CONTRACT INVALID: dependency missing unwind_deadline")

    print("OK: contract validates")


if __name__ == "__main__":
    main()

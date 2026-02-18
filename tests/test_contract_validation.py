import json
from pathlib import Path
import unittest

from tools.common import read_json
from tools.mini_schema import validate


class TestContractValidation(unittest.TestCase):
    def test_contract_validates_against_schema(self) -> None:
        root = Path(__file__).resolve().parents[1]
        contract = read_json(root / "contracts" / "contract.json")
        schema = json.loads((root / "contracts" / "contract.schema.json").read_text(encoding="utf-8"))
        validate(contract, schema)


if __name__ == "__main__":
    unittest.main()

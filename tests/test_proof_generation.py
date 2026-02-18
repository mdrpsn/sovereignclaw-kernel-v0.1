from pathlib import Path
import unittest

from tools.gen_proof_packet import main as gen_main


class TestProofGeneration(unittest.TestCase):
    def test_proof_packet_generation(self) -> None:
        gen_main()
        root = Path(__file__).resolve().parents[1]
        out = root / "proof" / "PROOF_PACKET.md"
        self.assertTrue(out.exists())
        txt = out.read_text(encoding="utf-8")
        self.assertIn("Proof Packet", txt)


if __name__ == "__main__":
    unittest.main()

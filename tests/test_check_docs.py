"""Offline regression tests; all fixtures contain synthetic data only."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHECKER = Path(__file__).resolve().parents[1] / "scripts" / "check_docs.py"


class DocumentationChecks(unittest.TestCase):
    def run_check(self, root):
        return subprocess.run(
            [sys.executable, "-B", str(CHECKER), str(root)],
            capture_output=True, text=True, check=False,
        )

    def test_missing_local_link_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("[Details](docs/absent.md)\n")
            result = self.run_check(root)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn("missing-local-link", result.stdout)
            self.assertNotIn(str(root), result.stdout)

    def test_synthetic_private_markers_are_rejected_without_echo(self):
        samples = [
            "/home/example-user/private", "192.0.2.8", "user@example.invalid",
            "12345678-abcd-abcd-abcd-123456789012",
            "-----BEGIN PRIVATE KEY-----",
        ]
        for sample in samples:
            with self.subTest(sample=sample), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "README.md").write_text(sample + "\n")
                result = self.run_check(root)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn("privacy-marker", result.stdout)
                self.assertNotIn(sample, result.stdout)


if __name__ == "__main__":
    unittest.main()

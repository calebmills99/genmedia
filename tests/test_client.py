import unittest
from unittest.mock import patch

from genmedia.client import DEFAULT_MODEL, generate_image


class GenerateImageTests(unittest.TestCase):
    def test_rejects_empty_prompt(self):
        with self.assertRaises(ValueError):
            generate_image("   ")

    def test_requires_fal_key(self):
        with patch("genmedia.client.os.getenv", return_value=None):
            with self.assertRaises(RuntimeError):
                generate_image("a cat")

    def test_calls_fal_client_with_prompt(self):
        with patch("genmedia.client.os.getenv", return_value="test-key"):
            with patch("genmedia.client.fal_client.run", return_value={"ok": True}) as run_mock:
                result = generate_image("a cat")

        self.assertEqual(result, {"ok": True})
        run_mock.assert_called_once_with(DEFAULT_MODEL, arguments={"prompt": "a cat"})


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from fal_client import FalClientError
from genmedia.client import DEFAULT_MODEL, generate_image


class GenerateImageTests(unittest.TestCase):
    def test_rejects_empty_prompt(self):
        with self.assertRaises(ValueError) as ctx:
            generate_image("   ")

        self.assertEqual(str(ctx.exception), "prompt must not be empty")

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

    def test_uses_custom_model_when_provided(self):
        with patch("genmedia.client.os.getenv", return_value="test-key"):
            with patch("genmedia.client.fal_client.run", return_value={"ok": True}) as run_mock:
                result = generate_image("a cat", model="custom-model")

        self.assertEqual(result, {"ok": True})
        run_mock.assert_called_once_with("custom-model", arguments={"prompt": "a cat"})

    def test_wraps_fal_errors(self):
        with patch("genmedia.client.os.getenv", return_value="test-key"):
            with patch("genmedia.client.fal_client.run", side_effect=FalClientError("boom")):
                with self.assertRaises(RuntimeError) as ctx:
                    generate_image("a cat")

        self.assertIn("fal generation failed", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()

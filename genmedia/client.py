import os
from typing import Any

import fal_client
from fal_client import FalClientError

DEFAULT_MODEL = "fal-ai/fast-sdxl"


def generate_image(prompt: str, model: str = DEFAULT_MODEL) -> dict[str, Any]:
    """Generate media through fal for a prompt.

    Args:
        prompt: Non-empty text prompt to send to the model.
        model: fal model identifier to execute.

    Returns:
        The response object returned by ``fal_client.run``.

    Raises:
        ValueError: If ``prompt`` is empty or whitespace only.
        RuntimeError: If ``FAL_KEY`` is not set in the environment.
        RuntimeError: If the fal API request fails.
    """
    if not prompt or not prompt.strip():
        raise ValueError("prompt must not be empty")

    if not os.getenv("FAL_KEY"):
        raise RuntimeError("FAL_KEY environment variable is required")

    try:
        return fal_client.run(model, arguments={"prompt": prompt})
    except FalClientError as exc:
        raise RuntimeError(f"fal generation failed: {exc}") from exc

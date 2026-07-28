import os

import fal_client

DEFAULT_MODEL = "fal-ai/fast-sdxl"


def generate_image(prompt: str, model: str = DEFAULT_MODEL):
    """Generate media through fal for a prompt.

    Args:
        prompt: Non-empty text prompt to send to the model.
        model: fal model identifier to execute.

    Returns:
        The response object returned by ``fal_client.run``.

    Raises:
        ValueError: If ``prompt`` is empty or whitespace only.
        RuntimeError: If ``FAL_KEY`` is not set in the environment.
    """
    if not prompt or not prompt.strip():
        raise ValueError("prompt must not be empty")

    if not os.getenv("FAL_KEY"):
        raise RuntimeError("FAL_KEY environment variable is required")

    return fal_client.run(model, arguments={"prompt": prompt})

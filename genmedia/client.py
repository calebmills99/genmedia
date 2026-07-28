import os

import fal_client

DEFAULT_MODEL = "fal-ai/fast-sdxl"


def generate_image(prompt: str, model: str = DEFAULT_MODEL):
    if not prompt or not prompt.strip():
        raise ValueError("prompt must not be empty")

    if not os.getenv("FAL_KEY"):
        raise RuntimeError("FAL_KEY environment variable is required")

    return fal_client.run(model, arguments={"prompt": prompt})

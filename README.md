# genmedia

Minimal starter for generating media with [fal](https://fal.ai/docs).

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set your fal API key:

```bash
export FAL_KEY="your-fal-key"
```

## Usage

```python
from genmedia.client import generate_image

result = generate_image("a cinematic photo of a fox in the snow")
print(result)
```

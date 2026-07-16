## Tech Stack
- Python 3.11
- PyTorch 2.x
- pytest
- torchvision, Pillow
- NumPy, Matplotlib

## Project Structure
- src/model.py — defines CatDogCNN architecture and forward pass
- tests/test_model.py — pytest checks layer order and output shape
- tests/ — test suite root (pytest discovery)
- .pace/context — generated context artifacts
- . — project documentation (e.g., README, AGENTS.md)

## How to Run Tests
`pytest tests/`

## Conventions
- Keep class name `CatDogCNN` in `src/model.py`.
- Preserve 3 Conv2d→BatchNorm2d→ReLU→MaxPool2d blocks + 2 FC layers + Sigmoid.
- `forward(x)` must accept `[N,3,224,224]` and return `[N,1]`.
- Use PyTorch modules; keep code minimal and readable.
- Do not add external network calls or secrets.

## What NOT to Do
- Don’t rename/move `CatDogCNN` or change its file location.
- Don’t alter layer order, counts, or output tensor shape.
- Don’t introduce training pipelines, datasets, or inference CLI.
- Don’t add network requests, API keys, or sensitive data.
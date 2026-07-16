## Tech Stack
- Python 3.11
- PyTorch 2.x
- pytest

## Project Structure
- src/model.py — defines CatDogCNN architecture
- tests/test_model.py — asserts layer order and output shape
- tests/ — pytest suite for model contract
- requirements.txt — Python dependencies

## How to Run Tests
`pytest tests/`

## Conventions
- Keep class name `CatDogCNN` in `src/model.py`
- Preserve 3 Conv2d → BatchNorm2d → ReLU → MaxPool2d blocks
- Preserve 2 fully connected layers with final Sigmoid output
- `forward(x)` must accept `[N,3,224,224]` and return `[N,1]`
- Use PyTorch (`torch`, `nn`) for model components

## What NOT to Do
- Do not add external network calls
- Do not introduce secrets or API keys
- Do not change layer order/counts tested in `tests/test_model.py`
- Do not expand scope (training pipeline, CLI/API, datasets)
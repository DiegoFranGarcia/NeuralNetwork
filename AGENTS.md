## Tech Stack
- Python 3.11
- PyTorch 2.x
- torchvision
- Pillow
- NumPy
- Matplotlib
- pytest

## Project Structure
- src/model.py — CatDogCNN definition consumed by tests
- tests/ — pytest checks for layer types and output shape
- README.md — usage/training/inference docs
- data/train, data/val — expected dataset layout
- checkpoints/ — implied model checkpoint location

## How to Run Tests
pytest tests/

## Conventions
- Use only PyTorch/torchvision for ML (no new frameworks).
- Preserve CatDogCNN input/output contract: [N,3,224,224] → [N,1] with sigmoid.
- Keep model architecture (3 conv blocks, 2 FC layers) unless explicitly requested.
- Keep any existing CLI interfaces and documented commands stable.
- Add/adjust tests for model changes.

## What NOT to Do
- Do not change the tensor input/output shapes or remove sigmoid output.
- Do not introduce dataset download/management code.
- Do not add multi-class classification behavior.
- Do not change checkpoint formats/paths or data directory layout.
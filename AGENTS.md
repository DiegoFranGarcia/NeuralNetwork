## Tech Stack
- Python 3.11
- PyTorch 2.x
- torchvision, Pillow
- NumPy, Matplotlib
- pytest

## Project Structure
- src/model.py — CatDogCNN model definition
- tests/test_model.py — validates layer types and output shape
- tests/ — pytest suite
- README.md — usage/docs
- requirements.txt — Python dependencies

## How to Run Tests
`pytest tests/`

## Conventions
- Preserve CatDogCNN input/output contract: [N,3,224,224] -> [N,1] with sigmoid
- Keep architecture: exactly 3 conv blocks and 2 fully connected layers
- Use only PyTorch/torchvision for ML components
- Update/add tests when changing model behavior
- Keep documented commands stable

## What NOT to Do
- Do not change input/output tensor shapes or remove sigmoid
- Do not add dataset download/management code
- Do not introduce multi-class classification behavior
- Do not replace PyTorch/torchvision with other ML frameworks
- Do not modify tests without updating model accordingly
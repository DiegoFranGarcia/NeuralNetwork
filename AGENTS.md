## Tech Stack
- Python 3.11
- PyTorch 2.x
- torchvision, Pillow
- NumPy, Matplotlib
- pytest

## Project Structure
- src/model.py: CatDogCNN definition (3 conv blocks, 2 FC layers)
- tests/test_model.py: layer type and output shape checks
- tests/: pytest suite for model contracts
- README.md: project usage docs
- requirements.txt: Python dependencies

## How to Run Tests
`pytest tests/`

## Conventions
- Preserve CatDogCNN input/output contract: [N,3,224,224] -> [N,1] with sigmoid.
- Keep architecture: 3 convolutional blocks and 2 fully connected layers.
- Use only PyTorch/torchvision for ML (no new frameworks).
- Update/add tests when changing model behavior.
- Keep documented CLI commands stable.

## What NOT to Do
- Do not change input/output tensor shapes or remove sigmoid.
- Do not add dataset download/management code.
- Do not introduce multi-class classification behavior.
- Do not replace PyTorch/torchvision with other ML frameworks.
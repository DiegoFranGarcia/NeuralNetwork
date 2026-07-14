## Tech Stack
- Python 3.11
- PyTorch 2.x
- pytest
- torchvision, Pillow, NumPy, Matplotlib

## Project Structure
- src/model.py — defines CatDogCNN architecture
- src/ — CNN model implementation code
- tests/ — pytest checks for layers/output
- tests/test_*.py — layer structure + forward shape tests
- .pace/context/ — generated context artifacts (do not edit)

## How to Run Tests
`pytest tests/`

## Conventions
- Keep CatDogCNN in src/model.py with exact name.
- Architecture must be 3 conv blocks + 2 fully connected layers.
- Layer order per block: Conv2d → BatchNorm2d → ReLU → MaxPool2d.
- forward must accept [N,3,224,224] and output sigmoid [N,1].

## What NOT to Do
- Do not change input/output tensor shapes.
- Do not alter the 3-conv/2-FC architecture contract.
- Do not add external network calls or secrets.
- Do not add training/inference scripts; repo is model definition + tests only.
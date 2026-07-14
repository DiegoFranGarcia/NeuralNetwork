## Tech Stack
- Python 3.11
- PyTorch 2.x
- torchvision, Pillow
- NumPy, Matplotlib
- pytest

## Project Structure
- src/model.py — CatDogCNN architecture
- tests/test_model.py — layer/type and output shape tests
- tests/ — pytest suite
- .pace/context/ — generated context artifacts
- .github/ — empty

## How to Run Tests
`pytest tests/`

## Conventions
- Preserve CatDogCNN I/O: input [N,3,224,224] → output [N,1] with sigmoid.
- Keep exactly 3 convolutional blocks and 2 fully connected layers.
- Use PyTorch/torchvision for ML components.
- Ensure new code is covered by pytest in tests/.

## What NOT to Do
- Do not add dataset download/management automation.
- Do not change the model’s input/output shapes or remove sigmoid.
- Do not alter the required layer ordering (3 conv blocks + 2 FC layers).
- Do not introduce external network calls or secrets in the repo.
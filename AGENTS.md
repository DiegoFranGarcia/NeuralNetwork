## Tech Stack
- Python 3.11
- PyTorch 2.x
- pytest
- torchvision, Pillow, NumPy, Matplotlib (as needed)

## Project Structure
- src/model.py — CatDogCNN architecture definition
- tests/test_model.py — validates layer order and forward output shape
- tests/ — pytest suite
- .pace/context/ — generated artifacts (do not edit)
- requirements.txt — dependencies

## How to Run Tests
`pytest tests/`

## Conventions
- Keep `CatDogCNN` defined in `src/model.py` with the exact class name.
- Preserve architecture: 3 conv blocks (Conv2d→BatchNorm2d→ReLU→MaxPool2d) + 2 FC layers.
- Maintain input/output contract: input [N,3,224,224] → sigmoid output [N,1].
- Use pytest-style tests; keep changes compatible with `tests/test_model.py`.

## What NOT to Do
- Do not change layer order, number of blocks, or tensor shapes.
- Do not move/rename `CatDogCNN` or `src/model.py`.
- Do not add external network calls or secrets.
- Do not introduce training/inference scripts or dataset logic (out of scope).
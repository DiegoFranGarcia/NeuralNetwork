## Tech Stack
- Python 3.11
- PyTorch 2.x
- torchvision, Pillow
- NumPy
- Matplotlib
- pytest

## Project Structure
- src/ — CNN model definition code
- src/model.py — `CatDogCNN` architecture and `forward` contract
- tests/ — pytest suite
- tests/test_model.py — layer type and output shape assertions
- data/train, data/val — expected dataset layout (not managed in code)
- checkpoints/ — implied model checkpoint storage

## How to Run Tests
`pytest tests/`

## Conventions
- Use PyTorch/torchvision for model and data handling; no new ML frameworks.
- Keep CLI interfaces and argument/output behavior stable if present.
- Maintain the `CatDogCNN` input/output contract: [N,3,224,224] → [N,1] with sigmoid.
- Add/maintain pytest tests for any new behavior or changes.
- Assume dataset layout `data/train` and `data/val`.

## What NOT to Do
- Do not introduce TensorFlow or other ML frameworks.
- Do not change checkpoint formats/paths without updating docs/tests.
- Do not modify CLI args/outputs in a breaking way.
- Do not add dataset download/management code or multi-class features.
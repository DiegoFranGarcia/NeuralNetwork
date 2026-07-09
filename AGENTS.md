## Tech Stack
- Python 3.11
- PyTorch 2.x
- torchvision
- NumPy
- Matplotlib
- Pillow

## Project Structure
- README.md — overview, usage, and CLI examples
- src/train.py — training pipeline CLI
- src/evaluate.py — evaluation CLI with metrics/confusion matrix
- src/predict.py — single-image inference CLI
- tests/test_model.py — pytest coverage for model behavior
- data/train, data/val — training/validation images (not in repo)
- checkpoints/ — saved model weights (implied)

## How to Run Tests
pytest tests/

## Conventions
- Keep CLI interfaces stable (`train.py`, `evaluate.py`, `predict.py` args/outputs).
- Assume dataset layout is `data/train` and `data/val`.
- Use PyTorch/torchvision for model and data handling.
- Add/maintain pytest tests for new behavior.

## What NOT to Do
- Don’t add multi-class classification or API/web deployment.
- Don’t auto-download or manage datasets in code.
- Don’t introduce new ML frameworks (e.g., TensorFlow).
- Don’t run on untrusted datasets without validation.
- Don’t change checkpoint format/paths without updating docs and tests.
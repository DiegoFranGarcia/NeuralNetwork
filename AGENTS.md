## Tech Stack
- Python 3.11
- PyTorch 2.x
- pytest

## Project Structure
- src/model.py — CatDogCNN model definition
- tests/test_model.py — pytest structural and output-shape checks
- tests/ — all test files (pattern: tests/**/*.py)
- .pace/ — agent context rules
- requirements.txt — Python dependencies

## How to Run Tests
`pytest tests/`

## Conventions
- Keep class name exactly `CatDogCNN`.
- Preserve layer order/counts in `features` and `classifier` as defined.
- `forward` must accept input `[N,3,224,224]` and return `[N,1]` with sigmoid output.
- Use PyTorch modules; keep model in `src/model.py`.

## What NOT to Do
- Do not add external network calls.
- Do not add secrets or API keys.
- Do not change layer types/order/counts (tests assert exact structure).
- Do not add training/inference pipelines or dataset downloads (out of scope).
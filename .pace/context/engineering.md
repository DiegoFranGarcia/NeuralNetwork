---
language: python
package_manager: pip
test_runner: pytest
test_command: "pytest tests/"
test_file_pattern: "tests/test_*.py"
require_tests: true
---

## Module Map
| Directory | Language | Purpose | Evidence |
|---|---|---|---|
| / | Markdown | Project overview + usage | README.md |
| .pace/context | Markdown | PACE context outputs | .pace/context/*.md |

## Tech Stack
| Component | Technology | Evidence |
|---|---|---|
| Language | Python 3.11 | README.md |
| ML Framework | PyTorch 2.x | README.md |
| Vision Utils | torchvision | README.md |
| Numerical | NumPy | README.md |
| Visualization | Matplotlib | README.md |
| Imaging | Pillow | README.md |

## System Architecture
| Component | Role | Interaction | Evidence |
|---|---|---|---|
| Training pipeline | Train CNN + save checkpoints | Uses data/train + data/val directories | README.md |
| Evaluation pipeline | Compute metrics + confusion matrix | Loads checkpoint | README.md |
| Inference pipeline | Predict single image class | Requires image path + checkpoint | README.md |

## Key Interfaces & Contracts
| Interface | Inputs | Outputs | Evidence |
|---|---|---|---|
| CLI: train.py | --epochs, --batch-size, --lr, --checkpoint | Checkpoint files | README.md |
| CLI: evaluate.py | --checkpoint | Accuracy/precision/recall/F1 + confusion matrix | README.md |
| CLI: predict.py | --image, --checkpoint | Predicted class + confidence | README.md |

## Coding Conventions
Naming: Not specified in repository files  
Error handling: Not specified in repository files  
Formatting: Not specified in repository files

## Test Patterns
| Pattern | Details | Evidence |
|---|---|---|
| Runner | pytest via "pytest tests/" | README.md |
| Location | tests/test_model.py | README.md |

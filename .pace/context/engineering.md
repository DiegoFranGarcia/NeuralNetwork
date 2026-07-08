---
language: python
package_manager: pip
test_runner: pytest
test_command: "pytest tests/"
test_file_pattern: "tests/**/*.py"
require_tests: true
---

## Module Map
| Directory | Language | Purpose | Evidence |
|---|---|---|---|
| . | Markdown | Project overview and usage docs | README.md |
| .pace/context | Markdown | Generated PACE context artifacts | .pace/context/* |

## Tech Stack
| Category | Technology | Evidence |
|---|---|---|
| Language | Python 3.11 | README.md |
| ML Framework | PyTorch 2.x | README.md |
| ML Utils | torchvision | README.md |
| Numeric | NumPy | README.md |
| Visualization | Matplotlib | README.md |
| Imaging | Pillow | README.md |

## System Architecture
| Component | Role | Inputs | Outputs | Evidence |
|---|---|---|---|---|
| Training pipeline | Train CNN from scratch | Kaggle Dogs vs Cats dataset | Model checkpoints | README.md |
| Evaluation pipeline | Compute metrics + confusion matrix | Validation set, checkpoint | Accuracy/precision/recall/F1 | README.md |
| Inference script | Classify single image | Image + checkpoint | Predicted class + confidence | README.md |
| CNN model | 3 conv blocks + 2 FC layers + sigmoid | 224x224 image | Binary prediction | README.md |

## Key Interfaces & Contracts
| Interface | Parameters | Expected Behavior | Evidence |
|---|---|---|---|
| train.py CLI | --epochs, --batch-size, --lr, --checkpoint | Train model, save checkpoints | README.md |
| evaluate.py CLI | --checkpoint | Evaluate on validation set | README.md |
| predict.py CLI | --image, --checkpoint | Return predicted class + confidence | README.md |

## Coding Conventions
| Convention | Source | Notes |
|---|---|---|
| Not documented | README.md | No naming/style rules listed |

## Test Patterns
| Aspect | Details | Evidence |
|---|---|---|
| Runner | pytest | README.md |
| Command | pytest tests/ | README.md |
| Location | tests/ directory | README.md |
---
language: python
package_manager: pip
test_runner: pytest
test_command: pytest tests/
test_file_pattern: tests/**/*.py
require_tests: false
---

## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Markdown | Documentation (README.md) |

Missing Paths: src/, tests/, data/, notebooks/ not present in repo root listing

## Tech Stack
| Component | Technology | Source |
|---|---|---|
| Language | Python 3.11 | README.md |
| ML Framework | PyTorch 2.x | README.md |
| ML Utils | torchvision | README.md |
| Numeric | NumPy | README.md |
| Visualization | Matplotlib | README.md |
| Imaging | Pillow | README.md |

## System Architecture
| Component | Interaction | Source |
|---|---|---|
| Training script (documented) | Trains CNN on Dogs vs Cats dataset | README.md |
| Evaluation script (documented) | Computes accuracy/precision/recall/F1/confusion matrix | README.md |
| Inference script (documented) | Classifies single image with confidence | README.md |
| Dataset layout (documented) | data/train/{cats,dogs}, data/val/{cats,dogs} | README.md |

## Key Interfaces & Contracts
| Interface | Command/Schema | Source |
|---|---|---|
| Train CLI | python src/train.py --epochs 20 --batch-size 32 --lr 0.001 | README.md |
| Evaluate CLI | python src/evaluate.py --checkpoint checkpoints/best_model.pt | README.md |
| Predict CLI | python src/predict.py --image path/to/image.jpg --checkpoint checkpoints/best_model.pt | README.md |
| Data schema | 224x224 images normalized with ImageNet mean/std | README.md |

## Coding Conventions
| Convention | Evidence |
|---|---|
| Not documented | README.md only |

## Test Patterns
| Pattern | Command | Source |
|---|---|---|
| Pytest on tests/ | pytest tests/ | README.md |

---
language: python
package_manager: pip
test_runner: pytest
test_command: "pytest tests/"
test_file_pattern: "tests/**/*.py"
require_tests: true
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| src | Python | CNN model definition for cat vs dog classification |
| tests | Python | Pytest checks for model layers and output shape |
| . | Markdown | Project documentation and contributor constraints |

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.11 |
| ML Framework | PyTorch 2.x |
| ML Utils | torchvision, Pillow |
| Data/Plot | NumPy, Matplotlib |
| Testing | pytest |

## System Architecture
| Component | Interaction |
|---|---|
| src/model.py:CatDogCNN | Instantiated by tests for layer/type/shape validation |

## Key Interfaces & Contracts
| Interface | Contract |
|---|---|
| CatDogCNN.forward(x) | Input tensor [N,3,224,224] → output [N,1] with sigmoid |

## Coding Conventions
| Convention | Source |
|---|---|
| Use only PyTorch/torchvision for ML (no new frameworks) | AGENTS.md |
| Preserve CatDogCNN input/output shape and sigmoid output | AGENTS.md |
| Keep model architecture: 3 conv blocks, 2 FC layers | AGENTS.md |
| Keep documented CLI commands stable if present | AGENTS.md |
| Add/adjust tests for model changes | AGENTS.md |

## Test Patterns
| Pattern | Details |
|---|---|
| Layer type assertions | tests/test_model.py validates feature block layer types |
| Shape checks | tests/test_model.py asserts output shape (2,1) |
---
language: python
package_manager: pip
test_runner: pytest
test_command: "pytest tests/"
test_file_pattern: "tests/test_*.py"
require_tests: true
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| src/ | Python | CNN model definition (CatDogCNN) |
| tests/ | Python | Pytest checks for layer order and output shape |
| .pace/context/ | N/A | Generated context artifacts (do not edit) |

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.11 |
| ML Framework | PyTorch 2.x |
| Testing | pytest |
| Imaging/Utils | torchvision, Pillow, NumPy, Matplotlib (README) |

## System Architecture
| Component | Interacts With | Notes |
|---|---|---|
| src/model.py:CatDogCNN | tests/test_model.py | Tests instantiate model and validate layers/output |

## Key Interfaces & Contracts
| Interface | Signature | Contract |
|---|---|---|
| CatDogCNN.__init__ | () -> None | 3 conv blocks + 2 FC layers; layer order fixed |
| CatDogCNN.forward | (x: torch.Tensor) -> torch.Tensor | Input [N,3,224,224] → output sigmoid [N,1] |

## Coding Conventions
| Rule | Source |
|---|---|
| Keep CatDogCNN in src/model.py with exact name | AGENTS.md |
| Do not change input/output tensor shapes | AGENTS.md |
| Architecture: 3 conv blocks (Conv2d→BatchNorm2d→ReLU→MaxPool2d) + 2 FC layers | AGENTS.md |
| No external network calls or secrets | AGENTS.md |

## Test Patterns
| Test File | Focus | Notes |
|---|---|---|
| tests/test_model.py | Layer order + forward output shape | Uses pytest and torch.randn input |

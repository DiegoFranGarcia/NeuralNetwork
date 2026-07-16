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
| src | Python | CNN model architecture |
| tests | Python | Pytest validation for model |
| .pace/context | Markdown/JSON | Generated context artifacts |
| . | Markdown | Project documentation |

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.11 |
| ML Framework | PyTorch 2.x |
| Test Runner | pytest |
| Image Utils | torchvision, Pillow |
| Data/Plot | NumPy, Matplotlib |

## System Architecture
| Component | Interactions |
|---|---|
| CatDogCNN (src/model.py) | Accepts image tensors [N,3,224,224] → outputs sigmoid [N,1] |
| Tests (tests/test_model.py) | Instantiates CatDogCNN and asserts layers/shape |

## Key Interfaces & Contracts
| Interface | Contract |
|---|---|
| CatDogCNN.forward(x) | Input tensor shape [N,3,224,224] → output shape [N,1] |
| Architecture | 3 Conv2d→BatchNorm2d→ReLU→MaxPool2d blocks + 2 FC layers + Sigmoid |

## Coding Conventions
| Rule | Source |
|---|---|
| Keep class name CatDogCNN in src/model.py | AGENTS.md |
| Preserve layer order and tensor shapes | AGENTS.md |
| No external network calls or secrets | AGENTS.md |

## Test Patterns
| Test File | Focus | Notes |
|---|---|---|
| tests/test_model.py | Layer order, forward output shape | Uses torch.randn input |
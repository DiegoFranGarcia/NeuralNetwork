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
| src | Python | CNN model implementation |
| tests | Python | Pytest checks for model layers/output |
| .pace/context | Markdown/JSON | Generated PACE context artifacts |

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.11 |
| ML Framework | PyTorch 2.x |
| Testing | pytest |
| Libraries | torchvision, Pillow, NumPy, Matplotlib |

## System Architecture
| Component | Interactions |
|---|---|
| CatDogCNN | Consumes image tensors [N,3,224,224] and outputs sigmoid predictions [N,1] |
| Tests | Instantiate CatDogCNN and validate layer types/output shape |

## Key Interfaces & Contracts
| Interface | Contract |
|---|---|
| CatDogCNN.forward | Input: torch.Tensor [N,3,224,224] → Output: torch.Tensor [N,1] sigmoid |
| Architecture | 3 conv blocks + 2 fully connected layers |

## Coding Conventions
| Rule | Details |
|---|---|
| Layer ordering | Conv2d → BatchNorm2d → ReLU → MaxPool2d repeated 3x |
| Output activation | Sigmoid applied after classifier |
| Module naming | CatDogCNN in src/model.py |

## Test Patterns
| Pattern | Details |
|---|---|
| Layer structure tests | Assert types in model.features sequence |
| Forward tests | Validate output shape (2,1) for batch input |

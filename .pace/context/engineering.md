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
| src | Python | CNN model definition |
| tests | Python | Pytest coverage for model behavior |

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.11 |
| ML Framework | PyTorch 2.x |
| Data/Imaging | torchvision, Pillow |
| Math | NumPy |
| Plotting | Matplotlib |
| Testing | pytest |

## System Architecture
| Component | взаимодействие |
|---|---|
| CatDogCNN (src/model.py) | Consumes image tensors, outputs sigmoid probability |
| Pytest suite (tests/test_model.py) | Instantiates CatDogCNN and validates layer types/output shape |

## Key Interfaces & Contracts
| Interface | Definition | Contract |
|---|---|---|
| CatDogCNN.__init__ | src/model.py | 3 conv blocks + 2 FC layers + sigmoid output |
| CatDogCNN.forward(x) | src/model.py | Input tensor shape [N,3,224,224] -> output shape [N,1] |

## Coding Conventions
| Rule | Source |
|---|---|
| Keep CLI interfaces stable if present | AGENTS.md |
| Assume dataset layout data/train and data/val | AGENTS.md |
| Use PyTorch/torchvision for model/data handling | AGENTS.md |
| Add/maintain pytest tests for new behavior | AGENTS.md |

## Test Patterns
| Pattern | Details |
|---|---|
| Layer type assertions | tests/test_model.py validates feature/classifier layers |
| Output shape checks | tests/test_model.py expects [batch,1] |
| Run command | pytest tests/ |

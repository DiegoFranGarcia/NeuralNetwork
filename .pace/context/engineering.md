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
| src | Python | Cat vs dog CNN model definition |
| tests | Python | Pytest validation of model layers and output shape |
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
| src/model.py:CatDogCNN | Instantiated by tests to validate layer types and output shape |

## Key Interfaces & Contracts
| Interface | Contract |
|---|---|
| CatDogCNN.forward(x) | Input tensor [N,3,224,224] -> output [N,1] with sigmoid |
| CatDogCNN.__init__ | 3 conv blocks + 2 fully connected layers |

## Coding Conventions
| Convention | Source |
|---|---|
| Preserve CatDogCNN input/output contract and sigmoid output | AGENTS.md |
| Keep architecture: 3 conv blocks, 2 FC layers | AGENTS.md |
| Use only PyTorch/torchvision for ML | AGENTS.md |
| Update/add tests when changing model behavior | AGENTS.md |
| Keep documented CLI commands stable if present | AGENTS.md |

## Test Patterns
| Pattern | Details |
|---|---|
| Layer type assertions | tests/test_model.py validates feature block layer types |
| Shape checks | tests/test_model.py asserts output shape (2,1) |
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
| src/ | Python | CNN model definition |
| tests/ | Python | Pytest assertions for model contract |
| .pace/ | Markdown | Agent context rules |

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.11 |
| ML Framework | PyTorch 2.x |
| Testing | pytest |

## System Architecture
| Component | взаимодействие | Details |
|---|---|---|
| CatDogCNN | forward(x) | Tensor input [N,3,224,224] → sigmoid output [N,1] |

## Key Interfaces & Contracts
| Interface | Location | Contract |
|---|---|---|
| CatDogCNN.__init__ | src/model.py | 3 Conv2d→BatchNorm2d→ReLU→MaxPool2d blocks; 2 FC layers; sigmoid output |
| CatDogCNN.forward | src/model.py | Accepts torch.Tensor [N,3,224,224]; returns torch.Tensor [N,1] |
| Layer order tests | tests/test_model.py | Enforces specific layer types and classifier layers |

## Coding Conventions
| Rule | Source |
|---|---|
| Class name must remain CatDogCNN | AGENTS.md |
| Preserve layer order/counts in features and classifier | AGENTS.md, tests/test_model.py |
| No external network calls | AGENTS.md |
| No secrets or API keys | AGENTS.md |

## Test Patterns
| Aspect | Details |
|---|---|
| Framework | pytest |
| Location | tests/test_model.py |
| Pattern | Structural layer assertions + forward output shape |
| Run Command | pytest tests/ |

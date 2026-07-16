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
| src | Python | CNN model definition (CatDogCNN) |
| tests | Python | Pytest checks for model architecture/output |

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.11 |
| ML Framework | PyTorch 2.x |
| Testing | pytest |

## System Architecture
| Component | Interaction |
|---|---|
| CatDogCNN (src/model.py) | Consumes image tensors [N,3,224,224] → outputs sigmoid scores [N,1] |
| Tests (tests/test_model.py) | Instantiates CatDogCNN → asserts layer order and output shape |

## Key Interfaces & Contracts
| Interface | Definition |
|---|---|
| Class | CatDogCNN(nn.Module) |
| Method | forward(x: torch.Tensor) -> torch.Tensor |
| Input Shape | [N,3,224,224] |
| Output Shape | [N,1] |

## Coding Conventions
| Rule | Source |
|---|---|
| Keep class name CatDogCNN in src/model.py | AGENTS.md |
| Preserve 3 Conv2d→BatchNorm2d→ReLU→MaxPool2d blocks | AGENTS.md |
| Preserve 2 FC layers + Sigmoid output | AGENTS.md |
| No external network calls or secrets | AGENTS.md |

## Test Patterns
| Pattern | Details |
|---|---|
| Layer order checks | tests/test_model.py::test_catdogcnn_has_expected_layers |
| Output shape checks | tests/test_model.py::test_catdogcnn_forward_returns_predictions |
| Runner | pytest tests/ |

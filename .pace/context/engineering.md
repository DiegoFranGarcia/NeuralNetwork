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
| tests | Python | Pytest assertions for model layers and output |
| . | Markdown | Project and agent guidelines |

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
| src/model.py:CatDogCNN | Consumed by pytest tests for layer/shape validation |

## Key Interfaces & Contracts
| Interface | Contract |
|---|---|
| CatDogCNN.forward(x) | Input tensor [N,3,224,224] → output [N,1] with sigmoid |

## Coding Conventions
| Convention | Source |
|---|---|
| Use PyTorch/torchvision only (no new ML frameworks) | AGENTS.md |
| Maintain CatDogCNN input/output contract | AGENTS.md |
| Keep CLI interfaces stable if present | AGENTS.md |

## Test Patterns
| Pattern | Details |
|---|---|
| Layer type assertions | tests/test_model.py validates feature block layer types |
| Shape checks | tests/test_model.py asserts output shape (2,1) |

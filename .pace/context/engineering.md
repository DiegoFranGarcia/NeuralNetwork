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
| src/ | Python | Model architecture (CatDogCNN) |
| tests/ | Python | Pytest coverage for model layers and output |
| .pace/context/ | Markdown/JSON | Existing PACE context outputs |
| .github/ | N/A | Empty directory |

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.11 |
| ML Framework | PyTorch 2.x |
| Vision Utils | torchvision, Pillow |
| Data/Plotting | NumPy, Matplotlib |
| Testing | pytest |

## System Architecture
| Component | Interaction |
|---|---|
| CatDogCNN (src/model.py) | Accepts [N,3,224,224] tensor → outputs [N,1] sigmoid predictions |
| Tests (tests/test_model.py) | Instantiate CatDogCNN → validate layer types and output shape |

## Key Interfaces & Contracts
| Interface | Definition |
|---|---|
| Model forward | Input: torch.Tensor [N,3,224,224]; Output: torch.Tensor [N,1] with sigmoid |
| CLI commands | pytest tests/ (documented in README/AGENTS) |

## Coding Conventions
| Rule | Evidence |
|---|---|
| Preserve model I/O contract | AGENTS.md: input/output shape + sigmoid required |
| Keep 3 conv blocks + 2 FC layers | AGENTS.md + tests/test_model.py expectations |
| Use PyTorch for ML components | AGENTS.md constraints |

## Test Patterns
| Test File | Coverage |
|---|---|
| tests/test_model.py | Layer type order, classifier layer types, forward output shape |
| Test Runner | pytest tests/ |

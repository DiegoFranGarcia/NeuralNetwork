## Vision
Purpose: Classify images as cat or dog using a CNN model
Users: Not specified in repo

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Not specified | Not specified | Not specified |

## MVP Scope
In Scope:
- CatDogCNN model definition (src/model.py)
- Pytest validation of layers and output shape (tests/test_model.py)
- Project usage documentation (README.md)
Out of Scope:
- Dataset download/management code (AGENTS.md)
- Multi-class classification behavior (AGENTS.md)
- Changes to input/output tensor shapes or sigmoid output (AGENTS.md)

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Use only PyTorch/torchvision for ML | AGENTS.md |
| Preserve input/output contract [N,3,224,224] -> [N,1] with sigmoid | AGENTS.md + tests |
| Keep model architecture: 3 conv blocks, 2 FC layers | AGENTS.md |
## Vision
Purpose: Classify images as cat or dog with a PyTorch CNN
Users: Developers or researchers training/inferencing a binary pet classifier

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML practitioner | Needs a simple CNN baseline for cats vs dogs | Train and evaluate a binary classifier |
| Student/learner | Wants a reference CNN architecture | Study model structure and test coverage |

## MVP Scope
In Scope:
- CatDogCNN model definition (3 conv blocks, 2 FC layers)
- Pytest validation of layers and output shape
- Documented training/evaluation/inference commands (README)

Out of Scope:
- Dataset download/management code
- Multi-class classification
- Changing checkpoint formats/paths

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Use PyTorch/torchvision only | AGENTS.md convention |
| Maintain input/output contract [N,3,224,224]→[N,1] | AGENTS.md requirement |
| Assume dataset layout data/train and data/val | AGENTS.md/README expectation |

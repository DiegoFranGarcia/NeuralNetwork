## Vision
Purpose: Classify images as cat or dog using a CNN trained from scratch
Users: ML learners and developers needing a basic binary image classifier

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML Student | Needs a simple CNN example with training/eval/inference | Learn end-to-end image classification |
| Developer | Wants a baseline cat vs dog classifier | Run training and inference quickly |

## MVP Scope
In Scope:
- CNN model definition for binary classification
- Training, evaluation, and single-image inference scripts
- Pytest checks for model layers and output shape
Out of Scope:
- Dataset download/management automation
- Multi-class classification
- Web/UI for inference

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Input/Output contract [N,3,224,224] 0 [N,1] with sigmoid | AGENTS.md + tests enforce model behavior |
| Use only PyTorch/torchvision for ML | AGENTS.md constraint |
## Vision
Purpose: Classify images as cat vs dog using a CNN model
Users: ML practitioners evaluating a basic PyTorch CNN

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML learner | Needs a simple CNN reference | Understand model architecture and outputs |
| QA/tester | Needs verifiable model contract | Validate layer order and output shape |

## MVP Scope
In Scope:
- CatDogCNN model definition in src/model.py
- Forward pass producing [N,1] sigmoid scores
- Pytest validation of layers and output shape

Out of Scope:
- Training pipeline or dataset handling
- Inference CLI or API service
- Hyperparameter tuning or metrics reporting

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Keep class name CatDogCNN | AGENTS.md contract |
| Preserve layer order and counts | Tests enforce architecture |
| No external network calls | AGENTS.md restriction |

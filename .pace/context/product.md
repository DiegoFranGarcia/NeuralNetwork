## Vision
Purpose: Classify images as cat vs dog using a CNN model
Users: ML learners or developers validating CNN architecture

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML student | Needs reference CNN architecture | Inspect/verify model structure |
| QA tester | Needs deterministic contract | Validate layer order and output shape |

## MVP Scope
In Scope:
- CNN architecture definition in src/model.py
- Forward pass producing sigmoid output
- Pytest checks for layer order and output shape

Out of Scope:
- Training pipeline
- Dataset handling
- Inference CLI

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Preserve CatDogCNN class name and location | tests and AGENTS.md contract |
| Maintain 3 conv blocks + 2 FC layers | tests and AGENTS.md contract |
| No external network calls or secrets | AGENTS.md |
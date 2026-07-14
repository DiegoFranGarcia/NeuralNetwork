## Vision
Purpose: Classify images as cat vs dog using a CNN model definition
Users: ML developers who need a reference CNN architecture and tests

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML Engineer | Needs a simple, test-verified CNN baseline | Reuse a fixed CatDogCNN architecture |
| QA/Test Engineer | Needs deterministic model structure checks | Validate layer order and output shape |

## MVP Scope
In Scope:
- CatDogCNN architecture in src/model.py
- Forward pass output shape [N,1] with sigmoid
- Pytest checks for layer order and output shape
Out of Scope:
- Training, evaluation, inference scripts
- Dataset management or downloading
- UI or API service

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Architecture must remain 3 conv blocks + 2 FC layers | AGENTS.md contract |
| Keep CatDogCNN name and location | AGENTS.md contract |
| No external network calls or secrets | AGENTS.md rule |

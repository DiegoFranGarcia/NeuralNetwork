## Vision
Purpose: Classify images as cat or dog with a PyTorch CNN
Users: ML practitioners or learners running local training/inference

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML learner | Needs simple CNN example | Understand binary image classification |
| Hobbyist engineer | Wants baseline model | Train and evaluate cat vs dog classifier |

## MVP Scope
In Scope:
- CNN model definition (CatDogCNN)
- PyTorch forward pass for [N,3,224,224] inputs
- Pytest-based model structure checks
Out of Scope:
- Training pipeline, evaluation CLI, or inference scripts (not in repo)
- Dataset download automation

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Preserve CatDogCNN layer order/counts | Tests assert exact layer types/order |
| No external network calls | AGENTS.md restriction |
| No secrets or API keys | AGENTS.md restriction |

## Vision
Purpose: Classify images as cat vs dog with a CNN model
Users: ML practitioners or students training a binary classifier

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML Student | Needs a simple CNN example | Train and inspect a working classifier |
| Data Scientist | Wants a baseline model | Evaluate cat vs dog classification accuracy |

## MVP Scope
In Scope:
- CNN architecture definition (CatDogCNN)
- PyTorch model forward pass for binary prediction
- Pytest model layer/output checks
Out of Scope:
- Dataset download/management automation
- Training/evaluation/inference scripts in repo
- Deployment or serving

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Preserve input/output shapes | Required by tests and conventions |
| Keep 3 conv blocks + 2 FC layers | Locked architecture contract |
| No external network calls or secrets | Repo constraint from AGENTS.md |

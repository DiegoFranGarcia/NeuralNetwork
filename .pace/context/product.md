## Vision
Purpose: Classify cat vs dog images with a CNN trained from scratch
Users: ML learners or practitioners evaluating binary image classification

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML student | Needs a reference CNN implementation | Train and evaluate a binary classifier |
| Hobbyist | Wants simple inference on images | Predict cat vs dog from a single image |

## MVP Scope
In Scope:
- Train CatDogCNN model on Dogs vs Cats dataset
- Evaluate metrics and confusion matrix (README)
- Single-image inference (README)

Out of Scope:
- Multi-class classification
- Dataset download/management automation
- Web or API deployment

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Keep CatDogCNN I/O shape [N,3,224,224] -> [N,1] with sigmoid | AGENTS.md contract + tests |
| Preserve 3 conv blocks + 2 FC layers | AGENTS.md + tests expectations |
| Use PyTorch/torchvision only for ML | AGENTS.md constraint |

## Vision
Purpose: Classify images as cat vs dog using a CNN
Users: ML practitioners needing a simple binary image classifier

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML learner | Needs reference CNN training pipeline | Train a working cat/dog classifier |
| Data scientist | Needs quick baseline model | Evaluate dataset with standard metrics |
| Developer | Needs single-image inference | Predict class for new images |

## MVP Scope
In Scope:
- Train CNN from scratch on Dogs vs Cats dataset
- Evaluate with accuracy/precision/recall/F1 and confusion matrix
- Single-image inference with confidence score

Out of Scope:
- Multi-class classification
- Model deployment service/API
- Automated dataset download

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Dataset must be Kaggle Dogs vs Cats | README.md dataset instructions |
| Input images resized to 224x224 with ImageNet normalization | README.md model architecture section |
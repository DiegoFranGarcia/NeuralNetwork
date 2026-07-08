## Vision
Purpose: Classify images as cat or dog using a CNN
Users: ML practitioners or students training/evaluating/inferencing on Dogs vs Cats

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML learner | Needs an end-to-end CNN example | Train and evaluate a binary classifier |
| Practitioner | Needs quick baseline for cats vs dogs | Run training/evaluation/inference scripts |

## MVP Scope
In Scope:
- Train CNN from scratch on Dogs vs Cats dataset
- Evaluate metrics (accuracy, precision, recall, F1, confusion matrix)
- Single-image inference with confidence
Out of Scope:
- Multi-class classification beyond cat/dog
- Web/API serving layer
- Automated dataset download inside code

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Dataset is Kaggle Dogs vs Cats | README.md specifies dataset source |
| Input size 224x224 with ImageNet normalization | README.md model preprocessing |

## Vision
Purpose: Classify images as cat vs dog using a CNN trained on Kaggle Dogs vs Cats dataset
Users: ML practitioners or learners training/evaluating/inferencing on image data

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML learner | Needs a complete CNN training/evaluation example | Train a binary image classifier end-to-end |
| Practitioner | Needs quick inference on new images | Predict cat/dog label with confidence |

## MVP Scope
In Scope:
- Train CNN from scratch with configurable epochs/batch size/lr
- Evaluate model with accuracy, precision, recall, F1, confusion matrix
- Single-image inference with checkpoint

Out of Scope:
- Multi-class classification
- Deployment as API or web app
- Automated dataset download/management

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Dataset: Kaggle Dogs vs Cats | Project is built around this dataset |
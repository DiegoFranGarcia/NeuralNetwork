## Vision
Purpose: Classify images as cat or dog using a custom CNN trained on Kaggle Dogs vs Cats.
Users: ML learners and developers needing a simple binary image classifier.

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| ML Student | Needs clear CNN example | Train/evaluate a binary classifier |
| ML Engineer | Wants simple inference CLI | Predict cat vs dog on new images |

## MVP Scope
In Scope:
- CNN architecture for binary classification
- Training/evaluation/inference scripts (per README)
- Dataset layout: data/train and data/val
Out of Scope:
- Multi-class classification
- Dataset download/management in code
- Web/API deployment

## Strategic Constraints
| Constraint | Reason |
|---|---|
| No new ML frameworks | AGENTS.md: avoid TensorFlow, keep PyTorch |
| Keep CLI args/outputs stable | AGENTS.md |
| Do not alter checkpoint format/paths without docs/tests | AGENTS.md |

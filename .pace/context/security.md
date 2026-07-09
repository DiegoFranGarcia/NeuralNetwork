## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| Training/validation images | data/train, data/val | Not specified in repository files |
| Model checkpoints | checkpoints/ (implied) | Not specified in repository files |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| User CLI | train.py/evaluate.py/predict.py | None (local execution) |

## Security Requirements
- Do not run untrusted datasets without validation
- Store checkpoints securely if used outside local environment

## Security Checklist
Dataset license reviewed: fail
Dependency vulnerability scan configured: fail
Secrets management documented: fail
Input validation for inference image: fail
## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| Training/validation images | data/ directory | Not specified in README.md |
| Model checkpoints | checkpoints/ path (CLI arg) | Not specified in README.md |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| User CLI | train.py/evaluate.py/predict.py | None (local execution) |

## Security Requirements
- Do not store credentials in repo (not specified in README.md)
- Validate CLI file paths exist before use (not specified in README.md)

## Security Checklist
Secrets scanning: fail (no evidence)
Dependency pinning: fail (requirements.txt not found)
Input validation documented: fail
Access control documented: fail
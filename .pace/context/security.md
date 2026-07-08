## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| Training/validation images | data/train, data/val | Not specified in README.md |
| Model checkpoints | checkpoints/ (documented path) | Not specified in README.md |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| User CLI | train.py/evaluate.py/predict.py | None documented |

## Security Requirements
- Do not commit dataset images or checkpoints to public repo
- Validate file paths for --image and --checkpoint inputs before use

## Security Checklist
Secrets stored in repo: FAIL (not assessed; no secrets files listed)
Input validation for CLI args: FAIL (not documented)
Dependency pinning in requirements.txt: FAIL (requirements.txt not present in repo root listing)

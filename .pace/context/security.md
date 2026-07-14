## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| Training/validation images | data/ (README structure) | Not specified in repo |
| Model checkpoints | checkpoints/ path (README) | Not specified in repo |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Local user | CLI scripts (train/evaluate/predict per README) | None (local execution) |

## Security Requirements
- Do not add dataset download/management code (AGENTS.md)
- Preserve model I/O contract and architecture (AGENTS.md)

## Security Checklist
Dataset download automation: fail (explicitly forbidden)
External network calls in code: fail (no files beyond model.py; unknown elsewhere)
Secrets in repo: fail (no evidence in scanned files)

## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| Model checkpoints | checkpoints/ (implied) | Not specified in repo |
| Training/validation images | data/train, data/val (implied) | Not specified in repo |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Local user | CLI scripts (train/evaluate/predict) | OS user permissions (implied) |

## Security Requirements
- Do not run on untrusted datasets without validation (AGENTS.md)
- Avoid adding new frameworks or data pipelines without review (AGENTS.md constraints)

## Security Checklist
Dataset validation documented: fail
Checkpoint integrity verification: fail
Access control for data directories: fail
Dependency pinning in requirements.txt: fail

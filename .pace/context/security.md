## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| Image dataset (cats/dogs) | data/train, data/val (expected layout) | Not specified |
| Model checkpoints | checkpoints/ (implied) | Not specified |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| User running scripts | Python modules (src/model.py) | None |

## Security Requirements
- No explicit security requirements documented

## Security Checklist
Dependency pinning file present: fail (requirements.txt not found)
Auth required for local scripts: fail (none specified)
Sensitive data handling documented: fail (not specified)

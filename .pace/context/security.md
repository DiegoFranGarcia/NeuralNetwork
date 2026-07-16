## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| None identified in repo | N/A | N/A |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Tests | CatDogCNN class | None (in-process) |

## Security Requirements
- Do not add external network calls (AGENTS.md)
- Do not add secrets or API keys (AGENTS.md)

## Security Checklist
No external network calls: pass
No secrets added: pass
Input tensor shape enforced by tests: pass

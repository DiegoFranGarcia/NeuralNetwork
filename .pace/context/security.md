## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| None specified | N/A | N/A |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Local user | PyTorch model code | N/A (local execution) |

## Security Requirements
- No external network calls or secrets (AGENTS.md)
- Keep model architecture unchanged to satisfy tests

## Security Checklist
No external network calls: pass
No secrets in repo: pass (none found)
Input tensor shape validated by tests: pass
## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| Model weights | Not present in repo | N/A |
| Training data | Not present in repo | N/A |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Developer | PyTorch model code | Local execution only |

## Security Requirements
- No external network calls or secrets in repository
- Preserve model I/O shapes and architecture per conventions

## Security Checklist
No external network calls: pass
No secrets in repo: pass
Tests enforce architecture: pass

# Backend

FastAPI backend foundation for the Phase 1 MVP.

## Scope in this skeleton

- Health-check API route.
- Structured logging helper.
- RBAC role hierarchy helper.
- Package and test configuration.

No production authentication, payment, credit, gym reservation, notification, or hardware control is implemented in this skeleton.

## Local commands

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
pytest
ruff check .
```

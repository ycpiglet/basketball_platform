# Local Development

## Prerequisites

- Node.js 20 or newer.
- npm 10 or newer.
- Python 3.11 or newer.
- Docker and Docker Compose for local PostgreSQL and MongoDB.

## Frontend

```bash
cd frontend
npm install
npm run dev
npm run lint
npm run test
npm run build
```

The development app defaults to `http://localhost:5173`.

## Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
pytest
ruff check .
```

The API defaults to `http://localhost:8000/api/v1`.

## Databases

```bash
docker compose up -d postgres mongodb
```

The compose file starts only local development databases. It does not start payment, credit, notification, ad, or production hardware services.

## Health check

```bash
curl http://localhost:8000/api/v1/health
```

Expected JSON shape:

```json
{
  "status": "ok",
  "service": "Basketball Platform API",
  "environment": "local"
}
```

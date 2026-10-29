# pytest-api-demo

Minimal FastAPI + pytest unit tests (health, create, get, 404, duplicate).

## Run tests
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn pytest httpx
pytest -q

from fastapi.testclient import TestClient
from app.main import app, items_db

client = TestClient(app)

def setup_function():
    items_db.clear()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_create_and_get_item():
    r = client.post("/items/1", json={"name": "Laptop", "price": 999.0})
    assert r.status_code == 200
    assert r.json()["name"] == "Laptop"

    r2 = client.get("/items/1")
    assert r2.status_code == 200
    assert r2.json()["price"] == 999.0

def test_get_missing_item():
    r = client.get("/items/99")
    assert r.status_code == 404

def test_duplicate_item():
    client.post("/items/2", json={"name": "Mouse", "price": 25.0})
    r = client.post("/items/2", json={"name": "Mouse", "price": 25.0})
    assert r.status_code == 400

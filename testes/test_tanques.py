from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_listar_tanques():
    response = client.get("/tanques")
    assert response.status_code == 200
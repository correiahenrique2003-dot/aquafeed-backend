from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_sensores():
    response = client.get("/sensores")
    assert response.status_code == 200

    dados = response.json()

    assert "temperatura" in dados
    assert "ph" in dados
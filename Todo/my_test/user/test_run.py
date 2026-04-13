from fastapi.testclient import TestClient
from my_app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    
def test_get_user():
    response = client.post("/")
    assert response.status_code == 200
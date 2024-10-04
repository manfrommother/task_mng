import pytest
from app.database import init_db, engine
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    init_db()

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Task Manager API"}

def test_read_task():
    response = client.get('/tasks/')
    assert response.status_code == 200

def test_create_task():
    task_data = {
        'title': 'Test Task',
        'description': 'This is a test task.'
    }
    response = client.post('/tasks/', json=task_data)
    assert response.status_code == 200
    assert response.json()["title"] == task_data["title"]
    assert response.json()["description"] == task_data["description"]


    
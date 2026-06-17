from fastapi.testclient import TestClient
import pytest

import main


@pytest.fixture(autouse=True)
def reset_state():
    main.db.clear()
    main.counter = 0


@pytest.fixture
def client():
    return TestClient(main.app)


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_item(client):
    create_response = client.post("/items", json={"name": "Widget", "price": 9.99})
    assert create_response.status_code == 201
    item = create_response.json()
    assert item == {"id": 1, "name": "Widget", "price": 9.99}

    get_response = client.get("/items/1")
    assert get_response.status_code == 200
    assert get_response.json() == item


def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404


def test_delete_item(client):
    client.post("/items", json={"name": "Widget", "price": 9.99})

    delete_response = client.delete("/items/1")
    assert delete_response.status_code == 204

    get_response = client.get("/items/1")
    assert get_response.status_code == 404

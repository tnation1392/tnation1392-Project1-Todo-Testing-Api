import threading
import time
import requests
import pytest

from app import app

BASE_URL = "http://127.0.0.1:5001"


def wait_for_server():
    for _ in range(40):  # wait up to ~8 seconds
        try:
            response = requests.get(f"{BASE_URL}/tasks")
            if response.status_code in (200, 400, 404, 405):
                return
        except:
            pass

        time.sleep(0.2)

    raise RuntimeError("Server did not start in time")


@pytest.fixture(scope="session")
def client():
    server = threading.Thread(
        target=app.run,
        kwargs={
            "host": "127.0.0.1",
            "port": 5001,
            "debug": False,
            "use_reloader": False,   # ✅ CRITICAL
            "threaded": True,
        },
        daemon=True
    )

    server.start()

    wait_for_server()  # ✅ THIS IS THE FIX

    yield BASE_URL

def test_get_tasks_empty(client):
    response = requests.get(f"{client}/tasks")

    assert response.status_code == 200
    assert response.json() == []

def test_create_task(client):
    response = requests.post(
        f"{client}/tasks",
        json={"description": "Test task"}
    )

    assert response.status_code == 201
    data = response.json()

    assert data["description"] == "Test task"
    assert data["completed"] is False

def test_complete_task(client):
    # create task
    res = requests.post(
        f"{client}/tasks",
        json={"description": "Task A"}
    )

    task_id = res.json()["id"]

    # complete task
    res2 = requests.post(f"{client}/tasks/{task_id}/complete")

    assert res2.status_code == 200

def test_create_task_missing_description(client):
    response = requests.post(f"{client}/tasks", json={})

    assert response.status_code == 400

def test_complete_invalid_task(client):
    response = requests.post(f"{client}/tasks/999/complete")

    assert response.status_code == 404

def test_complete_already_completed(client):
    # create task
    res = requests.post(
        f"{client}/tasks",
        json={"description": "Test Task"}
    )

    task_id = res.json()["id"]

    # complete once
    requests.post(f"{client}/tasks/{task_id}/complete")

    # complete again
    res2 = requests.post(f"{client}/tasks/{task_id}/complete")

    assert res2.status_code == 400

def test_delete_invalid_task(client):
    response = requests.delete(f"{client}/tasks/999")

    assert response.status_code == 404

def test_delete_task(client):
    res = requests.post(
        f"{client}/tasks",
        json={"description": "To delete"}
    )

    task_id = res.json()["id"]

    res2 = requests.delete(f"{client}/tasks/{task_id}")

    assert res2.status_code == 200

import pytest

@pytest.mark.parametrize("task_id", [0, -1, 999])
def test_invalid_task_ids(client, task_id):
    response = requests.post(f"{client}/tasks/{task_id}/complete")

    assert response.status_code == 404


@pytest.mark.parametrize("task_id, expected_status", [
    (1, 200),
    (999, 404),
])
def test_complete_task_cases(client, task_id, expected_status):
    response = requests.post(f"{client}/tasks/{task_id}/complete")

    assert response.status_code == expected_status

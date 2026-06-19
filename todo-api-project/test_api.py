import threading
import time
import requests
import pytest

from app import app

BASE_URL = "http://127.0.0.1:5001"


def wait_for_server():
    for _ in range(30):  # try for ~6 seconds
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
            "threaded": True
        },
        daemon=True
    )

    server.start()

    wait_for_server()   # ✅ WAIT until server is actually ready

    yield BASE_URL

use_reloader=False

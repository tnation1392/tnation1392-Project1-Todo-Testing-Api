## Test Infrastructure

- **Framework**: pytest
- **Server Startup:** Flask app started in background thread
- **Base URL in Testing:** http://127.0.0.1:500
- **Reusability:** Session-scope pytest fixture
- **Server Readiness Check:** wait_for_server() repeatedly sends GET requests until the server responds

---

## Server readiness check
- **Function**: wait_for_server()
- **Behavior**:
  - repeatedly sends GET requests to /tasks
  - returns once the server responds with one of these status codes:
    - 200
    - 400
    - 404
    - 405
- **Purpose**:
  - ensure tests do not start before the server is ready

# Database Server Project

This repository contains two simple HTTP server implementations in Python:

- **FastAPI server** (`fastapi_server/fastapi_app.py`)
- **Built-in HTTPServer server** (`http_server/simple_http_server.py`)

---

## Requirements

- Python 3.7+
- For FastAPI server: `fastapi` and `uvicorn` packages

You can install the FastAPI dependencies with:

```bash
pip install fastapi uvicorn
```

---

## Running the servers

### 1. FastAPI Server

Run the FastAPI server using Uvicorn:

```bash
python -m uvicorn fastapi_server.fastapi_app:app --host 127.0.0.1 --port 4000 --reload
```

- The server will be accessible at: `http://localhost:4000`
- Use `/set?key=value` and `/get?key=your_key` endpoints.

---

### 2. Built-in HTTPServer

Run the simple HTTPServer-based server:

```bash
python http_server/simple_http_server.py
```

- The server listens on port 4000 by default.
- Use `/set?key=value` and `/get?key=your_key` endpoints similarly.

---

## Notes

- Both servers store key-value pairs **in memory** and will lose data on restart.
- The FastAPI server supports automatic reload on code changes.
- The built-in HTTPServer server has no external dependencies.



# WSGI vs ASGI in Python Web Development

## What is WSGI?

**WSGI** (Web Server Gateway Interface) is the **standard interface** between
Python web applications and web servers. It was introduced in PEP 333 (and
updated in PEP 3333) to allow any WSGI-compliant server (like Gunicorn or
uWSGI) to run any WSGI-compliant web framework (like Django or Flask).

- **Synchronous only**: WSGI apps run in a blocking, synchronous fashion.
- **One request per thread/process**: Each incoming request is handled
  sequentially in its own thread or process.
- **No native support for WebSockets or background tasks**.

### WSGI-Based Frameworks & Servers

- **Frameworks**:
  - Flask
  - Django (pre-3.0)
  - Bottle
  - Pyramid
- **Servers**:
  - Gunicorn
  - uWSGI
  - mod_wsgi (Apache)

---

## What is ASGI?

**ASGI** (Asynchronous Server Gateway Interface) is the spiritual successor to
WSGI, defined in [PEP 484](https://www.python.org/dev/peps/pep-0484/) and
formalized in the [ASGI specification](https://asgi.readthedocs.io). It enables
**asynchronous Python web apps** and supports long-lived connections like
WebSockets and Server-Sent Events.

- **Supports async and sync**: ASGI apps can be fully async or hybrid.
- **Handles WebSockets, HTTP/2, background tasks, etc.**
- **Concurrency**: Built to take advantage of `asyncio`, enabling multiple
  requests per thread via event loops.

### ASGI-Based Frameworks & Servers

- **Frameworks**:
  - FastAPI
  - Django (3.0+ with `asgiref`)
  - Starlette
  - Quart
  - Sanic
  - aiohttp _(does not use ASGI, but is async-native — see note below)_
- **Servers**:
  - Uvicorn
  - Daphne
  - Hypercorn

---

## Quick Comparison

| Feature             | WSGI                 | ASGI                      |
| ------------------- | -------------------- | ------------------------- |
| Protocols supported | HTTP only            | HTTP, WebSocket, more     |
| Concurrency model   | Blocking (sync)      | Async (via asyncio)       |
| WebSockets support  | ❌                   | ✅                        |
| Streaming support   | Limited              | Full                      |
| Performance         | Good (with workers)  | Better for async I/O apps |
| Use cases           | Traditional web apps | Real-time, async, APIs    |

---

## Special Note: What About `aiohttp`?

- `aiohttp` is **not** ASGI-based, but is built **directly on asyncio**.
- It provides its own HTTP server and client.
- It’s great for writing async APIs, but **won’t work with ASGI servers** like
  Uvicorn unless wrapped.

---

## TL;DR

- Use **WSGI** for classic, sync-based web apps (e.g., Flask, older Django
  projects).
- Use **ASGI** for modern, async-capable apps (e.g., FastAPI, Starlette,
  WebSocket support).
- Choose **ASGI** if you need high concurrency, streaming, or real-time
  communication.

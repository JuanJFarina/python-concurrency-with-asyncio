import uvicorn
from fastapi import FastAPI
import os
import asyncio

### FOR WINDOWS SYSTEMS ONLY ###

if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

### FOR LINUX OR MACOS SYSTEMS ###

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = FastAPI()


@app.get("/hello-world")
async def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("03_hello_world:app", port=8080, workers=4)

# Reaches a maximum throughput of roughly 6000 requests per second

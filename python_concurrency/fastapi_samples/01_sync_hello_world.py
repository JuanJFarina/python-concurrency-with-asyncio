import uvicorn
from fastapi import FastAPI
import threading
import os

app = FastAPI()


@app.get("/hello-world")
def hello_world():
    # print("Python application is running on process:", os.getpid())
    # print(
    #     f"Thread {threading.current_thread().native_id} from a total of {threading.active_count()} threads"
    # )
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080)

# this code has a throughput of roughly 3500 requests per second

import uvicorn
from fastapi import FastAPI, Depends
from python_concurrency.utils import SyncDatabaseService

app = FastAPI()


def get_database_service():
    return SyncDatabaseService()


@app.get("/get")
def get(database_service: SyncDatabaseService = Depends(get_database_service)):
    return {"data": database_service.fetch_data()}


if __name__ == "__main__":
    uvicorn.run(app, port=8080)

# This code has a throughput of roughly 1 request per second.

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
    uvicorn.run("python_concurrency.fastapi_samples.05_sync_get:app", port=8080, workers=4)

# This code has a throughput of roughly 150 request per second.

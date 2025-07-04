import uvicorn
from fastapi import FastAPI, Depends, Request
from python_concurrency.utils import ASyncDatabaseService

app = FastAPI()


db_service = ASyncDatabaseService()


@app.on_event("startup")
async def startup_event():
    app.state.db_service = ASyncDatabaseService()
    await app.state.db_service.connect_pool()


@app.on_event("shutdown")
async def shutdown_event():
    await app.state.db_service.close_pool()


async def get_database_service(request: Request) -> ASyncDatabaseService:
    return request.app.state.db_service


@app.get("/get")
async def get(
    request: Request,
    database_service: ASyncDatabaseService = Depends(get_database_service),
):
    data = await database_service.fetch_data()
    return {"data": data}


if __name__ == "__main__":
    uvicorn.run(app, port=8080)


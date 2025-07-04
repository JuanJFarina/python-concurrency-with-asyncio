from aiohttp.web_app import Application
from asyncpg.pool import Pool
from typing import Any
from unittest.mock import MagicMock


DB_KEY = "database"

### code for simulation without database


async def return_fake_data(_) -> list[dict[str, Any]]:
    return [
        {"brand_id": 1, "brand_name": "Brand A"},
        {"brand_id": 2, "brand_name": "Brand B"},
    ]


###


async def create_database_pool(app: Application) -> None:
    print("Creating database pool")
    # pool: Pool = await asyncpg.create_pool(
    #     user="postgres",
    #     password="password",
    #     database="products",
    #     host="127.0.0.1",
    #     port=5432,
    # )
    # app[DB_KEY] = pool
    pool = MagicMock()
    pool.fetch = return_fake_data
    pool.fetchrow = return_fake_data
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application) -> None:
    print("Destroying database pool")
    pool: Pool = app[DB_KEY]
    await pool.close()

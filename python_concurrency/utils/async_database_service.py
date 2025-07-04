from fastapi import FastAPI
import asyncpg

app = FastAPI()

DB_HOST = "samples.mindsdb.com"
DB_PORT = "5432"
DB_NAME = "demo"
DB_USER = "demo_user"
DB_PASSWORD = "demo_password"
DB_SCHEMA = "demo"


class ASyncDatabaseService:
    def __init__(self):
        self.conn_params = {
            "host": DB_HOST,
            "port": DB_PORT,
            "database": DB_NAME,
            "user": DB_USER,
            "password": DB_PASSWORD,
        }
        self.pool = None

    async def connect_pool(self):
        if not self.pool:
            self.pool = await asyncpg.create_pool(**self.conn_params)

    async def close_pool(self):
        if self.pool:
            await self.pool.close()
            self.pool = None

    async def fetch_data(self, table_name: str = "customer_churn", limit: int = 10):
        if not self.pool:
            await self.connect_pool()

        conn = None
        try:
            conn = await self.pool.acquire()

            query = f"SELECT * FROM {DB_SCHEMA}.{table_name} LIMIT {limit};"

            return await conn.fetch(query)

        except Exception as e:
            raise RuntimeError(f"Database error: {e}") from e
        finally:
            if conn:
                await self.pool.release(conn)

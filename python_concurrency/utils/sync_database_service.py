from fastapi import FastAPI
import psycopg

app = FastAPI()

DB_HOST = "samples.mindsdb.com"
DB_PORT = "5432"
DB_NAME = "demo"
DB_USER = "demo_user"
DB_PASSWORD = "demo_password"
DB_SCHEMA = "demo"


class SyncDatabaseService:
    def __init__(self):
        self.conn_string = (
            f"host={DB_HOST} port={DB_PORT} dbname={DB_NAME} "
            f"user={DB_USER} password={DB_PASSWORD}"
        )

    def fetch_data(self, table_name: str = "customer_churn", limit: int = 10):
        conn = None
        try:
            conn = psycopg.connect(self.conn_string)

            conn.row_factory = psycopg.rows.dict_row

            with conn.cursor() as cur:
                query = f"SELECT * FROM {DB_SCHEMA}.{table_name} LIMIT {limit};"
                cur.execute(query)

                results = cur.fetchall()
                return results

        except Exception as e:
            raise RuntimeError(f"Database error: {e}") from e
        finally:
            if conn:
                conn.close()

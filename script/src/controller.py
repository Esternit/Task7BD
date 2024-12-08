from fastapi import FastAPI, HTTPException
import script as s
from pydantic import BaseModel

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
import time

for i in range(10):
    try:
        cursor, conn = s.connect()
        redis_client = s.get_redis()
        break
    except Exception as e:
        print(f"Error connecting to DB or Redis: {e}. Sleeping for 5 seconds and trying again.")
        time.sleep(5)

class QueryInput(BaseModel):
    query: str

@app.get("/users")
async def get_users():
    try:
        result = s.get_cached_data(redis_client, cursor, "users:all", "SELECT * FROM users")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching users: {e}")

@app.get("/products")
async def get_products():
    try:
        result = s.get_cached_data(redis_client, cursor, "products:all", "SELECT * FROM products")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching products: {e}")

@app.on_event("shutdown")
def close_connection():
    try:
        cursor.close()
        conn.close()
        redis_client.close()
        print("Database and Redis connections closed.")
    except Exception as e:
        print(f"Error closing DB or Redis connection: {e}")
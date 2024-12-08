import psycopg2
import logging
import redis

logging.basicConfig(level=logging.INFO, format="%(asctime)s.%(msecs)03d %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

redis_client = None

def connect():
    try:
        conn = psycopg2.connect(
            database="db",
            user="user",
            password="pass",
            port="5432",
            host="dbpg-mtg",
        )
        print("Connected to DB successfully")
        cur = conn.cursor()
        return cur, conn
    except Exception as e:
        print(f"Error while connecting to DB: {e}")
        raise

def get_redis():
    global redis_client
    if not redis_client:
        try:
            redis_client = redis.Redis(host="redis-mtg", port=6379, decode_responses=True)
            print("Connected to Redis successfully")
        except Exception as e:
            print(f"Error while connecting to Redis: {e}")
            raise
    return redis_client

def get_cached_data(redis_client, cursor, cache_key, query):
    try:
        cached_result = redis_client.get(cache_key)
        if cached_result:
            return {"data": eval(cached_result), "cached": True}

        cursor.execute(query)
        result = cursor.fetchall()
        redis_client.set(cache_key, str(result), ex=60)
        return {"data": result, "cached": False}
    except Exception as e:
        logging.error("Error fetching data with cache: %s", e)
        raise

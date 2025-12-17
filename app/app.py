import os
import time
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
SLEEP_SECONDS = float(os.getenv("SLEEP_SECONDS", "2"))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

while True:
    r.incr("counter")
    print("Counter:", r.get("counter").decode(), "| Redis:", REDIS_HOST, REDIS_PORT)
    time.sleep(SLEEP_SECONDS)

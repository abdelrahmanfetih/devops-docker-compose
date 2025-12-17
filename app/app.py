import redis
import time

while True:
    try:
        r = redis.Redis(host="redis", port=6379)
        r.ping()
        break
    except redis.exceptions.ConnectionError:
        print("Waiting for Redis...")
        time.sleep(2)

while True:
    r.incr("counter")
    print("Counter:", r.get("counter").decode())
    time.sleep(2)

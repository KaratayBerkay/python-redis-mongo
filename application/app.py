import os
import time

from mongo.mongo_actions import MongoActions
from redis.redis_actions import RedisActions


class App:
    def __init__(self):
        self.routes = os.getenv("ROUTES", {})

    def boot_application(self):
        path = os.getenv("PATH_INFO")
        method = os.getenv("REQUEST_METHOD")
        print("path", path)
        print("method", method)
        print("routes", self.routes)
        return {"routes": self.routes}


if __name__ == "__main__":
    app = App()
    while True:
        mongo_client = MongoActions()
        app.boot_application()
        redis_cli = RedisActions()
        for _ in range(1000):
            redis_cli.set(f"key{_}", f"value{_}")
        time.sleep(10)

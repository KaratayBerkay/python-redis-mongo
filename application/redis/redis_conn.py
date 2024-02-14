import os
from redis import Redis

# redis_conn = Redis(
#     host="localhost",
#     password="redis_password",
#     port=6379,
#     db=0
# )
#
# connection = redis_conn.get_connection_kwargs()


class RedisConn:

    def __init__(self):
        self.redis = Redis(
            host=os.getenv("REDIS_PASSWORD", "localhost"),
            password=os.getenv("REDIS_PASSWORD", "redis_password"),
            port=6379,
            db=0
        )
        if not self.check_connection():
            raise Exception("Connection error")

    def check_connection(self):
        return self.redis.ping()

    def set_connection(self, host, password, port, db):
        self.redis = Redis(
            host=host,
            password=password,
            port=port,
            db=db
        )
        return self.redis

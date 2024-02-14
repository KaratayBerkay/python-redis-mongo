import json

from redis_conn import RedisConn


class RedisActions(RedisConn):
    def __init__(self):
        super().__init__()

    def set(self, key, value):
        self.redis.set(key, value)

    def get(self, key):
        return self.redis.get(key).decode("utf-8")

    def delete(self, key):
        self.redis.delete(key)

    def exists(self, key):
        return self.redis.exists(key)

    def get_keys(self):
        return [key.decode('utf-8') for key in self.redis.keys()]

    def flush_all(self):
        return self.redis.flushall()

    def flush_db(self):
        return self.redis.flushdb()

    def set_expire(self, key, value, time):
        self.redis.setex(key, time, value)

    def get_expire(self, key):
        return self.redis.ttl(key)

    def set_hash(self, name, key, value):
        self.redis.hset(name, key, value)

    def get_hash(self, name, key):
        return json.loads(self.redis.hget(name, key))

    def get_all_hash(self, name):
        result = {}
        for key in self.redis.hkeys(name):
            result[key.decode("utf-8")] = json.loads(self.redis.hget(name, key))
        return result

    def delete_hash(self, name, key):
        self.redis.hdel(name, key)

    def set_list(self, name, value):
        self.redis.lpush(name, value)

    def get_list(self, name):
        result = []
        for item in self.redis.lrange(name, 0, -1):
            result.append(json.loads(item))
        return result

    def delete_list(self, name):
        self.redis.delete(name)

    def set_set(self, name, value):
        self.redis.sadd(name, value)

    def get_set(self, name):
        return self.redis.smembers(name)

    def delete_set(self, name, value):
        self.redis.srem(name, value)

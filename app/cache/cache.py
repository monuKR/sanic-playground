import json

from redis import Redis

from app.config import Config

config = Config.CONFIG
cache_config = config["CACHE"]


class Cache:
    _cache = None
    _host = cache_config["HOST"]
    _port = cache_config["PORT"]
    _prefix = config["NAME"]

    @classmethod
    def init(cls):
        cls._cache = Redis(host=cls._host, port=cls._port)

    @classmethod
    def close(cls):
        if not cls._cache:
            return

        cls._cache.close()
        cls._cache = None

    @classmethod
    def get_key(cls, key: str):
        return f"{cls._prefix}:{key}"

    @classmethod
    def get(cls, key: str):
        value = cls._cache.get(cls.get_key(key))
        if value:
            return json.loads(value)

    @classmethod
    def set(cls, key: str, value):
        cls._cache.set(cls.get_key(key), json.dumps(value))

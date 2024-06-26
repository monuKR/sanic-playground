from app.cache import Cache


async def setup_cache(app, loop):
    Cache.init()


async def close_cache(app, loop):
    Cache.close()

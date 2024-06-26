from sanic import Sanic
from tortoise.contrib.sanic import register_tortoise

from app.config import Config
from app.listeners import close_cache, setup_cache
from app.routes import blueprint

config = Config.CONFIG


def setup_app():
    sanic_app = Sanic(config["NAME"])
    sanic_app.blueprint(blueprint)
    sanic_app.register_listener(setup_cache, "before_server_start")
    sanic_app.register_listener(close_cache, "after_server_stop")
    db = config["DATABASE"]
    register_tortoise(
        sanic_app,
        config={
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": db["HOST"],
                        "port": db["PORT"],
                        "user": db["USER"],
                        "password": db["PASSWORD"],
                        "database": db["NAME"],
                    }
                },
            },
            "apps": {
                "models": {
                    "models": ["app.models"],
                    "default_connection": "default",
                }
            }

        },
        modules={"models": ["app.models"]},
    )
    return sanic_app


app = setup_app()

if __name__ == "__main__":
    app.run(host=config["HOST"], port=config["PORT"], dev=config.get("DEBUG"))

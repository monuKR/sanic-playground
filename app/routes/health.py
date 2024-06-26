from sanic import Blueprint, Request, json

from app.cache import Cache

health = Blueprint("health")


@health.get("/ping")
async def ping(request: Request):
    return json({"ping": "pong"})

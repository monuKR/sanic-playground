from sanic import Blueprint, Request, json

health = Blueprint("health")


@health.get("/ping")
async def ping(request: Request):
    return json({"ping": "pong"})

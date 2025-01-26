import pytest
from sanic import Sanic

from app.config import Config
from app.routes import blueprint

config = Config.CONFIG

@pytest.fixture
def app():
    sanic_app = Sanic(f"test-{config['NAME']}")

    sanic_app.blueprint(blueprint)
    return sanic_app

@pytest.fixture
def test_client(app):
    return app.asgi_client

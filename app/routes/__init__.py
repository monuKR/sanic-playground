from sanic.blueprints import Blueprint

from .health import health

blueprint = Blueprint.group(health)

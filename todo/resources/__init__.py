from flask import Blueprint
from flask_restx import Api

from .task_api import ns

api_bp = Blueprint("api", __name__, url_prefix=None)

api = Api(
    api_bp,
    version="1.0",
    title="TodoGARPIX API",
    description="A simple TodoGARPIX API",
)
api.add_namespace(ns)


def init_api(app):
    app.register_blueprint(api_bp)

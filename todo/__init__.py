from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from .models.task_model import create_tables, drop_tables, filling_db
from .resources import init_api


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    init_api(app)
    drop_tables()
    create_tables()
    filling_db()
    return app

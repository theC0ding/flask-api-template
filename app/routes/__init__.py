from .task_routes import task_routes
from flask import Flask


def register_routes(app: Flask):
    app.register_blueprint(task_routes)

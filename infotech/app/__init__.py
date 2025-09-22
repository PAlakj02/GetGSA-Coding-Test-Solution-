from flask import Flask
import logging
import os

def create_app():
    # Tell Flask where to find static files
    app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), "..", "static"))

    logging.basicConfig(level=logging.INFO)

    from app.api import api_bp
    app.register_blueprint(api_bp)

    # Root route → serve index.html
    @app.route("/")
    def index():
        return app.send_static_file("index.html")

    return app

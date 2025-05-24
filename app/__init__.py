from flask import Flask
from app.routes import main
import os

def create_app():
    # Set the template folder path relative to this file
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_path = os.path.join(os.path.dirname(base_dir), 'templates')

    app = Flask(__name__, template_folder=template_path)
    app.register_blueprint(main)
    return app


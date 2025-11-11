#!/usr/bin/env python3
"""
jokes api

@author:
@version: 2025.11
"""

import pathlib
import tomllib

from flask import Flask, request
from flask_cors import CORS


def create_app() -> Flask:

    # TODO: Implement this function
    from routes import main

    app = Flask(__name__)
    CORS(app)
    this_dir = pathlib.Path(__file__).parent
    with open(this_dir / pathlib.Path("config.toml"), "rb") as f:
        config = tomllib.load(f)
    app.config.update(config)
    # this_app.config["LANGUAGES"] = Joker(this_app.config)

    app.register_blueprint(main)

    return app

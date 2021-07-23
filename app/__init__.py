from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from app.models.card import Card
    from app.models.player import Player
    from app.models.deck import Deck

    from .routes import decks_bp
    from .routes import players_bp
    
    app.register_blueprint(decks_bp)
    app.register_blueprint(players_bp)

    CORS(app)
    return app
    
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Configs

db = SQLAlchemy()

def create_app(config_class=Configs):
    app = Flask(__name__)
    app.config.from_object(Configs)
    db.init_app(app)

    from app.user.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors

    app.register_blueprint(users, url_prefix="/user")
    app.register_blueprint(posts, url_prefix="/post")
    app.register_blueprint(main)
    app.register_blueprint(errors, url_prefix="/errors")

    return app


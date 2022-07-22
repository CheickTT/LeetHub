from flask import Flask
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_github import GitHub


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        SECRET_KEY = '063b5d59f24fbf66d126cfb5e661902f',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db',
        GITHUB_CLIENT_ID = 'ab4ba779cdca8f176427',
        GITHUB_CLIENT_SECRET = 'ba6477b7e725379cb403c1f6f41d1cc12a94982d'
    )

    return app

login_manager = LoginManager()

app = create_app()
proxied = FlaskBehindProxy(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
postdb = SQLAlchemy(app)
github = GitHub(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flasksite import routes


import os
from flask import Flask
from blog.core.views import core
from blog.errors.handlers import errors
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login' # TODO need to make views for users.login


db = SQLAlchemy(app)


app.register_blueprint(core)
app.register_blueprint(errors)
# Note setup vm (DONE)
# Grab requirements.txt  (DONE)
# Grab env file setup and add to gitignore (DONE)
# Test initial route setup for core cmp path (DONE)
# Do db config setup, clone from prev project and adjust as needed
# Not bothering with migrations, just deleting  I've migrated enough
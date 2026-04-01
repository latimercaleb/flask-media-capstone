import os
from flask import Flask
from blog.core.views import core
from blog.errors.handlers import errors
from blog.users.views import users
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
app.register_blueprint(users)
# Note setup vm (DONE)
# Grab requirements.txt  (DONE)
# Grab env file setup and add to gitignore (DONE)
# Test initial route setup for core cmp path (DONE)
# Delete extra folders & unneeded files
# Do db config setup, clone from prev project and adjust as needed
# Not bothering with migrations, just deleting  I've migrated enough
# Setup secret key, like actually
# Adjust db for using secret key config

'''
    Site test requirements:
    - At this point work on testing site behavior before implementing the posts section and do some bug fixes
    - Fix all todo items first
    - Routes should work, log in and log out should work
    - Updating user profile and picture should work
    - Be keen on profile pic integration, this part might get a little hairy
    - Include multi-part/form-type for image processing
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
sKey = os.getenv('Secret_Key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'media-data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = sKey

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'



from blog.core.views import core
from blog.errors.handlers import errors
from blog.users.views import users
from blog.posts.views import posts
app.register_blueprint(core)
app.register_blueprint(errors)
app.register_blueprint(users)
app.register_blueprint(posts)

# Note setup vm (DONE)
# Grab requirements.txt  (DONE)
# Grab env file setup and add to gitignore (DONE)
# Test initial route setup for core cmp path (DONE)
# Do db config setup, clone from prev project and adjust as needed (DONE)
# Not bothering with migrations, just deleting  I've migrated enough (DONE)
# Setup secret key, like actually (DONE)
# Adjust db for using secret key config (DONE)
# Check for pil install make sure its in requirements and imported correctly (DONE)
# Get bulma imported properly into templates (DONE)
# Review user_posts template and do paginator implementation (DONE)
# Run db setup (should be configured need to try running it, DONE)
# Delete extra folders & unneeded files
# Finish writing out forms get all logic 
# Form validation tested

'''
    Site test requirements:
    - At this point work on testing site behavior before implementing the posts section and do some bug fixes (DONE)
    - Routes should work, log in and log out should work (DONE)
    - Include multi-part/form-type for image processing (DONE)
    - Fix all todo items first 
    - Updating user profile and picture should work (DONE BUT default picture needs to be adjusted via styles START HERE IN THE MORNING!)
    - Add a default_pic.png to the folder
    - Be keen on profile pic integration, this part might get a little hairy
'''
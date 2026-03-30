from flask import Flask
from blog.core.views import core
from blog.errors.handlers import errors
app = Flask(__name__)
app.register_blueprint(core)
app.register_blueprint(errors)
# Note setup vm (DONE)
# Grab requirements.txt  (DONE)
# Grab env file setup and add to gitignore (DONE)
# Test initial route setup for core cmp path (DONE)
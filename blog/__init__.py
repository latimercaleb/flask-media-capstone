from flask import Flask
from blog.core.views import core
app = Flask(__name__)
app.register_blueprint(core)
# Note setup vm (DONE)
# Grab requirements.txt  (DONE)
# Grab env file setup and add to gitignore (DONE)
# Test initial route setup for core cmp path (DONE)
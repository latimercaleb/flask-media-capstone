from flask import Flask
from core.views import core
app = Flask(__name__)
app.register_blueprint(core)
# Note setup vm
# Grab requirements.txt 
# Grab env file setup and add to gitignore

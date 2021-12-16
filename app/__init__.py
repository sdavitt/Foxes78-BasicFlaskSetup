# import our necessary modules/files/classes/packages/whatever else we need for this file to work
from flask import Flask
from config import Config

# define our application as an instance of the Flask object... aka tell the computer this is a flask app
app = Flask(__name__)

# tell our application to configure itself based on the config class
app.config.from_object(Config)

# tell our app where it find its routing information
# note that this import specifically (and later a models import) must come AFTER the app is defined
from . import routes
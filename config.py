# we're going to set up the application's configuration using a class and some variables
# we're also gonna help out the application by telling it a little bit about it's own file structure

# import - we need a little help from the os package
import os

# set the base directory of the entire project - so that our computer knows the location of various files in this project
basedir = os.path.abspath(os.path.dirname(__name__))

# set up our configuration
class Config:
    """
    set config variables for our flask app
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
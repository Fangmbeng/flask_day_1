from flask import Flask

app = Flask(__name__)

#import all routes packages

from . import routes
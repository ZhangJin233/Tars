from flask import Flask
from config import Config

tars = Flask(__name__)
tars.debug = True
tars.config.from_object(Config)

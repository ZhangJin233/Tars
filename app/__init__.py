from flask import Flask
from config import Config
from flask_cors import CORS

tars = Flask(__name__)
CORS(tars, supports_credentials=True)
tars.debug = True
tars.config.from_object(Config)

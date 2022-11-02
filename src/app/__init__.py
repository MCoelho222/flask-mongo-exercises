import os
from flask import Flask
from src.app.config import app_config
from src.app.swagger import create_swagger
from flask_cors import CORS
from src.app.utils import mongo

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('FLASK_ENV')])
create_swagger(app)
mongo.init_app(app)
mongo_client = mongo.db
CORS(app)



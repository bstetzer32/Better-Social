import os
from .models import db
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .config import Config

app = Flask(__name__)

db.init_app(app)
Migrate(app, db)
CORS(app)
better_social = 'As1F#d8e0&'

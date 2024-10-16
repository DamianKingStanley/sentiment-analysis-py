from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from app.config import Config
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config.from_object(Config)

# Initialize CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

mongo = PyMongo(app)

from app import routes

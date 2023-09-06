# app/__init__.py
from flask import Flask

app = Flask(__name__)

from app import api

app.run(debug=True)  # Run the Flask app in debug mode for development
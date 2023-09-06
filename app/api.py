# app/api.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def index():
    response = {
        1: "Never gonna give you up",
        2: "Never gonna let you down",
        3: "Never gonna run around and desert you",
        4: "Never gonna make you cry",
        5: "Never gonna say goodbye",
        6: "Never gonna tell a lie and hurt you"
    }
    return jsonify(response), 200

#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API"


@app.route('/data')
def jsonfy():
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    return jsonify({'users': users})


@app.route('/status')
def status():
    status = jsonify(success=200)
    return status


@app.route('/users/<username>')
def name(username: str):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=['POST'])
def register():
    data = request.get_json()

    username = data['username']

    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', ''),
        "city": data.get('city', '')
    }

    return jsonify({"message": "User added", "user": users[username]})


if __name__ == "__main__":
    app.run()

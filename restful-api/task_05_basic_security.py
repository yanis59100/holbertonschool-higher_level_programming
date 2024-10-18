from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()


app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)


users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username


@app.route('/')
@auth.login_required
def index():
    return f"Hello, {auth.current_user()}!"


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401


    access_token = create_access_token(identity={"username": user['username'], "role": user['role']})
    return jsonify({"access_token": access_token})


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted", "user": current_user})

if __name__ == '__main__':
    app.run()

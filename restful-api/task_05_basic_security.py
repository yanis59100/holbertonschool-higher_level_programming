from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta



app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username)["password"], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted"), 200


app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    from flask import request

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted"), 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()

    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return jsonify(message="Admin Access: Granted"), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == '__main__':
    app.run()

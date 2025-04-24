from flask import Flask, jsonify, request, abort
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'  # Replace with a secure key

users = {}
USERNAME = "admin"
PASSWORD = "password"

# JWT token-required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get("username") == USERNAME and data.get("password") == PASSWORD:
        token = jwt.encode({
            'user': USERNAME,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/users', methods=['POST'])
@token_required
def create_user():
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        abort(400)
    user_id = max(users.keys(), default=0) + 1
    users[user_id] = {"id": user_id, "name": data["name"], "email": data["email"]}
    return jsonify(users[user_id]), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
@token_required
def update_user(user_id):
    if user_id not in users:
        abort(404)
    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id]), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
@token_required
def delete_user(user_id):
    if user_id not in users:
        abort(404)
    del users[user_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

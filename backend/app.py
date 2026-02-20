from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Credentials from env
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "admin123")


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    if username == ADMIN_USER and password == ADMIN_PASS:
        return jsonify({"status": "success", "message": "Login successful"})
    else:
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 401


@app.route("/table/<int:number>", methods=["GET"])
def get_table(number):
    if number < 2 or number > 20:
        return jsonify({"error": "Number must be between 2 and 20"}), 400

    table = [f"{number} x {i} = {number*i}" for i in range(1, 11)]
    return jsonify({"number": number, "table": table})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


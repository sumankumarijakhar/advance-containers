# app/main.py
import os, logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# ---------------- basic setup ----------------
app = Flask(__name__)
logging.basicConfig(filename="app.log", level=logging.INFO)

# Database connection string assembled from env vars
POSTGRES_USER = os.getenv("POSTGRES_USER", "appuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_DB = os.getenv("POSTGRES_DB", "appdb")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")   # service name in compose
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# ---------------- model & auto-migrate ----------------
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name  = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

# ---------------- REST endpoints ----------------
@app.before_request
def log_request():
    app.logger.info(f"--> {request.method} {request.path} | Body: {request.get_data()}")

@app.after_request
def log_response(res):
    app.logger.info(f"<-- {res.status}")
    return res

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    if not {"first_name", "last_name"} <= data.keys():
        return jsonify({"error": "first_name and last_name required"}), 400
    u = User(first_name=data["first_name"], last_name=data["last_name"])
    db.session.add(u); db.session.commit()
    return jsonify({"id": u.id, "first_name": u.first_name, "last_name": u.last_name}), 201

@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    u = User.query.get_or_404(user_id)
    return jsonify({"id": u.id, "first_name": u.first_name, "last_name": u.last_name})

if __name__ == "__main__":                     # dev mode only
    app.run(host="0.0.0.0", port=8000)

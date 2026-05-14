from flask import Blueprint, jsonify, session
from models.db import get_db

dashboard_bp = Blueprint("dashboard_bp", __name__)


@dashboard_bp.route("/dashboard-stats")
def dashboard_stats():

    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_db()

    total = conn.execute(
        "SELECT COUNT(*) as count FROM analyses WHERE email=?",
        (session["user"],)
    ).fetchone()["count"]

    avg_score = conn.execute(
        "SELECT AVG(score) as avg FROM analyses WHERE email=?",
        (session["user"],)
    ).fetchone()["avg"]

    return jsonify({
        "total_resumes": total,
        "average_score": round(avg_score or 0, 2)
    })
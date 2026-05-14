from flask import Blueprint, request, jsonify, session
from models.db import get_db
from services.resume_service import analyze_resume
import os

resume_bp = Blueprint("resume_bp", __name__)

UPLOAD_FOLDER = "uploads"


# -----------------------------
# Upload Resume
# -----------------------------
@resume_bp.route("/upload", methods=["POST"])
def upload_resume():

    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    file = request.files["resume"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    score = analyze_resume(filepath)

    conn = get_db()
    conn.execute(
        "INSERT INTO analyses (email, filename, role, score) VALUES (?, ?, ?, ?)",
        (session["user"], file.filename, "SDE", score),
    )
    conn.commit()

    return jsonify({
        "message": "Resume uploaded",
        "score": score
    })


# -----------------------------
# Resume History
# -----------------------------
@resume_bp.route("/history")
def history():

    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_db()

    rows = conn.execute(
        "SELECT filename, role, score FROM analyses WHERE email=?",
        (session["user"],)
    ).fetchall()

    data = [dict(r) for r in rows]

    return jsonify(data)
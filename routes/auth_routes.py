from flask import Blueprint, jsonify, request, render_template, redirect, session
from models.db import get_db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]

        conn = get_db()
        conn.execute("INSERT OR IGNORE INTO users(email) VALUES(?)",(email,))
        conn.commit()

        session["user"] = email
        return redirect("/")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
from flask import session



from __future__ import annotations

from flask import Flask, flash, redirect, render_template, request, session, url_for

from demo_data import get_demo_data

app = Flask(__name__)
app.secret_key = "modern-car-service-demo"


@app.context_processor
def inject_common_context():
    data = get_demo_data()
    return {
        "app_name": "AutoFlow Service Hub",
        "current_user": session.get("user"),
        "demo_now": data["now"],
    }


@app.route("/")
def index():
    if session.get("user"):
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()

    if not email or not password:
        flash("Unesite email i lozinku.", "error")
        return redirect(url_for("index"))

    session["user"] = {
        "name": request.form.get("name") or "Servisni menadžer",
        "email": email,
        "role": "Administrator",
    }
    flash("Uspješna prijava u demo verziju platforme.", "success")
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    flash("Odjavljeni ste iz aplikacije.", "info")
    return redirect(url_for("index"))



def require_auth():
    if not session.get("user"):
        return redirect(url_for("index"))
    return None


@app.route("/dashboard")
def dashboard():
    auth = require_auth()
    if auth:
        return auth
    data = get_demo_data()
    return render_template("dashboard.html", **data)


@app.route("/vehicles")
def vehicles():
    auth = require_auth()
    if auth:
        return auth
    data = get_demo_data()
    return render_template("vehicles.html", **data)


@app.route("/appointments")
def appointments():
    auth = require_auth()
    if auth:
        return auth
    data = get_demo_data()
    return render_template("appointments.html", **data)


@app.route("/booking", methods=["GET", "POST"])
def booking():
    auth = require_auth()
    if auth:
        return auth
    data = get_demo_data()
    if request.method == "POST":
        flash(
            f"Termin za vozilo {request.form.get('plate', 'N/A')} je kreiran i čeka potvrdu servisnog savjetnika.",
            "success",
        )
        return redirect(url_for("appointments"))
    return render_template("booking.html", **data)


@app.route("/customers")
def customers():
    auth = require_auth()
    if auth:
        return auth
    data = get_demo_data()
    return render_template("customers.html", **data)


@app.route("/inventory")
def inventory():
    auth = require_auth()
    if auth:
        return auth
    data = get_demo_data()
    return render_template("inventory.html", **data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

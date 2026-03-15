import os
from functools import wraps

import requests
from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getenv("FRONTEND_SECRET_KEY", "change-me-in-production")
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000").rstrip("/")  # Base backend URL, for example https://your-backend.onrender.com
TIMEOUT = 12


def api_request(method: str, endpoint: str, *, json=None, auth=True):
    headers = {"Content-Type": "application/json"}
    token = session.get("token")
    if auth and token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.request(
        method,
        f"{API_URL}{endpoint}",
        json=json,
        headers=headers,
        timeout=TIMEOUT,
    )
    return response


@app.context_processor
def inject_globals():
    return {
        "current_user_email": session.get("user_email"),
        "current_user_name": session.get("user_name"),
    }


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "token" not in session:
            return redirect(url_for("login_page"))
        return view(*args, **kwargs)

    return wrapped


@app.route("/")
def login_page():
    if session.get("token"):
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    payload = {
        "email": request.form.get("email", "").strip(),
        "password": request.form.get("password", ""),
    }
    response = api_request("POST", "/api/auth/login/", json=payload, auth=False)
    if response.status_code != 200:
        flash("Invalid email or password.", "error")
        return redirect(url_for("login_page"))

    data = response.json()
    session["token"] = data["access"]
    session["refresh"] = data["refresh"]
    session["user_email"] = data["user"]["email"]
    session["user_name"] = f"{data['user']['first_name']} {data['user']['last_name']}".strip()
    session["user_role"] = data["user"]["role"]
    flash("Welcome back.", "success")
    return redirect(url_for("dashboard"))


@app.route("/register", methods=["POST"])
def register():
    payload = {
        "email": request.form.get("email", "").strip(),
        "first_name": request.form.get("first_name", "").strip(),
        "last_name": request.form.get("last_name", "").strip(),
        "password": request.form.get("password", ""),
    }
    response = api_request("POST", "/api/auth/register/", json=payload, auth=False)
    if response.status_code not in (200, 201):
        try:
            message = response.json().get("error", "Registration failed.")
        except Exception:
            message = "Registration failed."
        flash(message, "error")
        return redirect(url_for("login_page"))

    data = response.json()
    session["token"] = data["access"]
    session["refresh"] = data["refresh"]
    session["user_email"] = data["user"]["email"]
    session["user_name"] = f"{data['user']['first_name']} {data['user']['last_name']}".strip()
    session["user_role"] = data["user"]["role"]
    flash("Account created successfully.", "success")
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
@login_required
def dashboard():
    summary = {}
    recent_appointments = []
    try:
        summary_response = api_request("GET", "/api/dashboard/summary/")
        if summary_response.ok:
            summary = summary_response.json()

        appointments_response = api_request("GET", "/api/appointments/")
        if appointments_response.ok:
            recent_appointments = appointments_response.json()[:5]
    except requests.RequestException:
        flash("The backend service is currently unavailable.", "error")

    return render_template(
        "dashboard.html",
        summary=summary,
        recent_appointments=recent_appointments,
    )


@app.route("/vehicles")
@login_required
def vehicles():
    vehicles_data = []
    try:
        response = api_request("GET", "/api/vehicles/")
        if response.ok:
            vehicles_data = response.json()
    except requests.RequestException:
        flash("Unable to load vehicles.", "error")
    return render_template("vehicles.html", vehicles=vehicles_data)


@app.route("/appointments")
@login_required
def appointments():
    appointments_data = []
    try:
        response = api_request("GET", "/api/appointments/")
        if response.ok:
            appointments_data = response.json()
    except requests.RequestException:
        flash("Unable to load appointments.", "error")
    return render_template("appointments.html", appointments=appointments_data)


@app.route("/booking")
@login_required
def booking():
    vehicles_data = []
    services_data = []
    staff_data = []
    try:
        vehicles_response = api_request("GET", "/api/vehicles/")
        services_response = api_request("GET", "/api/services/")
        staff_response = api_request("GET", "/api/staff/")
        if vehicles_response.ok:
            vehicles_data = vehicles_response.json()
        if services_response.ok:
            services_data = services_response.json()
        if staff_response.ok:
            staff_data = staff_response.json()
    except requests.RequestException:
        flash("Unable to load booking resources.", "error")

    return render_template(
        "booking.html",
        vehicles=vehicles_data,
        services=services_data,
        staff_members=staff_data,
    )


@app.route("/booking", methods=["POST"])
@login_required
def create_booking():
    payload = {
        "vehicle": int(request.form.get("vehicle")),
        "service": int(request.form.get("service")),
        "staff": int(request.form.get("staff")),
        "start_time": request.form.get("start_time"),
    }

    try:
        response = api_request("POST", "/api/appointments/", json=payload)
        if response.status_code in (200, 201):
            flash("Appointment created successfully.", "success")
            return redirect(url_for("appointments"))

        try:
            data = response.json()
            detail = data.get("detail") or data.get("non_field_errors") or data
        except Exception:
            detail = "Could not create the appointment."
        flash(str(detail), "error")
    except requests.RequestException:
        flash("Unable to reach the backend service.", "error")

    return redirect(url_for("booking"))


@app.route("/customers")
@login_required
def customers():
    customers_data = []
    try:
        response = api_request("GET", "/api/customers/")
        if response.ok:
            customers_data = response.json()
    except requests.RequestException:
        flash("Unable to load customers.", "error")
    return render_template("customers.html", customers=customers_data)


@app.route("/inventory")
@login_required
def inventory():
    inventory_items = [
        {"name": "Engine Oil 5W-30", "sku": "OIL-530", "stock": 24, "status": "In stock"},
        {"name": "Brake Pads Set", "sku": "BRK-204", "stock": 7, "status": "Low stock"},
        {"name": "Air Filter", "sku": "FLT-110", "stock": 16, "status": "In stock"},
        {"name": "Battery 70Ah", "sku": "BAT-70", "stock": 3, "status": "Critical"},
    ]
    return render_template("inventory.html", items=inventory_items)


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been signed out.", "success")
    return redirect(url_for("login_page"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 3000)))

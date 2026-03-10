from flask import Blueprint, request, jsonify
from app.extensions import db
from sqlalchemy import text

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/", methods=["POST"])
def create_booking():
    data = request.json

    query = text("""
        INSERT INTO appointments_appointment
        (vehicle_id, service_id, staff_id, start_time, end_time, status, created_at)
        VALUES (:vehicle, :service, :staff, :start, :end, 'CONFIRMED', NOW())
    """)

    db.session.execute(query, {
        "vehicle": data["vehicle_id"],
        "service": data["service_id"],
        "staff": data["staff_id"],
        "start": data["start_time"],
        "end": data["end_time"],
    })

    db.session.commit()

    return jsonify(message="Appointment created"), 201
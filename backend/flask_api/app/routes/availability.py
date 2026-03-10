from flask import Blueprint, request, jsonify
from app.extensions import db
from datetime import datetime
from sqlalchemy import text

availability_bp = Blueprint("availability", __name__)

@availability_bp.route("/", methods=["GET"])
def check_availability():
    staff_id = request.args.get("staff_id")
    start = request.args.get("start")
    end = request.args.get("end")

    query = text("""
        SELECT COUNT(*) FROM appointments_appointment
        WHERE staff_id = :staff_id
        AND status IN ('PENDING', 'CONFIRMED')
        AND start_time < :end
        AND end_time > :start
    """)

    result = db.session.execute(query, {
        "staff_id": staff_id,
        "start": start,
        "end": end
    }).scalar()

    return jsonify(available=result == 0)
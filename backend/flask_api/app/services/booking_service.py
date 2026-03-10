from app.extensions import db
from sqlalchemy import text


def create_booking(vehicle_id, service_id, staff_id, start_time, end_time):
    query = text("""
        INSERT INTO appointments_appointment
        (vehicle_id, service_id, staff_id, start_time, end_time, status, created_at)
        VALUES (:vehicle_id, :service_id, :staff_id, :start_time, :end_time, 'CONFIRMED', NOW())
    """)

    db.session.execute(query, {
        "vehicle_id": vehicle_id,
        "service_id": service_id,
        "staff_id": staff_id,
        "start_time": start_time,
        "end_time": end_time
    })

    db.session.commit()
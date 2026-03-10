from app.extensions import db
from sqlalchemy import text


def is_staff_available(staff_id, start_time, end_time):
    query = text("""
        SELECT COUNT(*) 
        FROM appointments_appointment
        WHERE staff_id = :staff_id
        AND status IN ('PENDING','CONFIRMED')
        AND start_time < :end_time
        AND end_time > :start_time
    """)

    result = db.session.execute(query, {
        "staff_id": staff_id,
        "start_time": start_time,
        "end_time": end_time
    }).scalar()

    return result == 0
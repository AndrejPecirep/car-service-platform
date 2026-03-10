from dataclasses import dataclass
from datetime import datetime


@dataclass
class BookingSchema:
    vehicle_id: int
    service_id: int
    staff_id: int
    start_time: datetime
    end_time: datetime
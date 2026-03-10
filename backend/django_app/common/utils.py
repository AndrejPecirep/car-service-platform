from datetime import timedelta


def calculate_end_time(start_time, duration_minutes):
    """
    Calculate appointment end time
    """
    return start_time + timedelta(minutes=duration_minutes)


def normalize_license_plate(plate: str):
    """
    Normalize license plate format
    """
    return plate.strip().upper()
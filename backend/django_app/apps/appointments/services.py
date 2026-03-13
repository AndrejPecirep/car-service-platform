from .models import Appointment


def is_time_slot_available(staff, start_time, end_time):
    if not staff:
        return True
    return not Appointment.objects.filter(
        staff=staff,
        start_time__lt=end_time,
        end_time__gt=start_time,
        status__in=[Appointment.Status.PENDING, Appointment.Status.CONFIRMED],
    ).exists()

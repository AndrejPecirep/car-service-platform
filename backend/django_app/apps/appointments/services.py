from .models import Appointment


def is_time_slot_available(staff, start_time, end_time):
    return not Appointment.objects.filter(
        staff=staff,
        status__in=[Appointment.Status.PENDING, Appointment.Status.CONFIRMED],
        start_time__lt=end_time,
        end_time__gt=start_time,
    ).exists()

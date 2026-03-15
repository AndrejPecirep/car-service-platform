from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.appointments.models import Appointment
from apps.services.models import Service
from apps.users.models import User
from apps.vehicles.models import Vehicle


class Command(BaseCommand):
    help = "Seed demo data for the car service platform"

    def handle(self, *args, **options):
        admin, _ = User.objects.get_or_create(
            email="admin@torqueflow.com",
            defaults={"first_name": "Workshop", "last_name": "Admin", "role": User.Role.ADMIN, "is_staff": True, "is_superuser": True},
        )
        if not admin.password:
            admin.set_password("Admin123!")
            admin.save()

        staff_members = []
        for first_name, last_name, email in [
            ("Mia", "Turner", "mia@torqueflow.com"),
            ("Liam", "Brooks", "liam@torqueflow.com"),
        ]:
            staff, created = User.objects.get_or_create(
                email=email,
                defaults={
                    "first_name": first_name,
                    "last_name": last_name,
                    "role": User.Role.STAFF,
                    "is_staff": True,
                },
            )
            if created or not staff.password:
                staff.set_password("Staff123!")
                staff.save()
            staff_members.append(staff)

        customers = []
        for first_name, last_name, email in [
            ("Oliver", "Stone", "oliver@example.com"),
            ("Emma", "Cole", "emma@example.com"),
        ]:
            customer, created = User.objects.get_or_create(
                email=email,
                defaults={
                    "first_name": first_name,
                    "last_name": last_name,
                    "role": User.Role.CLIENT,
                },
            )
            if created or not customer.password:
                customer.set_password("Client123!")
                customer.save()
            customers.append(customer)

        services = []
        for name, desc, duration, price in [
            ("Oil Change", "Standard oil and filter replacement", 45, 79.0),
            ("Brake Inspection", "Brake pad and disc diagnostics", 60, 95.0),
            ("Full Service", "Comprehensive multi-point inspection and maintenance", 150, 249.0),
        ]:
            service, _ = Service.objects.get_or_create(
                name=name,
                defaults={"description": desc, "duration_minutes": duration, "price": price},
            )
            services.append(service)

        vehicles = []
        for owner, brand, model, year, plate in [
            (customers[0], "Audi", "A4", 2021, "SA-101-AA"),
            (customers[1], "BMW", "320d", 2020, "MO-202-BB"),
        ]:
            vehicle, _ = Vehicle.objects.get_or_create(
                license_plate=plate,
                defaults={"owner": owner, "brand": brand, "model": model, "year": year},
            )
            vehicles.append(vehicle)

        start_time = timezone.now() + timedelta(days=1)
        for index, vehicle in enumerate(vehicles):
            service = services[index % len(services)]
            staff = staff_members[index % len(staff_members)]
            Appointment.objects.get_or_create(
                vehicle=vehicle,
                service=service,
                staff=staff,
                start_time=start_time + timedelta(hours=index * 3),
                defaults={
                    "end_time": start_time + timedelta(hours=index * 3, minutes=service.duration_minutes),
                    "status": Appointment.Status.CONFIRMED,
                },
            )

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully."))

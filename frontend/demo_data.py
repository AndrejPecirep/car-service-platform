from __future__ import annotations

from datetime import datetime, timedelta


def get_demo_data():
    now = datetime(2026, 3, 14, 9, 30)

    vehicles = [
        {
            "id": 1,
            "brand": "Audi",
            "model": "A4 Avant",
            "year": 2021,
            "plate": "SA-452-KT",
            "owner": "Amar H.",
            "status": "U radionici",
            "health": "Stabilno",
            "next_service": "Za 1.200 km",
            "service_type": "Veliki servis",
        },
        {
            "id": 2,
            "brand": "BMW",
            "model": "320d",
            "year": 2019,
            "plate": "TZ-119-AA",
            "owner": "Lejla M.",
            "status": "Čeka dijelove",
            "health": "Pažnja",
            "next_service": "Danas",
            "service_type": "Kočioni sistem",
        },
        {
            "id": 3,
            "brand": "Volkswagen",
            "model": "Golf 7",
            "year": 2018,
            "plate": "MO-775-LJ",
            "owner": "Nermin K.",
            "status": "Spremno za isporuku",
            "health": "Odlično",
            "next_service": "Za 3.500 km",
            "service_type": "Mali servis",
        },
        {
            "id": 4,
            "brand": "Škoda",
            "model": "Octavia",
            "year": 2020,
            "plate": "ZE-628-RR",
            "owner": "Mia P.",
            "status": "Rezervisan termin",
            "health": "Praćenje",
            "next_service": "Za 10 dana",
            "service_type": "Dijagnostika",
        },
    ]

    services = [
        {"id": 1, "name": "Mali servis", "duration": 60, "price": 120},
        {"id": 2, "name": "Veliki servis", "duration": 180, "price": 420},
        {"id": 3, "name": "Dijagnostika", "duration": 45, "price": 55},
        {"id": 4, "name": "Kočioni sistem", "duration": 90, "price": 165},
    ]

    staff = [
        {"id": 1, "name": "Adnan S.", "role": "Glavni mehaničar", "utilization": 84},
        {"id": 2, "name": "Sara T.", "role": "Servisni savjetnik", "utilization": 68},
        {"id": 3, "name": "Mahir D.", "role": "Auto električar", "utilization": 76},
    ]

    appointments = [
        {
            "id": 1001,
            "customer": "Amar H.",
            "vehicle": "Audi A4 Avant",
            "plate": "SA-452-KT",
            "service": "Veliki servis",
            "advisor": "Sara T.",
            "start": now.replace(hour=9, minute=0),
            "end": now.replace(hour=12, minute=0),
            "status": "U toku",
            "priority": "Visok",
            "amount": 420,
        },
        {
            "id": 1002,
            "customer": "Lejla M.",
            "vehicle": "BMW 320d",
            "plate": "TZ-119-AA",
            "service": "Kočioni sistem",
            "advisor": "Adnan S.",
            "start": now.replace(hour=11, minute=30),
            "end": now.replace(hour=13, minute=0),
            "status": "Čeka dijelove",
            "priority": "Srednji",
            "amount": 165,
        },
        {
            "id": 1003,
            "customer": "Nermin K.",
            "vehicle": "Volkswagen Golf 7",
            "plate": "MO-775-LJ",
            "service": "Mali servis",
            "advisor": "Mahir D.",
            "start": now.replace(day=15, hour=8, minute=30),
            "end": now.replace(day=15, hour=9, minute=30),
            "status": "Potvrđen",
            "priority": "Nizak",
            "amount": 120,
        },
        {
            "id": 1004,
            "customer": "Mia P.",
            "vehicle": "Škoda Octavia",
            "plate": "ZE-628-RR",
            "service": "Dijagnostika",
            "advisor": "Sara T.",
            "start": now.replace(day=16, hour=10, minute=0),
            "end": now.replace(day=16, hour=10, minute=45),
            "status": "Zakazan",
            "priority": "Srednji",
            "amount": 55,
        },
    ]

    customers = [
        {"name": "Amar Hadžić", "email": "amar@example.com", "tier": "Gold", "visits": 8, "last": "prije 5 dana"},
        {"name": "Lejla Mujić", "email": "lejla@example.com", "tier": "Silver", "visits": 4, "last": "danas"},
        {"name": "Nermin Karić", "email": "nermin@example.com", "tier": "Bronze", "visits": 2, "last": "prije 12 dana"},
    ]

    inventory = [
        {"part": "Ulje 5W-30", "sku": "OIL-530", "stock": 26, "state": "Dostupno"},
        {"part": "Filter zraka", "sku": "FLT-AIR-02", "stock": 7, "state": "Nisko stanje"},
        {"part": "Kočione pločice", "sku": "BRK-118", "stock": 4, "state": "Hitno naručiti"},
        {"part": "Akumulator 74Ah", "sku": "BAT-74", "stock": 11, "state": "Dostupno"},
    ]

    kpis = {
        "revenue_today": 760,
        "open_orders": 12,
        "vehicles_in_shop": 7,
        "on_time_rate": 96,
    }

    timeline = [
        {"time": "08:00", "title": "Preuzimanje vozila i prijem", "type": "done"},
        {"time": "09:30", "title": "Dijagnostika i procjena", "type": "current"},
        {"time": "12:00", "title": "Nabavka dijelova", "type": "planned"},
        {"time": "15:30", "title": "Kontrola kvaliteta i isporuka", "type": "planned"},
    ]

    booking_slots = [
        (now + timedelta(days=1)).replace(hour=8, minute=30).strftime("%d.%m. %H:%M"),
        (now + timedelta(days=1)).replace(hour=10, minute=0).strftime("%d.%m. %H:%M"),
        (now + timedelta(days=2)).replace(hour=9, minute=15).strftime("%d.%m. %H:%M"),
        (now + timedelta(days=2)).replace(hour=13, minute=45).strftime("%d.%m. %H:%M"),
    ]

    return {
        "now": now,
        "vehicles": vehicles,
        "services": services,
        "staff": staff,
        "appointments": appointments,
        "customers": customers,
        "inventory": inventory,
        "kpis": kpis,
        "timeline": timeline,
        "booking_slots": booking_slots,
    }

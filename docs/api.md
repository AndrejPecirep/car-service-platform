# Car Service Platform API

## Authentication

POST /api/auth/login

Body

{
  "email": "user@example.com"
}

Response

{
  "access_token": "JWT_TOKEN"
}

---

## Check availability

GET /api/availability?staff_id=1&start=2026-01-01T10:00&end=2026-01-01T11:00

---

## Create booking

POST /api/booking

{
  "vehicle_id":1,
  "service_id":2,
  "staff_id":3,
  "start_time":"2026-01-01T10:00",
  "end_time":"2026-01-01T11:00"
}
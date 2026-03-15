# Car Service Platform

A modern workshop management platform for service garages.

## Deployment target
This package is prepared for:

- **Frontend on Render**
- **Backend on Render**
- **Database on Render PostgreSQL**

## Architecture
- **Frontend**: Flask dashboard app
- **Backend**: Django REST API + Django Admin
- **Database**: Render PostgreSQL

## Main features
- Secure login and registration
- Dashboard with live business summary
- Vehicle overview
- Appointment scheduling
- Customer directory
- Inventory overview
- Django Admin for back-office management

## Environment variable note
The frontend already uses `API_URL`.

Set it to the backend base URL, for example:

```
https://car-service-backend.onrender.com
```

Do not add `/api` at the end.

## Files included
- `render.yaml` for Render Blueprint deployment
- `DEPLOY_RENDER.md` with step-by-step deployment instructions
- demo data seeding command for backend testing

See `DEPLOY_RENDER.md` for the full deployment guide.

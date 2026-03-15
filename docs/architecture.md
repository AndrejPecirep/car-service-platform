# Architecture Overview

## Frontend
A Flask-based server-rendered dashboard used for authentication and operational views.

## Backend
A Django REST API that exposes authentication, vehicles, services, appointments, staff, customers, and dashboard summary endpoints.

## Database
PostgreSQL stores users, vehicles, services, and appointment data.

## Deployment
Recommended target:
- Frontend on Render
- Backend on Render
- PostgreSQL on Render

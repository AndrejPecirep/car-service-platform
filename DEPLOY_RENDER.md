# Deploy on Render

This package is prepared for this setup:

- **Frontend**: Flask app on Render
- **Backend**: Django API on Render
- **Database**: Render PostgreSQL

## Important
The frontend already uses an environment variable called `API_URL`.

Use the **backend base URL only**, without `/api` at the end.

Correct example:

```
https://car-service-backend.onrender.com
```

Do **not** use:

```
https://car-service-backend.onrender.com/api
```

The frontend code already appends routes such as `/api/auth/login/` and `/api/appointments/`.

---

## 1. Upload the project to GitHub
1. Create a new GitHub repository.
2. Upload the full project from this ZIP file.
3. Make sure `render.yaml` stays in the root of the repository.

---

## 2. Create the database on Render
1. Open Render.
2. Click **New**.
3. Select **PostgreSQL**.
4. Choose the **Free** plan.
5. Name it something like `car-service-db`.
6. Wait until the database is provisioned.

You do not need to manually copy database credentials if you deploy with `render.yaml`, because the backend service is already configured to read the database values from Render automatically.

---

## 3. Deploy the backend on Render
1. In Render, click **New**.
2. Select **Web Service**.
3. Connect your GitHub repository.
4. Deploy the service using the repository root.
5. Confirm these settings for the backend service:

- **Root Directory**: `backend/django_app`
- **Build Command**: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
- **Start Command**: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

### Required backend environment variables
- `DJANGO_SECRET_KEY` = generate a strong random value
- `DJANGO_DEBUG` = `False`
- `DJANGO_ALLOWED_HOSTS` = your backend Render domain, for example `car-service-backend.onrender.com`

If you use the included `render.yaml`, the Postgres variables are already wired from the Render database service.

---

## 4. Deploy the frontend on Render
1. In Render, click **New**.
2. Select **Web Service**.
3. Connect the same GitHub repository.
4. Confirm these settings for the frontend service:

- **Root Directory**: `frontend`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`

### Required frontend environment variables
- `FRONTEND_SECRET_KEY` = generate a strong random value
- `API_URL` = your backend base URL, for example `https://car-service-backend.onrender.com`

Again, do not add `/api` at the end.

---

## 5. Recommended deploy method
The easiest method is to use the included `render.yaml`.

From Render, you can create a **Blueprint** deployment from the repository root. That file already defines:

- one backend web service
- one frontend web service
- one free PostgreSQL database

You will still set your secrets when prompted.

---

## 6. Seed demo data
After the backend is live, open the backend Render shell and run:

```bash
python manage.py seed_demo_data
```

This creates sample users, vehicles, services, and appointments for testing.

---

## 7. Create an admin user
In the backend Render shell, run:

```bash
python manage.py createsuperuser
```

Then open:

```
https://<your-backend>.onrender.com/admin/
```

---

## 8. Test the application
1. Open the frontend Render URL.
2. Register a user or sign in with seeded demo data.
3. The frontend will communicate with the backend through the configured `API_URL`.

If the backend is sleeping on the free plan, the first request can take a little longer.

---

## 9. Free plan note
Render free services can spin down after inactivity. Render free PostgreSQL is suitable for demo and testing use, not long-term production use.


## Render-ready updates
- Backend now supports `DATABASE_URL` directly for Render PostgreSQL.
- Optional `DB_SSL=true` is supported for external Postgres connections.
- Added `/health/` endpoint for Render health checks.
- Optional `CSRF_TRUSTED_ORIGINS` env var is supported for production domains.

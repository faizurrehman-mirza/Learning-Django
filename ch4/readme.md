# 📘 Day 4 — Understanding the Project Files

## What this chapter covers
Understanding the project files that `startproject` generates.

## 🧠 Explanation
Day 4 went through the files created in Day 3:

- **`manage.py`** — entry point for command-line tasks: `runserver`, `makemigrations`, `migrate`, `createsuperuser`, etc.
- **`settings.py`** — project configuration: installed apps, database config, middleware, timezone, static files, `SECRET_KEY`.
- **`urls.py`** — the project's main router. Requests get matched against patterns here (directly, or through an app's own urls file).
- **`wsgi.py`** — entry point traditional (synchronous) servers use to talk to the app in production.
- **`asgi.py`** — the async equivalent, used for things like websockets or async views.

Summary: `manage.py` is what you run, `settings.py` is what configures the project, `urls.py` is what routes traffic, and wsgi/asgi are what production servers use to talk to Django.


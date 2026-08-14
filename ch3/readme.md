# 📘 Day 3 — Creating a Django Project

## What this chapter covers
Creating a project in Django.

## 🧠 Explanation
With the virtual environment active and Django installed, this chapter created the project with:
```bash
django-admin startproject ch3
```
That generated:
- `manage.py` — the command-line tool for running the server, making migrations, creating apps, etc.
- A `ch3/` package folder with `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py` — the project's core configuration.
- `db.sqlite3` — the default SQLite database file.

Nothing is wired up yet — this is just the skeleton Django needs before adding apps and views. Running `python manage.py runserver` at this point shows Django's default welcome page.


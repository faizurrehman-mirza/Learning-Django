# 📘 Day 5 — Making an App and Understanding App Files

## What this chapter covers
Making an app in Django and understanding the files inside an app.

## 🧠 Explanation
Django separates a **project** (the overall site) from an **app** (a self-contained module inside it). This chapter created two apps, `app1` and `app2`:
```bash
python manage.py startapp app1
python manage.py startapp app2
```
Each app came with:
- **`models.py`** — where database tables are defined as Python classes.
- **`views.py`** — where the logic lives that decides what to send back for a request (empty at this stage, just the `render` import in place).
- **`admin.py`** — where models get registered to show up in Django's built-in admin panel.
- **`apps.py`** — small config class Django uses to identify the app.
- **`tests.py`** — placeholder for the app's tests.
- **`migrations/`** — tracks changes to models over time so Django can update the database schema.

At this point the apps exist structurally, but nothing is wired up — no views written, no URLs pointing to them yet.


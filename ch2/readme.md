# 📘 Day 2 — Virtual Environments

## What this chapter covers
Creating a virtual environment and activating it.

## 🧠 Explanation
A virtual environment is a self-contained Python install for one project — its own folder of packages, separate from the rest of the machine. This matters because:

- Each Django project can use its own version of Django and its own libraries, without conflicting with other projects.
- If something breaks, you can delete the `venv` folder and rebuild it without touching system Python.

Typical flow:

```bash
python -m venv venv        # creates the venv/ folder
venv\Scripts\activate      # activates it on Windows
# or
source venv/bin/activate   # activates it on Mac/Linux
```

Once activated, anything installed with `pip` (like Django) goes into that isolated environment rather than system-wide. The terminal prompt shows `(venv)` once it's active.

This chapter's `venv/` folder is the result of that process, with Django and its dependencies (like `tzdata`) installed inside it.



# 📘 Day 7 — Multiple Apps and Naming Conflicts

## What this chapter covers
Creating multiple applications in Django and resolving name conflicts between them, shown two different ways.

## 🧠 Explanation
With two apps (`app1` and `app2`) both having a `views.py`, importing from both into the same `urls.py` can cause naming collisions. This chapter covered two ways to avoid that.

**Way 1 — alias the whole module (left commented out in the file, kept for reference):**
```python
from app1 import views as ap1
from app2 import views as ap2

urlpatterns = [
    path('', ap1.home, name='home'),
    path('app1', ap1.app1, name='app1'),
    path('app2', ap2.app2, name='app2'),
    path('ap2me', ap2.app2_me, name='app2_me'),
]
```
Importing the module under an alias (`ap1`, `ap2`) avoids clashes even if both apps define a function with the same name, since each is called through its own namespace.

**Way 2 — import specific functions directly (the active version):**
```python
from app1.views import home, app1
from app2.views import app2, app2_me

urlpatterns = [
    path('', home, name='home'),
    path('app1', app1, name='app1'),
    path('app2', app2, name='app2'),
    path('ap2me', app2_me, name='app2_me'),
]
```
This works here because none of the function names collide between the two apps. If they did, this approach would break and Way 1's aliasing would be needed instead.


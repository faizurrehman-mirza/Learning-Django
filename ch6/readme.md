# 📘 Day 6 — Function-Based Views

## What this chapter covers
Using function-based views in Django to make pages, and writing view functions that return different types of responses.

## 🧠 Explanation
`app1/views.py` defines four view functions, each returning something different:

```python
def home(request):
    return HttpResponse("home page")            # plain string

def learn_django(request):
    return HttpResponse("Hello Django")          # plain string

def learn_python(request):
    return HttpResponse("<h1>Hello python<h1>")  # HTML string

def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)                       # a number, coerced to string
```
Each view function takes `request` and returns an `HttpResponse` (or something Django can convert into one).

`ch6/urls.py` connects each function to a URL path:
```python
path('', views.home, name='home')
path('dj/', views.learn_django, name='learn_django')
path('py/', views.learn_python, name='learn_python')
path('lm/', views.learn_math, name='learn_math')
```
The `name=` argument labels each route so it can be referenced elsewhere in the project (templates, redirects) instead of hardcoding the URL string.

One detail from `learn_math`: `HttpResponse` expects text, and Django converts a plain integer to a string automatically — worth noting, since returning `str(a)` explicitly is the more correct habit.


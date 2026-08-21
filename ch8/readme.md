# 📘 Day 8 — URL Patterns and Keyword Arguments

## What this chapter covers
URL patterns in Django, and sending keyword arguments into view functions through the URLconf.

## 🧠 Explanation
The full signature of `path()` is:
```python
path(route, view, kwargs=None, name=None)
```
Earlier chapters only used `route`, `view`, and `name`. Day 8 introduced `kwargs` — a dictionary passed directly into the view function alongside `request`.

```python
path('py/', learn_django),
path('dj/', learn_django, {'status': 'OK'}),
```
The same view (`learn_django`) is reused for two routes — `/dj/` passes in `{'status': 'OK'}` as extra keyword arguments, `/py/` passes nothing.

On the view side, this is caught with `**kwargs`:
```python
def learn_django(req, **kwargs):
    status = kwargs.get('status', 'Not Allowed')
    return HttpResponse(f"<h1>hello django {status}- app1<h1>")
```
`kwargs.get('status', 'Not Allowed')` uses the passed-in value if there is one, and falls back to `'Not Allowed'` otherwise — which is what happens on `/py/`. The same view behaves differently depending on what the URLconf feeds it, without needing separate functions.


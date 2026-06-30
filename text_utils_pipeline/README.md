# Module 03: Django Website — Laying the Pipeline

This directory documents the phase where we lay the underlying **architectural pipeline** for our Text Utilities application. Moving beyond solitary view files, this configuration sets up structural data flows to route incoming raw text strings across empty behavioral functions before processing final user output.

---

## What is a "Pipeline" in Django?

In web application architecture, a **Pipeline** refers to a deliberate layout of sequential stages that a user’s data travels through. Rather than handling every data operation inside a single giant script, the logic is divided into modular, individual processing hubs.


### The Core Flow:
1. **The Entry point (Landing Dashboard)**: The user visits the homepage (`/`) and enters raw text into an application environment.
2. **The Routing Valves (`urls.py`)**: Individual URL routes act as dedicated valves matching text operations to specific backend logical channels.
3. **The Logical Filter Hubs (`views.py`)**: The raw text flows directly into a specific function block designed to isolate and transform it (e.g., removing punctuation or clearing whitespace).

---

## Operational Pipeline Blueprint

This milestone builds multiple distinct processing endpoints to establish an architectural baseline before injecting deep logical operations.

### 1. Functional Hub Mapping (`urls.py`)
Using modern routing path definitions, endpoints are bound sequentially to intercept traffic and direct it to specialized string processing locations:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('removepunc/', views.removepunc, name='removepunc'),
    path('capitalizefirst/', views.capfirst, name='capitalizefirst'),
    path('newlineremover/', views.newlineremover, name='newlineremover'),
    path('spaceremover/', views.spaceremover, name='spaceremover'),
    path('charcount/', views.charcount, name='charcount'),
]

```

### 2. Isolated Behavioral Processing (`views.py`)

Each operational function accepts structural request metadata and yields distinct state confirmations back to the dashboard stream:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Text Utilities Landing Dashboard [Home]")

def removepunc(request):
    return HttpResponse("Processing Step: Punctuation Removal Engine Active")

def capfirst(request):
    return HttpResponse("Processing Step: First Capitalization Engine Active")

def newline_remove(request):
    return HttpResponse("Processing Step: Newline Cleansing Engine Active")

def space_remove(request):
    return HttpResponse("Processing Step: Whitespace Reduction Engine Active")

def char_count(request):
    return HttpResponse("Processing Step: Character Metrics Calculator Active")

```

---

## Pipeline Testing & Validation

1. Launch your operational runtime container from the target directory containing `manage.py`:
```bash
python manage.py runserver

```


2. Run validation sweeps across your structural routing table paths inside your browser window to ensure no `404 Page Not Found` collisions occur:
* **Base Entry**: `http://127.0.0.1:8000/`
* **Punctuation Check**: `http://127.0.0.1:8000/removepunc/`
* **Formatting Check**: `http://127.0.0.1:8000/capitalizefirst/`
---
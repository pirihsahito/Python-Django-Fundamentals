# Module 02: URL Routing, Views, and HTTP Responses

This directory contains the initial functional build of our **Text Utilities (text_utils)** core engine. Moving beyond basic scaffolding, this module implements custom request handling, view logic configuration, and modular URL routing structures.

---

## Request-Response Architecture Overview

The codebase demonstrates the foundational Model-View-Template (MVT) lifecycle pattern utilized by Django to receive, process, and answer web browser requests:


```

[ Web Browser ] ---> ( urls.py Routing ) ---> ( views.py Logic ) ---> [ HTTP Response ]

```

### Core File Configurations:
* **`text_utils/urls.py`**: Acts as the central traffic controller. It parses incoming browser URL strings against the defined `urlpatterns` list to navigate users to the appropriate backend Python function.
* **`text_utils/views.py`**: Created manually as a dedicated controller layer. It contains Python functions that accept structural server data and compute user-facing outputs.

---

## Code Implementation Breakdown

### 1. Modern View Implementations (`views.py`)
Every view function must handle web transactions cleanly. Two critical conventions were established here:
* **The Request Parameter**: Functions accept a mandatory `request` argument to ingest metadata sent by the browser. Failing to include this triggers a default execution `TypeError`.
* **HTTP Protocol Objects**: Instead of returning raw Python string primitives, views import and wrap strings inside `HttpResponse` from the `django.http` module.

```python
from django.http import HttpResponse

# Home routing endpoint
def index(request):
    return HttpResponse("<h1>Text Utilities Home</h1>")

# Secondary feature endpoint
def about(request):
    return HttpResponse("About Text Utilities Engine")

```

### 2. Multi-Route Navigation Matching (`urls.py`)

Using Django's core `path()` utility, explicit endpoints match targeted views using a structured 3-argument architecture:

```python
from django.contrib import admin
from django.urls import path
from . import views  # Global local controller import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),          # Route for base homepage
    path('about/', views.about, name='about'),    # Route for app information
]

```

* **Argument 1 (String Route)**: The target path addition (e.g., `'about/'`). A blank string `''` points directly to the domain root index.
* **Argument 2 (View Target)**: The executable pointer callback linking to the Python file function (e.g., `views.about`).
* **Argument 3 (Global Name Token)**: A dedicated `name='...'` reference pointer that allows developers to safely reference the path across HTML templates even if structural route names change.

---

## Testing Endpoints Locally

1. Launch your operational workspace shell inside the base project folder containing `manage.py`.
2. Boot up the local web service container:
```bash
python manage.py runserver

```


3. Open a local window and query the developed application routes to verify text data rendering:
* **Main Application Root**: `http://127.0.0.1:8000/`
* **About Service Metadata**: `http://127.0.0.1:8000/about/`
# Module 01: E-Commerce Architecture — Project Initialization & Installation

This directory contains the foundational milestone for **SmartCart**, a fully functional e-commerce web platform engineered with the Python Django framework. This module outlines the baseline project initialization and global configuration steps required to establish the workspace architecture within a local code editor ecosystem.

All core source code files, application scripts, and project configurations are actively maintained within the local `Creating_E_Com_Website` repository folder.

---

## Workspace Setup & Global Installation

Unlike rigid IDEs that hide project setup behind background automation menus, the workspace configuration for **Visual Studio Code (VS Code)** relies on direct, explicit commands executed in the integrated terminal.

The global system initialization consists of the following procedural steps:

1. **Global Framework Provisioning:**
Open the VS Code integrated terminal and install the core Django framework engine globally onto your local system:

```bash
pip install django
```


2. **Initialize the SmartCart Project Structures:**
Generate the master administrative project files using the Django management script, binding the files directly to our workspace directory layout:

```bash
django-admin startproject SmartCart
```


---

## Technical Pipeline & Project Structure

The resulting folder layout generated inside the `Creating_E_Com_Website` directory separates top-level administrative routing routines from your future application components:

```
Creating_E_Com_Website/      └── Root repository folder housing the source files
│
├── SmartCart/               └── Project administrative directory
│   ├── __init__.py          └── Package initialization marker
│   ├── settings.py          └── Global engine configurations, middleware, & database bridges
│   ├── urls.py              └── Top-level routing system and URL pattern dispatchers
│   └── wsgi.py              └── Web Server Gateway Interface for production hosting
└── manage.py                └── Django's command-line management utility wrapper
```

### Key Setup Features:

* **VS Code Terminal Integration**: Completely decoupled from proprietary IDE software configurations, optimizing the runtime pipeline for standard terminal execution.
* **Encapsulated Scripting**: All core logic, system adjustments, and localized assets are packaged cleanly inside the root folder, ensuring seamless workspace portability.
* **Scalable Core Settings**: Base system definitions inside `settings.py` are prepared to register upcoming standalone modular apps (such as customer checkouts, product catalogs, and shopping carts) seamlessly.

---

## Execution & Verification

To spin up the local development server block and verify that your global installation is completely operational, execute the following verification routine inside your VS Code terminal window:

1. Ensure your terminal path is pointing at the root repository directory:
```bash
cd Creating_E_Com_Website
```


2. Execute the local management development engine:
```bash
python manage.py runserver
```


3. Launch your web browser container and navigate to the default host endpoint:
* **Base Environment Destination**: `[http://127.0.0.1:8000/](http://127.0.0.1:8000/)`



Upon successful loading, the standard Django landing page confirms that the core **SmartCart** web infrastructure is active, configured correctly, and ready for app-layer stack building.

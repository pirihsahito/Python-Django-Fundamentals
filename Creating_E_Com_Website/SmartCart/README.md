# Module 01: E-Commerce Architecture — Project Initialization & Environment Setup

This directory contains the foundational milestone for **SmartCart**, a fully functional e-commerce web platform engineered with the Python Django framework. Building upon the structural design principles implemented in the previous `Revamping_TextUtils` iteration, this module establishes a clean, scalable workspace architecture tailored for production deployment.

All core source code files, application scripts, and environment configurations are actively maintained within the local `Creating_E_Com_Website` repository folder.

---

## Workspace Environment & Core Setup

The project workspace has been fully initialized and structured utilizing **Visual Studio Code (VS Code)** as the primary Integrated Development Environment (IDE). The system environment is established through the following architectural configuration steps:

1. **Workspace Root Definition**: A dedicated project directory named `Creating_E_Com_Website` is allocated inside the development environment to isolate the application files.
2. **Django Framework Provisioning**: The underlying Python environment is configured with the Django framework layer to handle request-response routing, ORM database mapping, and server-side template rendering.
3. **Project Initialization (SmartCart)**: The master project structure is generated directly within the workspace, assigning **SmartCart** as the primary administrative engine and system configuration boundary.

---

## Technical Pipeline & Project Structure

The underlying folder layout in the `Creating_E_Com_Website` directory separates configuration routines from local application components, ensuring an organized data stream across the backend:

```
Creating_E_Com_Website/      └── Root repository folder housing the source files
│
└── SmartCart/               └── Project administrative directory
    ├── __init__.py          └── Package initialization marker
    ├── settings.py          └── Global engine configurations, middleware, & database bridges
    ├── urls.py              └── Top-level routing system and URL pattern dispatchers
    ├── wsgi.py              └── Web Server Gateway Interface for production hosting
    └── manage.py            └── Django's command-line management utility wrapper
```

### Key Setup Features:

* **VS Code Task Integration**: Optimized for the VS Code editor ecosystem, utilizing local terminal configurations instead of rigid external IDE project files.
* **Encapsulated Scripting**: All core logic, backend adjustments, and localized assets are packaged cleanly inside the folder structure, making deployment on any production or development environment predictable.
* **Scalable Core Settings**: Base system definitions inside `settings.py` are set up to register future standalone apps (such as customer checkouts, inventory tracking, and shopping carts) smoothly.

---

## Execution & Verification

To spin up the server block and verify that the base setup is completely operational, run the following verification routine inside the VS Code integrated terminal:

1. Ensure you are situated within the root of the project directory:
```bash
cd Creating_E_Com_Website
```


2. Execute the local development engine:
```bash
python manage.py runserver
```


3. Launch your web browser container and navigate to the default host endpoint:
* **Base Environment Destination**: `[http://127.0.0.1:8000/](http://127.0.0.1:8000/)`



Upon successful navigation, the Django default landing page confirms that the core **SmartCart** infrastructure is running perfectly and is ready for application layer integration.
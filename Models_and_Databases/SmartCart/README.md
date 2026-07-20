# Module 05: Database Architecture — Object-Relational Mapping (ORM) & Schema Migrations

This directory documents the integration of persistent data structures within **SmartCart**. This milestone transitions the platform from serving purely static layouts to orchestrating an Object-Relational Mapping (ORM) architecture, enabling seamless database manipulation without writing raw SQL statements.

All model definitions, migration scripts, and updated application configurations are actively maintained inside the `Models_and_Databases` folder.

---

## Data Layer Architecture: Django ORM & Database Sync

Rather than requiring direct SQL queries to create or query tables, Django acts as an abstraction bridge between Python data objects and the underlying relational database management system (such as SQLite or MySQL):

```
[ Python Model (models.py) ] ───► [ makemigrations ] ───► [ Migration File (0001_initial.py) ]
                                                                     │
                                                                     ▼
[ Relational Database (db.sqlite3) ] ◄─── [ migrate ] ◄──────────────┘
```

### Architectural Concepts:

* **The Single Source of Truth**: Models act as the authoritative blueprint for your application data structures. Every class defined within `models.py` represents a database table, where each attribute corresponds to a table column.
* **Declarative Field Mapping**: Data types, length constraints, and specialized behaviors (such as auto-incrementing keys or date handling) are explicitly controlled using Django's built-in model field classes.
* **Two-Phase Schema Generation**: Schema changes are managed in two distinct phases: draft generation (`makemigrations`) compiles raw Python changes into versioned migration blueprints, and database execution (`migrate`) applies those blueprints onto the actual database storage engine.

---

## Workspace Configuration & App Integration

To enable model tracking, the application configuration is upgraded to register the full application class path rather than using a simple string identifier.

### App Configuration Upgrade (`SmartCart/settings.py`)

In previous setups, the app was registered by appending `'shop'` to `INSTALLED_APPS`. In this module, it is updated to reference the dedicated app configuration class inside `shop/apps.py`:

```python
INSTALLED_APPS = [
    'shop.apps.ShopConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

This ensures that any app-level signals, custom configurations, or model tracking parameters managed by `ShopConfig` are loaded into the core framework runtime properly.

---

## Schema Definition & Entity Design

Inside `shop/models.py`, the core entity structure for store products is initialized using Django's ORM model class:

```python
from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
```

### Data Fields Breakdown:

* **`product_id`**: Assigned as an auto-incrementing field type to generate distinct primary keys for individual catalog entries.
* **`product_name`**: Constrained character field allocating up to 50 characters for item naming.
* **`desc`**: Expanded text container capped at 300 characters to store concise product descriptions.
* **`pub_date`**: Dedicated date container tracking item creation and store publishing timelines.

---

## Migration Pipeline & Database Execution

To generate the underlying database tables from your Python models, execute the schema synchronization sequence within your VS Code integrated terminal:

1. **Synchronize Base Framework Schemas:**
Apply default system migrations to create core built-in tables (e.g., authentication, administrative session data):

```bash
python manage.py migrate
```


2. **Compile Custom Application Schema Blueprints:**
Generate new migration files based on the newly added `Product` model inside `shop/models.py`:

```bash
python manage.py makemigrations
```

*Output Confirmation:* Generates `shop/migrations/0001_initial.py` containing the `Create model Product` instructions.


3. **Execute Application Schema Migrations:**
Apply the compiled application blueprint to create the `Product` table directly inside the underlying database:

```bash
python manage.py migrate
```


---

## Environment Execution & Local Verification

To verify that the database layer is active and properly synced, run the verification routine in your VS Code workspace:

1. Confirm your integrated terminal path is set to the current project directory:
```bash
cd Models_and_Databases
```


2. Boot up the local runtime server:
```bash
python manage.py runserver
```


3. Confirm that the terminal startup logs run without throwing any `unapplied migrations` warnings, verifying that all database tables are synchronized with the **SmartCart** domain models.
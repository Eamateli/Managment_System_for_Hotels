* 1. **Create a new Django project:**
    ```bash
    django-admin startproject projectname
    ```

    * Create new apps: 
    ```bash
    python manage.py startapp appname
    ```

  * Add the apps in settings.py:
    ```python
    INSTALLED_APPS = [
        # ...
        'addon',
        'hotel',
        'user_dashboard',
        'userauths',
    ]
    ```

    Install required libraries:
    ```bash
    pip install django-ckeditor django-ckeditor-5 django-crispy-forms django-import-export django-mathfilters django-taggit pillow shortuuid
    ```

    Add installed packages/libraries to requirements.txt:
    ```bash
    pip freeze > requirements.txt
    ```

    Add the libraries in settings.py:
    ```python
    INSTALLED_APPS = [
        # ...
        'import-export',
        'crispy-forms',
        'mathfilters',
        'ckeditor_uploader',
        'django_ckeditor_5',
        'taggit',
    ]
    ```

    Start the server:
    ```bash
    python manage.py runserver
    ```

* **Setup Django Admin:**
    Install Django Jazzmin:
    ```bash
    pip install django-jazzmin
    ```

    Add Jazzmin to INSTALLED_APPS in settings.py:
    ```python
    INSTALLED_APPS = [
        # ...
        'jazzmin'
    ]
    ```

    Configure Jazzmin Settings:
    ```python
    JAZZMIN_SETTINGS = {
        # ...
    }
    ```

    Configure Jazzmin UI Tweaks:
    ```python
    JAZZMIN_UI_TWEAKS = {
        # ...
    }
    ```

    Migrate Database:
    ```bash
    python manage.py migrate
    ```

    Create Superuser:
    ```bash
    python manage.py createsuperuser
    ```

    Login to the admin dashboard: http://127.0.0.1:8000/admin/

MANAGEMENT SYSTEM FOR HOTELS USING DJANGO 

1. **Create a new Django project:**
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

  * Install required libraries:
    ```bash
    pip install django-ckeditor django-ckeditor-5 django-crispy-forms django-import-export django-mathfilters django-taggit pillow shortuuid
    ```

  * Add installed packages/libraries to requirements.txt:
    ```bash
    pip freeze > requirements.txt
    ```

  * Add the libraries in settings.py:
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

  * Start the server:
    ```bash
    python manage.py runserver
    ```

2. **Setup Django Admin:**
  * Install Django Jazzmin:
    ```bash
    pip install django-jazzmin
    ```

  * Add Jazzmin to INSTALLED_APPS in settings.py:
    ```python
    INSTALLED_APPS = [
        # ...
        'jazzmin'
    ]
    ```

  * Configure Jazzmin Settings:
    ```python
    JAZZMIN_SETTINGS = {
        # ...
    }
    ```

  * Configure Jazzmin UI Tweaks:
    ```python
    JAZZMIN_UI_TWEAKS = {
        # ...
    }
    ```

  * Migrate Database:
    ```bash
    python manage.py migrate
    ```

  * Create Superuser:
    ```bash
    python manage.py createsuperuser
    ```

  * Login to the admin dashboard: http://127.0.0.1:8000/admin/


3. **Configure Templates and Static Files:**
    * Create a new folder named `templates`.
    * Set the template configuration in `settings.py`:
        ```python
        TEMPLATES = [
            # ... 
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            # ...
        ]
        ```
    * Create new folders named `media` and `static`.
    * Configure the static and media folders in `settings.py`:
        ```python
        STATIC_URL = '/static/'

        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

        MEDIA_URL = '/media/'

        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        ```
    * Add files (css, fonts, images, scripts, Stock Images, etc.) to the `static` folder.


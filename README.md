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
    'site_header': "Luxury",
    'site_brand': "Luxury",
    'site_logo': "images/logo.png",
    'copyright': "The Agency",
    'welcome_sign':"Welcome to Luxury, Admin! Please Log in.",
    'topmenu_links': [
        
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Company","url":"/admin/addon/company/"},
        {"name": "Users", "url":"/admin/userauths/user/"},
        
        {"model": "AUTH_USER_MODEL.User"},
    ],
    "order_with_respect_to": [
        "hotel",
        "hotel.Hotel",
        "hotel.Room",
        "hotel.Booking",
        "hotel.BookingDetail",
        "hotel.Guest",
        "hotel.RoomServices",
        "userauths",
        "addon",
        
        
    ],
    "icons": {
        "admin.LogEntry": "fas fa-file",
        
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        
        "userauths.User": "fas fa-user",
        "userauths.Profile": "fas fa-address-card",
        
        "hotel.Hotel": "fas fa-th",
        "hotel.Booking": "fas fa-calendar-week",
        "hotel.BookingDetail": "fas fa-calendar-alt",
        "hotel.Guest": "fa fa-user",
        "hotel.Room": "fas fa-bed",
        "hotel.RoomServices":"fas fa-user-cog",
        "hotel.Notification":"fas fa-bell",
        "hotel.Coupon":"fas fa-tag",
        "hotel.Bookmark": "fas fa-heart",
    },
    
    "show_ui_builder": True
    }

  * Configure Jazzmin UI Tweaks:
    ```python
    JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-lightblue text-white ",
    "accent": "accent-cyan",
    "navbar": "navbar-lightblue navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-yellow",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success":"btn-success"
             
    }
    }
        

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


4. **Custom User and Profile Model**
    * Create 'user'and 'profile' models in 'userauths/models.py'
    * Add the in the 'userauths/admin.py' 'UserAdmin' and 'ProfileAdmin'
    * Run migration commands
    ```bash
    python manage.py makemigrations
    ```
    ```
    python mange.py migrate
    ```
    * Run server and test the models
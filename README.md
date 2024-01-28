MANAGEMENT SYSTEM FOR HOTELS USING DJANGO 

1. Create a new django project
      * Create a new django project where you want it: <pre> ``` django-admin startproject projectname ``` </pre>

      * Create new app userauths, hotel, user_dashboard, userauths: <pre> ``` python manage.py startapp appname ``` </pre>

      * Add the apps in settings.py (make sure to have commas and single quotation marks, order is irrelevant):
        ```python
        INSTALLED_APPS = [
               ...
               #Apps
              'addon',
              'hotel',
              'user_dashboard',
              'userauths',
              
        ] 
      * Install the required libraries: <pre> ``` pip install django-ckeditor django-ckeditor-5 django-crispy-forms django-import-export django-mathfilters django-taggit pillow shortuuid ``` </pre>
      * Add installed packages/libraries to requirements.txt: <pre>``` pip freeze > requirements.txt ```</pre>
      * Add the libries in **settings.py**:
           ```python
                   INSTALLED_APPS = [
                                   ...
                         #Libs
                         'import-export',
                         'crispy-forms',
                         'mathfilters',
                         'ckeditor_uploader',
                         'django_ckeditor_5',
                         'taggit',
              
        ]
      * Start the server:<pre>``` python manage.py runserver ```</pre> (click the link showing on the terminal, ctrl + left click)
      
2. Setup Django Admin 
      * Install Django Jazzmin: <pre>``` pip install django-jazzmin ```</pre>
      * Add Jazzmin to settings.py INSTALLED_APPS, at the end:
        ```python
           INSTALLED_APPS = [
                   ...
                 'jazzmin'
           ]
      * Configure Jazzmin Settings:
        
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
      * Configure Jazzmin UI Tweaks
       
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

      * Migrate Database: <pre> ``` python manage.py migrate ``` </pre>
      * Create Superuser: <pre> ``` python manage.py createsuperuser ``` </pre>
      * Login to the admin dashboard: http://127.0.0.1:8000/admin/
   

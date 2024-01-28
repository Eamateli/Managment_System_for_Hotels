MANAGEMENT SYSTEM FOR HOTELS USING DJANGO 

1. Create a new django project
      * Create a new django project where you want it: <pre> ``` django-admin startproject projectname ``` </pre>

      * Create new app userauths, hotel, user_dashboard, userauths: <pre> ``` python manage.py startapp appname ``` </pre>

      * Add the apps in settings.py (make sure to have commas and single quotation marks, order is irrelevant)
        
      * Install the required libraries: **pip install django-ckeditor django-ckeditor-5 django-crispy-forms     django-import-export django-mathfilters django-taggit pillow shortuuid**
      * Add installed packages/libraries to requirements.txt: **pip freeze > requirements.txt**
      * Add the libries in **settings.py**: 'import-export', 'crispy-forms', 'mathfilters', 'ckeditor_uploader', 'django_ckeditor_5', 'taggit',
      * Run the server: **python manage.py runserver** (click the link showing on the terminal, ctrl + left click)
      
2. Setup Django Admin 
      * Install Django Jazzmin: **pip install django-jazzmin**
      * Add Jazzmin to settings.py INSTALLED_APPS, at the end
      * Configure Jazzmin Settings
      * Configure Jazzmin UI Tweaks
      * Migrate Database: **python manage.py migrate**
      * Create Superuser: **python manage.py createsuperuser**
      * Login to the admin dashboard: http://127.0.0.1:8000/admin/
   

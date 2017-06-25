# django-blog
django blog using viewflow material

# System Requirements
* python3

# Quick Start
Creat a virtual environment, migrate and blog!
* git fetch https://github.com/iMMAP-Afg/django-blog.git
* cd django-blog
* python3 -m venv env
* source env/bin/activate
* pip install django django-material
* ./manage.py makemigrations blog
* ./manage.py migrate
* ./manage.py createsuperuser
* ./manage.py runserver 0.0.0.0:8000

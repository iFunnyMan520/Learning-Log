# Learning Log
Create web application Learning Log with [Django](http://djangoproject.com/)

### Create project
```
python3.7 -m venv env
source env/bin/activate
pip install django
django-admin.py startproject learning_log .
python manage.py migrate  # create database
python manage.py runserver  # run server
python manage.py startapp learning_logs  # create app
python manage.py makemigration learning_logs  # change db for app
python manage.py migrate  # run migrate
python manage.py createsuperuser  # create administrator
```

### Preparation for development
```
git clone https://github.com/iFunnyMan520/Learning-Log
python3.7 -m venv env
source env/bin/activate
pip3 install requirements.txt
```
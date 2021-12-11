# cloud-computing

## Requirements
1. Install django:
    `pip install django`
2. Instal django rest framework:
    `pip install djangorestframework`
3. Install numpy:
    `pip install numpy`
4. Install matplotlib:
    `pip install matplotlib`

## Convert CSV to Sqlite3
1. `sqlite3 db.sqlite3`
2. `.mode csv`
3. `.import vgsales.csv app_vgsales`

## How make multiple database
1. change settings.py
```python
DATABASES = {
    'default': {},
    'users_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'users.db.sqlite3',
    },
    'vgsales_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'vgsales.db.sqlite3',
    },
}

DATABASE_ROUTERS = ['routers.db_routers.AuthRouter','routers.db_routers.Vgsales']
```
2. add routers/db_routers
```python
class AuthRouter:
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin', 'account', 'authtoken'}
    ....
class Vgsales:
    route_app_labels = {'main_service'}
    ...
```
3. makemigrations
    `python manage.py makemigrations`
4. migrate
    `python manage.py migrate --database=users_db`
    `python manage.py migrate --database=vgsales_db`

## Problem in dockerize
1. Localhost not opened. The first I used this code.
```docker
FROM python:3.8
...

CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --database=users_db --noinput && \
    python3 manage.py migrate --database=vgsales_db --noinput && \
    python3 csvtodb.py && \
    python3 manage.py collectstatic --noinput && \
    python manage.py runserver
```
So I use gunicorn.
```docker
FROM python:3.8
...

CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --database=users_db --noinput && \
    python3 manage.py migrate --database=vgsales_db --noinput && \
    python3 csvtodb.py && \
    python3 manage.py collectstatic --noinput && \
    gunicorn -b 0.0.0.0:8000 project.wsgi
```
2. I want to use python:alpine for media and static files, but matplotlib didn't install. And I figure out for install matplotlib on python:alpine, must use this code.
```docker
FROM python:3.8-alpine3.15
...
RUN apk add g++ jpeg-dev zlib-dev libjpeg make
...
```
3. We need import CSV to sqlite,I used `sqlite3 vgsales.db.sqlite3 -cmd ".mode csv" ".import vgsales.csv main_service_vgsales"` before, But docker doesn't know what `sqlite3` is, So I make a `csvtodb.py`, I call it for import csv to sqlite.
4. The last problem is media and static file doesn't work, So I think must use `nginx`, But the problem is in my directory.
I got used to my directory is:
```
├── volume
    │   ├── project
    │   ├── media
    │   └── static
```
But the directory must be:
```
├── volume
    │   ├── project
        │   ├── media
        │   └── static
```

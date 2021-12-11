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

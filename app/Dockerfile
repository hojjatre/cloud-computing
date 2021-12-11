FROM python:3.8
# FROM alpine:3.15
# FROM python:3.8-alpine3.15
# ENV PYTHON_VERSION 3.8.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=admin
# RUN apk add g++ jpeg-dev zlib-dev libjpeg make
# RUN apk add --update sqlite && rm -rf /var/cache/apk/*
RUN mkdir /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install django djangorestframework numpy matplotlib pytz pandas 
RUN pip3 install gunicorn
# ADD sqlite_commands.sql /

CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --database=users_db --noinput && \
    python3 manage.py migrate --database=vgsales_db --noinput && \
    # python3 csvtodb.py && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --database=users_db --user admin --email admin@gmail.com --noinput; \
    gunicorn -b 0.0.0.0:8000 project.wsgi


# RUN sqlite3 panama.sqlite < sqlite3 vgsales.db.sqlite3 -cmd ".mode csv" ".import vgsales.csv main_service_vgsales"
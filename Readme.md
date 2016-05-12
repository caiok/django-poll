# Django Poll

> **Warning**
> This project is intended for personal use only

Simple Django application from the official tutorial: https://docs.djangoproject.com/en/1.9/intro/tutorial01/

## Docker Build and Run

```
git clone https://github.com/caiok/docker-builds
cd docker-builds/django
docker build --build-arg HTTP_PROXY=http://proxy.mmfg.it:8080 -t caio/django:mysql .
docker run -i -t -d --name "django_poll" -p 80:80 -p 3306:3306 -v <workspace>:/repo caio/django:mysql
docker exec -it django_poll /bin/bash -l
```

```
cd /repo/django_poll
python manage.py runserver 0.0.0.0:80
```

## Documentation

#### Start a Project

```
$ django-admin startproject <mysite>
```

Creates:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

#### Start an App

```
cd <mysite>
$ python manage.py startapp <myapp>
```

Creates:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    myapp/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
```
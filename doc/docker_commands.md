# Docker Commands

### Build

```
cd docker_build
docker build -t django_poll:latest .
```

### Run

```
docker run -i -t -d django_poll:latest
```


```
docker build --build-arg HTTP_PROXY=http://proxy.mmfg.it:8080 -t caio/django:mysql .
docker run -i -t -d --name "django_poll" -p 80:80 -p 3306:3306 -v /Users/francescocaliumi/devel:/repo caio/django:mysql
docker exec -it django_poll /bin/bash -l
```
# flightServices
Flight Services api source code.

## Docker build
docker build .

## Docker compose build
docker-compose build

## Create a django project.
docker-compose run app sh -c "django-admin.py startproject app ."

## Run Test
docker-compose run app sh -c "python manage.py test

docker-compose run app sh -c "python manage.py  startapp core"

docker-compose run app sh -c "python manage.py makemigrations"

### Test & Lint
docker-compose run --rm app sh -c "python manage.py test && flake8"

### App url 
http://127.0.0.1:8000/

### create a superuser
docker-compose run app sh -c "python manage.py createsuperuser"

## creating a user app
docker-compose run --rm app sh -c "python manage.py startapp user"
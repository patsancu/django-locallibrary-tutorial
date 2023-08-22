# Better to keep the following two lines

container-name:= "django-library"
external-port := "9999"
default:
    just --list

build-image:
    docker build -t  {{container-name}} .

run-image:
  docker run -d -p {{external-port}}:8000 -v $(pwd):/usr/src -w /usr/src/ --name {{container-name}} -it {{container-name}} python3 manage.py runserver 0.0.0.0:8000

stop:
    -docker stop {{container-name}}
    -docker rm {{container-name}}

restart: stop run-image

enter:
    docker exec -w /usr/src -it {{container-name}} bash

build-and-run-image: build-image run-image

give-me-permissions:
    sudo chown -R patrick:patrick .

logs:
    docker logs -f {{container-name}}

run ARGS:
    docker exec -ti {{container-name}} {{ARGS}}

makemigrations: (run "python manage.py makemigrations")
migrate: (run "python manage.py migrate")
run-migrations: makemigrations migrate

generate-schema: (run "python manage.py generateschema --file openapi-schema.yml")
create-super-user: (run "python manage.py createsuperuser")

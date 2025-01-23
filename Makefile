SHELL:=/bin/bash
REPO := quantum-management

prep:
	python3 -m venv venv

venv_activate:
	source ./venv/bin/activate

install:
	pip3 install -r requirements.txt
	python3 -m pip install Pillow

venv_migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

run_local:
	python3 manage.py runserver

prep_migrate:
	pipenv run python3 manage.py makemigrations

migrate:
	pipenv run python3 manage.py migrate

prep_and_migrate: prep_migrate
	pipenv run python3 manage.py migrate

test:
	python3 manage.py test

prep_static:
	python3 manage.py collectstatic

docker_build_local:
	docker build -t quantummanagement .

docker_run_local:
	docker run -it -d --env-file .env.dev -p 8000:8000 quantummanagement

docker_compose_local:
	docker-compose up --build

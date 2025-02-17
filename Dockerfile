#--------------------#
# TESTING DOCKERFILE.
# COPY/PASTE or USE DOCKERFILE FROM ENVIRONMENTS FOLDER TO USE OR TEST OTHERS
#--------------------#
FROM python:3.8-buster AS builder

# Hacky - but for now copying the .env file inside the container, which Terraform will read
# and run Docker run with --env-file .env to pick up the env vars
COPY .env .env

# don't write pyc file
ENV PYTHONDONTWRITEBYTECODE=1

# don't buffer log message submission
ENV PYTHONUNBUFFERED=1

RUN python3 -m venv /venv

RUN pip3 install virtualenv

# Create virtual env for docker container to run python in
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

RUN python3 -m pip install Pillow

COPY quantummanagementapp/fixtures quantummanagementapp/fixtures

#RUN python manage.py makemigrations

#RUN python manage.py migrate

#COPY db.sqlite3 db.sqlite3

# RUN python3 manage.py loaddata */fixtures/*.json

#######################################

# App stage #
# Smaller official Debian-based Python image
FROM python:3.8-slim-buster AS app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ENV PATH="/venv/bin:$PATH"

WORKDIR /usr/src/app

# copy in Python environment
COPY --from=builder /venv /venv

COPY . .

# ENV DEBUG=True

# ENV ENVIRONMENT=development

ENV DJANGO_SETTINGS_MODULE=quantummanagement.settings

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

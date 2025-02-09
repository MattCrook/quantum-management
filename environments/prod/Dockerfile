FROM python:3.11-alpine AS builder

# Hacky - but for now copying the .env file inside the container, which Terraform will read
# and run Docker run with --env-file .env to pick up the env vars
COPY /environments/dev/.env .env

RUN pip3 install virtualenv

RUN virtualenv venv

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

ENV PATH "/venv/bin:$PATH"

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

RUN python3 -m pip install Pillow

#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate

ENV DJANGO_SETTINGS_MODULE quantummanagement.settings

#######################################
# App stage #
FROM python:3.11-slim AS app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ENV PATH="/venv/bin:$PATH"

WORKDIR /usr/src/app

COPY --from=builder /venv /venv

COPY . .

ENV DJANGO_SETTINGS_MODULE=quantummanagement.settings


EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

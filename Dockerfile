FROM python:3.8-buster AS builder

# Hacky - but for now copying the .env file inside the container, which Terraform will read
# and run Docker run with --env-file .env to pick up the env vars
COPY .env.dev .env

# Setup the virtualenv
RUN python -m venv /venv

# don't write pyc file
ENV PYTHONDONTWRITEBYTECODE 1

# don't buffer log message submission
ENV PYTHONUNBUFFERED 1

# don't check for pip updates
# ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Create virtual env for docker container to run python in
ENV PATH "/venv/bin:$PATH"

RUN pip install --upgrade pip

# Old - with just requirements.txt file no Pipfile
COPY requirements.txt .
RUN pip install -r requirements.txt

#######################################
# App stage #
# Smaller official Debian-based Python image
FROM python:3.8-slim-buster AS app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PATH "/venv/bin:$PATH"

WORKDIR /usr/src/app

# copy in Python environment
COPY --from=builder /venv /venv

COPY . .

ENV DJANGO_SETTINGS_MODULE=quantummanagement.settings

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

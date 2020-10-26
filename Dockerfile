# FROM alpine:latest

# ----- Base image of Python to build upon
# FROM python:3.7-buster
FROM python:3.7.3-slim


# ----- Nginx installation commands and COPY the configuration file inside the container
# FROM nginx:1.19.0-alpine
# RUN rm /etc/nginx/conf.d/default.conf
# COPY nginx.conf /etc/nginx/conf.d
# RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
# COPY nginx.conf /etc/nginx/sites-available/default
# RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#     && ln -sf /dev/stderr /var/log/nginx/error.log



# ---- set work directory
# create directory for the app user
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# create the app user
# RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/app
ENV APP_HOME=/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

# ENV PATH=$PATH:/app/.local/bin

# install psycopg2 dependencies
RUN apk update && apk add libpq


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
COPY startup.sh /app/
RUN pip install -r requirements.txt


# Set up Virtual Env
ENV DJANGO_SETTINGS_MODULE=quantummanagement.settings
ENV PYTHONPATH=/app/.local
ENV PATH=$PATH:/app/.local/bin
# RUN chown -R www-data:www-data /app

# copy entrypoint-prod.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
# USER app


# ---- copy project
# COPY . /app/


# ---- Collect Static files
# RUN python manage.py collectstatic

# EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]

# CMD ["bash", "startup.sh"]

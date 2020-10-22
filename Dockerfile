# FROM alpine:latest

# ----- Base image of Python to build upon
FROM python:3.7-buster

# ----- Nginx installation commands and COPY the configuration file inside the container
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# ---- set work directory
# RUN mkdir /app
WORKDIR /app
COPY . /app



# ---- Install Node
FROM node:lts-alpine
# ENV NODE_ENV=production
# WORKDIR /tmp


# ---- Install node dependencies
COPY ./package.json /app/
COPY ./package-lock.json /app/
# COPY src/js /tmp/js
# COPY src/static-files /tmp/static-files
# RUN npm run build
RUN npm install
# COPY . /app/

# ---- Webpack Dependencies
# COPY src/webpack.config.js /tmp/webpack.config.js
# COPY src/js /tmp/js
# COPY src/static-files /tmp/static-files
# RUN npm run build && npm run replace-links




# ---- pull official base image &&
# ---- Install python dependencies
FROM python:3.7.3-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /quantummanagement/requirements.txt
RUN pip install -r /quantummanagement/requirements.txt
# COPY . /app/


# ---- Set up Virtual Environment && Python run Image
ENV DJANGO_SETTINGS_MODULE=/app/settings.py
ENV STATIC_ROOT=/app/static/
ENV PYTHONPATH=/app/.local
ENV PATH=$PATH:/app/.local/bin



# ---- set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1


# ---- copy project
COPY . /app/

EXPOSE 8000


# ---- Listen to all interfaces with "0.0.0.0"
ENTRYPOINT [ "python" ]
CMD [ "manage.py", "runserver", "--host", "0.0.0.0" ]

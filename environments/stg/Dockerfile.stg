FROM python:3.8-buster AS builder

# Hacky - but for now copying the .env file inside the container, which Terraform will read
# and run Docker run with --env-file .env to pick up the env vars
COPY .env.dev .env

# Setup the virtualenv
RUN python -m venv /venv

# don't write pyc file
ENV PYTHONDONTWRITEBYTECODE=1

# don't buffer log message submission
ENV PYTHONUNBUFFERED=1

# don't check for pip updates
# ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Create virtual env for docker container to run python in
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip

# Old - with just requirements.txt file no Pipfile
COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python -m pip install Pillow

RUN python manage.py makemigrations
RUN python manage.py migrate

# fixtures not working right now...
# RUN python manage.py loaddata */fixtures/*.json


#######################################

FROM nginx:latest
#RUN rm /etc/nginx/conf.d/default.conf
#COPY content /usr/share/nginx/html
#COPY conf /etc/nginx
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
#COPY --from=build /app/build /usr/share/nginx/html
COPY ./nginx/content /usr/share/nginx/html


# Maintaining Content and Configuration Files in the Container
#COPY content /usr/share/nginx/html
#COPY conf /etc/nginx
#VOLUME /usr/share/nginx/html
#VOLUME /etc/nginx

# customized logging
#COPY content /usr/share/nginx/html
#COPY conf /etc/nginx
#VOLUME /var/log/nginx/log

#-------------------#
# Stage-2 (Production Environment)
# https://medium.com/@wawerumwaura/nginx-and-docker-configuration-aac7b26210fe
# Use the nginx 1.12-alpine runtime image for the production environment
FROM nginx:1.12-alpine

# Copy the tagged files from the build to the production environmnet of the nginx server
COPY --from=build-deps /usr/src/app/build /usr/share/nginx/html
#COPY  /nginx/content /usr/share/nginx/html

# Copy nginx configuration 
COPY --from=build-deps /usr/src/app/default.conf /etc/nginx/conf.d/ 
#COPY /nginx/nginx.conf /etc/nginx/conf.d/ 

EXPOSE 80

# Run the nginx server
CMD ["nginx", "-g", "daemon off;"]
#-------------------#


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

ENV DJANGO_SETTINGS_MODULE=quantummanagement.settings


EXPOSE 80
EXPOSE 443

# STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]

# FROM alpine:latest

# ----- Base image of Python to build upon
FROM python:3.7-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ----- Nginx installation commands and COPY the configuration file inside the container
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# ---- set work directory
WORKDIR /app


RUN pip install --upgrade pip
COPY requirements.txt /app/
COPY start-server.sh /app/
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/app


# ---- copy project
COPY . /app/

EXPOSE 8000
CMD ["/startup.sh"]

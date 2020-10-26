FROM alpine:latest

# ----- Base image of Python to build upon
FROM python:3.7.3-slim

# ---- set work directory
WORKDIR /app


RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.conf /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log


# Set up Virtual Env
ENV DJANGO_SETTINGS_MODULE=quantummanagement.settings
ENV PYTHONPATH=/app/.local
ENV PATH=$PATH:/app/.local/bin
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
COPY startup.sh /app/
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /app




# ---- copy project
COPY . /app/

# change to the app user
# USER app




# ---- Collect Static files
# RUN python manage.py collectstatic

EXPOSE 8000

# ENTRYPOINT ["entrypoint.sh"]

CMD ["bash", "startup.sh"]

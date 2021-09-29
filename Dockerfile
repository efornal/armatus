# docker build -t armatus:latest .

FROM python:3.7-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y python-dev python-pip python-apt python-ldap \
   libcairo2-dev libcairo2 \
   pkg-config gettext libpq-dev libyaml-dev \
   libldap2-dev libsasl2-dev libjpeg-dev zlib1g-dev libgtk2.0-dev \
   libgirepository1.0-dev
 
RUN pip install --upgrade pip
WORKDIR /srv/armatus
EXPOSE 8000

COPY requirements.txt .
RUN pip install -r requirements.txt


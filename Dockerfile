# docker build -t armatus:latest .

FROM python:3.9-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get install -y libcairo2-dev libcairo2 \
   pkg-config gettext libpq-dev libyaml-dev \
   libldap2-dev libsasl2-dev libjpeg-dev zlib1g-dev libgtk2.0-dev \
   libgirepository1.0-dev \
   procps

RUN pip install --upgrade pip
WORKDIR /srv/armatus
EXPOSE 8000

COPY app app
COPY armatus armatus
COPY armatus/settings.tpl.py.env armatus/settings.py
COPY LICENSE .
COPY locale locale
COPY manage.py .
COPY README.md .
COPY static static
COPY templates templates

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get clean && apt-get autoremove

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn", "armatus.wsgi:application", "--bind 0.0.0.0:8000"]

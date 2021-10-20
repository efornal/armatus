# armatus
Allows to keep a record of variables of the useful life of a generator


### Required debian packages
```bash
apt install libcairo2-dev
apt install libcairo2
apt install pkg-config
apt install gettext
apt install libpq-dev
apt install libyaml-dev
apt install libldap2-dev
apt install libsasl2-dev
apt install libjpeg-dev
apt install zlib1g-dev
apt install libgtk2.0-dev
apt install libgirepository1.0-dev
```

### Python lib Installation
```bash
pip install -r requirements.txt
```

### Using docker composer

```bash
docker volume create pgdata
```

```bash
docker-compose up
```

### Configuration
* Copy .env.tpl to .env.dev and configure with custom values

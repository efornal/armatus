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

### Configuration
* Copy .env.tpl to .env.dev and configure with custom values

### Using docker

* Image compilation
```bash
docker build -t armatus:latest .
```

* Volume creation
```bash
docker volume create pgdata
```
Note that for this local development environment, the app directory is mounted inside the image. While for the database, the volume is previously created and used as an external volume.

* Database initialization
To initialize the database (creation of connection users, etc) or import the database from a dump, the file must be added to the db directory, which will then be mounted where the postgresql image requires it.
```bash
$ ls db/
init_db_or_dump.sql
```

* Image test
```bash
docker run --env-file .env.dev -it armatus:latest
```

* Environment creation with docker-compose 
```bash
docker-compose up
```

## django configuration

DEBUG=on
BASE_URL=https://0.0.0.0:8000
SECRET_KEY=*********************************
ALLOWED_HOSTS=['*']

ADMINS=(("admin", "admin@domain"),)

MANAGERS=(("Manager", "manager@domain"),)

TIME_ZONE=America/Argentina/Buenos_Aires

STATIC_ROOT=/srv/armatus/shared/static

STATIC_URL=/static/

SESSION_COOKIE_NAME=armatussessionid


LOGIN_URL=/generador/login
LOGIN_REDIRECT_URL=/generador
SESSION_COOKIE_NAME=armatussessionid

CONTEXT_ROOT=/generador
CONTEXT_PATH=/srv/armatus

# ldap configuration
LDAP_SERVER=ldap://ldap_host:389
LDAP_BIND_DN=dc=rectorado,dc=unl,dc=edu,dc=ar
LDAP_DN_AUTH_GROUP=ou=Group,dc=domain
LDAP_DN_AUTH_USERS=ou=People,dc=domain

DB_NAME=armatus_db
DB_USER=armatus_user
DB_USER_PASSWORD=*********
DB_PORT=5432
DB_HOST=db
DB_OWNER=armatus_owner
DB_OWNER_PASSWORD=*********


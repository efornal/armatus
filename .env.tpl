## django configuration

DEBUG=on

BASE_URL=https://base_url

SECRET_KEY=5l4#u+^9(f5ej@=@e!%@hq#xm@kaz0lf-m45z7iesu=w(fdhz9

ALLOWED_HOSTS=['*']

ADMINS=(("admin", "admin@site.com"),)

MANAGERS=(("Manager Name", "manager@site.com"),)

TIME_ZONE=America/Argentina/Buenos_Aires

CONTEXT_ROOT=/generador

CONTEXT_PATH=/srv/armatus

LOGIN_URL=/generador/login

LOGIN_REDIRECT_URL=/generador

STATIC_ROOT=/srv/armatus/shared/static

STATIC_URL=/static/

SESSION_COOKIE_NAME=armatussessionid


## ldap configuration
LDAP_SERVER=ldap://ldap.site.com:389
LDAP_DN=dc=site,dc=com
# Organizational Unit for Person
LDAP_PEOPLE=People
LDAP_GROUP=Group


## database configuration
# for default user
DB_NAME_DEF=armatus_db
DB_USER_DEF=armatus_user
DB_PASS_DEF=user_password
DB_HOST_DEF=db
DB_PORT_DEF=5432
# for user with privileged access 
DB_NAME_OWN=armatus_db
DB_USER_OWN=armatus_owner
DB_PASS_OWN=owner_password
DB_HOST_OWN=db
DB_PORT_OWN=5432

from .settings import *

DEBUG = True

#variable added here to permit any IP address computer to run this file
ALLOWED_HOSTS = []

# Crie a secret key para seu ambiente de produção
SECRET_KEY = 'ixb6fha#ts=&b4t2u%p1_62-!8dw2j==j)d^3-j$!z(@*m+-h'
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}
}
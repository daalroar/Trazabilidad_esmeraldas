from Registro.settings.base import*

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['trazabilidad-esmeraldas.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Registros_trazabilidad',
        'USER':'sistemas',
        'PASSWORD':'Csimcchg2019.',
        'HOST':'190.110.197.116',
        'DATABASE_PORT':'5432',
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')
from app_settings import app_settings


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': app_settings.postgres_db,
        'USER': app_settings.postgres_user,
        'PASSWORD': app_settings.postgres_password,
        'HOST': 'postgresql',
        'PORT': '5432',
    }
}

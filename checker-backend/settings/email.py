from app_settings import app_settings


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = app_settings.application_email
EMAIL_HOST_PASSWORD = app_settings.application_email_key

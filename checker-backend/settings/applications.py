BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'applications.checker.apps.CheckerConfig',
]

ADDITIONAL_APPS = [
    'corsheaders',
    'rest_framework',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + ADDITIONAL_APPS

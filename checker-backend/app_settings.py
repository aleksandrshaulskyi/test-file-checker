from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    Pydantic application settings.
    """
    #POSTGRES
    postgres_db: str = Field(validation_alias='POSTGRES_DB')
    postgres_user: str = Field(validation_alias='POSTGRES_USER')
    postgres_password: str = Field(validation_alias='POSTGRES_PASSWORD')

    #BASE
    django_settings_module: str = Field(validation_alias='DJANGO_SETTINGS_MODULE')
    file_storage_location: str = '/checker-backend/file_storage/checker_files/'
    file_storage_base_url: str = '/media/'
    garbage_collection_interval: int = 3600

    #CELERY
    celery_broker_url: str = Field(validation_alias='CELERY_BROKER_URL')
    celery_result_backend: str = Field(validation_alias='CELERY_RESULT_BACKEND')

    #EMAIL
    application_email: str = Field(validation_alias='APPLICATION_EMAIL')
    application_email_key: str = Field(validation_alias='APPLICATION_EMAIL_KEY')
    

    model_config = {
        'env_file': '.env',
        'extra': 'allow',
    }

app_settings = AppSettings()

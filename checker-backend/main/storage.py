"""
This module contains storages that are used to well... store files
as it is fancier than using upload_to.
"""
from django.core.files.storage import FileSystemStorage

from app_settings import app_settings


file_storage = FileSystemStorage(
    location=app_settings.file_storage_location,
    base_url=app_settings.file_storage_base_url,
)

from os import listdir
from os.path import join
from pathlib import Path

from app_settings import app_settings

from applications.checker.models import File


class GarbageCollectorService:
    """
    This service collects files that are not linked to File entities
    and deletes them.
    """

    def execute(self) -> None:
        file_paths = File.objects.all().values_list('file', flat=True)

        for path in listdir(app_settings.file_storage_location):
            if path not in file_paths:
                full_path = join(app_settings.file_storage_location, path)
                Path(full_path).unlink(missing_ok=True)

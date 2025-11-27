from time import sleep

from django.core.management.base import BaseCommand

from app_settings import app_settings

from applications.checker.services import GarbageCollectorService


class Command(BaseCommand):
    """
    This command is used to demonstrate an another way of
    running scheduled tasks.

    It is meant to run in a separated process (whole docker-container will be built for this purpose)
    to avoid gunicorn processes to repeat the same job (i.e. 8 gunicorn workers would run the same job
    8 times.)
    """
    garbage_collector = GarbageCollectorService()

    while True:
        garbage_collector.execute()
        sleep(app_settings.garbage_collection_interval)

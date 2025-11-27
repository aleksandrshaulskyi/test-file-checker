from celery import shared_task

from applications.checker.services import GarbageCollectorService


@shared_task
def collect_garbage():
    GarbageCollectorService().execute()

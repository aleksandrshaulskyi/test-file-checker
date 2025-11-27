from celery import shared_task

from applications.checker.services import CheckFileService


@shared_task
def check(id: int) -> None:
    CheckFileService(id=id).execute()

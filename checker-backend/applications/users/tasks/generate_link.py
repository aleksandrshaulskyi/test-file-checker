from celery import shared_task

from applications.users.services import GenerateActivationLinkService


@shared_task
def generate_link(id: int):
    GenerateActivationLinkService(id=id).execute()

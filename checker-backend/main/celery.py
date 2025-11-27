import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.main')

celery_app = Celery('project')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'collect-garbage': {
        'task': 'applications.checker.tasks.collect_garbage.collect_garbage',
        'schedule': crontab(minute=0),
    },
}

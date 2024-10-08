import os
from celery import Celery
from django.conf import settings
import time


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def debug_task():
    print('!!!!! debug_task started !!!!!!')
    time.sleep(20)
    print('!!!!! debug_task ended !!!!!!')

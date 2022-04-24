import logging
import os

from celery import Celery

app = Celery()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "campaignerapi.settings")
logging.captureWarnings(True)

app = Celery("campaignerapi")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task()
def debug_task():
    print("Debug task")

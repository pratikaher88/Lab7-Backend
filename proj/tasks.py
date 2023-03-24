import os
import time

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True

@celery.task(name="count_words")
def create_task_text(text):
    return len(text.split())

@celery.task(name="count_words_and_sleep")
def count_words_and_sleep(text):
    count = len(text.split())
    time.sleep(count)
    return count

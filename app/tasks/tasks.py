from time import sleep

from celery import Celery

celery = Celery(__name__, broker="redis://host.docker.internal:6379/0")


@celery.task
def add(x, y):
    sleep(10)
    return x + y

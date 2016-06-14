from __future__ import absolute_import
import time
from mysite.celery_app import app

from celery.utils.log import get_task_logger
logger = get_task_logger("abacus_celery")

@app.task
def add(x, y):
    logger.debug("before sleep")
    time.sleep(5)
    logger.debug("after sleep")
    return (x + y,"JKLF")


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
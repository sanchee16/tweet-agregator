from __future__ import absolute_import
from celery import Celery

celery = Celery(
    'twee_pro',
    backend='redis://localhost',
    broker='redis://localhost:6379/0',
    include=['twee_pro.tasks'])


celery.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)


if __name__ == '__main__':
    celery.start()

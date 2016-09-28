BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'redis://localhost'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Asia/Kolkata'
CELERY_ENABLE_UTC = True
CELERY_ROUTES = {
        'tasks.add': 'low-priority',
}
CELERY_ANNOTATIONS = {
        'tasks.add': {'rate_limit': '10/m'}
}

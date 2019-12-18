from celery.schedules import crontab
import os

class config():

    @property
    def MONGODB_URI():
        if os.environ.get('DB_USER', False):
            return 'mongodb://{0}:{1}@{2}'.format(os.environ.get('DB_USER', None), os.environ.get('DB_PASS', None), os.environ.get('DB_HOST', "127.0.0.1"))
        return 'mongodb://{0}'.format(os.environ.get('DB_HOST', "127.0.0.1"))
    
    MONGODB_DB   = os.environ.get('DB_DB', "zhdb")
        
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', MONGODB_URI)
    CELERY_BROKER_URL     = os.environ.get('CELERY_BROKER_URL', MONGODB_URI) 
    CELERY_CREATE_MISSING_QUEUES = True
    # CELERYBEAT_SCHEDULE = {
    #     'SEND_EMAILS': {
    #         'task': "periodic_task",
    #         'schedule': crontab(minute="*")
    #     }
    # }

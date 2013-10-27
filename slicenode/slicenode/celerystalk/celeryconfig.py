BROKER_HOST = 'localhost'
BROKER_PORT = 5672
BROKER_TRANSPORT = 'amqp'
BROKER_VHOST = 'test_host'
BROKER_USER = 'test'
BROKER_PASSWORD = 'test_pass'

# Define routes
"""CELERY_ROUTES = {
    'tasks.add': 'low-priority',}
"""

# Potentially Useful
#CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'
#CELERY_TIMEZONE = 'Europe/Oslo'
#CELERY_ENABLE_UTC = True
#CELERY_IMPORTS = ('tasks',)


CELERY_RESULT_BACKEND = 'mongodb'
BROKER_HOST = 'localhost'
BROKER_PORT = 27017
BROKER_TRANSPORT = 'mongodb'
BROKER_VHOST = 'celery-db'
CELERY_MONGODB_BACKEND_SETTINGS = {
    'host': 'localhost',
    'port': 27017,
    'database': 'testdb',
#    'user': user,
#    'password': password,
    'taskmeta_collection':'teskmeta'}

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


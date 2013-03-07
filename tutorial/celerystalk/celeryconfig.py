BROKER_URL = 'mongodb://localhost:27017/simple_tasks'
CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
        "host": "192.168.1.100",
            "port": 30000,
                "database": "mydb",
                    "taskmeta_collection": "my_taskmeta_collection",
                    }


# Define routes
CELERY_ROUTES = {
    'tasks.add': 'low-priority',
}

# Potentially Useful
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True



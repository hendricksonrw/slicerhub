from simpleslicer import SimpleSlic3r
from celery import Celery
import celeryconfig

celery = celery.config_from_object('celeryconfig')

@celery.task
def add(x, y):
    return x + y

@celery.task
def enqueue_job(stl, config, output):
    print 'starting job'
    if stl and config:
        slicer = SimpleSlic3r()
        slicer.slice(stl, config, output)
        return True
    return False

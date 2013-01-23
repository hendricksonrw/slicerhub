from simpleslicer import SimpleSlic3r
from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def add(x, y):
	return x + y

@celery.task
def enqueue_job(stl, config, output):

	if stl and config:
		slicer = SimpleSlic3r()
		slicer.slice(stl, config, output)
		return True
	return False

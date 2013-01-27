from celery import Celery
from slicebase.slicers import SlicerFactory

# Needs to be moved out to a config file
celery = Celery('tasks', broker='amqp://guest@localhost//')

@celery.task
def process_job(slice_job, slicer_type, slicer_version):
	"""Celery Task that actually kicks off the slicing subprocess when 
	it is run. In the future should handle auto-merging the STLS into one
	file. A slice_job is a Slice Object from models and contains all required
	information to run a task
	"""

	# If we have everything we need
	if slice_job and slicer_type and slicer_version:
		
		# GET STL and write to temp dir
		# GET config and write to temp dir

		# POST that the slicing job has started
		slicer = SlicerFactory.create_slicer(slicer_type, slicer_version)
		results = slicer.slice(slice_job.stl, config, output)
		
		# POST The status of the result of the job. If it sliced correctly
		# and gcode is availble to download POST SUCCESS status.
		
		# On Success
		# POST GCODE to job_id
		# DELETE temp files used for slicing
		# Kick off 'Notification' task for this job
		return True
	return False

@celery.task
def send_results(slice_job, slicer_results):
	"""Takes the messaging method (right now just an e-mail) and sends the 
	results of the slicing job to the job's e-mail address
	"""

	# Build E-mail text
	# Should contain what happened and a link to their gcode file

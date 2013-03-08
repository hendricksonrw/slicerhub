
import logging
from celery import Celery
import celeryconfig
from slicebase.slicers import SlicerFactory
from slicebase.models import SliceState
from task_helper import TaskHelper
from slicebase import models
from mongoengine import *

#connect('celery-db')

celery = Celery()
celery.config_from_object(celeryconfig)

@celery.task
def process_job(slice_id, slicer_type, slicer_version):
	"""Takes a slice_job and tries to generate gcode based on it.

        Rev 1: This is all local, there are no temp files or POST/GET calls
            because everything will be local. Eventually it will be moved
            so a server could be devoted to just processing tasks so it would
            have to communicate with another server to get stls, configs etc.

        Celery Task that actually kicks off the slicing subprocess when
	it is run. In the future should handle auto-merging the STLS into one
	file. A slice_job is a Slice Object from models and contains all
        required information to run a task.

        Args:
            slice_job: a SliceJob object
            slicer_type: a string, 'slic3r' used by the factory to determine
                which type of slicer to return.
            slicer_version: a string, 'VERSION097' used by the factory to build
                the path to the slicer executable
        Returns:
            True if the stls were sliced and everything was perfect.
            False if there was an error.
	"""

        # Need to get the slice_job from the db.
        if not slice_id:
            return False

        logging.info('trying to slice job %s' % str(slice_id))
        slice_job = models.get_job_by_id(slice_id)

	# If we don't have everything we need bail
	if not slice_job or not slicer_type or not slicer_version:
            return False

        # GET STL and write to temp dir
        # GET config and write to temp dir
        stl_path, config_path = TaskHelper.get_stl_config_path(slice_job)

        output = TaskHelper.generate_output(slice_job)

        # POST that the slicing job has started
        slicer = SlicerFactory.create_slicer(slicer_type, slicer_version)
        result = slicer.slice_job_files(stl_path, config_path, output)

        # POST The status of the result of the job. If it sliced correctly
        # and gcode is availble to download POST SUCCESS status.
        # On Success
        if not result:
            TaskHelper.update_job_state(slice_job, SliceState.FAILED)

        TaskHelper.post_gcode(output_path)
        TaskHelper.update_job_state(slice_job, SliceState.SUCCESS)
        TaskHelper.cleanup_temp(file_paths)

        # Kick off 'Notification' task for this job
        send_results.delay(slice_job, result)
        return True

@celery.task
def send_results(slice_job, slicer_results):
	"""Takes the messaging method (right now just an e-mail) and sends the
	results of the slicing job to the job's e-mail address
	"""

	# Build E-mail text
	# Should contain what happened and a link to their gcode file
        TaskHelper.send_notifications(slice_job)
        return True

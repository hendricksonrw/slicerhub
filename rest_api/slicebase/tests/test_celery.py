"""
"""
import logging
import os
import unittest

from mongoengine import *

from slicebase.celerystalk import TaskHelper
from slicebase.celerystalk import tasks
from slicebase.models import SliceJob
from slicebase.models import SliceState
from slicebase.slicers import SlicerFactory
from slicebase.slicers.slic3rwrap import Slic3rWrappers
from slicebase import models

class TestCeleryTasks(unittest.TestCase):
    """Tests both the ability to add tasks but their functions as well.
    """
    def setUp(self):
        connect('testing')
        self.slice_job = create_dummy_job()
        self.slicer = SlicerFactory.SLIC3R
        self.version = Slic3rWrappers.VERSION097

    def tearDown(self):
        # Cleans up the testing db
        models.SliceJob.drop_collection()

    def test_celery_process_task(self):
        """Test the actual celery process by firing it off.

        Requires a celery worker and mongodb to be running. See the shell
        scripts in the celerystalk module. Will expand setup to make the call
        to spin up a celery worker for testing.
        """

        slice_job = create_dummy_job()
        job = models.get_job_by_id(slice_job.job_id)
        self.assertIsNotNone(job)
        logging.info('starting task tests')
        tasks.process_job.delay(slice_job.job_id, self.slicer, self.version)


    def test_get_stl_config_path(self):
        """Given a job and job id can we get the full path to stl & config?
        """
        slice_job = create_dummy_job()
        base = os.getcwd() + '/slices/' + str(slice_job.job_id) + '/'
        stl_path = base + 'test.stl'
        logging.info('stl_path %s' % stl_path)
        config_path = base + 'test.ini'

        s_result, c_result = TaskHelper.get_stl_config_path(slice_job)

        self.assertEqual(len(s_result), 1)
        self.assertEqual(stl_path, s_result[0])
        self.assertEqual(config_path, c_result)

    def test_get_output(self):
        """Given a SliceJob generate the output filename.
        """

        result = TaskHelper.generate_output(None)
        self.assertFalse(result)

        compare = ['test.gcode']
        result = TaskHelper.generate_output(self.slice_job)

        self.assertEqual(compare, result)

    def test_update_state(self):
        """Test if our task update method works.
        """

        job = create_dummy_job()
        job.state = SliceState.FAILED

        self.assertEqual(job.state, SliceState.FAILED)

        new_state = SliceState.SUCCESS
        result = TaskHelper.update_job_state(job, new_state)
        self.assertTrue(result)
        self.assertEqual(job.state, new_state)

def create_dummy_job():
    num_jobs = len(models.SliceJob.objects) + 1
    result = models.create_store_job(
            num_jobs, 'test.ini', ['test@test.com'],
            ['test.stl'])


    return result


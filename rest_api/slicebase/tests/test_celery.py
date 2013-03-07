"""
"""
import logging
import os
import unittest

from mongoengine import *

from slicebase.celerystalk import TaskHelper
from slicebase.models import SliceJob
from slicebase.models import SliceState
from slicebase import models

class TestCeleryTasks(unittest.TestCase):
    """Tests both the ability to add tasks but their functions as well.
    """
    def setUp(self):
        self.db = connect('testing')
        self.slice_job = create_dummy_job()

    def tearDown(self):
        # Cleans up the testing db
        models.SliceJob.drop_collection()

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
    temp_job = models.SliceJob(
        job_id=str(num_jobs), config='test.ini', stls=['test.stl'],
        responses=['test@test.com'])
    temp_job.save()
    return temp_job


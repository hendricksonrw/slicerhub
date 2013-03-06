"""
"""
import unittest
from mongoengine import *
import logging

from slicebase import models

class TestModelAPI(unittest.TestCase):

    def setUp(self):

        self.config_filename = 'config.ini'
        self.model_filename = 'test.stl'
        self.email = 'ross@savorywatt.com'
        self.job_id = 1308410
        self.db = connect('testing')

        jobs = models.SliceJob.objects.filter(job_id=self.job_id)

        for job in jobs:
            job.delete()

    def tearDown(self):
        """Need to remove whatever we tested with from the db.
        """

        jobs = models.SliceJob.objects.filter(job_id=self.job_id)

        for job in jobs:
            job.delete()

    def test_models_remove_by_job_id(self):
        """Tests if we can remove a job by id.
        """
        # Verify that the remove method can handle requests to remove objects
        # that don't exist
        result = models.remove_job_by_id(self.job_id)
        self.assertFalse(result)

        result = self.gen_test_job()
        self.assertTrue(result)

        result = models.remove_job_by_id(result.job_id)
        self.assertTrue(result)


    def test_models_create_store_delete(self):
        """Test data model layer.
        """
        result = self.gen_test_job()

        self.assertTrue(result)

        result = models.remove_job_by_id(result.job_id)

        self.assertTrue(result)

    def test_models_get_job(self):
        """ Test if we are able to get a job by the job_id.
        """
        result = self.gen_test_job()

        result = models.get_job_by_id(result.job_id)

        self.assertIsNotNone(result)

    def test_models_update_job(self):
        """ Tests if we can update properties and persist them.
        """
        test_job = self.gen_test_job()

        self.assertIsNotNone(test_job)

        # Change the config filename
        config = 'new_config.ini'
        test_job.config = config

        # Update the job
        result = models.update_job(test_job)
        self.assertTrue(result)

        # Retrieve the job to ensure that we have what is in the DB
        result = models.get_job_by_id(test_job.job_id)
        self.assertIsNotNone(result)
        self.assertEqual(result.config, unicode(config))

        # Cleanup - remove the item from the db
        result = models.remove_job(result)
        logging.info('remove_result: %s' % str(result))
        self.assertTrue(result)

    def gen_test_job(self):
        result = models.create_store_job(
            self.job_id, self.config_filename, [self.model_filename],
            [self.email])

        return result



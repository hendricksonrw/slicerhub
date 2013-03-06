"""
"""


import unittest

class TestModelAPI(unittest.TestCase):

	def setUp(self):

		self.config_filename = 'config.ini'
		self.model_filename = 'test.stl'
		self.email = 'ross@savorywatt.com'

	def test_models_create_store_delete(self):
        """Test data model layer.
		"""
		result = get_test_job()

        self.assertTrue(result)

        result = models.delete_job(job_id)

        self.assertTrue(result)

	def test_models_get_job(self):
		""" Test if we are able to get a job by the SliceJob or job_id.
		"""
		result = gen_test_job()

	def test_models_update_job(self):

		test_job = gen_test_job()

		self.assertIsNotNone(test_job)

		# Change the config filename
		config = 'new_config.ini'
		test_job.config = config

		# Update the job
		models.update_job(test_job)

		# Retrieve the job to ensure that we have what is in the DB
		result = models.get_job(test_job.job_id)
		self.assertNotEqual(result.config, config)
		
		# Cleanup - remove the item from the db
		result = models.remove_job(result)
		self.assertTrue(result)


def gen_test_job():

	job_id = 1308410

	result = models.create_store_job(
		job_id, self.config_filename, [self.model_filename], [self.email])

	return result



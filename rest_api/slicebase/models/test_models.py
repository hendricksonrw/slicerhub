import unittest
from mongoengine import *
import models

class TestSliceJob(unittest.TestCase):

	def setUp(self):
		self.db = connect('testing')

	def tearDown(self):
		# Cleans up the testing db
		models.SliceJob.drop_collection()

	def test_create_slice_job(self):

		"""Make sure that we can create and persist a slice job.
		"""
		num_jobs = len(models.SliceJob.objects) + 1
		temp_job = models.SliceJob(job_id=str(num_jobs), config='test.ini', stls=['one.stl'], email='test@test.com')
		temp_job.save()
		self.assertTrue(temp_job.id)
	
	def test_get_slice_job(self):

		""" Make sure we can get jobs based on job_id.
		"""

		dummy_id = create_dummy_slice()
		dummy_slice = models.SliceJob.objects(id=dummy_id)
		self.assertTrue(dummy_slice)

	def test_update_slice_job(self):	
		""" Make sure that we can update a specific job id.
		"""
		dummy_id = create_dummy_slice()

		job = models.SliceJob.objects.get(id=dummy_id)
		self.assertIsNotNone(job)

		new_config = 'new_config'
		job.config = new_config

		job.save()
		job = None
		job = models.SliceJob.objects.get(id=dummy_id)

		self.assertIsNotNone(job)
		self.assertEqual(job.config, new_config)

	def test_remove_slice_job(self):
		""" Make sure we can remove specific jobs.
		"""
		count = 0

		for num in range(100):
			create_dummy_slice()

		for job in models.SliceJob.objects:
			count += 1
			job.delete()

		self.assertGreaterEqual(count, 100)


def create_dummy_slice():
	num_jobs = len(models.SliceJob.objects) + 1
	temp_job = models.SliceJob(job_id=str(num_jobs), config='test.ini', stls=['one.stl'], email='test@test.com')
	temp_job.save()
	return temp_job.id


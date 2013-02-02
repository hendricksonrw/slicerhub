
import unittest
from slicebase import models

class TestSliceModel(unittest.TestCase):

	def setUp(self):
		"""
		"""

	def test_slice_creation_incorrect_params(self):
		"""Test we can create a slice object with the right params
		"""
		with self.assertRaises(Exception):
			slice_one = models.Slice(stls=None, 
											config='whatver.ini', 
											email='jorge@jorge.com')

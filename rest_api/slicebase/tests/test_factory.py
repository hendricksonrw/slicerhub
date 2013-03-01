import logging
import unittest

class TestFactory(unittest.TestCase):

	def startup(self):
		"""Setup everything.
		"""
		return True

	def test_create_slic3r(self):
		"""Create a slicer wrapper for different versions of slicer installed.
		"""
		slicer = SlicerFactory.SLIC3R
		version = SlicerWrapper.Slicer.VERSION097

		slicer_wrapper = SlicerFactory.create_slicer(slicer, version)
		logging.info('got here')
		self.assertIsNotNone(slicer_wrapper)
		

import logging
import unittest

from slicebase.slicers import SlicerFactory
from slicebase.slicers.slic3rwrap import Slic3rWrappers

class TestFactory(unittest.TestCase):

	def startup(self):
		"""Setup everything.
		"""
		return True

	def test_create_slic3r(self):
		"""Create a slicer wrapper for different versions of slicer installed.
		"""
		slicer = SlicerFactory.SLIC3R
		version = Slic3rWrappers.VERSION097

		slicer = SlicerFactory.create_slicer(slicer, version)
		self.assertIsNotNone(slicer)
		

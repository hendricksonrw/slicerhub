import nose
import unittest


class TestSlicerHub(unittest.TestCase):

#	def setup_class(self):
#		if self.base_url is None:
#			self.base_url = 'slicerhub.com'

	def setUp(self):
		self.base_url = 'bastard'

	def test_have_base_url(self):
		if self.base_url is None:
			assert False
		if self.base_url is not  None:
			assert True

def test():
	assert False

"""
	assert we can GET from a slice and get JSON
	assert we can POST to a slice and enqueue a job
	assert we can POST to a slice - gcode | stl | config
	assert we can do all the above using oauth2
"""


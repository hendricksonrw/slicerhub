import unittest
import requests
import logging
import json

class TestEntry(unittest.TestCase):

	def setUp(self):
		"""Setup the slicing info needed for testing
		"""
		self.test_id = 0121013
		self.test_stl = 'test.stl'
		self.test_config = 'test_config.ini'
		self.test_email = 'test@slicerhub.com'

	def test_serve_stls_405(self):
		"""Test we're not able to POST or PUT"""
		r = requests.post('http://localhost:8080/slice/10323/stls/')
		self.assertEqual(r.status_code, 405)

		r = requests.put('http://localhost:8080/slice/10323/stls/')
		self.assertEqual(r.status_code, 405)


	def test_get_index(self):
		"""Test base index get works"""
		r = requests.get('http://localhost:8080/')
		self.assertEqual(r.status_code, 200)

	def test_post_slices(self):
		"""Test post slices works"""
		with open(self.test_stl, 'r') as f:
			model = f.read()
			payload = {'email': self.test_email, 'model': self.test_stl, 'email': self.test_email, 'config': self.test_config} 
			r = requests.post('http://localhost:8080/slices', data=payload)
			self.assertEqual(r.status_code, 200)

	def test_get_slice_id(self):
		"""Test get by slice id works"""
		url = 'http://localhost:8080/slices/%s/' % self.test_id
		logging.info(url)
		r = requests.get(url)
		self.assertEqual(r.status_code, 200)
	
	def test_put_slice_id(self):
		"""Test put by slice id works"""
		url = 'http://localhost:8080/slices/%s/' % self.test_id
		logging.info(url)
		payload = None	
		r = requests.put(url, data=payload)
		self.assertEqual(r.status_code, 200)
	
	def test_get_slice_gcode(self):
		"""Test get slice"""
		url = 'http://localhost:8080/slices/%s/gcode' % self.test_id
		logging.info(url)
		r = requests.get(url)
		self.assertEqual(r.status_code, 200)

	def test_put_slice_gcode(self):
		"""Test put slice"""
		url = 'http://localhost:8080/slices/%s/gcode' % self.test_id
		logging.info(url)
		payload = None	
		r = requests.put(url, data=payload)
		self.assertEqual(r.status_code, 200)

	def test_get_slice_config(self):
		"""Test get slice config"""
		url = 'http://localhost:8080/slices/%s/config' % self.test_id
		logging.info(url)
		r = requests.get(url)
		self.assertEqual(r.status_code, 200)
	
	def test_put_slice_config(self):
		"""Test put slice configs"""
		url = 'http://localhost:8080/slices/%s/config' % self.test_id
		logging.info(url)
		r = requests.get(url)
		self.assertEqual(r.status_code, 405)

	def test_get_slice_stls(self):
		"""Test get slice stls"""
		url = 'http://localhost:8080/slices/%s/stls' % self.test_id
		logging.info(url)
		r = requests.get(url)
		self.assertEqual(r.status_code, 200)

	def test_put_slice_stls(self):
		"""Test put slice stls"""
		url = 'http://localhost:8080/slices/%s/stls' % self.test_id
		logging.info(url)
		r = requests.get(url)
		self.assertEqual(r.status_code, 405)

	def test_get_slice_state(self):
		"""Test get slice state"""
		url = 'http://localhost:8080/slices/%s/state' % self.test_id
		logging.info(url)
		r = requests.get(url)
		self.assertEqual(r.status_code, 200)

	def test_put_slice_state(self):
		"""Test put slice state"""
		url = 'http://localhost:8080/slices/%s/state' % self.test_id
		logging.info(url)
		payload = None	
		r = requests.put(url, data=payload)
		self.assertEqual(r.status_code, 200)

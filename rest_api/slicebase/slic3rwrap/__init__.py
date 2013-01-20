"""
Slic3r Python Wrapper
Copyright 2013 Ross Hendricksonn
BSD License
"""
import re, subprocess
from random import randrange

class Slic3r():

	def slice(self, stl_name=None, config_name=None, output_name=None):
		dirty = "--load %s %s" % (config_name, stl_name)
		args = ['--load', config_name, '--output-filename-format', output_name , stl_name]
		return subprocess.call(["slic3r", args[0], args[1], args[2], args[3], args[4]])

	def slice_name(self, filename):
		filename = re.sub(r'\.\w+', '', filename)
		return  repr(filename) #+ "_" + repr(randrange(200))

	def gen_slice_id(self):
		return randrange(500000)
	

"""
Slic3r Python Wrapper
Copyright 2013 Ross Hendricksonn
BSD License
"""
import re, subprocess
from random import randrange


class Slic3rWrappers():

	def create_slic3r(version)
		if version == '0.9.7':
			# Can move this string to a config file in the future
			slicer = new Slic3r('~/utils/Slic3r097/bin/')

class Slic3r():

	def __init__(self, slicer_bin):
		
		self.slicer_bin = slicer_bin
		
	def slice(self, stl_name=None, config_name=None, output_name=None):
	    """Takes a filename and path for the model to be sliced and for the config
		to be used while slicing. Also has an output_name added."""
		
		args = ['--load', config_name, '--output-filename-format', output_name , stl_name]
		result = subprocess.call([self.slicer_bin + 'slic3r', args[0], args[1], args[2], args[3], args[4]])
		# if result > 0 : we successfuly sliced | == 0 then we failed to slice
		return result

	def slice_name(self, filename):
		filename = re.sub(r'\.\w+', '', filename)
		return  repr(filename) #+ "_" + repr(randrange(200))

	def gen_slice_id(self):
		return randrange(500000)
	

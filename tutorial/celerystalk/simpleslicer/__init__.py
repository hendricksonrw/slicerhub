#!/usr/bin/python
import subprocess, re, os
from random import randrange

class SimpleSlic3r:
	def __init__(self):
		print 'slic3r created'

	def slice(self, stl_name=None, config_name=None, output_name=None):
		print 'slicing %s using config %s' % (stl_name, config_name)
		dirty = "--load %s %s" % (config_name, stl_name)
		args = ['--load', config_name, '--output-filename-format', output_name , stl_name]
	        execute = '/home/hendricksonrw/utils/Slic3r097/bin/slic3r'
                return subprocess.call([execute, args[0], args[1], args[2], args[3], args[4]])

	def slice_name(self, filename):
		filename = re.sub(r'\.\w+', '', filename)
		return  repr(filename) #+ "_" + repr(randrange(200))

	def gen_slice_id(self):
		return randrange(500000)
	
	def send_email(self, addreess, file_name):
		print 'send e-mail'		


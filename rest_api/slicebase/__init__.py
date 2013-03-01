#!/usr/bin/python
import subprocess, re, os, sys
from slicers.slic3rwrap import Slic3r

class SliceBase():

	@staticmethod
	def get_slice(request, slice_id):
		"""Going to need some way to get the slices for the slice URLs.
		This method should make the SQLAlchemey calls and prep the
		information to return through the request"""

	@staticmethod
	def send_email(address, body, replyto=None):
		"""When a job is done being sliced we need to send an e-mail out.
		"""
	
	@staticmethod
	def process_slice_request(email, model, config):
		"""Handles the slice request. Writes the 3d and config files
		to disk and stores the job in the db and adds it to the queue.
		This should be kicked off in a process to not block the return.
		"""

		if email and model and config:
			try:
				# Read the files - THIS IS DANGEROUS FOR LARGE FILES
				model_raw = model.file.read()
				config_raw = config.file.read()

				# Make and instance of the Slic3r Wrapper
				slicer = Slic3r()
				model_filename = slicer.slice_name(model.filename)
				config_filename = slicer.slice_name(config.filename)
				output_filename = model_filename.replace('\'', '') + '.gcode'

				# Write data to disk
				# Make sure the slice has a unique folder
				slice_id = repr(slicer.gen_slice_id())
				slice_folder = os.path.join(os.getcwd(), 'slices', slice_id)
				if not os.path.exists(slice_folder):
					os.makedirs(slice_folder)

				# Write the 3D model to the new folder
				model_filename = os.path.join(slice_folder, model.filename)
				with open(model_filename, 'w') as f:
					f.write(model_raw)
					f.close()
				
				# Write the Configuration to the new folder - If we have a user
				# we need to write this config to their user dir
				config_filename = os.path.join(slice_folder, config_filename + '.ini')
				with open(config_filename, 'w') as f:
					f.write(config_raw)
					f.close()

				# Write into the DB an instance of the Slice
				# Slice should have timestamp of job start
				# Slice shoudl have e-mail of who to send this too after
				# If a User ID got passed in on the request - Put that in too (history)
				# Adds the Slice to the job queue with status finished = False
				message = "Job %s successfully added to the queue" % slice_id
				return True , message
			except Exception, e:
				message = "Job was not added to the queue: " + str(sys.exc_info()[0]) + ":" + str(e)
				return False, message 
	


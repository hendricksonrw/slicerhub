#!/usr/bin/python
import logging
import os 
import re
import subprocess
import sys

from slicers import SlicerFactory
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
    def process_slice_request(request):
        """Extracts needed information out of the request.
        """
        email = request.forms.email
        slicer = request.forms.slicer
        version = request.forms.version
        model = request.files.model
        config = request.files.config

        try:
            # Read the files - THIS IS DANGEROUS FOR LARGE FILES
            logging.info('model %s' % str(model.file))
            model_raw = model.file.read()
            config_raw = config.file.read()
            
            return SliceBase.process_slice_job(email, model_raw,
                    config_raw)

        except Exception, e:
            message = "Job add failed: %s" % str(e)
            return False, message 

    @staticmethod  
    def slice_job_files(
            email, slicer, version, model_path, config_path,
            output_path, job_id):

        """Fires up the slicer and slices the given file with the given config.
        """

        # If we don't have right args, bail

        # Try slicing it
        slicer = SlicerFactory.create_slicer(slicer, version)
        if not slicer:
            raise Exception('unable to create slicer')

        slicer.slice_job(model_path, config_path, output_path)
        # When slicer is finished add task to queue to send state update
        # and notification for job_id

    @staticmethod
    def write_slice_files(
            email, slicer, version, model_filename, model_raw, config_filename, 
            config_raw):
        """Handles the slice request. Writes the 3d and config files
        to disk and stores the job in the db and adds it to the queue.
        This should be kicked off in a process to not block the return.
        """

        if not email or not model_filename or not model_raw or not config_raw:
            return False, 'Malformed arguments: %s:%s:%s' % (email,
                    model_filename, config_filename) 
        try:
            logging.info('start slice')                            

            # Make static factory call to create specified slicer 
            slicer = SlicerFactory.create_slicer(slicer, version)
            if not slicer:
                raise Exception
            
            output_filename = model_filename.replace('\.\w+', '') + '.gcode'

            # Write data to disk
            # Make sure the slice has a unique folder
            slice_id = repr(slicer.gen_slice_id())
            slice_folder = os.path.join(os.getcwd(), 'slices', slice_id)
            if os.path.exists(slice_folder):
                slice_id = repr(slicer.gen_slice_id())
                slice_folder = os.path.join(os.getcwd(), 'slices', slice_id)
            else:
                os.makedirs(slice_folder)

            # Write the 3D model to the new folder
            model_filename = os.path.join(slice_folder, model_filename)
            with open(model_filename, 'w') as f:
                f.write(model_raw)
                f.close()

            # Write the Configuration to the new folder - If we have a user
            # we need to write this config to their user dir
            config_filename = os.path.join(slice_folder, config_filename)
            with open(config_filename, 'w') as f:
                f.write(config_raw)
                f.close()

            # Write into the DB an instance of the Slice
              # full path to stl, config, output
            # Slice should have timestamp of job start
            # Slice should have e-mail of who to send this too after
            # Adds the Slice to the job queue with status finished = False
            message = "Job %s successfully added to the queue" % slice_id
            return True , message, slice_id
        except Exception, e:
                message = "Job add failed: " + str(sys.exc_info()[0]) + ":" + str(e)
                return False, message 



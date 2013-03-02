"""
Slic3r Python Wrapper
Copyright 2013 Ross Hendricksonn
BSD License
"""
import logging
import re
import subprocess
from random import randrange


class Slic3rWrappers():

    @staticmethod
    def create_slicer(version):

        if not version:
            return None

        # Can move these strings to a config file in the future
        if version == '0.9.7':
            slicer = Slic3r('~/utils/Slic3r097/bin/')

        if not slicer:
            return None

        return slicer


class Slic3r():

    VERSION097 = '0.9.7'

    def __init__(self, slicer_bin):
        logging.info('attempting to create wrapper around %s' % slicer_bin)
        self.slicer_bin = slicer_bin
        logging.info('Slic3r created')

    def slice_job(self, stl_path=None, config_path=None, output_path=None):
        """Takes a filename and path for the model to be sliced and for the
        config to be used while slicing. Also has an output_name added."""

        logging.info("got here")

        args = ['--load', config_path, '--output-filename-format', output_path,
                stl_path]
        logging.info('args: %s' % str(args))
        result = subprocess.call([self.slicer_bin + 'slic3r', args[0], args[1], args[2], args[3], args[4]])
        # if result > 0 : we successfuly sliced | == 0 then we failed to slice
        return result

    def gen_slice_id(self):
        return randrange(500000)

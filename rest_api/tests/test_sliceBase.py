import logging
import unittest
import os
import re

import bottle
from slicebase import SliceBase
from slicebase.slicers.slic3rwrap import Slic3r
from slicebase.slicers import SlicerFactory

class TestSlicerBase(unittest.TestCase):

    def setUp(self):
        """Set up references to files needed for testing.
        """

        # These tests are meant to be fired off from the rest_api folder
        self.email = 'ross.hendrickson@gmail.com'
        self.slicer = SlicerFactory.SLIC3R
        self.version = Slic3r.VERSION097
        self.request = bottle.BaseRequest()

        self.model_filename = 'tests/test.stl'
        f = open(self.model_filename, 'r')
        self.model = bottle.FormsDict()
        self.model.file = f
        self.model_raw = f.read()
        self.model_filename = 'test.stl'
        f.close()

        self.config_filename = 'tests/test.ini'
        g = open(self.config_filename, 'r')
        self.config = bottle.FormsDict()
        self.config.file = g
        self.config_raw = g.read()
        self.config_filename = 'test.ini'
        g.close()

        logging.info('start tests')

    def tearDown(self):
        """Need to remove any temp files used for testing.
        """

        logging.info('tests ended')

    def test_write_and_run_slice_files(self):
        """test that we can slice model using the slicer factory.
        """

        # setUp has set the variables we need to test this method

        result, message, slice_id = SliceBase.write_slice_files(
                self.email, self.slicer, self.version, self.model_filename,
                self.model_raw, self.config_filename, self.config_raw)

        logging.info('message: %s' % message)

        self.assertTrue(result)

        output_filename = re.sub('\.\w+', '', self.model_filename)
        output_filename += '.gcode'

        # Build paths
        slice_folder = os.path.join(os.getcwd(), 'slices', slice_id)
        stl_path = os.path.join(slice_folder, self.model_filename)
        config_path = os.path.join(slice_folder, self.config_filename)
        output_path = output_filename

        result, message = SliceBase.slice_job_files(
                self.email, self.slicer, self.version, stl_path, config_path,
                output_path, slice_id)



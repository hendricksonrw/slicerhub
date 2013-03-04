import logging
import unittest
import os
import re

import bottle
from slicebase import SliceBase
from slicebase.slicers.slic3rwrap import Slic3r
from slicebase.slicers import SlicerFactory
from slicebase import models

class TestSlicerBase(unittest.TestCase):

    def setUp(self):
        """Set up references to files needed for testing.
        """

        # These tests are meant to be fired off from the rest_api folder
        self.email = 'test@slicerhub.com'
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
        if not  hasattr(self, 'property'):
            return None

        if not self.slice_id:
            return None

        # Need to remove test files.
        import os
        folder = os.path.join(os.getcwd(), 'slices', self.slice_id)
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception, e:
                logging.WARNING('Test files not deleted %s' % str(e))
        try:
            os.rmdir(folder)
        except Exception, e:
            logging.WARNING('Test folder not deleted %s' % str(e))

    def test_models_create_store_delete(self):
        """Test data model layer.
        """
        job_id = 1308410

        result = models.create_store_job(job_id, self.config_filename,
                [self.model_filename], [self.email])

        self.assertTrue(result)

        result = models.delete_job(job_id)

        self.assertTrue(result)

    def test_write_and_run_slice_files(self):
        """test that we can slice model using the slicer factory.
        """

        # setUp has set the variables we need to test this method
        # Test writing files to disk and making a DB entry
        result, message, self.slice_id = SliceBase.write_slice_files(
                self.email, self.slicer, self.version, self.model_filename,
                self.model_raw, self.config_filename, self.config_raw)

        logging.info('message: %s' % message)

        self.assertTrue(result)

        output_filename = re.sub('\.\w+', '', self.model_filename)
        output_filename += '.gcode'

        # Build paths
        slice_folder = os.path.join(os.getcwd(), 'slices', self.slice_id)
        stl_path = os.path.join(slice_folder, self.model_filename)
        config_path = os.path.join(slice_folder, self.config_filename)
        output_path = output_filename

        # Test able to slice job
        result = SliceBase.slice_job_files(
                self.email, self.slicer, self.version, stl_path, config_path,
                output_path, self.slice_id)

        self.assertTrue(result)

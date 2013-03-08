""
import os
import logging

from slicebase import models

class TaskHelper():

    @staticmethod
    def get_stl_config_path(slice_job):
        """Returns the full path to the stl and the config.
        """

        if not slice_job:
            return False, False

        if not slice_job.config or not slice_job.stls or not slice_job.job_id:
            return False, False

        base = os.getcwd() + '/slices/' + str(slice_job.job_id) + '/'
        config_path = base + slice_job.config
        stl_paths = []
        for stl in slice_job.stls:
            stl_paths.append(base + stl)

        return stl_paths, config_path

    @staticmethod
    def generate_output(slice_job):
        """Returns what the gcode file should be named.

        Rev 1. Only handles STL files.. needs to be more robust
        """
        if not slice_job:
            return False

        if not slice_job.stls:
            return False

        result = []
        for stl in slice_job.stls:
            name = stl.replace('stl', 'gcode')
            result.append(name)

        return result


    @staticmethod
    def update_job_state(slice_job, state):
        """Updates the slice_job state through a POST to the server.

        Rev 1. Since we are all on one server this does not need to post. It
        will simply update the slice_job state and then save it.
        """
        if not slice_job or not state:
            return False

        slice_job.state = state
        return models.update_job(slice_job)


    @staticmethod
    def send_notifications():
        """Iterates over notfication end points in the job and executes them.

        Rev1.1 Should send an e-mail saying x job was finished.
        """

        return False

# Unimplemented for Rev 1
    @staticmethod
    def post_gcode(slice_job, gcode):
        """Takes the generated gcode and sends it to the main server.

        Rev 1. This just writes the gcode into the write slice dir. Which
        Slic3r does automatically
        """

        return False

    @staticmethod
    def delete_job_temp_files(file_paths):
        """Cleans up any temporary files used during the slice job.

        Rev 1. We won't be using temp files.
        """
        return False

    @staticmethod
    def write_stl_config_temp(stls, config):
        """Takes the stls and config objects in memory and writes them to disk.

        Rev 1. All stls and configs are local to the task queue manager so
        there is no need to do this.
        """
        return False
    @staticmethod
    def get_stl_config(job_id):
        """Makes a request and pulls down the stl and config from the server.
        """
        return False



import slice_job

SliceJob = slice_job.SliceJob

def create_store_job(job_id, config, stls, responses):
    """Creates a job and then stores it into the db.

        Args:
            job_id: Unique int identifier
            config: String of the filename for the config used to slice
            stls: List of stl filenames to be sliced for the job
            responses: List of possible responses, e-mail addresses or URLs
                that should be notified when the job is sliced

        Returns:
            Simply returns true if the job was created and put in the db
    """
    return slice_job.create_store_job(job_id, config, stls, responses)

def update_job(job):
    """Updates a job in the db
    """
	return slice_job.update_job

def get_job_by_id(job_id):
    """Retrieves a job from the db.
    """
	return slice_job.get_job_by_id(job_id)

def delete_job_by_id(job_id):
    """Deletes a job in the db.
    """
    return slice_job.delete_job_id(job_id)

def delte_job(job):
	"""Deletes a job in the db.
	"""
	return slice_job.delete_job(job)

def get_json_job(job_id):
    """Grabs a job out of the db and formats it into JSON.
    """
	return slice_job.get_json_by_id(job_id)

def get_xml_job(job_id):
    """Grabs a job out of the db and formats it into XML.
    """
	return slice_job.get_xml_by_id(job_id)

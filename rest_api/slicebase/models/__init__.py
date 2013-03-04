import slice_job


def create_store_job(slice_id, config, stls, responses):
    """Creates a job and then stores it into the db.

        Args:
            slice_id: Unique int identifier
            config: String of the filename for the config used to slice
            stls: List of stl filenames to be sliced for the job
            responses: List of possible responses, e-mail addresses or URLs
                that should be notified when the job is sliced

        Returns:
            Simply returns true if the job was created and put in the db
    """
    return slice_job.create_store_job(slice_id, config, stls, responses)

def update_job(job):
    """Updates a job in the db
    """

def get_job(slice_id):
    """Retrieves a job from the db.
    """

def delete_job(slice_id):
    """Deletes a job in the db.
    """
    return slice_job.delete_job(slice_id)

def get_json_job(job_id):
    """Grabs a job out of the db and formats it into JSON.
    """

def get_xml_job(job_id):
    """Grabs a job out of the db and formats it into XML.
    """

import datetime
import logging

from mongoengine import *

class SliceJob(Document):

    """Simple class that handles any information that needs to be persisted
    related to a slicing job.
    """

    # Required properties
    job_id = IntField(required=True)
    config = StringField(required=True)
    responses = ListField(StringField(), required=True)
    stls = ListField(StringField(), required=True)

    # Optional properties
    state = StringField(default='CREATED')
    output_name = StringField(default='%s.gcode' % str(job_id))
    submit_time = DateTimeField(default=datetime.datetime.utcnow())
    end_time = DateTimeField()
    public = BooleanField(default=True)
    priority = IntField(default=0)


def create_job(job_id, config, responses, stls):
    """Create job.
    """
    job = SliceJob()
    job.job_id = job_id
    job.config = config
    job.responses = responses
    job.stls = stls
    logging.info('create_job %s ' % str(job.job_id))
    return job

def create_store_job(job_id, config, responses, stls):
    """Create and add to db.
    """
    connect('testing')
    job = create_job(job_id, config, responses, stls)
    result = job.save()

    if result:
        return result
    else:
        return None

def delete_job(job_id):
    """Removes a job from the db.
    """
    job = SliceJob.objects(job_id=job_id)
    if job:
        job.delete()
        return True
    else:
        return False

import datetime
import logging

from mongoengine import *

class SliceState():
    """Simple light weight class for the states a job could be in.
    """
    FAILED='failed'
    SUCCESS='success'

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

def update_job(job):
    if not job:
        return False
    result = job.save()
    if result:
        return True

def get_job_by_id(job_id):
    """Get the job from the db with an id.
    """
    result = SliceJob.objects.get(job_id=job_id)
    return result

def remove_job(job):
    """Remove job from db.
    """
    if job:
        job.delete()
        return True
    else:
        return False

def remove_job_by_id(job_id):
    """Removes a job from the db using the job_id.
    """
    try:
        job = SliceJob.objects.get(job_id=job_id)
    except SliceJob.DoesNotExist:
        job = None

    if job:
        result = remove_job(job)
        return result
    else:
        return False

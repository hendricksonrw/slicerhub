import datetime

from mongoengine import *

class SliceJob(Document):

	"""
	Simple class that handles any information that needs to be persisted related
	to a slicing job.
	"""
	# Required properties
	job_id = StringField(required=True)	
	config = StringField(required=True)	
	email = StringField(required=True)	
	stls = ListField(StringField(), required=True)

	# Optional properties
	state = StringField(default='CREATED')
	output_name = StringField(default='%s.gcode' % str(job_id))
	submit_time = DateTimeField(default=datetime.datetime.utcnow())
	end_time = DateTimeField()
	public = BooleanField(default=True)
	priority = IntField(default=0)




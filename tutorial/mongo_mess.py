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



connect('testing')

sj = SliceJob(job_id='1001', config='test.ini', email='waht@ata.com', stls=['one.stl', 'two.stl'])

result = sj.save()
print 'result: %s' % result


for job in SliceJob.objects:
	print job.job_id
	print job
	


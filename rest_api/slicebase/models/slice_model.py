from mongoengine import DynamicDocument


class Slice(DynamicDocument):
	
	def __init__(self, stls, config, email, **kwargs):
		"""
		Requires a job_id, stls list, config filename, and an e-mail."""

		# If we don't have these we cannot run this job
		if stls is None or config is None or email is None:
			raise Exception

		# Assign given required properties
		self.job_id = job_id
		self.stls = stls
		self.config = config
		self.email = email

		# Assign potential optional properties with defaults
		self.state = kwargs.get('state', 'CREATED')
		self.output_name = kwargs.get('output_name', '%s.gcode' % str(job_id))
		self.submit_time = kwargs.get('submit_time', datetime.datetime.utcnow())
		self.start_time = kwargs.get('start_time', '')
		self.end_time = kwargs.get('end_time', '')
		self.public = kwargs.get('public', True)
		self.priority = kwargs.get('priority', 0)



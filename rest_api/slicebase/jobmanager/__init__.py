"""
Copyright 2013 Ross Hendrickson
Multiprocessor based slicing job processor
"""

# This is a quick pass attempt for something that will work on a single server at a time.
# Should be expandable by putting this on a different server and having another server update
# the pull_queue for this server.
# Going to need a way to track all the processer jobs and monitor them for failure | completion

class SliceJobManager():
	
	def add_slice_job(slicer_type, model, config):
		"""Adds a new entry into the DB based Job Queue with the
		status of 'ready'. Should timestamp when the job started
		accepts the slicer type (Slic3r is our only one right now)
		model | full path to the 3D STL to be sliced
		config | full path the INI to be used

		"""

	def start_job(job_id):
		"""This kicks off a process from multiproccesing that slices the model"""
		# get the DB job representation by job_id
		# determine what slicing engine
		# kick off the right slice on a process that calls subprocess thorugh the
		# right adapter


	def clean_jobs():
		"""Go through the Slice table and remove finished items and delete their files
		off the hard drive, STL, gcode, ini if in the dir (save user INIs)
		--- this should be used time sensitively
		"""

	def clean_pull():
		"""This goes through the job queue and removes all finished rows. Makes sure
		that the files actually exist. If not then re-enqueues job if it can, if 
		it can't then it deletes the job.
		"""

	def check_pull():
		"""This iterates over the processes that are currently active and polls them
		for CPU usage and completion, updates the pull_queue with job state, and 
		if there is room in the running_list starts more jobs in it."""
		# make sure running_list is the right size by checking self._max_jobs
		# iterate over running_list
		# if the state for each proc is different than the state_list
			# update DB & state_list
			# for each finished proc or empty slot increment new_job count

		# for job in range(0, new_job)
			# pull out new job info from DB pull_queue
			# start proc and add new proc to running_list with new entry in state_list
		
	def change_max_jobs(max_jobs):
		"""Modifies what the max number of jobs that can be processed at a time.
		"""

	def run_stats():
		"""Every day statistics should be generated on how much work was done during the day.
		"""

# Check how long it has been since we ran clean_jobs and run it

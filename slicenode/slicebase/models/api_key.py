"""
Copyright 2013 Ross Hendricksonn
BSD License
"""

class ApiKey():

	def __init__(self, api_id, api_secret):

		if api_id or api_secret is None:
			throw Exception

		self.api_id = api_id
		self.api_secret = api_secret

	

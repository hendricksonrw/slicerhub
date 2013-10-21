#!/usr/bin/python

class AuthenticationException(Exception)
		pass

def authenticated(function):
	def wrapper(*args, **kwargs):
		"""Takes the request object and verifies that the hash matches.
		"""

		# Right now authentication isn't in place so we just assumem True
		hash_match = True
		if hash_match:
			fn(*args, **kwargs)
		else:
			# This needs to be expanded to throw a 401-unauthorized
			raise AuthenticationException("Not Authenticated")


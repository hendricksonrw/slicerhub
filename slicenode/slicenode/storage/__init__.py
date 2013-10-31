
import redis

class StorageEngine:

	def __init__(self):

		self.db = redis.StrictRedis(host='localhost', port=6379, db=0)	
	
	def set(self, key, value):

		self.db.set(key, value)

	def get(self, key):

		return self.db.get(key)



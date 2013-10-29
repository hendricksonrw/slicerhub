from wsgiref import simple_server
import falcon
import redis
import json
import logging

class StorageEngine:

	def __init__(self):

		self.db = redis.StrictRedis(host='localhost', port=6379, db=0)	
	
	def set(self, key, value):

		self.db.set(key, value)

	def get(self, key):

		return self.db.get(key)


class SliceResource:

	def __init__(self, db):
		self.db = db

	def on_get(self, req, resp, slice_id):
		"""Handles GET requests"""

		slice_id = req.get_param('slice_id') or ''
		try:
			result = self.db.get(slice_id)
		except Exception as ex:
			raise falcon.HTTPServiceUnavailable('Word', 'to yo mother', 30)

		resp.set_header('X-Powered-By', 'Donuts')
		resp.status = falcon.HTTP_200
		resp.body = json.dumps(result)
 
	def on_post(self, req, resp, slice_id):

		try:
			raw_body = req.stream.read()
		except:
			raise falcon.HTTPError(falcon.HTTP_748,
								   'Read Error',
								   'Could not read the request body. Must be '
								   'them ponies again.')
		try:
			db.set(slice_id, raw_body)
		except Exception as ex:
			raise falcon.HTTPError(falcon.HTTP_748, 'word', str(ex))

		resp.status = falcon.HTTP_201
		resp.location = 'slice\\%s'% str(slice_id)

wsgi_app = api = falcon.API()

db = StorageEngine()
slices = SliceResource(db)
api.add_route('/slices/{slice_id}/', slices)

app = application = api

if __name__ == '__main__':
	httpd = simple_server.make_server('127.0.0.1', 8080, app)
	httpd.serve_forever()

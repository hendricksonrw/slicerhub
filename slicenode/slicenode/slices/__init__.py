
import falcon

from slicenode.utils import generate_slice_id


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
 
	def on_post(self, req, resp):

		slice_id = generate_slice_id()
		try:
			raw_body = req.stream.read()
			print str(len(raw_body))
		except:
			raise falcon.HTTPError(falcon.HTTP_748,
								   'Read Error',
								   'Could not read the request body. Must be '
								   'them ponies again.')
		try:
			self.db.set(slice_id, raw_body)
			print "slice_id:", slice_id
		except Exception as ex:
			raise falcon.HTTPError(falcon.HTTP_748, 'word', str(ex))

		resp.status = falcon.HTTP_201
		resp.location = 'slices\\%s'% str(slice_id)



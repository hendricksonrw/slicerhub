import falcon

class STLResource:

	def __init__(self, db):

		self.db = db

	def on_get(self, req, resp, slice_id, stl_id=None):
		print slice_id
		print stl_id
		try:
			result = build_stl_result(slice_id, stl_id, self.db)
		except Exception as ex:
			raise falcon.HTTPError(falcon.HTTP_500, 'Request processing error', str(ex))

		resp.status = falcon.HTTP_200
		resp.body = result


def build_stl_result(slice_id, stl_id, db):

	return 'Nothing to respond'

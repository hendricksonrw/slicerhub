
class GCodeResource:

	def __init__(self, db):

		self.db = db

	def on_get(self, req, resp, slice_id, gcode_id):
		print slice_id
		pass



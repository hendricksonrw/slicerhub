import  falcon

from slicenode.storage import StorageEngine
from slicenode.stls import STLResource
from slicenode.slices import SliceResource
from slicenode.gcodes import GCodeResource

def build_api():

	db = StorageEngine()
	slices = SliceResource(db)
	stls = STLResource(db)
	gcodes = GCodeResource(db)

	api = falcon.API()
	api.add_route('/slices/', slices)
	api.add_route('/slices/{slice_id}/', slices)
	api.add_route('/slices/{slice_id}/stls/{stl_id}', stls)
	api.add_route('/slices/{slice_id}/gcodes/{gcode_id}', gcodes)
	api.add_route('/slices/{slice_id}/gcodes/', gcodes)

	return api

#!/usr/bin/python
import os
from  bottle import run, route, static_file, request

@route('/')
def serve_index():
	return static_file('index.html', os.getcwd())

@route('/slice', method='POST')
def slice_model():
	from multiprocessing import Process
	from slicebase import SliceBase
	
	email = request.forms.email
	model = request.files.model
	config = request.files.config

	if email and model and config:
		#p = Process(target=SliceBase.process_slice_request, args=(email, model, config))
		#p.start()
		#p.join()
		resp = SliceBase.process_slice_request(email, model, config)
		return resp
	else:
		return "You was missing some information, job was not added. %r %r %r" % (email, len(model), len(config))

@route('/slice/<slice_id>/gcode/', method='GET')
def serve_gcode_by_slice_id(slice_id=''):
	if slice_id != '':
			return static_file()

run(host='0.0.0.0', port=8080, debug=True)
#bottle.run(server=bottle.CGIServer)



#!/usr/bin/python
import os
from  bottle import run, route, static_file, request
from api import sliceapi

@route('/')
def serve_index():
	return static_file('index.html', os.getcwd())

@route('/slices', method='POST')
def slice_model():
	"""POST /slices
		Writes stl and config into /id_number/ folder
		Adds a task to the task queue to process the given ID (verify if we can pass raw data into the queue)
		Requires Header that details what API version to use
		param for which slicer to use
		param for priority level (will default to API Key Priority)
		responds with 
		200 + id number
		401 - not authenticated
		400 - if we're missing which slicer header information (API defaults to latest released version)
		"""
			
	email = request.forms.email
	model = request.files.model
	config = request.files.config

	if email and model and config:
		result, message = sliceapi.process_slice_request(email, model, config)
		if result:
				return "Success:\t" + message
		else:
				return "Error:\t" + message
	else:
		return "You was missing some information, job was not added. %r %r %r" % (email, len(model), len(config))


@route('/slices/<slice_id:int>/', method='GET')
def serve_slice_data(slice_id=''):
	"""GET /slices/<id number>/ -> JSON from db
	200 - Return JSON"""
	if slice_id != '':
		return sliceapi.return_static_slice(request)

@route('/slices/<slice_id:int>/', method='PUT')
def write_slice_data(slice_id=''):
	"""PUT /slices/<id number>/
	With JSON that includes statistics that go into the DB for time to slice
	200 - JSON inserted into DB
	400 - If JSON poorly formed
	5** - If we run into a server error"""
	if slice_id != '':
		return sliceapi.write_slice_data(request, slice_id)

@route('/slices/<slice_id:int>/config', method='GET')
def serve_config_by_slice_id(slice_id=''):
	"""GET /slices/<id number>/config -> config for job"""
	if slice_id != '':
		return	sliceapi.serve_config_by_slice_id(request, slice_id) 

#POST|PUT /slices/<id number>/config
#	405 - Method not allowed

@route('/slices/<slice_id:int>/gcode/', method='GET')
def serve_gcode_by_slice_id(slice_id=''):
	"""GET /slices/<id number>/gcode -> Serve file"""
	if slice_id != '':
		return	sliceapi.serve_gcode_by_slice_id(request, slice_id) 

@route('/slices/<slice_id:int>/gcode/', method='PUT')
def write_gcode_by_slice_id(slice_id=''):
	"""PUT /slices/<id_number>/gcode
	Posts the created Gcode to be written
	200 - Gcode was written
	401 - Not authenticated
	5*** - We ran into a server error
	"""
	if slice_id != '':
		return	sliceapi.write_gcode_by_slice_id(request, slice_id) 

@route('/slices/<slice_id:int>/stls/', method='GET')
def serve_stls_by_slice_id(slice_id=''):
	"""	
	GET /slices/<id number/stls/ -> returns zip of all STLs for job
	"""
	if slice_id != '':
		return	sliceapi.serve_stls_by_slice_id(request, slice_id) 

#POST|PUT /slices/<id number>/stls
#	405 - Method not allowed

@route('/slices/<slice_id:int>/state/', method='GET')
def serve_state_by_slice_id(slice_id=''):
	"""
	GET /slices/<id number>/state
	200 - JSON current state | XML current state"""	
	if slice_id != '':
		return	sliceapi.serve_state_by_slice_id(request, slice_id) 


@route('/slices/<slice_id:int>/state/', method='PUT')
def write_state_by_slice_id(slice_id=''):
	"""
		PUT /slices/<id number>/state
	200 - Entry into the DB was successful
	"""
	if slice_id != '':
		return	sliceapi.write_state_by_slice_id(request, slice_id) 

run(host='0.0.0.0', port=8080, debug=True)



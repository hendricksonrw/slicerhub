#!/usr/bin/python
import os
from  bottle import run, route, static_file, request

@route('/')
def serve_index():
	return static_file('index.html', os.getcwd())

@route('/slices', method='POST')
def slice_model():
	from slicebase import SliceBase
	
	email = request.forms.email
	model = request.files.model
	config = request.files.config

	if email and model and config:
		result, message = SliceBase.process_slice_request(email, model, config)
		if result:
				return "Success:\t" + message
		else:
				return "Error:\t" + message
	else:
		return "You was missing some information, job was not added. %r %r %r" % (email, len(model), len(config))


@route('/slices/<slice_id:int>/', method='GET')
def serve_slice_page(slice_id=''):
	"""If successful returns 200 with JSON representation of a slice job
	"""
	if slice_id != '':
		return SliceBase.return_static_slice(request)

@route('/slices/<slice_id:int>/config', method='GET')
def 

@route('/slices/<slice_id:int>/gcode/', method='GET')
def serve_gcode_by_slice_id(slice_id=''):
	if slice_id != '':
			return static_file()

"""
Start jobs
POST /slices
Writes stl and config into /id_number/ folder
Adds a task to the task queue to process the given ID (verify if we can pass raw data into the queue)
Requires Header that details what API version to use
param for which slicer to use
param for priority level (will default to API Key Priority)
responds with 
200 + id number
401 - not authenticated
400 - if we’re missing which slicer header information (API defaults to latest rev)

Process job 
GET /slices/<id number>/ -> JSON from db
	200 - Return JSON
	404 - ID didn’t exist in DB
	401 - Not authenticated
PUT /slices/<id number>/
	With JSON that includes statistics that go into the DB for time to slice
	200 - JSON inserted into DB
	400 - If JSON poorly formed
	404 - If <id number> doesn’t exist
	401 - Not authenticated
	5** - If we run into a server error	
PUT /slices/<id_number>/gcode
	Posts the created Gcode to be written
	200 - Gcode was written
	401 - Not authenticated
	5*** - We ran into a server error
GET /slices/<id number>/gcode -> Serve file
GET /slices/<id number>/config -> config for job
POST|PUT /slices/<id number>/config
	405 - Method not allowed
GET /slices/<id number>/stls/<stl_num>/ -> stl for the job
POST|PUT /slices/<id number>/stls
	405 - Method not allowed
GET /slices/<id number/stls/ -> returns zip of all STLs for job

	Job State
	GET /slices/<id number>/state
	200 - JSON current state | XML current state
	PUT /slices/<id number>/state
	200 - Entry into the DB was successful
"""
run(host='0.0.0.0', port=8080, debug=True)



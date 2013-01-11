#!/usr/bin/python
import subprocess, re, os
from  bottle import run, route, static_file, request
from random import randrange

class SimpleSlic3r:
	def __init__(self):
		print 'slic3r created'

	def slice(self, stl_name=None, config_name=None, output_name=None):
		print 'slicing %s using config %s' % (stl_name, config_name)
		dirty = "--load %s %s" % (config_name, stl_name)
		args = ['--load', config_name, '--output-filename-format', output_name , stl_name]
		return subprocess.call(["slic3r", args[0], args[1], args[2], args[3], args[4]])

	def slice_name(self, filename):
		filename = re.sub(r'\.\w+', '', filename)
		return  repr(filename) #+ "_" + repr(randrange(200))

	def gen_slice_id(self):
		return randrange(500000)

@route('/')
def serve_index():
	return static_file('index.html', os.getcwd())

@route('/slice', method='POST')
def slice_model():
	email = request.forms.email
	model = request.files.model
	config = request.files.config

	if email and model and config:
			model_raw = model.file.read()
			config_raw = config.file.read()
			slicer = SimpleSlic3r()
			model_filename = slicer.slice_name(model.filename)
			config_filename = slicer.slice_name(config.filename)
			output_filename = model_filename.replace('\'', '') + '.gcode'

			#write data to disk
			slice_id = repr(slicer.gen_slice_id())
			if not os.path.exists(slice_id):
					    os.makedirs(slice_id)
			model_filename = os.path.join(slice_id, model.filename)
			with open(model_filename, 'w') as f:
				f.write(model_raw)
				f.close()
			
			config_filename = os.path.join(slice_id, config_filename + '.ini')
			with open(config_filename, 'w') as f:
				f.write(config_raw)
				f.close()
			
			#slice up the newly served models and return the gcode
			slicer.slice(model_filename, config_filename, output_filename)
			return static_file(output_filename, os.path.join(slice_id))
	return 'You are missing a field'

@route('/slice/<slice_id>/gcode/', method='GET')
def serve_gcode_by_slice_id(slice_id=''):
	if slice_id != '':
			return static_file()

run(host='localhost', port=8080, debug=True)

if __name__ == '__main__':
		slicer = SimpleSlic3r()
		
		#print slicer.slice('oshw.stl', 'random.ini', 'oshw0130813.stl')
		print 'slice something' + slicer.slice_name("whatever.stl") + '.stl'

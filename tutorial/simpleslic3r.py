#! /usr/bin/python
import subprocess


class SimpleSlic3r:
	def __init__(self, stl_name, config_name):
		self.stl_name = stl_name
		self.config_name = config_name

	def slice(self, stl_name=None, config_name=None):
		print 'slicing %s using config %s' % (stl_name, config_name)
		dirty = "--load %s %s" % (config_name, stl_name)
		args = ['--load', config_name, stl_name]
		return subprocess.call(["slic3r", args[0], args[1], args[2]])


if __name__ == '__main__':
		slicer = SimpleSlic3r('oshw.stl', 'random.ini')
		
		print 'slice something'
		print slicer.slice('oshw.stl', 'random.ini')

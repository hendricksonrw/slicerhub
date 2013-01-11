#!/usr/bin/python2.5
import bottle 
from bottle import route
@route('/')
def index():    
	return 'Hello World!'

if __name__ == '__main__':    
	from wsgiref.handlers import CGIHandler    
	CGIHandler().run(bottle.default_app())

#!/usr/bin/python2.5
import bottle 
from bottle import route
@route('/')
def index():    
	return 'Hello World!'

bottle.run(server=bottle.CGIServer)

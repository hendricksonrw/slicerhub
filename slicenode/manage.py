from wsgiref import simple_server
import falcon
import json
import logging

from slicenode import build_api

wsgi_app = api = build_api() 
app = application = api

if __name__ == '__main__':
	httpd = simple_server.make_server('127.0.0.1', 8080, app)
	httpd.serve_forever()

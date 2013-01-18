import logging
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname' : 'Ross'}
	return render_template('index.html', title = 'SavoryWatt', user = user)

@app.route('/hello')
def test():
	logging.info('hit hello')
	return "Hey YO!"

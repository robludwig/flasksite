from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
	print "error", e
	return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_error(e):
	print "error", e
	return render_template('500.html'), 500

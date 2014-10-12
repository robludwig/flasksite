#! /usr/bin/python
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
print "using basedir ", basedir
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class Unit(db.Model):
	__tablename__ = 'units'
	id = db.Column(db.Integer, primary_key=True)
	created = db.Column(db.Date)
	value = db.Column(db.String(1024))
	name = db.Column(db.String(256), index=True)
	votes = db.Column(db.Integer)

	def __repr__(self):
		return "entry %d %s:%s with %d votes" % (id, name, value, votes)

@app.route('/')
def index():
	return '<h1>Hello World</h1>'

if __name__ == '__main__':
	app.run(debug=True)

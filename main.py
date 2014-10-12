#! /usr/bin/python
import os
import datetime

from flask import Flask, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

basedir = os.path.abspath(os.path.dirname(__file__))
print "using basedir ", basedir
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'hellothisismykeylalalala'
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

class UnitForm(Form):
	name = StringField("What's your idea called?", validators=[Required()])
	idea = StringField("What's short description of your idea?", validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/')
def index():
	return '<h1>Hello World</h1>'

@app.route('/unit/', methods = ['GET', 'POST'])
def unit():
	form  = UnitForm()
	if form.validate_on_submit():
		unit = Unit(name=form.name.data, value = form.idea.data)
		unit.created = datetime.now()
		unit.votes = 0
		db.session.add(unit)
		return redirect(url_for('index'))
	else:
		return render_template('unit.html', form=form)
	
if __name__ == '__main__':
	app.run(debug=True)

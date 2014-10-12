#! /usr/bin/python
import os
import datetime
import random

from flask import Flask, render_template, url_for, redirect

#sqlalch
from flask.ext.sqlalchemy import SQLAlchemy

#wtf
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

#frontend
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

basedir = os.path.abspath(os.path.dirname(__file__))
print "using basedir ", basedir
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'hellothisismykeylalalala'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class Unit(db.Model):
	__tablename__ = 'units'
	id = db.Column(db.Integer, primary_key=True)
	created = db.Column(db.Date)
	value = db.Column(db.String(1024))
	name = db.Column(db.String(256), index=True)
	votes = db.Column(db.Integer)

	def __repr__(self):
		return "entry %d %s:%s with %d votes" % (self.id, self.name, self.value, self.votes)

class UnitForm(Form):
	name = StringField("What's your idea called?", validators=[Required()])
	idea = StringField("What's a short description of your idea?", validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/unit/', methods = ['GET', 'POST'])
def unit():
	form  = UnitForm()
	if form.validate_on_submit():
		unit = Unit(name=form.name.data, value = form.idea.data)
		unit.created = datetime.datetime.now()
		unit.votes = 0
		db.session.add(unit)
		return redirect(url_for('index'))
	else:
		return render_template('unit.html', form=form)

@app.route('/unit/<id>')
def getUnit(id):
	unit = Unit.query.filter_by(id=id).first()
	print "getting unit %d" % int(id)
	if not unit:
		print "unit not found"
		return redirect(url_for('index'))
	return render_template('display_unit.html',unit=unit)

@app.route('/unit/random/')
def getRandomUnit():
	unit_count = Unit.query.count()
	random_id = random.randint(1, unit_count)
	print "got random unit %d" % random_id
	unit = Unit.query.filter_by(id=random_id).first()
	return render_template('display_unit.html', unit=unit)

if __name__ == '__main__':
	app.run(debug=True)

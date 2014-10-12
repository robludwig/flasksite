import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import UnitForm
from .. import db
from ..models import Unit
import random


@main.route('/')
def index():
	return render_template('index.html')

@main.route('/unit/', methods = ['GET', 'POST'])
def unit():
	form  = UnitForm()
	if form.validate_on_submit():
		unit = Unit(name=form.name.data, value = form.idea.data)
		unit.created = datetime.datetime.now()
		unit.votes = 0
		db.session.add(unit)
		return redirect(url_for(index))
	else:
		return render_template('unit.html', form=form)

@main.route('/unit/<id>')
def getUnit(id):
	unit = Unit.query.filter_by(id=id).first()
	print "getting unit %d" % int(id)
	if not unit:
		print "unit not found"
		return redirect(url_for(index))
	return render_template('display_unit.html',unit=unit)

@main.route('/unit/random/')
def getRandomUnit():
	unit_count = Unit.query.count()
	random_id = random.randint(1, unit_count)
	print "got random unit %d" % random_id
	unit = Unit.query.filter_by(id=random_id).first()
	return render_template('display_unit.html', unit=unit)

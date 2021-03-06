import datetime
from flask import render_template, session, redirect, url_for, abort
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
		db.session.commit()
		return redirect(url_for('main.index'))
	else:
		return render_template('unit.html', form=form)

@main.route('/unit/<id>')
def get_unit(id):
	unit = Unit.query.filter_by(id=id).first()
	print "getting unit %d" % int(id)
	if not unit:
		print "unit not found"
		return redirect(url_for('main.index'))
	return render_template('display_unit.html',unit=unit)

@main.route('/unit/random/')
def random_unit():
	unit_count = Unit.query.count()
	random_id = random.randint(1, unit_count)
	print "got random unit %d" % random_id
	unit = Unit.query.filter_by(id=random_id).first()
	return render_template('display_unit.html', unit=unit)

@main.route('/unit/<id>/vote/')
def vote_up(id):
	unit = Unit.query.filter_by(id=id).first()
	print "getting unit %d" % int(id)
	if not unit:
		print "unit not found"
		abort(404)
		return
	print "current unit", unit
	unit.votes += 1
	db.session.add(unit)
	db.session.commit()
	return "unit upvoted"

@main.route('/units/')
def list_units():
	units = Unit.query.all()
	return render_template("list_units.html", units=units)

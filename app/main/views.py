from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import UnitForm
from .. import db
from ..models import Unit

@main.route('/')
def index():
	return render_template('index.html')

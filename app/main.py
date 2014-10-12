#! /usr/bin/python
import os
import datetime
import random

from flask import Flask, render_template, url_for, redirect

#sqlalch
from flask.ext.sqlalchemy import SQLAlchemy

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



if __name__ == '__main__':
	app.run(debug=True)

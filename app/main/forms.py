from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class UnitForm(Form):
	name = StringField("What's your idea called?", validators=[Required()])
	idea = StringField("What's a short description of your idea?", validators=[Required()])
	submit = SubmitField('Submit')

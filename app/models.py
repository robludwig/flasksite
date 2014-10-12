from . import db

class Unit(db.Model):
	__tablename__ = 'units'
	id = db.Column(db.Integer, primary_key=True)
	created = db.Column(db.Date)
	value = db.Column(db.String(1024))
	name = db.Column(db.String(256), index=True)
	votes = db.Column(db.Integer)

	def __repr__(self):
		return "entry %d %s:%s with %d votes" % (self.id, self.name, self.value, self.votes)

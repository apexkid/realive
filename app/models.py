from flask.ext.sqlalchemy import SQLAlchemy
from app import db
import time
import hashlib
import bson


class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	isactive = db.Column(db.Boolean(), default=0, nullable=False)
	isdeleted = db.Column(db.Boolean(), default=0, nullable=False)
	added_on = db.Column(db.DateTime(), default=db.func.current_timestamp(), nullable=False)
	modified_on = db.Column(db.DateTime(), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)


class  Campaign(Base):
	__tablename__ = 'campaign'

	city = db.Column(db.String(30), nullable=False)
	officeLocation = db.Column(db.String(100), nullable=False)
	localityPref = db.Column(db.String(100), nullable=False)
	poi = db.Column(db.String(100), nullable=False)
	livingCost = db.Column(db.Integer(), nullable=False)
	priorities = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		return '<Campaign: %r>' % self.id

	def __init__(self, city, officeLocation, localityPref, poi, livingCost, priorities):
		self.city =  city
		self.officeLocation = officeLocation
		self.localityPref = localityPref
		self.poi = poi
		self.livingCost = livingCost
		self.priorities = priorities


	def to_json(self):
		json_data = {
			'city' : self.city,
			'officeLocation' : self.officeLocation,
			'localityPref' : self.localityPref,
			'poi' : self.poi,
			'livingCost' : self.livingCost,
			'priorities' : self.priorities
		}
		return bson.dumps(json_data)

# define book structure to enforce data structure
from json import JSONEncoder
import json

class Book:
	sellers = list()
	def __init__(self, name, department, course_name, seller):
		self.sellers = list()
		self.sellers.append(seller)
		self.name = name
		self.department = department
		self.course_name = course_name

	def insert_seller(self, seller):
		self.sellers.append(seller)


class Seller:
	buy = False
	rent = False

	def __init__(self, name, link, buy_price, rent_price, location, verified):
		self.name = name
		self.link = link.lower()

		if float(buy_price) == 0.00:
			self.buy = False
		else:
			self.buy = True

		if float(rent_price) == 0.00:
			self.rent = False
		else: 
			self.rent = True
		self.buy_price = float(buy_price)
		self.rent_price = float(rent_price)
		self.location = location
		self.verified = verified

		# self.email = email

class Insert:
	def __init__(self, department, course_num, section, seller):
		self.department = department
		self.course_num = course_num
		self.section = section
		self.seller = seller.__dict__

class Verify:
	def __init__(self, email, department, course_num, section):
		self.email = email
		self.department = department
		self.course_num = course_num
		self.section = section

class InsertEncoder(JSONEncoder):
	def default(self, object):
		if isinstance(object, Insert):
			return object.__dict__
		else:
			return json.JSONEncoder.default(self, object)

class VerifyEncoder(JSONEncoder):
	def default(self, object):
		if isinstance(object, Verify):
			return object.__dict__
		else:
			return json.JSONEncoder.default(self, object)

class SellerEncoder(JSONEncoder):
	def default(self, object):
		if isinstance(object, Seller):
			return object.__dict__
		else:
			return json.JSONEncoder.default(self, object)


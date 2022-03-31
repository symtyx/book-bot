# define book structure to enforce data structure

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
		self.link = link

		if buy_price == 0.00:
			self.buy = False
		else:
			self.buy = True

		if (rent_price == 0.00):
			self.rent = False
		else: 
			self.rent = True
		self.buy_price = buy_price
		self.rent_price = rent_price
		self.location = location
		self.verified = verified

		# self.email = email


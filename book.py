# define book structure to enforce data structure

class Book:
	sellers = list()
	def __init__(self, name, department, course_name, price, seller):
		self.sellers = list()
		self.sellers.append(seller)
		self.name = name
		self.department = department
		self.course_name = course_name
		self.price = price
		# self.book_type = book_type
		# self.sellers = sellers

	def insert_seller(self, seller):
		self.sellers.append(seller)


class Seller:
	def __init__(self, name, link, buy, rent, location):
		self.name = name
		self.link = link
		self.location = location
		self.buy = buy
		self.rent = rent
		# self.email = email


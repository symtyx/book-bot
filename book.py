# define book structure to enforce data structure

class Book:
	sellers = list()
	def __init__(self, name, course, price, book_type, sellers):
		self.name = name
		self.course = course
		self.price = price
		self.type = book_type
		self.sellers = list()

	def insert_seller(self, seller):
		self.sellers.append(seller)


class Seller:
	def __init__(self, name, location, email):
		self.name = name
		self.location = location
		self.email = email


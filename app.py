from flask import Flask, render_template, request
from json import dumps, loads
from bot import client
from dotenv import load_dotenv
from threading import Thread
from functools import partial
import time
import os
import db

from book import Book, Seller
app = Flask(__name__)

@app.route('/')
def get_books():
	try:
		books = list()
		all_books = db.db.books_collection.find({}, {"_id": 0})
		for book in all_books:
			books.append(book)
		return dumps(books, indent=4, sort_keys=True)

	except Exception as e:
		return dumps({"error": str(e)})

# localhost:8000/book?course=<course>&number=<course-number>
@app.route('/book/<department>/<course_num>', methods=['GET'])
def get_book(department, course_num):
	query = {"department": department, "course": course_num}
	document = db.db.books_collection.find(query, {"_id": 0})
	
	for book in document:	
		return dumps(book)


@app.route('/book/insert')
def insert_book():
	seller = Seller("GMU Bookstore", "https://gmu.bncollege.com/course-material/course-finder", True, True, "Fairfax Campus")
	seller_dict = {"name": seller.name, "link": seller.link, "buy": seller.buy, "rent": seller.rent, "location": seller.location}
	book = Book("Introduction to Python Programming", "CS", "112", 45.50, seller_dict)

	book_dict = {
		"name": book.name, 
		"department": book.department,
		"course": book.course_name, 
		"price": book.price, 
		"sellers": book.sellers
		}

	db.db.books_collection.insert_one(book_dict)
	return f"Book name: {book.name} | Department: {book.department} | Course: {book.course_name} | Price: {book.price}"


# example: localhost:8000/book/insert/seller/Mostafa/mostaf@gmu.edu/true/false/Faifax
@app.route('/book/insert/seller/<name>/<link>/<buy>/<rent>/<location>')
def insert_seller(name, link, buy, rent, location):
	print(link)
	seller = {
			"name": name, 
			"link": link, 
			"buy": bool(buy), 
			"rent": bool(rent), 
			"location": location
			}

	# FIXME: This query should be the parameter passed into the bot command
	query = {"department": "CS", "course": "112"}
	book = db.db.books_collection.find(query)

	for doc in book:
		db.db.books_collection.update_one({"_id": doc["_id"]}, {"$push": {"sellers": seller}})
	return "Added seller to book"

if __name__ == '__main__':
	load_dotenv(".env")
	partial_run = partial(app.run, host="0.0.0.0", port=8000, debug=True, use_reloader=False)
	t = Thread(target=partial_run)
	t.start()
	bot = client.run("OTQxNDQzMzc1MDUwMTU0MDE1.YgWBdw.LeFD_15NEXvfJ80TRjmFBLnNN-k", bot=True)

	
	














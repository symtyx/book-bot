from flask import Flask
import db

from book import Book
app = Flask(__name__)

@app.route('/')
def flask_monogdb_atlas():
	book = Book("Logic and Language Models", "CS 330", 45.50, "buy", "GMU Bookstore")
	x = {"name": book.name, "course": book.course, "price": book.price, "type": book.type, "sellers": book.sellers}
	db.db.books_collection.insert_one(x)
	return f"Name: {book.name} | Course: {book.course}"

@app.route('/insert_book')
def insert_book():
	book = Book("Intro to Programming", "CS 112", 125.50, "buy", "GMU Bookstore")
	x = {"name": book.name, "course": book.course, "price": book.price, "type": book.type, "sellers": book.sellers}
	db.db.books_collection.insert_one(x)
	print(x)
	return f"Book name: {book.name} | Course: {book.course} | Price: {book.price}"

@app.route('/insert_seller')
def insert_seller():
	seller = {"name": "Patrick", "location": "Fairfax, VA", "year": "Junior"}
	query = {"course": "CS 112"}
	book = db.db.books_collection.find(query)
	
	for doc in book:
		db.db.books_collection.update_one({"_id": doc["_id"]}, {"$set": {"sellers": seller}})
	return "Added seller to book"

if __name__ == '__main__':
	app.run(port=8000)
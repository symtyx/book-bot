import json 
import requests 
from app import db

with open('book_data.json', "r") as file:
	file_data = json.load(file)
	# db.db.books_collection.insert_many(file_data)

requests.post("http://localhost:8000/book/insert-many", data=file_data)
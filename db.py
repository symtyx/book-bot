from flask import Flask
import pymongo
from pymongo import MongoClient
from app import app

CONNECTION_STRING = "mongodb+srv://cs321-project:cs321-project@cluster0.43ypd.mongodb.net/book-bot?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client["book-bot"]
books_collection = db["books"]
		
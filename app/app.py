from flask import Flask, render_template, request
from flask_mail import *
from random import *
from json import dumps, loads
from bot import client
from threading import Thread
from functools import partial
import time
import os
import db
from book import Book, Seller
import json 

app = Flask(__name__)

app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465      
app.config["MAIL_USERNAME"] = 'queuedelivery@gmail.com'  
app.config['MAIL_PASSWORD'] = 'PatPC021862?'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
mail = Mail(app)  
otp = randint(000000,999999)

# API route to return a book given department, course number, and section from Database
@app.route('/book/<department>/<course_num>/<section>', methods=['GET'])
def book(department, course_num, section):
	query = {"department": department, "course": course_num, "section": section}
	document = db.db.books_collection.find(query, {"_id": 0})
	
	for book in document:	
		return dumps(book)
	return dumps(None)


# Insert book into the database from Selenium bot
@app.route('/book/insert', methods=["POST"])
def insert_book():
	dat = loads(request.data)
	print(dat)
	# Initialize book with the GMU bookstore seller information
	# seller = Seller("GMU Bookstore", link, float(buy_price), float(rent_price), "Fairfax Campus", True)
	
	# # Initialize seller and book data with request params and seller data
	# bookstore_dict = {"name": seller.name, "link": seller.link, 
	# 				"buy": seller.buy,
	# 				"buy_price": seller.buy_price, 
	# 				"rent": seller.rent, 
	# 				"rent_price": seller.rent_price, 
	# 				"location": seller.location,
	# 				"verified": seller.verified
	# 			}
	# book = Book(name, dep, cnum, bookstore_dict)

	# # create dict struct to insert proper format into Mongo collection
	# book_dict = {
	# 	"name": book.name, 
	# 	"department": book.department,
	# 	"course": book.course_name, 
	# 	"sellers": book.sellers
	# 	}

	# Insert book into Database
	db.db.books_collection.insert_one(dat)
	return "Success!"


# example: localhost:8000/book/insert/seller/Mostafa/mostaf@gmu.edu/true/false/Faifax
# Insert a student seller into the database as unverified until they enter a valid OTP code into the web link
@app.route('/book/insert/seller/<dep>/<cnum>/<section>/<name>/<link>/<buy_price>/<rent_price>/<location>', methods=["POST"])
def insert_seller(dep, cnum, section, name, link, buy_price, rent_price, location, methods=["POST"]):
	# temporary solution to interrupted POST request due to # tag in string passed into request
	name_arg = name.split("@")
	name = name_arg[0] + "#" + name_arg[1]
	
	seller = Seller(name, link, float(buy_price), float(rent_price), location, False)
	seller_dict = {
			"name": seller.name, 
			"link": seller.link, 
			"buy": seller.buy,
			"buy_price": seller.buy_price,
			"rent": seller.rent,
			"rent_price": seller.rent_price, 
			"location": seller.location,
			"verified": seller.verified,
			}

	query = {"department": dep, "course": cnum, "section": section}
	book = db.db.books_collection.find(query)

	for doc in book:
		db.db.books_collection.update_one({"_id": doc["_id"]}, {"$push": {"sellers": seller_dict}})
	return "Added seller to book"

# Send the student an email with an OTP code
@app.route('/verify/<email>/<dep>/<cnum>/<section>', methods=["POST"])
def verify(email, dep, cnum, section):  
	send_otp = f"{otp}-{dep}-{cnum}-{section}"
	msg = Message('Verify Student Seller', sender='queuedelivery@gmail.com', recipients=[email])  
	msg.body = f"Please click on the link to verify your student seller status\n {send_otp}\nhttp://localhost:8000/" 
	mail.send(msg)  

	return "Success"

# Webpage to return email and OTP form
@app.route('/', methods=["GET"])
def load_validation():
	return render_template("email.html")

# Update the students' status to verified if they enter the correct OTP code from their email
@app.route('/validate', methods=["POST"])   
def validate():  
	user_email = request.form['email']
	user_otp = request.form['otp']  

	args = user_otp.split('-')
	# check if numbervalue is equal to otp generated
	if int(args[0]) == otp: 
		query = {"department": args[1], "course": args[2], "section": args[3]}
		book = db.db.books_collection.find(query)
		for doc in book:
			db.db.books_collection.update_one(query, {"$set": {"sellers.$[t].verified": True}}, 
												array_filters=[{"t.link": user_email}])
		return "<h3>Your seller status has been activated.</h3>"  
	return "<h3>failure, OTP does not match</h3>"

# Thread Flask App and Discord Bot to run side by side
def flask_thread(func):
    thread = Thread(target=func)
    print('Start Separate Thread From Bot')
    thread.start()

def run():
    app.run(host='0.0.0.0', port=8000, use_reloader=False)


if __name__ == '__main__':
    flask_thread(func=run)
    client.run('OTQxNDQzMzc1MDUwMTU0MDE1.YgWBdw.LeFD_15NEXvfJ80TRjmFBLnNN-k', bot=True)



	
	














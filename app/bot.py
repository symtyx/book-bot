import discord
from discord.ext import commands
import os
import requests
import json
import asyncio
from book import Seller, SellerEncoder


client = discord.Client()
# client = commands.Bot(command_prefix="!", case_insensitive=True)
def insert_seller(dep, cnum, section, seller):
	response = requests.post(f"http://localhost:8000/book/insert/seller/{dep}/{cnum}/{section}", data=SellerEncoder().encode(seller))
	return response

def verify_student(email, dep, cnum, section):
	if ('@gmu.edu' in email):
		response = requests.post(f"http://localhost:8000/verify/{email}/{dep}/{cnum}/{section}")
		return response

	return False

def get_book(department, cnum, section):
	response = requests.get(f"http://localhost:8000/book/{department}/{cnum}/{section}")

	if (response.status_code == 404):
		return None

	json_data = json.loads(response.text)
	return json_data

def format_embed(book, dep, num, section, message):
	if (book != None):
		if (book['name'] == ""):
			embed = discord.Embed(title=f"{dep} {num}-{section} Textbook", description=f"\nThere are no requirements for this course section\n", color=0xFFD700)
			# await message.channel.send(embed=embed)
			return embed
		
		embed = discord.Embed(title=f"{dep} {num}-{section} Textbook", description=f"\n{book['name']}\n", color=0xFFD700)
		for i in book['sellers']:
			
			if i['verified'] == True:
				prices = ""
				if i['buy']:
					options = "buy"
					prices += str(i['buy_price'])
					prices += " "
				if i['rent']:
					options += "/rent"
					prices += str(i['rent_price'])

				if i['name'] == "GMU Bookstore":
					# hyperlink the bookstore link because it's long
					embed.add_field(name=f"{i['name']}", value=f"[Bookstore link]({i['link']})\nOptions: {options}\nPrices: {prices}\nLocation: {i['location']}",inline=False)
				else:
					embed.add_field(name=f"{i['name']} ({i['link']})", value=f"Options: {options}\nPrices: {prices}\nLocation: {i['location']}",inline=False)
			else:
				continue
		embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
		embed.set_footer(text="Powered by students. This is not an official GMU service.")
		return embed 

	embed = discord.Embed(title=f"{dep} {num}-{section} Textbook", description=f"\nWe're sorry, we have no information for this course at this time.\nFeel free to check the official GMU bookstore: [Bookstore Link](https://gmu.bncollege.com/course-material/course-finder)", color=0xFFD700)
	embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
	embed.set_footer(text="Powered by students. This is not an official GMU service.")
	return embed


@client.event
async def on_message(message):
	if (message.content.startswith("!bot help")):
		embed = discord.Embed(title="Welcome to the Textbook Market", color=0xFFD700)
		
		embed.add_field(name="To SEARCH", value="!bot check <dep> <num> <section>\nExample: !bot check ACCT 203 005", inline=False)
		embed.add_field(name="To SELL", value="!bot add <dep> <num> <section> <email> <sell> <rent>\nExample: !bot add ACCT 203 005 netid@gmu.edu 49.95 5.99", inline=False)
		embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
		embed.set_footer(text="Powered by students. This is not an official GMU service.")
		await message.channel.send(embed=embed)

	if (message.content.startswith('!bot check')):
		# Set message content (parameters) to uppercase
		args = message.content.upper().split()
		book = get_book(args[2], args[3], args[4])
	
		embed = format_embed(book, args[2], args[3], args[4], message)
		
		await message.channel.send(embed=embed)

	if (message.content.startswith('!bot add')):
		args = message.content.upper().split()
		try:
			book = get_book(args[2], args[3], args[4])

			# Stringify message.author because json cannot serialize Member object
			name = f"{message.author}"
			seller = Seller(name, args[5], args[6], args[7], "Fairfax, VA", False)

			if (book == None):
				embed = format_embed(book, args[2], args[3], args[4], message)
				await message.channel.send(embed=embed)
				return

			def check(msg):
				return msg.author == message.author and 'Y' in msg.content.upper()
			
			embed = discord.Embed(title=f"Is this your book (enter Y/N)?\n\n", description=f"\n{book['name']}\n", color=0xFFD700)
			await message.channel.send(embed=embed)

			try:
				msg = await client.wait_for("message", check=check, timeout=30)
			except asyncio.TimeoutError:
				await message.channel.send("Sorry, you didn't reply in time.")

			if (msg.content):
				# parameter 3 will save the seller with their discord user handle so prospective 
				# buyers can add them on discord to exchange textbooks.
				if (verify_student(seller.link.lower(), args[2], args[3], args[4]) == False):
					await message.channel.send("We're sorry, you cannot add you because you don't have a GMU email.")
					return
				# department | course number | section | email | buy price | rent price | location | display name
				insert_seller(args[2], args[3], args[4], seller)
				await message.channel.send("Great, please check your email for verification!")
			else:
				await message.channel.send("Sorry you don't have the required textbook to sell.")
		except IndexError:
			await message.channel.send("You are missing fields, please enter '!bot help' if you don't know what to enter.")



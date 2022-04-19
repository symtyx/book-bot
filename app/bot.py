import discord
from discord.ext import commands
import os
import requests
import json
import asyncio


client = discord.Client()
# client = commands.Bot(command_prefix="!", case_insensitive=True)
def insert_seller(dep, cnum, section, link, buy_price, rent_price, location, name):
	response = requests.post(f"http://localhost:8000/book/insert/seller/{dep}/{cnum}/{section}/{name}/{link}/{buy_price}/{rent_price}/{location}")
	return response

def verify_student(email, dep, cnum, section):
	if ('@gmu.edu' in email):
		response = requests.post(f"http://localhost:8000/verify/{email}/{dep}/{cnum}/{section}")
		return response

	return "Please enter a valid email"

def get_book(department, cnum, section):
	response = requests.get(f"http://localhost:8000/book/{department}/{cnum}/{section}")
	if (response == None):
		return None

	json_data = json.loads(response.text)
	return json_data


@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
	if (message.content.startswith("!bot help")):
		msg = "To check for a course textbook enter:\n'!bot check <department> <course_num>\n\nTo add yourself as a seller enter:\n'!bot add <department> <course_num> <your_name> <gmu_email> <buy_price> <rent_price> <city>'"
		await message.channel.send(msg)

	if (message.content.startswith('!bot check')):
		args = message.content.split()
		book = get_book(args[2], args[3], args[4])

		if (book['name'] == ""):
			embed = discord.Embed(title=f"{book['department']} {book['course']} Textbook", description=f"\nThere are no course requirements for this course section\n", color=0xFFD700)
			await message.channel.send(embed=embed)
			return
		
		embed = discord.Embed(title=f"{book['department']} {book['course']} Textbook", description=f"\n{book['name']}\n", color=0xFFD700)
		for i in book['sellers']:
			
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

		
		embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
		embed.set_footer(text="Powered by students. This is not an official GMU service.")
		await message.channel.send(embed=embed)

	if (message.content.startswith('!bot add')):
		args = message.content.split()
		book = get_book(args[2], args[3], args[4])
		if (book == None):
			await message.channel.send("Course requirements not found.")
			return

		def check(msg):
			return msg.author == message.author and 'Y' in msg.content
		
		embed = discord.Embed(title=f"Is this your book (enter Y/N)?\n\n", description=f"\n{book['name']}\n", color=0xFFD700)
		await message.channel.send(embed=embed)

		try:
			msg = await client.wait_for("message", check=check, timeout=30)
		except asyncio.TimeoutError:
			await message.channel.send("Sorry, you didn't reply in time.")

		if (msg.content):
			# parameter 3 will save the seller with their discord user handle so prospective 
			# buyers can add them on discord to exchange textbooks.
			name = f"{message.author}"
			regs = name.split('#')

			# department | course number | section | email | buy price | rent price | location | display name
			insert_seller(args[2], args[3], args[4], args[5], args[6], args[7], args[8], regs[0] + "@" + regs[1])

			# email | department | course number | section
			verify_student(args[5], args[2], args[3], args[4])
			await message.channel.send("Great, please check your email for verification!")
		else:
			await message.channel.send("Sorry you can't add that.")



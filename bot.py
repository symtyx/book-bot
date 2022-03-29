import discord
from discord.ext import commands
import os
import requests
import json
from verify_email import verify_email
from termcolor import colored
from flask import render_template
import asyncio


client = discord.Client()
# client = commands.Bot(command_prefix="!", case_insensitive=True)
def insert_seller(dep, cnum, link, buy_price, rent_price, location, name):
	response = requests.post(f"http://localhost:8000/book/insert/seller/{dep}/{cnum}/{name}/{link}/{buy_price}/{rent_price}/{location}")
	return response

def verify_student(email, dep, cnum):
	if ('@gmu.edu' in email):
		response = requests.post(f"http://localhost:8000/verify/{email}/{dep}/{cnum}")
		return response

	return "Please enter a valid email"

def get_book(department, course_num):
	response = requests.get(f"http://localhost:8000/book/{department}/{course_num}")
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
		book = get_book(args[2], args[3])

		embed = discord.Embed(title=f"{book['department']} {book['course']} Textbook", description=f"\n{book['name']}\n", color=0xFFD700)
		for i in book['sellers']:
			# hyperlink the bookstore link because it's long

			if i['buy']:
				options = "buy"
			if i['rent']:
				options += "/rent"

			if i['name'] == "GMU Bookstore":
				embed.add_field(name=f"{i['name']}", value=f"[Bookstore link]({i['link']})\nOptions: {options}\nLocation: {i['location']}",inline=False)
			else:
				embed.add_field(name=f"{i['name']} ({i['link']})", value=f"Options: {options}\nLocation: {i['location']}",inline=False)

		
		embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
		embed.set_footer(text="Powered by students. This is not an official GMU service.")
		await message.channel.send(embed=embed)

	if (message.content.startswith('!bot add')):
		args = message.content.split()
		book = get_book(args[2], args[3])
		if (book == None):
			await message.channel.send("Course requirements not found.")
			return

		def check(msg):
			return msg.author == message.author and 'Y' in msg.content
		# string = "/book/insert/seller/<dep>/<cnum>/<link>/<buy>/<rent>/<location>"
		# | 2: dep | 3: cnum | 4: link | 5: buy | 6: rent | 7: location |
		# email = args[5]
		
		embed = discord.Embed(title=f"Is this your book (enter Y/N)?\n\n", description=f"\n{book['name']}\n", color=0xFFD700)
		await message.channel.send(embed=embed)

		try:
			msg = await client.wait_for("message", check=check, timeout=30)
		except asyncio.TimeoutError:
			await message.channel.send("Sorry, you didn't reply in time.")

		if (msg.content):
			# parameter 3 will save the seller with their discord user handle so prospective 
			# buyers can add them on discord to exchange textbooks.
			# print(f"Parameters:\nAuthor {message.author}\nLink: {args[4]} {args[5]} {args[6]} {args[7]}")
			name = f"{message.author}"
			regs = name.split('#')
			insert_seller(args[2], args[3], args[4], args[5], args[6], args[7], regs[0] + "@" + regs[1])
			verify_student(args[4], args[2], args[3])
			await message.channel.send("OK!")
		else:
			await message.channel.send("Sorry you can't add that.")

# @tasks.loop(seconds=60)
# async def monitor():

# 	await bot.wait_until_ready()
# 	monitorVerification()


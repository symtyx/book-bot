import discord
from discord.ext import commands
import os
import requests
import json
# from color import color
from termcolor import colored

client = discord.Client()
# client = commands.Bot(command_prefix="!", case_insensitive=True)

def get_book(department, course_num):
	response = requests.get(f"http://localhost:8000/book/{department}/{course_num}")
	json_data = json.loads(response.text)
	return json_data

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if (message.content.startswith('!bot check')):
		args = message.content.split()
		book = get_book(args[2], args[3])

		# >>> {seller_string}
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




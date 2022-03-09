import discord
from discord.ext import commands
import os
import requests
import json

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
		await message.channel.send(f"Book: \n{book}")


# bot.py
import os
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()
# Server ID: 941431243801780274 
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord!'
        )


client = CustomClient()
client.run(TOKEN)
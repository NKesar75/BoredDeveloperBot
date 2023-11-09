# bot.py
import os
from dotenv import load_dotenv, find_dotenv

import discord
from constants import DISCORD_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')




if os.environ.get('LOAD_FILE', True):
    load_dotenv(find_dotenv())

client.run(DISCORD_TOKEN)
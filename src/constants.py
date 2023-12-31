import os
from dotenv import load_dotenv, find_dotenv

if os.environ.get('LOAD_FILE', True):
    load_dotenv(find_dotenv())

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", "")
DISCORD_GUILD = os.environ.get("DISCORD_GUILD", "")
HIDDEN_ROLES = ["@everyone", "Admin", "Bot", "Bored_Developer_Bot_App"]

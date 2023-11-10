import os
from dotenv import load_dotenv, find_dotenv

if os.environ.get('LOAD_FILE', True):
    load_dotenv(find_dotenv())

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", "")

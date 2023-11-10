from constants import DISCORD_TOKEN
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

@bot.command(help="Replies with latency of the bot")
async def ping(ctx):
    await ctx.send(f'pong! - {round(bot.latency, 2)}ms')

bot.run(DISCORD_TOKEN)


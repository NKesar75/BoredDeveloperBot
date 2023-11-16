from constants import DISCORD_TOKEN, HIDDEN_ROLES
import discord
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

@bot.command(help="Replies with latency of the bot")
async def ping(ctx):
    await ctx.send(f'pong! - {round(bot.latency, 2)}ms')


@bot.command(help="detects code changes and will restart the bot if there are any code changes on the main branch")
async def restart(ctx):
    await ctx.send(f"Please Ping @Hector for him to restart server")


@bot.command(help="Add or Remove user calling command to the role, if no role is passed in passes list of roles avaiable")
async def role(ctx, role_name=None):
    allowed_roles = [role.name for role in ctx.guild.roles if role.name not in HIDDEN_ROLES]
    string_roles = "\n".join(allowed_roles)

    if role_name is None:
        await ctx.send(f"Available roles are:\n{string_roles}")
    else:
        if role_name in allowed_roles:
            member = ctx.message.author
            role = get(member.guild.roles, name=role_name)

            if member.get_role(role.id) is None:
                await member.add_roles(role)
                await ctx.send(f"You have been added to role {role.name}")
            else:
                await member.remove_roles(role)
                await ctx.send(f"You have been removed from role {role.name}")
        else:
            await ctx.send(f"{role_name} is not a valid role please use one of the following:\n{string_roles}")

bot.run(DISCORD_TOKEN)


from constants import DISCORD_TOKEN, HIDDEN_ROLES
import discord
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

@bot.command(help="Replies with latency of the bot")
async def ping(ctx):
    """
    Sends a message with the bot's latency.

    Parameters:
    - ctx (discord.ext.commands.Context): The context of the command.

    Returns:
    - None
    """
    await ctx.send(f'pong! - {round(bot.latency, 2)}ms')

@bot.command(help="Add or Remove the role to the specific user calling command, if no role is passed in passes list of roles avaiable")
async def role(ctx, role_name=None):
    """
    Adds or removes a role from the specific user calling the command. If no role name is provided, it sends a list of available roles.

    Parameters:
    - ctx (discord.ext.commands.Context): The context of the command.
    - role_name (str, optional): The name of the role to add or remove. Defaults to None.

    Returns:
    - None
    """
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


@bot.command(help="Sync all commands into the discord server this will allow discord to show matching tree of commands")
async def sync(ctx):
    """
    Syncs all the commands into the Discord server, allowing Discord to display a matching tree of commands.

    Example Usage:
    ```python
    !sync
    ```
    This command can be used in a Discord server where the bot is present. When the command is executed, it will sync all the commands into the server and display a message saying "Command tree synced."

    Parameters:
    - ctx (context): The context object representing the invocation of the command.

    Returns:
    - None

    """
    await bot.tree.sync()
    await ctx.send('Command tree synced.')

bot.run(DISCORD_TOKEN)

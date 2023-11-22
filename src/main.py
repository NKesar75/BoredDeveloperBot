import discord

from discord import app_commands
from discord.utils import get

from typing import Optional

from constants import DISCORD_TOKEN, HIDDEN_ROLES, DISCORD_GUILD

MY_GUILD = discord.Object(id=DISCORD_GUILD)


class ClientClass(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = ClientClass(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def ping(interaction: discord.Interaction):
    """Replies with the bot's latency"""
    await interaction.response.send_message(f'pong! - {round(client.latency, 2)}ms')

@client.tree.command()
@app_commands.describe(
    role_name='Adds or Removes the role for you, if no role is passed will return a list of avaiable roles.'
)
async def role(interaction: discord.Interaction, role_name: Optional[str] = None):
    """
    Adds or removes a role from the specific user calling the command. If no role name is provided, it replies with a list of available roles.
    """
    allowed_roles = [role.name for role in interaction.guild.roles if role.name not in HIDDEN_ROLES]
    string_roles = "\n".join(allowed_roles)

    if role_name is None:
        await interaction.response.send_message(f"Available roles are:\n{string_roles}")
    else:
        if role_name in allowed_roles:
            member = interaction.user
            role = get(member.guild.roles, name=role_name)

            if member.get_role(role.id) is None:
                await member.add_roles(role)
                await interaction.response.send_message(f"You have been added to role {role.name}")
            else:
                await member.remove_roles(role)
                await interaction.response.send_message(f"You have been removed from role {role.name}")
        else:
            await interaction.response.send_message(f"{role_name} is not a valid role please use one of the following:\n{string_roles}")


client.run(DISCORD_TOKEN)
from discord import app_commands, Intents, Embed
from discord.ext import commands
import os, configparser

config = configparser.ConfigParser()
config.read('config.ini')
general = config['bot']

# -------- BOT SETUP ---------
bot = commands.Bot(command_prefix=general['prefix'], intents=Intents.all())

# ------- LOADING COGS --------
@bot.event
async def setup_hook():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):

            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"Loaded Cog: {filename[:-3]}")
        else:
            print("Unable to load pycache folder.")

# --- ACTIVATES WHEN A MEMBER JOINS -----
@bot.event
async def on_member_join(member):
    join_embed = Embed()
    join_embed.add_field(name='',value=f'Новый участник {member.mention} прыгнул на сервер!')
    join_channel = bot.get_channel(1219942526925148180)
    await join_channel.send(embed=join_embed)


bot.run(general['token'])
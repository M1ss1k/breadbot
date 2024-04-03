from discord import app_commands, Intents, Embed, Interaction
import discord
from typing import Literal, Optional

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


@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")


bot.run(general['token'])
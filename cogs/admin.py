from discord import app_commands
import discord
from discord.ext import commands
import json

class Administartion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ----- BAN USER -----
    @app_commands.command(name='ban', description='Забанить пользователя')
    async def ban_user(self, interaction: discord.Interaction, member: discord.Member , reason: str):
        ban_embed = discord.Embed(title='БАН')
        ban_embed.add_field(name='', value=f'Пользователь {member.name} был забанен на этом сервер по причине {reason}')
        await member.ban(reason=reason)
        return await interaction.response.send_message(embed=ban_embed)
    # ----- UNBAN USER -----
    @app_commands.command(name='unban', description='Разбанить игрока')
    async def unban_user(self, interaction: discord.Interaction, member: discord.Member):
        unban_embed = discord.Embed(title='РАЗБАН ИГРОКА')
        unban_embed.add_field(name='', value=f'Пользователь {member.name} был разбанен.')
        await member.unban()
        return await interaction.response.send_message(embed=unban_embed)
    
    # ----- KICK USER -----
    @app_commands.command(name='kick', description='Выгнать участника')
    async def kick_player(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        kick_embed = discord.Embed(title='ВЫГОНЕНИЕ')
        kick_embed.add_field(name='', value=f'Пользователя {member.name} выгнали.')
        await member.kick(reason=reason)
        return await interaction.response.send_message(embed=kick_embed)
    
    # # ----- WARN USER -----
    # @app_commands.command(name='warn', description='Выдать предупреждение')
    # async def warn_player(self, interaction: discord.Interaction, member: discord.Member, reason: str):
    #     warn_embed = discord.Embed(title='ПРЕДУПРЕЖДЕНИЕ')
    #     warn_embed.add_field(name='', value=f'Пользователь {member.name} получает предупреждение по причине: {reason}.')
    #     with open('warns.json', 'r+') as file:
    #         jsonf = json.load(file.read())]
    #         if [member.id] == 0:
    #             users.

    

async def setup(client):
    await client.add_cog(Administartion(client))



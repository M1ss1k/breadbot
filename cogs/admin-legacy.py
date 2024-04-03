from discord import app_commands
import discord
from discord.ext import commands
import json, sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


class AdministartionLegacy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ----- BAN USER -----
    @commands.command(name='ban', description='Забанить пользователя')
    async def ban_user(self, ctx, member: discord.Member , reason: str):
        ban_embed = discord.Embed(title='БАН')
        ban_embed.add_field(name='', value=f'Пользователь {member.name} был забанен на этом сервер по причине {reason}')
        await member.ban(reason=reason)
        return await ctx.send(embed=ban_embed)
    # ----- UNBAN USER -----
    @commands.command(name='unban', description='Разбанить игрока')
    async def unban_user(self, ctx, member: discord.Member):
        unban_embed = discord.Embed(title='РАЗБАН ИГРОКА')
        unban_embed.add_field(name='', value=f'Пользователь {member.name} был разбанен.')
        await member.unban()
        return await ctx.send(embed=unban_embed)
    
    # ----- KICK USER -----
    @commands.command(name='kick', description='Выгнать участника')
    async def kick_player(self, ctx, member: discord.Member, reason: str):
        kick_embed = discord.Embed(title='ВЫГОНЕНИЕ')
        kick_embed.add_field(name='', value=f'Пользователя {member.name} выгнали.')
        await member.kick(reason=reason)
        return await ctx.send(embed=kick_embed)
    
    # ----- WARN USER -----
    @commands.command(name='warn', description='Выдать предупреждение')
    async def warn_player(self, ctx, member: discord.Member, reason: str):
        warn_embed = discord.Embed(title='ПРЕДУПРЕЖДЕНИЕ')
        warn_embed.add_field(name='', value=f'Пользователь {member.name} получает предупреждение по причине: {reason}.')
        cursor.execute(f"INSERT INTO warnings (id, reason) VALUES {(member.id, reason)}")
        connection.commit()
        return await ctx.send(embed=warn_embed)
    
 
    @commands.command(name='warnings')
    async def player_warnings(self, ctx, member: discord.Member):
        warnings_embed = discord.Embed(title='ПРЕДУПРЕЖДЕНИЯ УЧАСТНИКА')
        warnings_embed.add_field(name='', value=f'Участник {member.mention} получил следующие предупреждения:')
        cursor.execute(f"SELECT FROM warnings WHERE id={member.id}")
        cursor.fetchone()
        

    

async def setup(client):
    await client.add_cog(AdministartionLegacy(client))



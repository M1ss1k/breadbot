from discord import app_commands
from discord.ext import commands


class Administartion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name='ban', description='Забанить пользователя')
    async def ban_user(self, member: Member , reason: str, interaction: Interaction):
        ban_embed = Embed(title='БАН')
        ban_embed.add_field(name='', value=f'Пользователь {member.name} был забанен на этом сервер по причине {reason}')
        await member.ban(reason=reason)
        await interaction.response(embed=ban_embed)
        return None



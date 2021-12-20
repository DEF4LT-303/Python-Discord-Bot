import discord
from discord.ext import commands
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions

@commands.command(ctx="Unmute")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   await member.send(f" You are unmuted from the server'{ctx.guild.name}'")
   await member.remove_roles(mutedRole)
   embed = discord.Embed(title="Unmuted", ctx=f" unmuted-{member.mention}",colour=discord.Colour.green())
   await ctx.send(embed=embed)
   


@commands.command(ctx="Mute")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    embed = discord.Embed(title="Stop Talking", ctx=f"{member.mention} was muted ", colour=discord.Colour.red())
    embed.add_field(name="Reason", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" You are muted from the server '{guild.name}' for {reason}")

def setup(client):
  client.add_command(mute)
  client.add_command(unmute)
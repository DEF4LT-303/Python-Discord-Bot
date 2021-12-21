import discord
from discord.ext import commands
import os
from main import *


async def remove_money(users, user, channel, amount):

  try: 
    if users[f'{user.id}']['money'] < 1000:
      await channel.send('You dont have enough **potatoes!**')
      return False

    # elif not f'{user.id}' in users:
    #   await channel.send('You dont have enough **potatoes!**')
    #   return False
    
    else:
      users[f'{user.id}']['money'] -= amount
      await channel.send(f'***Used*** `{amount}` 🥔')
      return True
  
  except KeyError:
      await channel.send('You dont have enough **potatoes!**')
      return False

@commands.command()
async def img(ctx, *,arg):

  with open('./cogs/Data/economy.json', 'r') as f:
      users = json.load(f)

  user = ctx.author
  channel = ctx.channel
  check = await remove_money(users, user, channel, 5000)
  
  if check is True:
    if ctx.guild.id == 736748152962547802:
      z=str(arg)
      await ctx.channel.send(file=discord.File(f'./cogs/Image/{z}.PNG'))

  with open('./cogs/Data/economy.json', 'w') as f:
      json.dump(users, f, indent=4)

def setup(client):
  # Every extension should have this function
  client.add_command(img)

import discord
from discord.ext import commands
import os
from main import *


async def remove_money(users, user, channel, amount):

  try: 
    if users[f'{user.id}']['money'] < amount:
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

  files = []
  for filename in os.listdir('./cogs/Image'):
      if filename.endswith('PNG'):

        files.append(filename[:-4])

  user = ctx.author
  channel = ctx.channel
    

  if arg in files:

    if arg=="list" and ctx.guild.id == 736748152962547802:
      msg = await ctx.channel.send(file=discord.File(f'./cogs/Image/{arg}.PNG'))
    else:
      if ctx.guild.id == 736748152962547802:
        check = await remove_money(users, user, channel, 10000)
        
        if check is True:
          
          z=str(arg)
          msg = await ctx.channel.send(file=discord.File(f'./cogs/Image/{z}.PNG'))
            

          await asyncio.sleep(15)
          await msg.delete()

  with open('./cogs/Data/economy.json', 'w') as f:
      json.dump(users, f, indent=4)

def setup(client):
  # Every extension should have this function
  client.add_command(img)

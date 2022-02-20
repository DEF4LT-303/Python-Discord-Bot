import discord
from discord.ext import commands
import os
from main import *
import random

async def add_money(users, user, channel, amount):
    users[f'{user.id}']['money'] += amount
    await channel.send(f'*Congratulation! You have been credited* `{amount}` 🥔')

async def remove_money(users, user, channel, amount):

  try: 
      if users[f'{user.id}']['money'] < amount:
        await channel.send('You dont have enough **potatoes!**')
        return False
      
      else:
        users[f'{user.id}']['money'] -= amount
        await channel.send(f'***Used*** `{amount}` 🥔')
        return True
    
  except KeyError:
      await channel.send('You dont have enough **potatoes!**')
      return False


@commands.command(name='meme', aliases=['memes'])
async def memes(ctx):

  with open('./cogs/Data/economy.json', 'r') as f:
    users = json.load(f)
  user = ctx.author
  channel = ctx.channel

  a = random.randint(0,31)
  if(a==0):
    await add_money(users, user, channel, 1000)

  else:
    check = await remove_money(users, user, channel, 500)

    if check is True:
      await ctx.channel.send(file=discord.File(f'./cogs/Memes/{a}.PNG'))
  
  with open('./cogs/Data/economy.json', 'w') as f:
    json.dump(users, f, indent=4)
  
  
def setup(client):
  # Every extension should have this function
  client.add_command(memes)


      
import discord
from discord.ext import commands
import os
from main import *
import asyncio
import random

@commands.command(name='genshin', aliases=['genshin impact', 'gi'])
async def genshin(ctx, *,arg=''):
  
  if(arg==''):
    await ctx.channel.send(file=discord.File(f'./cogs/Genshin/dongli.jpg'))
    
  else:
    z=str(arg)
    z=z.lower()
    # try:
      #texts for embed
    with open('./cogs/GenshinDATA/genshinimpact.txt', 'r') as f:
      counter = f.readline()
    text=''
    whereword=0
    countersplit=counter.split(' ')
    colour=[]
    kalar=''
    for i in range(0,len(countersplit)):
      if(countersplit[i]==z):
        whereword=int(i)
    kalar=countersplit[whereword+1]
    kalar=int(str(kalar),16)
    colour.append(kalar)
    
      
    for i in range(whereword+2,len(countersplit)):
      if(countersplit[i]=='/n\n'):
        break
      elif(countersplit[i]=='❀'):
        text= text+'\n'+countersplit[i]
      else:
        text=text+' '+countersplit[i]
      
    #embed-1
    embed = discord.Embed(title="Genshin Impact", description=arg.upper(), color=random.choice(colour)) 
    file = discord.File(f'./cogs/Genshin/{z}Banner.png', filename="image.png")
    embed.set_image(url="attachment://image.png")
    msg = ctx.send(file=file, embed=embed)
    await msg

    #embed-2
    embed= discord.Embed(title=arg.upper(), description=text, color=random.choice(colour))
    file = discord.File(f'./cogs/Genshin/{z}AS.jpg', filename="image.jpg")
    embed.set_image(url="attachment://image.jpg")
    msg = ctx.send(file=file, embed=embed)
    await msg
    # except:
    #   await ctx.channel.send(file=discord.File(f'./cogs/Genshin/notfound.gif'))
    
                   
def setup(client):
  # Every extension should have this function
  client.add_command(genshin)
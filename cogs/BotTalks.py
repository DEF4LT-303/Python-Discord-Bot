import discord
from discord.ext import commands
from main import *

class Greetings(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def simplifier(self, message):
    message.content=message.content.lower()
    signs=["''",".",","," ","?","՜","!","#","%","^","&","*","(",")","-"]
    for i in range(0,len(signs)):
      x=signs[i]
      message.content=message.content.replace(x,"")
    return message
      

  #------------------------------------------------------------------------------#
  @commands.Cog.listener()
  async def on_message(self, message):
    # await client.process_commands(message) # TO run client command
    
    await self.simplifier(message)

    if message.author == client.user:
      return

    #Hello
    greetings=["hello","hola","konichiwa","konnichiwa","ciao","hi","bonjour","ola","nihao","pershendetje","hayi","ahlan","voghju՜yn","salam","kaixo","pryvitannie","zdraveĭ","maingalarpar","Salute","privet","hey","namaste"]
    for i in range(0,len(greetings)):
      if message.content.startswith(f'{prefix}'+greetings[i]):
        await message.channel.send('Hello')
    

    #Bye
    farewells=["bye","adios","adiós","sayonara","ciao","addio","zaijian","avvedeci"]
    for i in range(0,len(farewells)):
      if message.content.startswith(f'{prefix}'+farewells[i]):
        await message.channel.send('Bye')


    if message.content.startswith(f'{prefix}'+"cyka"):
      await message.channel.send('Blyat')
    if message.content.startswith(f'{prefix}'+"blyat"):
      await message.channel.send('Cyka')
  #----------------------------------------------------------------------------------#
def setup(client):
    # Every extension should have this function
    client.add_cog(Greetings(client))
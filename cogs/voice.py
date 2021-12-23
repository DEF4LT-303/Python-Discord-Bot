import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import os
from main import *

class Voice(commands.Cog):

  def __init__(self, client):

    self.client = client

  async def remove_money(self, users, user, channel, amount):

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

  
  @commands.command(aliases=['vc'])
  async def voice(self, ctx, msg, channel: discord.VoiceChannel=None):

    with open('./cogs/Data/economy.json', 'r') as f:
      users = json.load(f)
    # Store all mp3 file names
    files = []
    for filename in os.listdir('./cogs/Voices'):
      if filename.endswith('mp3'):

        files.append(filename[:-4])
    
    if not channel:
      try:
          channel = ctx.author.voice.channel
      except AttributeError:
          raise InvalidVoiceChannel('No channel to join. Please either specify a valid channel or join one.')

    user = ctx.author
    channel = ctx.channel    

    servers = ['894632180821663835', '736748152962547802', '498919143337361422'] # server IDs
    if str(ctx.guild.id) in servers:
     
      if msg in files:
        check = await self.remove_money(users, user, channel, 1000)
        if check is True:

          channel = ctx.message.author.voice.channel
          voice = await channel.connect()
          

          source = FFmpegPCMAudio(f'./cogs/Voices/{msg}.mp3')
          await ctx.message.add_reaction('▶')
          
          player = voice.play(source)
          
          # DC after done
          while voice.is_playing(): #Checks if voice is playing
            await asyncio.sleep(1) #While it's playing it sleeps for 1 second

          else:
            await asyncio.sleep(1) #If it's not playing it waits 1 seconds
            while voice.is_playing(): #and checks once again if the bot is not playing
                break #if it's playing it breaks
              
        else:
            await voice.disconnect() #if not it disconnects
        
    else:
      await ctx.send('Not valid for this **Server**')

    with open('./cogs/Data/economy.json', 'w') as f:
      json.dump(users, f, indent=4)


def setup(client):

  client.add_cog(Voice(client))
import discord
from discord.ext import commands
import requests
import json
import asyncio
from main import client




class UrbanDictionary(commands.Cog):

  emojis = ['⬅️', '➡️']
  ud_index = 0
  term = None

  def __init__(self, client):
    self.client = client



  @commands.command(aliases=['ud'])
  async def urbandictionary(self, ctx, *, arg=None):

    UrbanDictionary.ud_index = 0

    if arg == None:
      
      embedVar = discord.Embed(title='Urban Dictionary', description=':warning: Please provide an argument', color=0xba0001)

      await ctx.channel.send(embed=embedVar)
    
    else:
      
      UrbanDictionary.term = arg

      url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

      querystring = {"term":UrbanDictionary.term}

      headers = {
          'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
          'x-rapidapi-key': "ca2d4917cdmsh8a43388ab8c5278p1e2e89jsn87def1dcf18e"
          }

      response = requests.request("GET", url, headers=headers, params=querystring)

      json_data = json.loads(response.text)  

      if len(json_data['list']) == 0:
          embedVar = discord.Embed(title='Urban Dictionary', description=':warning: No result found', color=0xba0001)
          await ctx.channel.send(embed=embedVar)

      else:

  
        ud_definition = json_data['list'][0]['definition']
        ud_example = json_data['list'][0]['example']
        ud_thumbs_up = json_data['list'][0]['thumbs_up']

        embedVar = discord.Embed(title='Urban Dictionary', description=ud_definition, color=0xffff00)
        embedVar.add_field(name="Example", value=ud_example, inline=False)
        embedVar.set_footer(text = f'\U0001F44D {ud_thumbs_up}')

        message = await ctx.channel.send(embed=embedVar)

    
    for emoji in UrbanDictionary.emojis:
      await message.add_reaction(emoji)


  @commands.Cog.listener()
  async def on_reaction_add(self, reaction, user):


    if user != client.user:

      def check(reaction, user):
            return  str(reaction.emoji) == '➡️' and str(reaction.emoji) == '⬅️'

      if str(reaction.emoji) == "➡️":
        UrbanDictionary.ud_index += 1
        

        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

        querystring = {"term":UrbanDictionary.term}

        headers = {
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
            'x-rapidapi-key': "ca2d4917cdmsh8a43388ab8c5278p1e2e89jsn87def1dcf18e"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        json_data = json.loads(response.text)

        if len(json_data['list']) == 0:
          embedVar = discord.Embed(title='Urban Dictionary', description=':warning: No result found', color=0xba0001)
          await reaction.channel.send(embed=embedVar)

        else:
          ud_definition = json_data['list'][UrbanDictionary.ud_index]['definition']
          ud_example = json_data['list'][UrbanDictionary.ud_index]['example']
          ud_thumbs_up = json_data['list'][UrbanDictionary.ud_index]['thumbs_up']

          embedVar = discord.Embed(title='Urban Dictionary', description=ud_definition, color=0xffff00)
          embedVar.add_field(name="Example", value=ud_example, inline=False)
          embedVar.set_footer(text = f'\U0001F44D {ud_thumbs_up}')

          await reaction.message.edit(embed=embedVar)
      
      if str(reaction.emoji) == "⬅️":
        UrbanDictionary.ud_index -= 1
        

        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

        querystring = {"term":UrbanDictionary.term}

        headers = {
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
            'x-rapidapi-key': "ca2d4917cdmsh8a43388ab8c5278p1e2e89jsn87def1dcf18e"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        json_data = json.loads(response.text)  

        if len(json_data['list']) == 0:
          embedVar = discord.Embed(title='Urban Dictionary', description=':warning: No result found', color=0xba0001)
          await reaction.channel.send(embed=embedVar)

        else:
          ud_definition = json_data['list'][UrbanDictionary.ud_index]['definition']
          ud_example = json_data['list'][UrbanDictionary.ud_index]['example']
          ud_thumbs_up = json_data['list'][UrbanDictionary.ud_index]['thumbs_up']

          embedVar = discord.Embed(title='Urban Dictionary', description=ud_definition, color=0xffff00)
          embedVar.add_field(name="Example", value=ud_example, inline=False)
          embedVar.set_footer(text = f'\U0001F44D {ud_thumbs_up}')

          await reaction.message.edit(embed=embedVar)

      if reaction.message.content.startswith('$$'):
        await reaction.message.clear_reactions()

      try:
        reaction.message = await self.client.wait_for('reaction_add', timeout=10.0, check=check)

      except asyncio.TimeoutError:
          await reaction.message.clear_reactions()
          return


def setup(client):
    # Every extension should have this function
    client.add_cog(UrbanDictionary(client))
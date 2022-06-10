import discord
from discord.ext import commands
import requests
import json
import asyncio
from discord.ui import Button, View
from main import client


class View(discord.ui.View):
    def __init__(self, timeout):
        super().__init__(timeout=timeout)
        self.response = None 

    async def on_timeout(self) -> None:
        for child in self.children: 
            child.disabled = True   

        await self.response.edit(view=self)

class UrbanDictionary(commands.Cog):

  def __init__(self, client):
    self.client = client


  @commands.command(aliases=['ud'])
  async def urbandictionary(self, ctx, *, arg=None):

    ud_index = 0

    if arg == None:
      
      embedVar = discord.Embed(title='Urban Dictionary', description=':warning: Please provide an argument', color=0xba0001)

      await ctx.channel.send(embed=embedVar)
    
    else:
      

      url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

      querystring = {"term":arg}

      headers = {
          'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
          'x-rapidapi-key': "ca2d4917cdmsh8a43388ab8c5278p1e2e89jsn87def1dcf18e"
          }

      response = requests.request("GET", url, headers=headers, params=querystring)

      json_data = json.loads(response.text)  

      if len(json_data['list']) == 0:
          embedVar = discord.Embed(title='Urban Dictionary', description=':warning: No results found', color=0xba0001)
          await ctx.channel.send(embed=embedVar)

      else:
        

        button1 = Button(style=discord.ButtonStyle.blurple, emoji='⬅')
        button2 = Button(style=discord.ButtonStyle.blurple, emoji='➡')

        view = View(timeout=60)
        view.add_item(button1)
        view.add_item(button2)
        
        

  
        ud_definition = json_data['list'][0]['definition']
        ud_example = json_data['list'][0]['example']
        ud_thumbs_up = json_data['list'][0]['thumbs_up']

        embedVar = discord.Embed(title=f'Urban Dictionary: {arg}', description=ud_definition, color=0xffff00)
        embedVar.add_field(name="Example", value=ud_example, inline=False)
        embedVar.set_footer(text = f'\U0001F44D {ud_thumbs_up}')

        message = await ctx.send(embed=embedVar, view=view)

        view.response = message

      
      async def button_callback1(interaction):
        nonlocal ud_index
        ud_index += 1
        
        ud_definition = json_data['list'][ud_index]['definition']
        ud_example = json_data['list'][ud_index]['example']
        ud_thumbs_up = json_data['list'][ud_index]['thumbs_up']

        embedVar = discord.Embed(title=f'Urban Dictionary: {arg}', description=ud_definition, color=0xffff00)
        embedVar.add_field(name="Example", value=ud_example, inline=False)
        embedVar.set_footer(text = f'\U0001F44D {ud_thumbs_up}')

        msg = await message.edit(embed=embedVar)

      async def button_callback2(interaction):
        nonlocal ud_index
        ud_index -= 1
        
        ud_definition = json_data['list'][ud_index]['definition']
        ud_example = json_data['list'][ud_index]['example']
        ud_thumbs_up = json_data['list'][ud_index]['thumbs_up']

        embedVar = discord.Embed(title=f'Urban Dictionary: {arg}', description=ud_definition, color=0xffff00)
        embedVar.add_field(name="Example", value=ud_example, inline=False)
        embedVar.set_footer(text = f'\U0001F44D {ud_thumbs_up}')

        msg = await message.edit(embed=embedVar)

        

      button1.callback = button_callback1
      button2.callback = button_callback2

      

      


def setup(client):
    # Every extension should have this function
    client.add_cog(UrbanDictionary(client))
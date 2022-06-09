from main import *
import discord
from discord.ext import commands
import json


class imgstore(commands.Cog):

  def __init__(self, client):
    self.client = client


  @commands.command(aliases=['store'])
  async def img_store(self, ctx):

    with open('./cogs/Image/image_store.json', 'r') as f:
      image_db = json.load(f)

    if len(ctx.message.attachments) == 0:
      await ctx.send('Please upload an **image**')
      return
      
    name=ctx.message.content.split(' ')

    #name[1]==name of the photo
    string = ctx.message.attachments[0]
    if name[1] in image_db.keys():
      await ctx.send('Name already in use')
      
    else:
      image_db[f'{name[1]}'] = f'{string}'

    #--------------json close----------------------------  
    with open('./cogs/Image/image_store.json', 'w') as f:
      json.dump(image_db, f, indent=4)

      
  @commands.command(aliases=['send'])
  async def img_send(self, ctx):
    
      with open('./cogs/Image/image_store.json', 'r') as f:
        image_db = json.load(f)

      name=ctx.message.content.split(' ')
    
      if name[1] in image_db.keys():
        await ctx.send(image_db[name[1]])
        
      if not name[1] in image_db.keys():
        await ctx.send(f'**{name[1]}** not Found')
        await ctx.send("Try storing an image")
    
      with open('./cogs/Image/image_store.json', 'w') as f:
        json.dump(image_db, f, indent=4)


  @commands.command(aliases=['del'])
  async def img_delete(self, ctx):

    with open('./cogs/Image/image_store.json', 'r') as f:
      image_db = json.load(f)

    if ctx.author.id == 305681776427139073 or ctx.author.id == 335808768979894283 or ctx.author.id == 560497173570256927:

      name=ctx.message.content.split(' ')

      if name[1] not in image_db:
        await ctx.send('**No image by that name**')

      else:
        del image_db[f'{name[1]}']
        await ctx.send(f'Image **{name[1]}** has been removed')

    with open('./cogs/Image/image_store.json', 'w') as f:
      json.dump(image_db, f, indent=4)
    

def setup(client):
  # Every extension should have this function
  client.add_cog(imgstore(client))
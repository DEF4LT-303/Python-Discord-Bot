from main import *
import discord
from discord.ext import commands
import math


class Calculator(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def cal(self, ctx,*, arg=None):
    number=str(arg)
    number=number.replace('^','**')
    for i in range(len(number)):
      total=eval(number)
    await ctx.send(total)

  @commands.command()
  async def round(self, ctx,*, arg=None):
    z=str(arg)
    z=z.split(',')
    res= round(float(z[0]),int(z[1]))
    await ctx.send(res)

  

    

def setup(client):
  # Every extension should have this function
  client.add_cog(Calculator(client))
from main import *
import discord
from discord.ext import commands
import random


class Calculator(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def cal(self, ctx,*, arg=None):

    z=str(arg)
    z=z.replace(' ','')
    total=int(z[0])


    for i in range(len(z)):
      if(z[i]=="+"):
        y=int(z[i+1])
        total =total+y

      elif(z[i]=="-"):
        y=int(z[i+1])
        total =total-y

    await ctx.send(total)

def setup(client):
  # Every extension should have this function
  client.add_cog(Calculator(client))
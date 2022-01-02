import discord
from discord.ext import commands
import random


@commands.command()
async def ppsize(ctx, arg=None):

  size='='
  if(arg==None):
    #RYANSHAYANTOSHAKIRA
    if(ctx.author.id == 305681776427139073 or ctx.author.id == 335808768979894283):
      owners_size=random.randint(10,20)
      pp = '8' + size*owners_size + 'D'

      embedVar = discord.Embed(title='PP Check', description=f'{ctx.author.name}\'s pp \n{pp}', color=0xFFBBAC)
      
      await ctx.channel.send(embed=embedVar)

    # Target case commented out, DO NOT DELETE

    # #havocsaki
    # elif(ctx.author.id == 557646464831193088 or ctx.author.id == 508887278068957186):
    #   cock_size=random.randint(0,9)
    #   pp = '8' + size*cock_size + 'D'

    #   embedVar = discord.Embed(title='PP Check', description=f'{ctx.author.name}\'s pp \n{pp}', color=0xFFBBAC)
      
    #   await ctx.channel.send(embed=embedVar)
    
    # #miraz
    # elif(ctx.author.id == 233934996015022080):
    #   mirag_size=random.randint(20,23)
    #   pp = '8' + size*mirag_size + 'D'

    #   embedVar = discord.Embed(title='PP Check', description=f'{ctx.author.name}\'s pp \n{pp}', color=0xFFBBAC)
      
    #   await ctx.channel.send(embed=embedVar)

    # #samin
    # elif(ctx.author.id == 399972625583177738):
    #   pp = "8D"

    #   embedVar = discord.Embed(title='PP Check', description=f'{ctx.author.name}\'s pp \n{pp}', color=0xFFBBAC)
      
    #   await ctx.channel.send(embed=embedVar)

    #shakira
    elif( ctx.author.id == 560497173570256927):
      pp = "Ayo no pp bruh"
      
      embedVar = discord.Embed(title='PP Check', description=f'{ctx.author.name}\'s pp \n{pp}', color=0xFFBBAC)
      
      await ctx.channel.send(embed=embedVar)
    
    else:
      normalsize=random.randint(0,10)
      pp = '8'+size*normalsize+'D'

      embedVar = discord.Embed(title='PP Check', description=f'{ctx.author.name}\'s pp \n{pp}', color=0xFFBBAC)
      
      await ctx.channel.send(embed=embedVar)
  
  else:

    if(arg=="<@!335808768979894283>"or arg=="<@!305681776427139073>"):
      owners_size=random.randint(14,20)
      pp = '8' + size*owners_size + 'D'

      embedVar = discord.Embed(title='PP Check', description=f'{arg}\'s pp \n{pp}', color=0xFFBBAC)
      
      await ctx.channel.send(embed=embedVar)


    #target case commented out, DO NO DELETE
    
    # #havoc saki
    # elif(arg=="<@!508887278068957186>" or arg=="<@!557646464831193088>"):
    #   owners_size=random.randint(0,11)
    #   pp = '8' + size*owners_size + 'D'
    #   embedVar = discord.Embed(title='PP Check', description=f'{arg}\'s pp \n{pp}', color=0xffdbac)
    #   await ctx.channel.send(embed=embedVar)
    
    #Shakira
    elif(arg=='<@!560497173570256927>'):

      embedVar = discord.Embed(title='PP Check', description=f'She is a girl. If she had one, It would be bigger than yours', color=0xFFBBAC)
      await ctx.channel.send(embed=embedVar)

    else:
      normalsize=random.randint(0,10)
      pp = '8'+size*normalsize+'D'

      embedVar = discord.Embed(title='PP Check', description=f'{arg}\'s pp \n{pp}', color=0xFFBBAC)
      
      await ctx.channel.send(embed=embedVar)

def setup(client):
  # Every extension should have this function
  client.add_command(ppsize)
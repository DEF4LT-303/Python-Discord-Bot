import discord
from discord.ext import commands
from main import *
import random
import asyncio

@commands.command()
async def giveaway(ctx,*,message=''):


  names=['<@228537642583588864>','<@894627029717237800>']
  if(message.startswith('start')):
    
    message=message.replace('start','')
    new=[]
    
    message=message.replace('add','')
    names=message.split(',')

    temp=[]
    temp=names
    number=1
    counter=True

    for i in range(len(temp)):
      
      part = ''
      for i in range(len(names)):
        part += names[i] + ' '

      if(counter==True):
        part1 = f'**Participants**  {part}'
  
      else:
        part1 = f'**Participants left**  {part}'
      
      if(len(temp)>=2):  
        random_numberEliminator=random.randint(0,len(temp)-1)
        
        eliminated = temp[random_numberEliminator]
        temp.remove(temp[random_numberEliminator])

      if counter==False:
        await asyncio.sleep(6)

      partAv=''
      for i in range(len(names)):
        partAv += f'\n *❀*  {names[i]}'
      
      part2=partAv
      
      
      if counter:
        elem = f'\n\n♱ {str(eliminated)}** was eliminated at phase {str(number)}** \n'
        embedVar = discord.Embed(title=f"Phase {str(number)}", description=part1, color=0x00ff00)
        embedVar.add_field(name='Eliminated', value=elem)

        embedVar.add_field(name='Available for Next Round', value=part2)

        msg = await ctx.send(embed=embedVar)

      else:
        elem += f'\n ♱ {str(eliminated)}** was eliminated at phase {str(number)}**\n'
        edit_embed = discord.Embed(title=f"Phase {str(number)}", description=part1, color=0xff0000)
        edit_embed.add_field(name='Eliminated', value=elem)

        edit_embed.add_field(name='Available for Next Round', value=part2)

        await msg.edit(embed=edit_embed)

      number=number+1

      if len(temp) == 1:
        embedVar2 = discord.Embed(title=f"**:tada: Winner!: ** ", description=temp[0], color=0x00ff00)
        await ctx.send(embed=embedVar2)
        # await ctx.send(f'**:tada: Winner!: ** {temp[0]}')
        return
      counter=False
    
  if(message=="demo"):
    temp=[]
    temp=names
    number=1
    counter=True

    for i in range(len(temp)):
      
      part = ''
      for i in range(len(names)):
        part += names[i] + ' '

      if(counter==True):
        part1 = f'**Participants**  {part}'
  
      else:
        part1 = f'**Participants left**  {part}'
      
      if(len(temp)>=2):  
        random_numberEliminator=random.randint(0,len(temp)-1)
        
        eliminated = temp[random_numberEliminator]
        temp.remove(temp[random_numberEliminator])

      if counter==False:
        await asyncio.sleep(6)

      partAv=''
      for i in range(len(names)):
        partAv += f'\n *❀*  {names[i]}'
      
      part2=partAv
      
      
      if counter:
        elem = f'\n\n♱ {str(eliminated)}** was eliminated at phase {str(number)}** \n'
        embedVar = discord.Embed(title=f"Phase {str(number)}", description=part1, color=0x00ff00)
        embedVar.add_field(name='Eliminated', value=elem)

        embedVar.add_field(name='Available for Next Round', value=part2)

        msg = await ctx.send(embed=embedVar)

      else:
        elem += f'\n ♱ {str(eliminated)}** was eliminated at phase {str(number)}**\n'
        edit_embed = discord.Embed(title=f"Phase {str(number)}", description=part1, color=0xff0000)
        edit_embed.add_field(name='Eliminated', value=elem)

        edit_embed.add_field(name='Available for Next Round', value=part2)

        await msg.edit(embed=edit_embed)

      number=number+1

      if len(temp) == 1:
        embedVar2 = discord.Embed(title=f"**:tada: Winner!: ** ", description=temp[0], color=0x00ff00)
        await ctx.send(embed=embedVar2)
        # await ctx.send(f'**:tada: Winner!: ** {temp[0]}')
        return
      counter=False

  elif(message=="participants"):
    
    part = ''
    for i in range(len(names)):
      part += names[i] + ' '
    
    embedVarPart = discord.Embed(title=f"Participants ",color=0xFFA500)
    for i in range(len(names)):
      embedVarPart.add_field(name=f'Player {i+1}', value=f'{names[i]}')

    msg = await ctx.send(embed=embedVarPart)

#----------------------------------------------------------------------------------#
def setup(client):
    # Every extension should have this function
  client.add_command(giveaway)
import discord
from discord.ext import commands
import random
import asyncio
# Tato - 305681776427139073
# Cyber - 335808768979894283
# Shakira - 560497173570256927
# Havoc - 557646464831193088
# Mohit - 275639430683951104
# Saki - 508887278068957186
# Samin - 399972625583177738

@commands.command()
async def howgay(ctx, arg=None):

  if arg == None:
    
    #RYANSHAYANTOSHAKIRA
    if(ctx.author.id == 305681776427139073 or ctx.author.id == 335808768979894283 or ctx.author.id == 560497173570256927):
      owners_nogay = (round(random.uniform(0.00, 20.00),2))
      gay = f'{ctx.author.name} is {owners_nogay}% gay :tada:'

      cols = [0x32a852, 0x3296a8, 0xb700ff, 0x9232a8, 0xa8326f, 0xf25207, 0x3efa00, 0xfa0000]
      embedVar = discord.Embed(title='Gay fortune teller', description=gay, color = random.choice(cols))

      msg=await ctx.channel.send(embed=embedVar)


      ##clearhere
      for i in range(100):
        embed2 = discord.Embed(title='Gay fortune teller', description=gay, color = random.choice(cols))
        await asyncio.sleep(1)
        await msg.edit(embed=embed2)

  ##-------Target Case--------------------------------------------------------------

    # #HAVOCSAKISAMIN
    # elif(ctx.author.id == 557646464831193088 or ctx.author.id == 508887278068957186 or ctx.author.id == 399972625583177738):
    #   gayhavoc=(round(random.uniform(69.00, 101.00),2))
    #   gay = f'{ctx.author.name} is {gayhavoc}% gay'

    #   embedVar = discord.Embed(title='Gay fortune teller', description=gay, color=0x00ECFF)
    #   await ctx.channel.send(embed=embedVar)

    # #MIRAZ
    # elif(ctx.author.id == 233934996015022080):
    #   gaymirag=(round(random.uniform(.00, 101.00),2))
    #   gay = f'{ctx.author.name} is {gaymirag}% gay'

    #   embedVar = discord.Embed(title='Gay fortune teller', description=gay, color=0x00ECFF)
    #   await ctx.channel.send(embed=embedVar)
  ##----------------------Dont delete target case----------------------------------
    else:
      x=(round(random.uniform(.00, 100.00),2))
      gay = f'{ctx.author.name} is {x}% gay'
      
      cols = [0x32a852, 0x3296a8, 0xb700ff, 0x9232a8, 0xa8326f, 0xf25207, 0x3efa00, 0xfa0000]
      embedVar = discord.Embed(title='Gay fortune teller', description=gay, color = random.choice(cols))
      
      msg=await ctx.channel.send(embed=embedVar)


      ##clearhere
      for i in range(100):
        embed2 = discord.Embed(title='Gay fortune teller', description=gay, color = random.choice(cols))
        await asyncio.sleep(1)
        await msg.edit(embed=embed2)


  else:

    #putting string arg on z to get the <@!xxxxx> value and removing <>@! to check
    #z=str(arg)
    # print(z)
    # z=z.replace("!","")
    # z=z.replace("<","")
    # z=z.replace(">","")
    # z=z.replace("@","")
    #initially I used z=='xxxxxxx' in if condition. But was able to figure out the arg format


    #When arg is a mention it uses the <@!xxxx> id format 
    if(arg=="<@!335808768979894283>"or arg=="<@!305681776427139073>"or arg=="<@!560497173570256927>"):

      cantgayme=(round(random.uniform(00.00, 10.00),2))
      gay = f'{arg} is {cantgayme}% gay'

      cols = [0x32a852, 0x3296a8, 0xb700ff, 0x9232a8, 0xa8326f, 0xf25207, 0x3efa00, 0xfa0000]
      embedVar = discord.Embed(title='Gay fortune teller', description=gay, color = random.choice(cols))
      
      msg=await ctx.channel.send(embed=embedVar)


      ##clearhere
      for i in range(100):
        embed2 = discord.Embed(title='Gay fortune teller', description=gay, color = random.choice(cols))
        await asyncio.sleep(1)
        await msg.edit(embed=embed2)

    # TO DO - fuck up havoc and everyone else use ELIF 

    else:
      x=(round(random.uniform(00.00, 100.00),2))
      gay = f'{arg} is {x}% gay'
      
      cols = [0x32a852, 0x3296a8, 0xb700ff, 0x9232a8, 0xa8326f, 0xf25207, 0x3efa00, 0xfa0000]
      embedVar = discord.Embed(title='Gay fortune teller', description=gay, color = random.choice(cols))#color=0x00ECFF)
      
      msg=await ctx.channel.send(embed=embedVar)


      ##clearhere
      for i in range(100):
        embed2 = discord.Embed(title='Gay fortune teller', description=gay, color = random.choice(cols)
        )
        await asyncio.sleep(1)
        await msg.edit(embed=embed2)

@commands.command()
async def lovemeter(ctx, arg=None):
  if(arg==None):

    if(ctx.author.id == 305681776427139073 or ctx.author.id == 335808768979894283 or ctx.author.id == 560497173570256927):
      metertester = (round(random.uniform(69.00, 100.00),2))
      loveometer= f'{metertester}% of the people are in love with {ctx.author.name}, :heart:'
      embedVar = discord.Embed(title='<:emoji_2:821388998395691029> The love guru', description=loveometer, color=0xba0001)
      await ctx.channel.send(embed=embedVar)

    else:
      metertester = (round(random.uniform(0.00, 100.00),2))

      loveometer= f'{metertester}% of the people are in love with {ctx.author.name}, :heart:'

      embedVar = discord.Embed(title='<:emoji_2:821388998395691029> The love guru', description=loveometer, color=0xba0001)
      await ctx.channel.send(embed=embedVar)

  else:
    #putting string arg on z to get the <@!xxxxx> value and removing <>@! to check
    #z=str(arg)
    # print(z)
    # z=z.replace("!","")
    # z=z.replace("<","")
    # z=z.replace(">","")
    # z=z.replace("@","")
    #initially I used z=='xxxxxxx' in if condition. But was able to figure out the arg format
    #no use of z, changed back to arg

    #arg mention is in <@!xxxx> id format 
    #admin
    if(arg=="<@!335808768979894283>"or arg=="<@!305681776427139073>"or arg=="<@!560497173570256927>"):
      metertester=(round(random.uniform(70.00, 100.00),2))
      loveometer = f' {metertester}% of people are in love with {arg} :heart:'
      embedVar = discord.Embed(title='<:emoji_2:821388998395691029> The love guru', description=loveometer, color=0xba0001)
      await ctx.channel.send(embed=embedVar)

    #samin
    elif(arg=="<@!399972625583177738>"):
      metertester=(round(random.uniform(99.00, 101.00),2))
      loveometer = f' {metertester}% of people are in love with {arg} :heart:'
      embedVar = discord.Embed(title='<:emoji_2:821388998395691029> The love guru', description=loveometer, color=0xba0001)
      await ctx.channel.send(embed=embedVar)

    #Target case commented out, DONT DELETE
    # #saki-havoc  
    # elif(arg=="<@!508887278068957186>" or arg=="<@!557646464831193088>"):
    #   metertester=(round(random.uniform(00.00, 70.00),2))
    #   loveometer = f' {metertester}% of people are in love with {arg} :heart:'
    #   embedVar = discord.Embed(title='<:emoji_2:821388998395691029> The love guru', description=loveometer, color=0xba0001)
    #   await ctx.channel.send(embed=embedVar) 
        
    else:
      metertester=(round(random.uniform(00.00, 98.00),2))
      loveometer = f' {metertester}% of people are in love with {arg} :heart:'
      embedVar = discord.Embed(title='<:emoji_2:821388998395691029> The love guru', description=loveometer, color=0xba0001)
      await ctx.channel.send(embed=embedVar)

def setup(client):
  # Every extension should have this function
  client.add_command(howgay)
  client.add_command(lovemeter)
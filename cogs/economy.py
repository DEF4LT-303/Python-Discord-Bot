from main import *
import random
import asyncio
import re


with open('./cogs/Data/text.txt', 'r') as f:
  sentences = [i.replace('\n', '') or i for i in f.readlines()]


class Economy(commands.Cog):

  def __init__(self, client):

    self.client = client 

  async def check(self, users, user):

    if not f'{user.id}' in users:
      users[f'{user.id}'] = {}
      users[f'{user.id}']['money'] = 100

  async def add(self, users, user, amount):

    users[f'{user.id}']['money'] += amount


  @commands.command(aliases=['race', 'work'])
  # @commands.cooldown(1, 3600, type=commands.BucketType.user)
  async def typerace(self, ctx):

    with open('./cogs/Data/economy.json', 'r') as f:
      users = json.load(f)

    await self.check(users, ctx.author)

    sentence = random.choice(sentences)
    length = len(sentence.split())
    formatted = re.sub(r'[^A-Za-z ]+', "", sentence).lower()
    emoji = ""

    for i in formatted:
      if i == " ":
        emoji += "    "
      
      else:
        emoji += f':regional_indicator_{i}: '

    send = await ctx.send(f"{emoji}")


    embedVar = discord.Embed(description='You have failed to answer correctly!', color=discord.Colour.random())


    #-------check if msg is from author-------#
    def check(m):
      return m.author == ctx.author
    #-----------------------------------------#

    try:
      msg = await self.client.wait_for("message", check=check, timeout=60.0)
      # pass
    
    except asyncio.TimeoutError:
      await ctx.send(embed=embedVar)
      await self.add(users, ctx.author, 50)

    else:
      
      sentence = sentence.replace(' ','')

      if msg.content.lower() == sentence.lower():
        time = str(datetime.utcnow() - send.created_at)
        time_format = time[:-5][5:]

        if time_format[0] == '0':
          time_format = time_format[1:]

        embedVar = discord.Embed(description=f'You have finished the typerace in {time_format} seconds!', color=discord.Colour.random())

        wpm = (length / (float(time_format)/60))
        money = int((wpm/100)*2000)

        embedVar.add_field(name='Potatoes earned 🥔 - ', value=money)
        embedVar.add_field(name='WPM - ', value=int(wpm))
        await ctx.send(embed=embedVar)

        await self.add(users, ctx.author, money)

        
      else:
        await ctx.send(embed=embedVar)
        await self.add(users, ctx.author, 50)
      
        

    with open('./cogs/Data/economy.json', 'w') as f:
      json.dump(users, f, indent=4, sort_keys=True)


  @commands.command(aliases=['bal'])
  async def balance(self, ctx, user: discord.Member=None):

    with open('./cogs/Data/economy.json', 'r') as f:
      users = json.load(f)
    
    # await self.check(users, user)
    
    if not user:
      user = ctx.author

      await self.check(users, user)

      money = users[f'{user.id}']['money']

      embedVar = discord.Embed(description=f'You have `{money}` 🥔', color=0x97572b)
      embedVar.set_footer(text=f'Requested by {ctx.author}',
                              icon_url=ctx.author.avatar_url)

      await ctx.send(embed=embedVar)
    
    else:
      await self.check(users, user)

      money = users[f'{user.id}']['money']

      embedVar = discord.Embed(description=f'{user} has `{money}` 🥔', color=0x97572b)
      

      await ctx.send(embed=embedVar)
    
    with open('./cogs/Data/economy.json', 'w') as f:
      json.dump(users, f, indent=4)
    
  @commands.command(aliases=['lb'])
  async def leaderboard(self, ctx):

    with open('./cogs/Data/economy.json', 'r') as f:
          users = json.load(f)

    lb = ''

    res = sorted(users.items(), key = lambda x: x[1]['money'])

    count = 1
    checker = len(res)-1
    
    for i in range(len(res)-1, -1, -1): 
      
      money = res[i][1]['money']
      person = ctx.message.guild.get_member(int(res[i][0]))
      
      if person is None:
        p = await client.fetch_user(int(res[i][0]))
        person = p.name

      lb += f'{count}. {person} - `{money}` 🥔\n'

      count += 1

    

    em = discord.Embed(title=':oncoming_automobile: Type Racer Rankings', description=f'{lb}')
    await ctx.send(embed=em)
  
  @commands.command()
  async def admin_add(self, ctx, user: discord.Member, amount):

    if ctx.author.id == 305681776427139073 or ctx.author.id==335808768979894283:
      with open('./cogs/Data/economy.json', 'r') as f:
        users = json.load(f)

      await self.check(users, user)

      users[f'{user.id}']['money'] += int(amount)

      await  ctx.send(f"{amount} potatoes added to {user}'s account")

      with open('./cogs/Data/economy.json', 'w') as f:
        json.dump(users, f, indent=4)    

  @commands.command()
  async def admin_del(self, ctx, user: discord.Member, amount):

    if ctx.author.id == 305681776427139073 or ctx.author.id==335808768979894283: 
      with open('./cogs/Data/economy.json', 'r') as f:
        users = json.load(f)

      await self.check(users, user)

      users[f'{user.id}']['money'] -= int(amount)

      await  ctx.send(f"{amount} potatoes removed {user}'s account")

      with open('./cogs/Data/economy.json', 'w') as f:
        json.dump(users, f, indent=4) 



def setup(client):

  client.add_cog(Economy(client))
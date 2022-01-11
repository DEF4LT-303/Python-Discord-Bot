from main import *
from discord import File, Member
from discord.ext import commands
# from easy_pil import Editor, Canvas, load_image_async, Font
from disrank.generator import Generator
import functools
import asyncio
from discord.utils import get

class LevelUp(commands.Cog):

  def __init__(self, client) -> None:
    self.client = client

  @commands.Cog.listener()
  async def on_member_join(self, member):

    with open('./cogs/Data/users.json', 'r') as f:
      users = json.load(f)

    await self.update_data(users, member)

    with open('./cogs/Data/users.json', 'w') as f:
      json.dump(users, f, indent=4)


  @commands.Cog.listener()
  async def on_message(self, message):

    if message.author == client.user: return
    if message.author.bot: return
    if 'rank' in message.content: return
    
    with open('./cogs/Data/users.json', 'r') as f:
      users = json.load(f)

    # await asyncio.sleep(10)
    await self.update_data(users, message.author)
    await self.add_xp(users, message.author, 2)
    await self.level_up(users, message.author, message.channel)

    with open('./cogs/Data/users.json', 'w') as f:
      json.dump(users, f, indent=4, sort_keys=True)

  async def update_data(self, users, user):

    if not f'{user.id}' in users:
      users[f'{user.id}'] = {}
      users[f'{user.id}']['exp_next_lvl'] = 20
      users[f'{user.id}']['exp_needed'] = 0
      users[f'{user.id}']['experience'] = 0
      users[f'{user.id}']['level'] = 1

  async def add_xp(self, users, user, xp):

    # await asyncio.sleep(10)
    users[f'{user.id}']['experience'] += xp

  async def level_up(self, users, user, message):

    exp = users[f'{user.id}']['experience']
    exp_next = users[f'{user.id}']['exp_next_lvl']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(exp ** (1/4))

    users[f'{user.id}']['exp_needed'] = exp_next - exp 

    if lvl_start < lvl_end:
      await message.send(f'{user.mention} has reached level {lvl_end}')

      users[f'{user.id}']['level'] = lvl_end
      users[f'{user.id}']['exp_next_lvl'] = (users[f'{user.id}']['level'] + 1)**4

  async def lb_check(self, users, user):

    res = sorted(users.items(), key = lambda x: x[1]['level'])

    checker = len(res)
    
    for i in range(len(res)-1, -1, -1): 
      
      author = res[i][0]
      
      if int(author) == user.id:
        return abs(i - checker)

      

  #--------------Rank Card---------------------#

  def get_card(self, args):
    image = Generator().generate_profile(**args)
    return image

  @commands.command()
  async def rank(self, ctx, user: Member=None):

    with open('./cogs/Data/users.json', 'r') as f:
      users = json.load(f)
    

    if user is None:
      user = ctx.author

    try:
      # if f'{user.id}' not in users:
      #   await ctx.send(f"**{user}** doesn't have any rank yet! ")
    
    

      rank = await self.lb_check(users, user)
        
      args = {
        'bg_image' : 'https://discordjs.guide/assets/canvas-preview.30c4fe9e.png', # Background image link (Optional)
        'profile_image' : str(user.avatar_url_as(format='png')), # User profile picture link
        'level' : users[f'{user.id}']['level'], # User current level 
        'current_xp' : users[f'{user.id}']['level']**4, # Current level minimum xp 
        'user_xp' : users[f'{user.id}']['experience'], # User current xp
        'next_xp' : users[f'{user.id}']['exp_next_lvl'], # xp required for next level
        'user_position' : rank, # User position in leaderboard
        'user_name' : str(user), # user name with descriminator 
        'user_status' : user.status.name, # User status eg. online, offline, idle, streaming, dnd
      }

      func = functools.partial(self.get_card, args)
      image = await asyncio.get_event_loop().run_in_executor(None, func)

      file = discord.File(fp=image, filename='image.png')
      await ctx.send(file=file)   

    except KeyError:
      await ctx.send(f"**{user}** doesn't have any rank yet! ")

  @commands.command(aliases=['top'])
  async def rank_leaderboard(self, ctx):

    with open('./cogs/Data/users.json', 'r') as f:
            users = json.load(f)

    lb = ''

    res = sorted(users.items(), key = lambda x: x[1]['experience'])
    res.reverse()

    count = 1
    
    for i in range(10): 
      
      level = res[i][1]['level']
      
      p = await client.fetch_user(int(res[i][0]))
      person = p.name

      lb += f'{count}. {person} - `lvl: {level}`\n'

      count += 1

    em = discord.Embed(title=':chart_with_downwards_trend: Global Level Rankings', description=f'{lb}')
    await ctx.send(embed=em)


def setup(client):

  client.add_cog(LevelUp(client))
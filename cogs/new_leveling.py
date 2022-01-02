from main import *
from pymongo import MongoClient

mongo_url = os.environ['Mongodb_url']
# cluster = motor.motor_asyncio.AsyncIOMotorClient(str(mongo_url))
cluster = MongoClient(str(mongo_url))
leveling = cluster['Database']['leveling']

class LevelSystem(commands.Cog):

  def __init__(self, client):
    self.client = client

  
  @commands.Cog.listener()
  async def on_message(self, msg):

    if msg.author == client.user: return
    if msg.author.bot: return
    if 'rank' in msg.content: return  

    await self.update_data(msg.author)
    await self.add_xp(msg.author, 2)
    await self.level_up(msg.author, msg.channel)


  async def update_data(self, user):

    stats = leveling.find_one({'id': user.id})

    if stats is None:

      new_user = {'id': user.id, 'xp': 0, 'exp_needed': 0, 'exp_next': 20, 'level': 1}
      leveling.insert_one(new_user)      

  async def add_xp(self, user, xp):

    stats = leveling.find_one({'id': user.id})

    xp = stats['xp'] + 2
    leveling.update_one({'id': user.id}, {'$set': {'xp': xp}})

  async def level_up(self, user, channel):

    stats = leveling.find_one({'id': user.id})

    exp = stats['xp']
    exp_next = stats['exp_next']
    lvl_start = stats['level']
    lvl_end = int(exp ** (1/4))

    reset = exp_next - exp
    leveling.update_one({'id': user.id}, {'$set': {'exp_needed': reset}})

    if lvl_start < lvl_end:
      await channel.send(f'{user.mention} has reached level {lvl_end}')

      new_exp = (stats['level'] + 1) ** 4
      leveling.update_one({'id': user.id}, {'$set': {'level': lvl_end}})
      leveling.update_one({'id': user.id}, {'$set': {'exp_next': new_exp}})


def setup(client):

  client.add_cog(LevelSystem(client))
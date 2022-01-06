from main import *
import datetime
from discord.utils import get


class Test(commands.Cog):

  def __init__(self, client):
    self.client = client

  @tasks.loop(seconds = 10)
  async def test(self):

    test = datetime.datetime.now()
    
    
    time_change = datetime.timedelta(hours=6)
    new_time = test + time_change
    new_time = new_time.strftime("%H:%M")

    channel = client.get_channel(927233418394218566)
    guild = client.get_guild(736748152962547802)
    role = get(guild.roles, name = 'Genshin Daily') 

    if new_time == '22:00':
      await channel.send(f'{role.mention} <:HuTaoEvil:884697993721294929> Don\'t forget you dailies! - {test.strftime("%d/%m/%Y")}')
    
      await asyncio.sleep(3600)

  @commands.Cog.listener()
  async def on_ready(self):

    self.test.start()

def setup(client):

  client.add_cog(Test(client))


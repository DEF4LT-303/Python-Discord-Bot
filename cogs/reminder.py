from main import *
import datetime


class DurationConverter(commands.Converter):

  async def convert(self, ctx, arg):

    amount = arg[:-1]
    unit = arg[-1]

    if amount.isdigit() and unit in ['s', 'm', 'h']:
      return (int(amount), unit)

    embedVar = discord.Embed(title=":warning: Not a valid argument", description="Usage: reminder `<time[s/m/h/d]>` `<message>`", color=0xba0001)
    raise commands.BadArgument(await ctx.channel.send(embed=embedVar))


# @commands.command(aliases=['remind', 'remindme'])
# async def reminder(ctx, duration: DurationConverter, *, msg=None):

#   multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600*24}
#   amount, unit = duration

#   user = ctx.author

#   sleep = amount * multiplier[unit]

#   if sleep > 7776000:
#     embedVar = discord.Embed(title=":warning: Duration too long", description="Please specify a duration below 90 days", color=0xba0001) 

#     raise commands.BadArgument(await ctx.channel.send(embed=embedVar))
#   embedVar = discord.Embed(title=":clock130: Reminder Set!", description=f"I will remind you about `{msg}` in {amount}{unit}", color=0x1C72E9)

#   embedVar.set_footer(text=f'Requested by {user}', icon_url=user.avatar_url)

#   await ctx.channel.send(embed=embedVar)

#   await asyncio.sleep(sleep) ### TIMER

#   embedVar2 = discord.Embed(title=":clock130: Reminder!", description=f"Hi {user.mention}, you asked me to remind you {amount}{unit} ago.", color=0x1C72E9)
  
#   embedVar2.add_field(name='Reason', value=f'{msg}')
#   embedVar2.set_footer(text=f'Requested by {user}', icon_url=user.avatar_url)

#   await ctx.channel.send(user.mention)
#   await ctx.channel.send(embed=embedVar2)

#-----------------------------------------------------------------------------#
class Reminder(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.msg = None
    self.amount = None
    self.unit = None
    self.reminder_task.start()


  @tasks.loop(seconds = 5)
  async def reminder_task(self):
    
    with open('./cogs/Data/reminders.json', 'r') as f:
      db = json.load(f)

    now = datetime.datetime.now()

    for i in db.keys():
      
      reminder = datetime.datetime.strptime(db[i]['reminder'], "%Y-%m-%dT%H:%M:%S")
      if now >= reminder:

        # channel = self.client.get_guild(db[i]['channel'])
        user = self.client.get_user(int(i))
        channel = self.client.get_channel(db[i]['channel'])
        
        embedVar2 = discord.Embed(title=":clock130: Reminder!", description=f"Hi {user.mention}, you asked me to remind you {self.amount}{self.unit} ago.", color=0x1C72E9)
  
        embedVar2.add_field(name='Reason', value=f'{self.msg}')
        embedVar2.set_footer(text=f'Requested by {user}', icon_url=user.avatar_url)

        await channel.send(embed=embedVar2)

        del db[i]

        with open('./cogs/Data/reminders.json', 'w') as f:
          json.dump(db, f, indent=4, sort_keys=True)
        
        return

  @commands.command(aliases=['reminder', 'remindme'])
  async def remind(self, ctx, duration: DurationConverter, *, msg=None):



    multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600*24}
    amount, unit = duration

    self.msg = msg
    self.amount = amount
    self.unit = unit

    sleep = amount * multiplier[unit]

    user = ctx.author
    guild = ctx.guild
    channel = ctx.channel

    with open('./cogs/Data/reminders.json', 'r') as f:
      db = json.load(f)

    now = datetime.datetime.now()
    remind_time = datetime.timedelta(seconds = sleep)
    new_time = now + remind_time
    new_time = new_time.replace(microsecond=0)
    # new_time = new_time.strftime("%Y-%m-%d %H:%M:%S")
    
    if not f'{user.id}' in db:
      db[f'{user.id}'] = {}
      db[f'{user.id}']['reminder'] = new_time.isoformat()
      db[f'{user.id}']['guild'] = guild.id
      db[f'{user.id}']['channel'] = channel.id
    
      embedVar = discord.Embed(title=":clock130: Reminder Set!", description=f"I will remind you about `{msg}` in {amount}{unit}", color=0x1C72E9)

      embedVar.set_footer(text=f'Requested by {user}', icon_url=user.avatar_url)

      await ctx.channel.send(embed=embedVar)

    with open('./cogs/Data/reminders.json', 'w') as f:
      json.dump(db, f, indent=4, sort_keys=True)


def setup(client):

  # client.add_command(reminder)
  client.add_cog(Reminder(client))


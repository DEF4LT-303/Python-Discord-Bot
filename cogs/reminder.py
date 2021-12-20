from main import *



class DurationConverter(commands.Converter):

  async def convert(self, ctx, arg):

    amount = arg[:-1]
    unit = arg[-1]

    if amount.isdigit() and unit in ['s', 'm', 'h']:
      return (int(amount), unit)

    embedVar = discord.Embed(title=":warning: Not a valid argument", description="Usage: reminder `<time[s/m/h/d]>` `<message>`", color=0xba0001)
    raise commands.BadArgument(await ctx.channel.send(embed=embedVar))


@commands.command(aliases=['remind', 'remindme'])
async def reminder(ctx, duration: DurationConverter, *, msg=None):

  multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 3500*24}
  amount, unit = duration

  user = ctx.author

  sleep = amount * multiplier[unit]

  if sleep > 7776000:
    embedVar = discord.Embed(title=":warning: Duration too long", description="Please specify a duration below 90 days", color=0xba0001) 

    raise commands.BadArgument(await ctx.channel.send(embed=embedVar))
  embedVar = discord.Embed(title=":clock130: Reminder Set!", description=f"I will remind you about `{msg}` in {amount}{unit}", color=0x1C72E9)

  embedVar.set_footer(text=f'Requested by {user}', icon_url=user.avatar_url)

  await ctx.channel.send(embed=embedVar)

  await asyncio.sleep(sleep) ### TIMER

  embedVar2 = discord.Embed(title=":clock130: Reminder!", description=f"Hi {user.mention}, you asked me to remind you {amount}{unit} ago.", color=0x1C72E9)
  
  embedVar2.add_field(name='Reason', value=f'{msg}')
  embedVar2.set_footer(text=f'Requested by {user}', icon_url=user.avatar_url)

  await ctx.channel.send(user.mention)
  await ctx.channel.send(embed=embedVar2)


def setup(client):

  client.add_command(reminder)
  # client.add_cog(DurationConverter(client))


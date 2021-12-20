from main import *

@commands.command()
async def probe(ctx, member: discord.Member=None):

  
  if member is None:

    created_at = ctx.author.created_at.strftime("%b %d, %Y")
    joined_at = ctx.author.joined_at.strftime("%b %d, %Y")
    

    embedVar = discord.Embed(title="User Information",
                                 description=f"**User**: {ctx.author}",
                                 color=0x00f100)

    embedVar.add_field(
        name="Joined Discord",
        value= created_at)

    embedVar.add_field(
        name=f"Joined Server [{ctx.guild.name}]",
        value= joined_at, inline=True) 
    
    embedVar.set_thumbnail(url=ctx.author.avatar_url)

    embedVar.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

  else:

    created_at = member.created_at.strftime("%b %d, %Y")
    joined_at = member.joined_at.strftime("%b %d, %Y")

    embedVar = discord.Embed(title="User Information",
                                  description=f"**User**: {member}",
                                  color=0x00f100)

    embedVar.add_field(
        name="Joined Discord",
        value= created_at)

    embedVar.add_field(
        name=f"Joined Server [{ctx.guild.name}]",
        value= joined_at, inline=False)  

    embedVar.set_thumbnail(url=member.avatar_url)
    
    embedVar.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

  #-----------cooool effect-----------------#
  msg = await ctx.send('`> Probing user`')

  for i in range(1, 4):
    dot = '.'
    send = f'`> Probing user{dot*i}`'
    await msg.edit(content=send)
    await asyncio.sleep(1)

  await ctx.send(embed=embedVar)


def setup(client):

  client.add_command(probe)
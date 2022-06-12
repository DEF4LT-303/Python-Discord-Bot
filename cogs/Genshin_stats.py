from main import *
import discord
import json
import genshinstats as gs


class GenshinApi2(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.command(aliases=['gi_regsiter', 'gi_reg'])
  async def genshin_register(self, ctx, ltuid, ltoken, UID):
    
    player = ctx.author.id

    with open('./cogs/Data/genshin_users.json', 'r') as f:
      users = json.load(f)

    if player not in users:

      users[f'{player}'] = {}
      users[f'{player}']['ltuid'] = ltuid
      users[f'{player}']['ltoken'] = ltoken
      users[f'{player}']['UID'] = UID

      await ctx.send('Registered!')
      
    with open('./cogs/Data/genshin_users.json', 'w') as f:
      json.dump(users, f, indent=4, sort_keys=True)

  @commands.command()
  async def gi_test(self, ctx):

    with open('./cogs/Data/genshin_users.json', 'r') as f:
      users = json.load(f)


    # if ctx.author.id in users:

    player_ltuid = int(users[f'{ctx.author.id}']['ltuid'])
    player_ltoken = users[f'{ctx.author.id}']['ltoken']
    uid = int(users[f'{ctx.author.id}']['UID'])



    gs.set_cookie(ltuid=player_ltuid, ltoken=player_ltoken)

    
    data = gs.get_user_stats(uid)
    total_characters = len(data['characters'])
    print('user has a total of', total_characters, 'characters')

    # stats = gs.get_user_stats(uid)['stats']
    # for field, value in stats.items():
    #   print(f"{field}: {value}")

    characters = gs.get_characters(uid)
    string = ''
    for char in characters:
        string += f"{char['rarity']}* {char['name']:10} | lvl {char['level']:2} C{char['constellation']}\n"
    
    embed = discord.Embed(title='Characters', description=string)

    await ctx.send(embed=embed)

    notes = gs.get_notes(uid)
    print(notes['resin'])
    print(f"Current resin: {notes['resin']}/{notes['max_resin']}")
    print(f"Current realm currency: {notes['realm_currency']}/{notes['max_realm_currency']}")
    print(f"Expeditions: {len(notes['expeditions'])}/{notes['max_expeditions']}")

    embed2 = discord.Embed(title='Notes')
    embed2.add_field(name='Resin', value=f"Current resin: {notes['resin']}/{notes['max_resin']}")
    embed2.add_field(name='Expeditions', value=f"Expeditions: {len(notes['expeditions'])}/{notes['max_expeditions']}")


    await ctx.send(embed=embed2)


def setup(client):

  client.add_cog(GenshinApi2(client))
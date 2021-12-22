from main import *
import animec


class Anime(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def anime(self, ctx, *, arg):

    try:
      anime = animec.Anime(arg)

    except:
      await ctx.send(f'No corresponding Anime is found for **{arg}**')
      return

    embedVar = discord.Embed(title=anime.title_english, url=anime.url, description=f'{anime.description[:200]}...\n[Read more]({anime.url})', color=discord.Color.random())

    embedVar.add_field(name='Episodes', value=str(anime.episodes), inline=False)
    embedVar.add_field(name='Rating', value=str(anime.rating), inline=True)
    embedVar.add_field(name='Genre', value=str(anime.genres), inline=True)
    embedVar.add_field(name='Status', value=str(anime.status), inline=False)
    # embedVar.add_field(name='Type', value=str(anime.type), inline=True)
    embedVar.add_field(name='NSFW Status', value=anime.is_nsfw(), inline=True)
    embedVar.set_thumbnail(url=anime.poster)

    await ctx.send(embed=embedVar) 

def setup(client):

  client.add_cog(Anime(client))
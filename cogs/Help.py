from main import *


class Help(commands.Cog):
    def __init__(self, client):

        self.client = client

    @commands.command(aliases=['info'], pass_context=True)
    async def help(self, ctx):

        servers = ['894632180821663835', '736748152962547802']


        with open('./cogs/Data/prefixes.json', 'r') as f:
            prefixes = json.load(f)


        prefix = prefixes[str(ctx.guild.id)]

        if str(ctx.guild.id) not in servers:
          embedVar = discord.Embed(title="Help Message",
                                 description="Showing all the commands",
                                 color=0x00ff00)
          embedVar.add_field(
              name=":exclamation: Prefix",
              value=
              f"○ Change Prefix: `prefix <argument>`\nThe current Prefix is `{prefix}`",
              inline=False)

          embedVar.add_field(
              name=":wrench: Utility",
              value=
              '○ Invite Link: `invite`\n○ urbandictionary: `ud <argument>`\n○  Calculator: `cal 1+2+3`\no Round off: `round(n,number after decimal)`\n○ Morse Code: `mc <argument>` \n○ Morse Code translator: `mcd <argument>` \n○ Reminder: `remind <time> <argument>`',
              inline=True)

          embedVar.add_field(
              name=":sparkles: Fun",
              value=
              "○ PP Machine: `ppsize <@user>` \n○ Gay Fortune: `howgay <@user>` \n○ Love Guru: `lovemeter <@user>`\n○ TalkingBot: `q <argument>`\n○ Search Anime: `anime <argument>`",
              inline=True)

          embedVar.add_field(
              name=":musical_note: Music",
              value=
              "♪ Play music: `play <song>` \n♪ Skip music: `skip <song>` \n♪ Queue: `queue` \n! Pause | Resume: `pause | resume` \n♪ Now playing: `np` \n♪ Volume: `vol <argument>` \n♪ Disconnect: `dc`",
              inline=False)            

          embedVar.add_field(
              name=":moneybag: Economy",
              value=
              "○ Play Type Racer [earn]: `typerace` \n○ Check  Balance [register]: `bal <@user>` \n○ Type Racer Leaderboard: `lbpotatoes` | `lbwpm` \n○ Give money to user: `give <@user> <amount>`",
              inline=True)      

          embedVar.add_field(
              name=":lock: Profile",
              value=
              "○ Check Rank: `rank <@user>` \n○ Ranking Leaderboard: `top` \n○ Fetch User Info: `probe <@user>`",
              inline=True)
        



          embedVar.set_footer(text=f'Requested by {ctx.author}',
                              icon_url=ctx.author.avatar_url)

          await ctx.send(embed=embedVar)

        else:

          embedVar = discord.Embed(title="Help Message",
                                  description="Showing all the commands",
                                  color=0x00ff00)
          embedVar.add_field(
              name=":exclamation: Prefix",
              value=
              f"○ Change Prefix: `prefix <argument>`\nThe current Prefix is `{prefix}`",
              inline=False)

          embedVar.add_field(
              name=":wrench: Utility",
              value=
              '○ Invite Link: `invite`\n○ urbandictionary: `ud <argument>`\n○  Calculator: `cal 1+2+3`\no Round off: `round(n,number after decimal)`\n○ Morse Code: `mc <argument>` \n○ Morse Code translator: `mcd <argument>` \n○ Reminder: `remind <time> <argument>`',
              inline=True)

          embedVar.add_field(
              name=":sparkles: Fun",
              value=
              "○ PP Machine: `ppsize <@user>` \n○ Gay Fortune: `howgay <@user>` \n○ Love Guru: `lovemeter <@user>`\n○ TalkingBot: `q <argument>`\n○ [Server Specific] Voice Commands: `vc <argument>`\n○ [Server Specific] Show Voice List: `voices`\n○ Search Anime: `anime <argument>`",
              inline=True)

          embedVar.add_field(
              name=":musical_note: Music",
              value=
              "♪ Play music: `play <song>` \n♪ Skip music: `skip <song>` \n♪ Queue: `queue` \n! Pause | Resume: `pause | resume` \n♪ Now playing: `np` \n♪ Volume: `vol <argument>` \n♪ Disconnect: `dc`",
              inline=False)            

          embedVar.add_field(
              name=":moneybag: Economy",
              value=
              "○ Play Type Racer [earn]: `typerace` \n○ Check  Balance [register]: `bal <@user>` \n○ Type Racer Leaderboard: `lbpotatoes` | `lbwpm` \n○ Give money to user: `give <@user> <amount>`",
              inline=True)      

          embedVar.add_field(
              name=":lock: Profile",
              value=
              "○ Check Rank: `rank <@user>` \n○ Ranking Leaderboard: `top` \n○ Fetch User Info: `probe <@user>`",
              inline=True)
          embedVar.add_field(
              name=":frame_photo:Image",
              value=
              "○ [Server Specific] Shows available img list: `img list`",
              inline=False)


          # embedVar.add_field(
          #     name=":envelope: Multilingual Greetings and Farewells",
          #     value="○ Try saying `hello` or `bye` in different languages",
          #     inline=False)

          embedVar.set_footer(text=f'Requested by {ctx.author}',
                              icon_url=ctx.author.avatar_url)

          await ctx.send(embed=embedVar)
          # await ctx.author.send(':poop:')

    @commands.command(aliases=['voices', 'voicelines'])
    async def voice_list(self, ctx):
        servers = ['894632180821663835', '736748152962547802'] # server IDs

        if str(ctx.guild.id) not in servers:
          await ctx.send('Not valid for this **Server**')
          return

        embedVar = discord.Embed(title="Voice List",
                                 description="Showing all the voice commands",
                                 color=0x00ff00)

        embedVar.add_field(
            name=":microphone2: Voices",
            value=
            '🔊 **sweet**: You are so sweet I like you <3\n🔊 **helikopter**: helikopter helikopter\n🔊 **fucking**: fahking...faked up bitch\n🔊 **kola**: ki...hotat kore mukhe asihe dhukay dao ken?? 🍌\n🔊 **buttplug**: 6 ta buttplug ase amar\n🔊 **like**: You are so sweet I like you <3 [Shakira]\n🔊 **sap**: ⚠ Don\'t play this!\n🔊 **dudh**: dudh khabo dudh dao\n🔊 **balls**: gimme my balls')
        embedVar.set_footer(text='Usage: {prefix}vc <argument>')

        await ctx.send(embed=embedVar)


def setup(client):
    # Every extension should have this function
    client.add_cog(Help(client))

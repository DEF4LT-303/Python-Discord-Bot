from main import *
import random
from random import sample
import asyncio
import re
import datetime
from discord.ext.commands import CommandOnCooldown

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

    async def add_wpm(self, users, user, wpm):

        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
            users[f'{user.id}']['wpm'] = wpm

        else:
            if wpm > users[f'{user.id}']['wpm']:
                users[f'{user.id}']['wpm'] = wpm

    @commands.command(aliases=['race', 'work'])
    @commands.cooldown(1, 1, type=commands.BucketType.user)
    ##
    async def typerace(self, ctx):

        with open('./cogs/Data/economy.json', 'r') as f:
            users = json.load(f)

        with open('./cogs/Data/wpm.json', 'r') as f:
            wpm_file = json.load(f)

        await self.check(users, ctx.author)

        sentence = random.choice(sentences[:200])

        length = len(sentence.split())
        formatted = re.sub(r'[^A-Za-z ]+', "", sentence).lower()
        emoji = ""

        for i in formatted:
            if i == " ":
                emoji += "    "

            else:
                emoji += f':regional_indicator_{i}: '

        send = await ctx.send(f"{emoji}")

        init_time = datetime.datetime.now()


        embedVar = discord.Embed(
            description='You have failed to answer correctly!',
            color=discord.Colour.random())

        #-------check if msg is from author-------#
        def check(m):
            return m.author == ctx.author

        #-----------------------------------------#

        try:
            msg = await self.client.wait_for("message",
                                             check=check,
                                             timeout=60.0)
            # pass

        except asyncio.TimeoutError:
            await ctx.send(embed=embedVar)
            await self.add(users, ctx.author, 50)

        else:

            sentence = sentence.replace(' ', '')

            if msg.content.lower() == sentence.lower():

                time = datetime.datetime.now() - init_time
                time_format = round(time.total_seconds(), 2)

                embedVar2 = discord.Embed(
                    description=
                    f'You have finished the typerace in {time_format} seconds!',
                    color=discord.Colour.random())

                wpm = (length / (float(time_format) / 60))
                money = int((wpm / 100) * 2000)

                embedVar2.add_field(name='Potatoes earned 🥔 - ', value=money)
                embedVar2.add_field(name='WPM - ', value=int(wpm))
                await ctx.send(embed=embedVar2)

                await self.add(users, ctx.author, money)

                await self.add_wpm(wpm_file, ctx.author, int(wpm))

            else:
                await ctx.send(embed=embedVar)
                await self.add(users, ctx.author, 50)

        with open('./cogs/Data/economy.json', 'w') as f:
            json.dump(users, f, indent=4, sort_keys=True)

        with open('./cogs/Data/wpm.json', 'w') as f:
            json.dump(wpm_file, f, indent=4, sort_keys=True)

    @commands.command(aliases=['bal'])
    async def balance(self, ctx, user: discord.Member = None):

        with open('./cogs/Data/economy.json', 'r') as f:
            users = json.load(f)

        # await self.check(users, user)

        if not user:
            user = ctx.author

            await self.check(users, user)

            money = users[f'{user.id}']['money']

            embedVar = discord.Embed(description=f'You have `{money}` 🥔',
                                     color=0x97572b)
            embedVar.set_footer(text=f'Requested by {ctx.author}',
                                icon_url=ctx.author.avatar.url)

            await ctx.send(embed=embedVar)

        else:
            await self.check(users, user)

            money = users[f'{user.id}']['money']

            embedVar = discord.Embed(description=f'{user} has `{money}` 🥔',
                                     color=0x97572b)

            await ctx.send(embed=embedVar)

        with open('./cogs/Data/economy.json', 'w') as f:
            json.dump(users, f, indent=4)

    @commands.command(aliases=['lb money', 'lbpotatoes'])
    async def leaderboard_money(self, ctx):

        with open('./cogs/Data/economy.json', 'r') as f:
            users = json.load(f)

        lb = ''

        res = sorted(users.items(), key=lambda x: x[1]['money'])
        res.reverse()

        count = 1

        for i in range(10):

            money = res[i][1]['money']

            p = await client.fetch_user(int(res[i][0]))
            person = p.name

            lb += f'{count}. {person} - `{money}` 🥔\n'

            count += 1

        em = discord.Embed(
            title=':oncoming_automobile: Type Racer Rankings [Money]',
            description=f'{lb}')
        await ctx.send(embed=em)

    @commands.command(aliases=['lbwpm'])
    async def leaderboard_wpm(self, ctx):

        with open('./cogs/Data/wpm.json', 'r') as f:
            users = json.load(f)

        lb = ''

        res = sorted(users.items(), key=lambda x: x[1]['wpm'])
        res.reverse()

        count = 1

        if len(res) > 10:
            for i in range(10):

                money = res[i][1]['wpm']

                p = await client.fetch_user(int(res[i][0]))
                person = p.name

                lb += f'{count}. {person} - `{money}` WPM\n'

                count += 1

        else:
            for i in range(len(res)):

                money = res[i][1]['wpm']

                p = await client.fetch_user(int(res[i][0]))
                person = p.name

                lb += f'{count}. {person} - `{money}` WPM\n'

                count += 1

        em = discord.Embed(
            title=':oncoming_automobile: Type Racer Rankings [WPM]',
            description=f'{lb}')
        await ctx.send(embed=em)

    @commands.command(aliases=['give'])
    async def user_add(self, ctx, user: discord.Member, amount):

        if user == ctx.author:
            await ctx.send('You cannot give money to yourself dumbass.')

        else:
            with open('./cogs/Data/economy.json', 'r') as f:
                users = json.load(f)

            await self.check(users, user)

            curr_money = users[f'{ctx.author.id}']['money']
            if curr_money > int(amount):
                users[f'{ctx.author.id}']['money'] -= int(amount)
                users[f'{user.id}']['money'] += int(amount)

                await ctx.send(
                    f'**{ctx.author}** has transferred {int(amount)} 🥔 to {user.mention}'
                )

            else:
                await ctx.send('You don\'t have enought money dumbass')

            with open('./cogs/Data/economy.json', 'w') as f:
                json.dump(users, f, indent=4)

    @commands.command()
    async def admin_add(self, ctx, user: discord.Member, amount):

        if ctx.author.id == 305681776427139073 or ctx.author.id == 335808768979894283:
            with open('./cogs/Data/economy.json', 'r') as f:
                users = json.load(f)

            await self.check(users, user)

            users[f'{user.id}']['money'] += int(amount)

            await ctx.send(f"{amount} 🥔 added to {user}'s account")

            with open('./cogs/Data/economy.json', 'w') as f:
                json.dump(users, f, indent=4)

    @commands.command()
    async def admin_del(self, ctx, user: discord.Member, amount):

        if ctx.author.id == 305681776427139073 or ctx.author.id == 335808768979894283:
            with open('./cogs/Data/economy.json', 'r') as f:
                users = json.load(f)

            await self.check(users, user)

            users[f'{user.id}']['money'] -= int(amount)

            await ctx.send(f"{amount} 🥔 removed {user}'s account")

            with open('./cogs/Data/economy.json', 'w') as f:
                json.dump(users, f, indent=4)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            command = client.get_command('race')
            await ctx.send(
                f'**You are on cooldown!** Retry after `{round(command.get_cooldown_retry_after(ctx), 2)}` seconds [Due to rate-limit]'
            )


def setup(client):

    client.add_cog(Economy(client))

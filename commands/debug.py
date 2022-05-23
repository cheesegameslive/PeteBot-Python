from discord.ext import commands, tasks
from itertools import cycle
import discord

class ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.status = cycle(['j', 'morbius the videogame', 'morbius the movie','morbius the tv show'])
    
    @tasks.loop(minutes=30)
    async def change_status(self):
        # print('Changing status')
        await self.bot.change_presence(activity=discord.Game(next(self.status)))


    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print('pete is online')
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Pong {round(self.bot.latency * 1000)}ms',reference = ctx.message)

def setup(bot):
    bot.add_cog(ping(bot))
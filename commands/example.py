from discord.ext import commands

class example(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def test(self,ctx):
        await ctx.send('test',reference = ctx.message)

def setup(bot):
    bot.add_cog(example(bot))
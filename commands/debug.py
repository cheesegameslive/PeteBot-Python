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
    @commands.command()
    async def twitter(self,ctx):
        embed=discord.Embed(
        title="Text Formatting",
            url="https://realdrewdata.medium.com/",
            description="Here are some ways to format text",
            color=discord.Color.blue())
        embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://cdn-images-1.medium.com/fit/c/32/32/1*QVYjh50XJuOLQBeH_RZoGw.jpeg")
        embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
        embed.add_field(name="*Italics*", value="Surround your text in asterisks (\*)", inline=False)
        embed.add_field(name="**Bold**", value="Surround your text in double asterisks (\*\*)", inline=False)
        embed.add_field(name="__Underline__", value="Surround your text in double underscores (\_\_)", inline=False)
        embed.add_field(name="~~Strikethrough~~", value="Surround your text in double tildes (\~\~)", inline=False)
        embed.add_field(name="`Code Chunks`", value="Surround your text in backticks (\`)", inline=False)
        embed.add_field(name="Blockquotes", value="> Start your text with a greater than symbol (\>)", inline=False)
        embed.add_field(name="Secrets", value="||Surround your text with double pipes (\|\|)||", inline=False)
        embed.set_footer(text="Learn more here: realdrewdata.medium.com")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))
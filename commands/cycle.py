from discord.ext import commands
import discord
from PIL import Image
import os
import functions
import asyncio

client = discord.Client()
class cycle(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    async def cycle(self,ctx):
        args = ctx.message.content[len("$cycle"):].strip()
        # args = ctx.message.content.split("$cycle ")
        if len(args)>0:
            args = args.split(',')
            if len(args) <= len(functions.cycleTextPos):
                centerImg = None
                if len(ctx.message.attachments)>0:
                    await ctx.message.attachments[0].save(ctx.message.attachments[0].filename)
                    centerImg = Image.open(ctx.message.attachments[0].filename).convert('RGBA')
                    imgName = ctx.message.attachments[0].filename
                elif ctx.message.reference is not None:#if message was referenced
                    image_message = await ctx.fetch_message(ctx.message.reference.message_id)
                    if len(image_message.attachments)>0:#if referenced message has image
                        await image_message.attachments[0].save(image_message.attachments[0].filename)
                        centerImg = Image.open(image_message.attachments[0].filename).convert('RGBA')
                        imgName = image_message.attachments[0].filename
                await functions.cycleText(args,ctx.message.id,centerImage = centerImg)
                await ctx.message.channel.send(file=discord.File(f'cycleedit_{ctx.message.id}.png'),reference=ctx.message)
                os.remove(f"cycleedit_{ctx.message.id}.png")
                if centerImg is not None and os.path.exists(imgName): 
                    centerImg.close()
                    os.remove(imgName)
            else:
                msg = await ctx.message.channel.send("too many arguments", reference=ctx.message)
                await asyncio.sleep(5)
                await msg.delete()
        else:
            msg = await ctx.message.channel.send("too few arguments", reference=ctx.message)
            await asyncio.sleep(5)
            await msg.delete()

def setup(bot):
    bot.add_cog(cycle(bot))




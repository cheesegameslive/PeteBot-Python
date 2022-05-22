from discord.ext import commands
import discord
from PIL import Image
import functions
import os
import json
with open('config.json', 'r') as f:
    config = json.load(f)

bubble_img = Image.open(config['bubble_path']).convert("RGBA")

tenor = config['tenor']



client = discord.Client()
class bubble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.command()
    async def bubble(self,ctx):
        bottom_image = None
        if len(ctx.message.attachments)>0:
            img_name = ctx.message.attachments[0].filename
            await ctx.message.attachments[0].save(img_name)
            bottom_image = Image.open(img_name).convert('RGBA')
        elif ctx.message.reference is not None:#if message was referenced
            image_message = await ctx.fetch_message(ctx.message.reference.message_id)
            if len(image_message.attachments)>0:#if referenced message has image
                img_name = image_message.attachments[0].filename
                await image_message.attachments[0].save(img_name)
                bottom_image = Image.open(img_name).convert('RGBA')
            elif image_message.content.startswith('https://tenor.com'):
                img_name = await functions.get_gif(image_message.content)
                bottom_image = Image.open(img_name)
            elif image_message.content.startswith("https://media.discordapp.net"):
                img_name = image_message.content[-5:]

        if bottom_image is not None:
            size = os.stat(img_name).st_size
            if size>8e6:
                await ctx.message.channel.send("Too Large",reference=ctx.message)
            elif img_name[-3:]=="gif" :
                gif_name = functions.stackGif(bubble_img,bottom_image,1,img_name)
            elif img_name[-3:]=="png" or 'jpg':
                gif_name = functions.stackImage(bubble_img,bottom_image,1,img_name)
            await ctx.message.channel.send(file=discord.File(gif_name),reference=ctx.message)
            os.remove(gif_name)
            os.remove(img_name)

        else:
            await ctx.message.channel.send("Must ",reference=ctx.message)


def setup(bot):
    bot.add_cog(bubble(bot))
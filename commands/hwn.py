from discord.ext import commands
from PIL import Image
import functions,json
import discord 


class hwn(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def hwn(self,ctx):
        text = ctx.message.content[len("$hwn"):].strip()
        text = "he will never " + text
        image = None
        hwn = Image.open("images/hwn.png").convert("RGBA")
        if len(ctx.message.attachments)>0:
            img_name = ctx.message.attachments[0].filename
            await ctx.message.attachments[0].save(img_name)
            image = Image.open(img_name).convert('RGBA')
        elif ctx.message.reference is not None:#if message was referenced
            image_message = await ctx.fetch_message(ctx.message.reference.message_id)
            if len(image_message.attachments)>0:#if referenced message has image
                img_name = image_message.attachments[0].filename
                await image_message.attachments[0].save(img_name)
                image = Image.open(img_name).convert('RGBA')
            elif image_message.content.startswith('https://tenor.com'):
                img_name = await functions.get_gif(image_message.content)
                image = Image.open(img_name)
            elif image_message.content.startswith("https://media.discordapp.net"):
                img_name = image_message.content[-5:]
        if image and text is not None:
            hwn = functions.place_image(0,0,252,196,hwn,image,img_name)
            hwn = functions.place_text(400,15,hwn,text)
            hwn.save(img_name)
            await ctx.message.channel.send(file=discord.File(img_name),reference=ctx.message)

    @commands.command()
    async def pfft(self,ctx):
        image1 = image2 = None
        pfft = Image.open("images/pfft.png").convert("RGBA")
        if len(ctx.message.attachments)>0:
            img_name1 = ctx.message.attachments[0].filename
            await ctx.message.attachments[0].save(img_name1)
            image1 = Image.open(img_name1).convert('RGBA')
        if ctx.message.reference is not None:#if message was referenced
            image_message = await ctx.fetch_message(ctx.message.reference.message_id)
            if len(image_message.attachments)>0:#if referenced message has image
                img_name2 = image_message.attachments[0].filename
                await image_message.attachments[0].save(img_name2)
                image2 = Image.open(img_name2).convert('RGBA')
            elif image_message.content.startswith('https://tenor.com'):
                img_name2 = await functions.get_gif(image_message.content)
                image2 = Image.open(img_name2)
            elif image_message.content.startswith("https://media.discordapp.net"):
                img_name2 = image_message.content[-5:]
        if image1 and image2 is not None:
            image1 = functions.place_image(0,3,252,196,pfft,image1,img_name1)
            image1.save(img_name1)
            pfft = functions.stackImage(image2,image1,1,img_name1)
            await ctx.message.channel.send(file=discord.File(img_name1),reference=ctx.message)

def setup(bot):
    bot.add_cog(hwn(bot))
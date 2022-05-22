from PIL import Image
import os
import json
from discord.ext import commands

global sb
with open('config.json', 'r') as f:
    config = json.load(f)
with open('soundboard.json', 'r') as f:
    sb = json.load(f)

token = config['token']
prefix = config['prefix']
image_types = config['image_types']
sound_types = config['sound_types']

bubble = Image.open(config['bubble_path']).convert("RGBA")

import os
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

for filename in os.listdir('./commands'):#load all cogs
  if filename.endswith('.py'):
    bot.load_extension(f'commands.{filename[:-3]}')



bot.run(token)


# client = discord.Client()
# client.run(token)

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
    

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     else:
#         if message.content.startswith(f'{prefix}ping'):
#             await message.channel.send("pong",reference=message)
#             await functions.get_image(message,client)

#         #bubble command (DO NOT LOOK AT THIS CODE YOU'LL REGRET IT)
#         if message.content.startswith(f'{prefix}bubble'):
#             img = None
#             if message.content.startswith(f'{prefix}bubblew'):
#                 w = 1
#             else: w = 0
#             if message.reference is not None:#
#                 if message.reference.cached_message is None:
#                     channel = client.get_channel(message.reference.channel_id)
#                     message = await channel.fetch_message(message.reference.message_id)
#                 else:
#                     message = message.reference.cached_message

#             if 'http' in message.content.lower():#if it's a link
#                 # if message.content.split(" ")[1]!=None and message.content.split(" ")[1].startswith('http'):
#                 #     message.content = message.content.split(" ")[1]
#                 r = requests.get(message.content, stream = True)
#                 if r.status_code == 200 and (message.content.endswith("png") or message.content.endswith("gif")):
#                     r.raw.decode_content = True
#                     with open(message.content.split("/")[-1]+"",'wb') as f:
#                         shutil.copyfileobj(r.raw, f)
#                         img = Image.open(message.content.split("/")[-1])
#             if message.attachments != [] or img is not None:
#                 for attachment in message.attachments:
#                     if any(attachment.filename.lower().endswith(image) for image in image_types):
#                         await attachment.save(attachment.filename)
#                         img = Image.open(attachment.filename)
#                 if img.format == "GIF":
#                     functions.stackGif(bubble,img,w)
#                 elif img.format == "PNG":
#                     functions.stackImage(bubble,img,w).save('bubble.gif')
#                 if os.path.getsize('bubble.gif')/pow(10,6)>8:
#                     msg = await message.channel.send("too big",reference=message)
#                     await msg.delete()
#                 else: 
#                     await message.channel.send(file=discord.File('bubble.gif'),reference=message)
#                 img.close()
#                 if message.attachments!=[]:
#                     os.remove(message.attachments[0].filename)
#                 else:
#                     os.remove(message.content.split("/")[-1])
#                 os.remove("bubble.gif")
#             else:
#                 msg = await message.channel.send("no image or invalid")
#                 await asyncio.sleep(5)
#                 await msg.delete()
#     #play sounboard
#         if message.content.startswith(f'{prefix}sb'):
#             name = message.content.split(f'{prefix}sb ')
#             global sb
#             user = message.author
#             voice_channel = client.get_channel(user.voice.channel.id)
#             channel = None
        
#             if voice_channel is not None and name[1] in sb:
#                 msg = await message.channel.send(f"Playing sound {name[1]} in {voice_channel.name}")
#                 vc = await voice_channel.connect()
#                 vc.play(discord.FFmpegPCMAudio(sb[name[1]]))
#                 while vc.is_playing():
#                     await asyncio.sleep(5)
#                 await vc.disconnect()
#                 await message.delete()
#                 await msg.delete()
#             else:
#                 await message.add_reaction("❌")
#     #cycle
#         if message.content.lower().startswith(f'{prefix}cycle'):
#             args = message.content.split(f'{prefix}cycle ')
#             args = args[1].split(',')
#             centerImg = None
#             if len(args)<=4:
#                 # get the needed image
#                 if len(message.attachments)>0:
#                     await message.attachments[0].save(message.attachments[0].filename)
#                     centerImg = Image.open(message.attachments[0].filename).convert('RGBA')
#                 await functions.cycleText(args,centerImage = centerImg)
#                 await message.channel.send(file=discord.File('cycleedit.png'),reference=message)
#                 os.remove("cycleedit.png")
#                 if centerImg is not None:
#                     os.remove(message.attachments[0].filename)
#             else:
#                 msg = await message.channel.send("too many arguments", reference=message)
#                 await asyncio.sleep(5)
#                 await msg.delete()

            


# #add to soundboard
#         if message.content.startswith(f'{prefix}asb '):
#             role = discord.utils.get(message.author.roles, name="petemaster")
#             if role is not None and message.author.id == "145220382012604416":
#                 name = message.content.split(f'{prefix}asb ')
#                 if message.reference is not None:#
#                     if message.reference.cached_message is None:
#                         channel = client.get_channel(message.reference.channel_id)
#                         message = await channel.fetch_message(message.reference.message_id)
#                     else:
#                         message = message.reference.cached_message
#                 if message.attachments != [] and name[1] is not None:
#                     for attachment in message.attachments:
#                         if any(attachment.filename.lower().endswith(sound) for sound in sound_types):
#                             await attachment.save("sounds/" + attachment.filename)
#                     functions.append_record(name[1],"sounds/" + attachment.filename)
#                     sb = functions.reload_sb()
#                     await message.channel.send(f'Added your sound with label {name[1]}')

#                 else:
#                     await message.channel.send("no sound",reference=message)
#             else:
#                 await message.channel.send("oh you don't have the right",reference=message)
# #list soundboard
#         if message.content.startswith(f'{prefix}lsb'):
#             s=""
#             for n in sb:
#                 s+= n + "\n"
#             await message.channel.send(s,reference=message)






from PIL import Image
import os
import requests
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
tenor = config['tenor']

bubble = Image.open(config['bubble_path']).convert("RGBA")

r = requests.get(f"https://api.tenor.com/v1/anonid?&key={tenor}")

bot = commands.Bot(command_prefix='$')

for filename in os.listdir('./commands'):#load all cogs
  if filename.endswith('.py'):
    bot.load_extension(f'commands.{filename[:-3]}')



bot.run(token)



# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     else:
#         if message.content.startswith(f'{prefix}ping'):
#             await message.channel.send("pong",reference=message)
#             await functions.get_image(message,client)

#         
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






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

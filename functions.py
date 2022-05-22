from PIL import Image, ImageFont, ImageDraw, ImageSequence
import json
import textwrap
from gifpy import Gifpy
import urllib.request
import requests


with open('config.json', 'r') as f:
    config = json.load(f)
bubble = Image.open(config['bubble_path']).convert("RGBA")
tenor = config['tenor']


cycleTextPos = [
    # 1 entry
    [(525, 198)],
    # 2 entries
    [(525, 198),
    (479, 801)],
    # 3 entries
    [(520, 197),
    (790, 624),
    (195, 585)],
    # 4 entries
    [(513, 197),
    (801,511),
    (483, 804),
    (192, 511)]
]
    
fontSize = 40
lineSpace = 35
centerW = centerH = 400



async def cycleText(text,id,centerImage = None):
    global cycleTextPos
    textPos = cycleTextPos[len(text) - 1]
    img = Image.open(f"images/Cycle{len(text)}.png")
    I1 = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('arial.ttf', fontSize)
    if centerImage is not None:
        if centerImage.height > centerImage.width: # portrait
            scaledW = int(centerImage.width * (centerH / centerImage.height))
            imgX = int(img.width / 2 - int(scaledW / 2))
            imgY = int(img.height / 2 - int(centerH / 2))
            centerImage = centerImage.resize((scaledW, centerH))
            img.alpha_composite(centerImage,(imgX, imgY))
        else: # widescr
            scaledH = int(centerImage.height * (centerW / centerImage.width))
            imgX = int(img.width / 2 - int(centerW / 2))
            imgY = int(img.height / 2 - int(scaledH / 2))
            centerImage = centerImage.resize((centerW, scaledH))
            img.alpha_composite(centerImage,(imgX, imgY))
    for i in range(len(text)):
        t = text[i].strip()
        x,y = textPos[i]
        wrapped = textwrap.wrap(t,width=10)
        for j in range(len(wrapped)):
            wrapText = wrapped[j].strip()
            I1.text((x - myfont.getsize(wrapText)[0] / 2,
                            y - lineSpace * (len(wrapped) - 1) / 2 + lineSpace * (j - 1)),
                            wrapText,fill=(0,0,0),font = myfont)
    img.save(f"cycleedit_{id}.png")
    img.close()

def stackImage(topImg, botImg,w,name, resample=Image.BICUBIC, resize_big_image=True):
    botImg.convert("RGBA")
    _topImg = topImg
    _botImg = botImg
    if topImg.width == botImg.width:
        _topImg = topImg
        _botImg = botImg
    elif (((topImg.width > botImg.width) and resize_big_image) or
          ((topImg.width < botImg.width) and not resize_big_image)):
        _topImg = topImg.resize((botImg.width, int(topImg.height * botImg.width / topImg.width)), resample=resample)
        _botImg = botImg
    if w:
        dst = Image.new('RGBA', (_botImg.width, _botImg.height+ _topImg.height),color = 0xffffff)
        dst.paste(_botImg,(0,_topImg.height))
        dst.alpha_composite(_topImg)
        dst.save(f"bubble_{name}")
    else:
        _botImg.alpha_composite(_topImg)
        _botImg.save(f"bubble_{name}")
    return f"bubble_{name}"

def stackGif(topImg,backImg,w,name):
    frames = []
    name = f'bubble_{name}'
    topImg = topImg.resize((backImg.width,int(backImg.height/5)),resample=3)
    for frame in ImageSequence.Iterator(backImg):
        frame = frame.copy()
        if w:
            dst = Image.new('RGBA', (backImg.width, backImg.height+ topImg.height),color = 0xffffff)
            dst.paste(frame,(0,topImg.height))
            dst.alpha_composite(topImg)
        else:
            dst = Image.new('RGBA', (frame.width, frame.height))
            dst.paste(frame)
            dst.alpha_composite(topImg)
        frames.append(dst)
    frames[0].save(name, save_all=True, append_images=frames[1:],loop=1)
    return name

def append_record(name,file):
    listObj = []
    with open('soundboard.json', 'r') as fp:
        listObj = json.load(fp)
        listObj[name] = file
    with open('soundboard.json','w') as json_file:
        json.dump(listObj,json_file,indent=4,separators = (',',':'))

def reload_sb():
    with open('soundboard.json') as np:
        np_data = np.read()
    return json.loads(np_data)


async def get_gif(message):
    id = message[-8:]
    api_link = f"https://api.tenor.com/v1/gifs?ids={id}&key={tenor}"
    r = requests.get(api_link)
    gif_link = (json.loads(r.content)['results'][0]['media'][0]['gif']['url'])
    urllib.request.urlretrieve(gif_link,id+".gif")
    return id+".gif"



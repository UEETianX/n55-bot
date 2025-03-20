from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from nonebot.params import CommandArg
from nonebot.rule import startswith
import os
import random
import nonebot
import requests
from urllib import error
import random
import time
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd
import cv2
from io import BytesIO
import sys
from translate import Translator
import textwrap
from pathlib import Path

banu=on_command("巴努语",aliases={"巴奴语"},priority=1)

@banu.handle()
async def handle_function(args: Message = CommandArg()):
    args = args.extract_plain_text()
    def is_Chinese(word):
        for ch in word:
            if '\u4e00' <= ch <= '\u9fff':
                en = Translator(from_lang="ZH",to_lang="EN-US").translate(word)
                return en
        return word
    word = is_Chinese(args)
    word = textwrap.fill(word, width=50)
    fontpath = "C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/Banu-Regular.otf"
    font1 = ImageFont.truetype(fontpath,50)
    x0, y0, x1, y1=font1.getbbox(word)
    width, height = x1-x0, y1-y0
    if len(word) <= 50:
        img = Image.new("RGB",((width+40),(height+60)),(255,248,220))
    else:
        x = len(word.split("\n"))
        img = Image.new("RGB",((max([font1.getsize(p)[0] for p in word.split("\n")])+40),(60*x+60)),(255,248,220))
    img.save("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/p.jpg")
    date = cv2.imread("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/p.jpg", cv2.IMREAD_UNCHANGED)
    b,g,r,a = 19,69,139,0
    img_pil = Image.fromarray(date)
    draw = ImageDraw.Draw(img_pil)
    draw.text((20,30),word,font=font1,fill=(b,g,r,a))
    img = np.array(img_pil)
    cv2.imwrite('C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/p.jpg', img)    
    path = os.path.split(os.path.realpath(__file__))[0] + '/p.jpg'
    print("sus banu")
    await banu.finish(MessageSegment.file_image(Path(__file__).parent / path))
    

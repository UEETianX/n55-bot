from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from nonebot.params import CommandArg
from nonebot.rule import startswith
import requests
import os
import random
import nonebot
import re
import urllib
import requests
from urllib import error
import random
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd
import cv2
from io import BytesIO
import sys

roll=on_command("roll",priority=1)

@roll.handle()
async def handle_function(event:Event,args: Message = CommandArg()):
    args = str(args)
    user_id = str(event.user_id)
    user_nick = str(event.card)
    if str(user_nick) == "None":
        user_nick = str(event.nickname)
    result = re.split(r'\W+', args)
    if args=="":
        result = ["100"]
    if len(result) ==1:
        sequence = range(1, int(result[0])+1)
        a=random.choice(sequence)
        msg=user_nick+"的取值："+str(a)
    elif len(result) ==2:
        sequence = range(int(result[0]), int(result[1])+1)
        a=random.choice(sequence)
        msg=user_nick+"的取值："+str(a)
    else:
        sequence = range(int(result[0]), int(result[1])+1)
        a=random.sample(sequence, int(result[2]))
        msg=user_nick+"的取值："+", ".join(map(str, a))
    await roll.finish(msg)

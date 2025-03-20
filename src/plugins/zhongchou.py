from nonebot.adapters.satori.event import MessageEvent
from nonebot.adapters.satori.message import MessageSegment
from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from nonebot.params import CommandArg
import os
import urllib.request
import requests
from urllib import error
from bs4 import BeautifulSoup
import time
from time import sleep
from PIL import ImageFont, ImageDraw, Image
import cv2
from fake_useragent import UserAgent
import numpy as np 
from io import BytesIO
from lxml import etree
import pandas as pd
import datetime

zhongchou=on_command("众筹",priority=1)

@zhongchou.handle()
async def handle_function(args: Message = CommandArg()):
    url='https://api.star-citizen.wiki/api/v2/stats/latest'
    request = requests.get(url)
    a=request.json()
    n=float(a['data']['funds'])/a['data']['fans']
    await zhongchou.finish("目前众筹金额为：" + a['data']['funds'] + "$\n参与的玩家有：" + str(a['data']['fans']) + "人\n平均消费："+str('%.2f'%n)+"$")

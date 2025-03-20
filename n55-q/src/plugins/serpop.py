from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from time import sleep
import datetime
from pytz import timezone
import pandas as pd
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import os
import requests
import sys
from io import BytesIO
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib import error
import urllib
from pathlib import Path
import json

serpop=on_command("服务器",priority=1)
@serpop.handle()
async def handle_function(bot:Bot,event:Event,state:T_State):
    def request_html(url):
        ua=UserAgent()
        headers={'User-Agent':str(UserAgent("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/fake_useragent_0.1.11.json").random)}
        request = urllib.request.Request(url, headers=headers)
        return request

    url='https://status.robertsspaceindustries.com/index.json'
    request = request_html(url)
    html = urllib.request.urlopen(request).read().decode('utf8')
    soup =json.loads(html)
    def trans(x):
        if x.lower() =="operational":
            info = "正常"
        elif x.lower() =="partial outage":
            info = "部分中断"
        elif x.lower() =="under maintenance":
            info = "维护中"
        elif x.lower() =="degraded performance":
            info = "性能下降"
        elif x.lower() =="major outage":
            info = "重大中断"
        elif x.lower() =="degraded":
            info = "性能下降"
        return info

    await serpop.finish("当前服务器状态使用时差推算已无意义，建议广加好友，右键好友加入更为稳妥。\n平台状态："+trans(soup['systems'][0]['status'])+"\nPU状态："+trans(soup['systems'][1]['status'])+"\nAC状态："+trans(soup['systems'][2]['status']))

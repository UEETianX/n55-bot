from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event
from nonebot.params import CommandArg
from nonebot.rule import startswith
import urllib.request
import requests
from urllib import error
import random
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
import numpy as np 
from io import BytesIO
import ssl

banben=on_command("游戏版本",aliases={"版本"},priority=1)

@banben.handle()
async def handle_function():
    await banben.finish("PU:4.0")
    def request_html(url):
        ua=UserAgent()
        headers={'User-Agent':str(UserAgent("C:\\Users\\Administrator\\Desktop\\Qbot\\n55\\src\\plugins/fake_useragent_0.1.11.json").random)}
        request = urllib.request.Request(url, headers=headers)
        return request
    ssl._create_default_https_context = ssl._create_unverified_context
    url='https://citizenwiki.cn/'
    request = request_html(url)
    html = urllib.request.urlopen(request).read().decode('utf8')
    soup =BeautifulSoup(html, 'lxml')
    textlist = soup.select('.home-gamestatus-patch__name')
    text=[p.get_text().split("\n") for p in textlist]
    titlelist = soup.select('.home-badge')
    title=[p.get_text().split("\n") for p in titlelist]
    text = title[0][0]+" "+text[0][0]+" → "+title[1][0]+" "+text[1][0]
    await banben.finish(text)

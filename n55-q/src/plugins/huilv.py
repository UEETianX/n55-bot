import contextlib
from typing import Any, Dict
from nonebot.adapters import Bot,Event
from nonebot import on_endswith, on_fullmatch, on_regex
from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot.params import Endswith, RegexDict
import urllib.request
import requests
from urllib import error
import random
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
from PIL import ImageFont, ImageDraw, Image
import numpy as np 
from io import BytesIO
import xml.etree.ElementTree as ET
import os
import ssl
from pathlib import Path

exchange = on_regex(r"(?P<amount>^\d+\.?\d*)(?P<currency>[\u4e00-\u9fff]{1,2}$)")


@exchange.handle()
async def _(event:MessageEvent,matched: Dict[str, Any] = RegexDict()) -> None:
    def request_html(url):
        ua=UserAgent()
        headers={'User-Agent':str(UserAgent("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/fake_useragent_0.1.11.json").random)}
        ssl._create_default_https_context = ssl._create_unverified_context
        request = urllib.request.Request(url, headers=headers)
        return request
    url='https://www.boc.cn/sourcedb/whpj/index.html'
    url1='https://www.boc.cn/sourcedb/whpj/index_1.html'
    request = request_html(url)
    request1 = request_html(url1)
    html = urllib.request.urlopen(request).read().decode('utf8')
    html1 = urllib.request.urlopen(request1).read().decode('utf8')
    soup =BeautifulSoup(html, 'lxml')
    soup1 =BeautifulSoup(html1, 'lxml')
    list_name = soup.select('td')
    list_name1 = soup1.select('td')
    name=[p.get_text() for p in list_name]
    name1=[p.get_text() for p in list_name1]
    name = name + name1
    num = float(matched["amount"])
    cont = matched["currency"]
    if cont == "美元" or cont == "美刀" or cont == "刀" or cont == "美金":
        CN = float(name[name.index("美元")+3])/100
    elif cont == "欧元" or cont == "欧":
        CN = float(name[name.index("欧元")+3])/100
    elif cont == "日元":
        CN = float(name[name.index("日元")+3])/100
    elif cont == "英镑":
        CN = float(name[name.index("英镑")+3])/100
    elif cont == "卢布":
        CN = float(name[name.index("卢布")+3])/100
    elif cont == "韩元":
        CN = float(name[name.index("韩国元")+3])/100
    elif cont == "人民币" or cont == "元" or cont == "块钱":
        CN = float(name[name.index("美元")+3])/100
        result = float(num)/CN
        msg = str('%.2f'%result)+"美元"
        await exchange.finish(msg)
    try:
        result = CN*float(num)
        print(str('%.2f'%result)+cont)
        msg = str('%.2f'%result)+"人民币"
        if int(result)<3500:
            await exchange.finish(msg)
        elif int(result) <7000:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/huilv500.jpg'
            print(path)
            await exchange.finish(msg +MessageSegment.file_image(Path(__file__).parent / path))
        else:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/maichuan.jpg'
            print(path)
            await exchange.finish(msg +MessageSegment.file_image(Path(__file__).parent / path))
    except:
        pass
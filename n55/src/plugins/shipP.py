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

shipP=on_command("价格",priority=1)

@shipP.handle()
async def handle_function(args: Message = CommandArg()):
    df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/船只价格表.csv',index_col=None,header=None)
    df.index=df.loc[:,0]
    df.columns=["ship","a","P"]
    #df["info"] = ["	$".join(i) for i in df.values]
    df.p=pd.to_numeric(df.P,errors='coerce')
    args = str(args)
    if args == "表":
        await shipP.finish("查[美元/游戏币]价格表")
    if len(pd.to_numeric(re.split("-| |_|,|，",args)))==1:
        arg1 = pd.to_numeric(re.split("-| |_|,|，",args)[0])
        data = df[(df.p==arg1)]
    else:
        try:
            arg1 = pd.to_numeric(re.split("-| |_|,|，",args)[0])
            arg2 = pd.to_numeric(re.split("-| |_|,|，",args)[1])
        except:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/查找失败.jpg'
            await shipP.finish("格式输错了吧~查价格100-150就行啦~"+MessageSegment.image(path))
        data = df[(df.p>=arg1) & (df.p<=arg2)]
    text1 = args + "(*为常驻)：\n" + "\n".join(data["ship"].tolist())
    text2 = "\n".join([str(i) for i in data["P"].tolist()])
    text3 = "\n".join([str(i) for i in data["a"].tolist()])
    x =data.shape[0]
    img = Image.new("RGB",(460,(70+38*x)),(255,248,220))
    img.save("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/p.jpg")
    date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/p.jpg", cv2.IMREAD_UNCHANGED)
    fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/1637505678825667.ttc"
    b,g,r,a = 19,69,139,0
    b1,g1,r1,a1 = 0,0,255,0
    font1 = ImageFont.truetype(fontpath,50)
    font2 = ImageFont.truetype(fontpath,40)
    img_pil = Image.fromarray(date)
    draw = ImageDraw.Draw(img_pil)
    draw.text((20,20),text1,font=font2,fill=(b,g,r,a))
    draw.text((350,63),text2,font=font2,fill=(b,g,r,a))
    draw.text((5,63),text3,font=font2,fill=(b1,g1,r1,a1))
#    for y in range(0, x):
#        draw.line([(170, (97+38*y)), (290,(97+38*y))], fill=(b,g,r,a),width = 3)
#        print(y)
    img = np.array(img_pil)
    cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/p.jpg', img)
    path = os.path.split(os.path.realpath(__file__))[0] + '/p.jpg'
    await shipP.finish(MessageSegment.image(path))

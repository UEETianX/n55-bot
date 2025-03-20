from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from nonebot.params import CommandArg
import requests
import os
import random
import nonebot
import urllib
import requests
from urllib import error
import random
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
from io import BytesIO
import sys
import pandas as pd
import string

yaoqingma=on_command("邀请码",priority=1)

@yaoqingma.handle()
async def handle_function(event: Event,args: Message = CommandArg()):
    if str(type(event)) =="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
        group_id = "A"
        user_id =event.author.user_openid
    else:
        group_id = event.group_openid
        user_id = event.author.member_openid
    print(user_id)
    df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\Qbot/n55-q/src/plugins/yaoqingma.csv',index_col=None,header=None)
    df.index=df.loc[:,0]
    df.columns=["ID","STAR"]
    
    args = str(args)
    print(df)
    print(args)
    print(user_id)
    print(df.index.tolist())
    if args and args.startswith("录入"):
        STAR = str(args.split("录入")[1])
        STAR=" ".join(STAR.split(",")).replace('查邀请码', '')
        if STAR == "":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/吃雪糕.jpg'
            await yaoqingma.finish("录入后面记得加内容啊"+MessageSegment.image(path))
        print(STAR)
        print(str(df.ID.tolist()))
        print(str(user_id) in str(df.ID.tolist()))
        if str(user_id) in str(df.ID.tolist()):
            df.loc[df.ID == str(user_id),"STAR"] = STAR
            df.to_csv('C:\\Users\\Administrator\\Desktop\\Qbot/n55-q/src/plugins/yaoqingma.csv',index = None,header = None)
            print("loc")
        else:
            df = df._append(pd.Series({"ID":user_id,"STAR":STAR},name=user_id))
            df.to_csv('C:\\Users\\Administrator\\Desktop\\Qbot/n55-q/src/plugins/yaoqingma.csv',index = None,header = None)
            print("append")
        print(df)
        await yaoqingma.finish("邀请码已录入")
    else:
        if user_id in str(df.ID.tolist()):
            msg = str(df.loc[df.ID == str(user_id),"STAR"].tolist()[0])
        else:
            msg = "尚未记录你的邀请码，请输入[查邀请码录入XXX]后使用本命令调用"
        await yaoqingma.finish(msg)

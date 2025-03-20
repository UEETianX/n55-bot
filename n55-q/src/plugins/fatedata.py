from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
import datetime
import math
import time
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import os
from pathlib import Path

FATEDATE=on_command("天命节日",aliases={"舰队节日"},priority=1)

@FATEDATE.handle()
async def handle_function(bot:Bot,event:Event,state:T_State):
    if str(type(event)) =="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
        await FATEDATE.finish("私聊不支持此功能")
    def yearadd(day1,day2):
        day1 = day1 + relativedelta(years=(day2.year-1))
        if day1<day2:
            day1 = day1 + relativedelta(years=1)
        days = day1 - day2
        return days
    group_id = event.group_openid
    if group_id == "955342491" or group_id == "881232934" or group_id == "473081444":
        fatedate1 = datetime.datetime(1, 3, 18, 0, 0, 0)
        fatedate2 = datetime.datetime(2021, 3, 18, 0, 0, 0)
        today = datetime.datetime.now()
        date1 = yearadd(fatedate1,today)
        date2 = today-fatedate2
        day1 = date1.days
        day2 = date2.days
        text1 = "距离天命舰队成立周年庆还有："
        text2 = "天命舰队已成立"+str(day2)+"天"
        date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/fatedate.png", cv2.IMREAD_UNCHANGED)
    elif group_id == "472786437" or group_id == "691702096" or group_id == "929172498" or group_id == "729806532":  
        fatedate1 = datetime.datetime(1, 2, 8, 0, 0, 0)
        fatedate2 = datetime.datetime(2020, 2, 8, 0, 0, 0)
        today = datetime.datetime.now()
        date1 = yearadd(fatedate1,today)
        date2 = today-fatedate2
        day1 = date1.days
        day2 = date2.days
        text1 = "距离深航舰队成立周年庆还有："
        text2 = "深航舰队已成立"+str(day2)+"天"
        date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/shenhangdate.png", cv2.IMREAD_UNCHANGED)
    else:
        await FATEDATE.finish("本群尚未设置")

    hour1 = int(date1.seconds/3600)
    min1 = int((date1.seconds/3600-hour1)*60)
    text3 = str(day1)+"天"+str(hour1)+"小时"+str(min1)+"分钟"
    fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/1637505678825667.ttc"
    b,g,r,a = 240,250,255,0
    font1 = ImageFont.truetype(fontpath,40)
    img_pil = Image.fromarray(date)
    draw = ImageDraw.Draw(img_pil)
    x0, y0, x1, y1=font1.getbbox(text2)
    w, h = x1-x0, y1-y0
    draw.text((365-w/2,50),text2,font=font1,fill=(b,g,r,a))
    x0, y0, x1, y1=font1.getbbox(text1)
    w, h = x1-x0, y1-y0
    draw.text((365-w/2,120),text1,font=font1,fill=(b,g,r,a))
    x0, y0, x1, y1=font1.getbbox(text3)
    w, h = x1-x0, y1-y0
    draw.text((365-w/2,170),text3,font=font1,fill=(b,g,r,a))
    img = np.array(img_pil)
    cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/fatedate.jpg', img)
    path = os.path.split(os.path.realpath(__file__))[0] + '/fatedate.jpg'
    await FATEDATE.finish(MessageSegment.file_image(Path(__file__).parent / path))

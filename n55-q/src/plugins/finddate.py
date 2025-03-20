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

FINDDATE=on_command("倒计时",aliases={"节日"},priority=1)

@FINDDATE.handle()
async def handle_function(bot:Bot,event:Event,state:T_State):
    today = datetime.datetime.now()
    huohong = datetime.datetime(1, 1, 29, 0, 0, 0)
    airen = datetime.datetime(1, 2, 14, 0, 0, 0)
    xingyun = datetime.datetime(1, 3, 15, 0, 0, 0)
    jiandui = datetime.datetime(1, 5, 18, 0, 0, 0)
    waixing = datetime.datetime(1, 6, 14, 0, 0, 0)
    dianji = datetime.datetime(1, 7, 13, 0, 0, 0)
    bis = datetime.datetime(1, 8, 16, 0, 0, 0)
    haidao = datetime.datetime(1, 9, 16, 0, 0, 0)
    gongmin = datetime.datetime(1, 10,19, 17, 0, 0)
    zhounian = datetime.datetime(1, 11, 23, 0, 0, 0)
    guangdeng = datetime.datetime(1, 12, 13, 0, 0, 0)
    def yearadd(day1,day2):
        day1 = day1 + relativedelta(years=(day2.year-1))
        if day1<day2:
            day1 = day1 + relativedelta(years=1)
        days = (day1 - day2).days
        hours = int((day1 - today).seconds/3600)
        return days,hours

    day_huohong,hours_huohong = yearadd(huohong,today)
    day_aireng,hours_aireng = yearadd(airen,today)
    day_xingyun,hours_xingyun = yearadd(xingyun,today)
    day_jiandui,hours_jiandui = yearadd(jiandui,today)
    day_waixing,hours_waixing = yearadd(waixing,today)
    day_dianji,hours_dianji = yearadd(dianji,today)
    day_bis,hours_bis = yearadd(bis,today)
    day_haidao,hours_haidao = yearadd(haidao,today)
    day_gongmin,hours_gongmin = yearadd(gongmin,today)
    day_zhounian,hours_zhounian = yearadd(zhounian,today)
    day_guangdeng,hours_guangdeng = yearadd(guangdeng,today)
    df = {"a":["火红节","爱人节","幸运星","舰队周","外星周","奠基节","Bis投票","海盗节","公民控","周年庆","光灯节"],"b":[day_huohong,day_aireng,day_xingyun,day_jiandui,day_waixing,day_dianji,day_bis,day_haidao,day_gongmin,day_zhounian,day_guangdeng],"c":[hours_huohong,hours_aireng,hours_xingyun,hours_jiandui,hours_waixing,hours_dianji,hours_bis,hours_haidao,hours_gongmin,hours_zhounian,hours_guangdeng]}
    df = pd.DataFrame(df)
    df = df.sort_values(by="b",ascending=True)
    date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot/n55-q/src/plugins/date.png", cv2.IMREAD_UNCHANGED)

    text1 = "距离" + str(df.iloc[0,0]) + "还有 " + str(df.iloc[0,1]) + " 天 "+ str(df.iloc[0,2])  + " 小时"
    text2 = str(df.iloc[1,0]) + " " + str(df.iloc[1,1]) + " 天"
    text3 = str(df.iloc[2,0]) + " " + str(df.iloc[2,1]) + " 天"
    text4 = str(df.iloc[3,0]) + " " + str(df.iloc[3,1]) + " 天"
    text5 = str(df.iloc[4,0]) + " " + str(df.iloc[4,1]) + " 天"
    text6 = str(df.iloc[5,0]) + " " + str(df.iloc[5,1]) + " 天"
    text7 = str(df.iloc[6,0]) + " " + str(df.iloc[6,1]) + " 天"
    text8 = str(df.iloc[7,0]) + " " + str(df.iloc[7,1]) + " 天"
    text9 = str(df.iloc[8,0]) + " " + str(df.iloc[8,1]) + " 天"
    text10 = str(df.iloc[9,0]) + " " + str(df.iloc[9,1]) + " 天"
    text11 = str(df.iloc[10,0]) + " " + str(df.iloc[10,1]) + " 天"
    text12 = "现在时间：" + str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日"+str(today.hour).rjust(2,'0')+":"+str(today.minute).rjust(2,'0')+":"+str(today.second).rjust(2,'0')
    text13 = "by: UEE_TianXing"
    fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot/n55-q/src/plugins/1637505678825667.ttc"
    b,g,r,a = 19,69,139,0
    font1 = ImageFont.truetype(fontpath,70)
    font2 = ImageFont.truetype(fontpath,50)
    font3 = ImageFont.truetype(fontpath,35)
    img_pil = Image.fromarray(date)
    draw = ImageDraw.Draw(img_pil)
    x0, y0, x1, y1=font1.getbbox(text1)
    w,h =x1-x0, y1-y0
    draw.text((535-w/2,160),text1,font=font1,fill=(b,g,r,a))
    draw.text((150,350),text2,font=font2,fill=(b,g,r,a))
    draw.text((570,350),text3,font=font2,fill=(b,g,r,a))
    draw.text((150,490),text4,font=font2,fill=(b,g,r,a))
    draw.text((570,490),text5,font=font2,fill=(b,g,r,a))
    draw.text((150,630),text6,font=font2,fill=(b,g,r,a))
    draw.text((570,630),text7,font=font2,fill=(b,g,r,a))
    draw.text((150,770),text8,font=font2,fill=(b,g,r,a))
    draw.text((570,770),text9,font=font2,fill=(b,g,r,a))
    draw.text((150,910),text10,font=font2,fill=(b,g,r,a))
    draw.text((570,910),text11,font=font2,fill=(b,g,r,a))
    x0, y0, x1, y1=font2.getbbox(text12)
    w,h =x1-x0, y1-y0
    draw.text((535-w/2,1080),text12,font=font2,fill=(b,g,r,a))
    draw.text((780,1000),text13,font=font3,fill=(b,g,r,a))
    img = np.array(img_pil)
    cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot/n55-q/src/plugins/date.jpg', img)
    path = os.path.split(os.path.realpath(__file__))[0] + '/date.jpg'
    await FINDDATE.finish(MessageSegment.file_image(Path(__file__).parent / path)+"因CIG没有节日预告，所以日期均为去年日期参考。\n如发现日期相关公告会第一时间更改，故日期不准或突然改动是正常现象。")





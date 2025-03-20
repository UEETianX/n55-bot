from nonebot.adapters.satori.event import MessageEvent
from nonebot.adapters.satori.message import MessageSegment
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

DFS1=on_command("S1量子",aliases={"s1量子"},priority=1)

@DFS1.handle()
async def handle_function(args: Message = CommandArg()):
    print(args)
    arg = args.extract_plain_text()
    args = pd.to_numeric(args.extract_plain_text())
    a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    df = pd.DataFrame(a)
    df = df.sort_values(by=['DS'],ascending=True)
    x =df.shape[0]
    print(df)
    img = Image.new("RGB",(850,(170+100*x)),(255,248,220))
    img.save("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png")
    date = cv2.imread("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png", cv2.IMREAD_UNCHANGED)
    fontpath = "C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/1637505678825667.ttc"
    b,g,r,a = 19,69,139,0
    font1 = ImageFont.truetype(fontpath,50)
    font2 = ImageFont.truetype(fontpath,40)
    img_pil = Image.fromarray(date)
    draw = ImageDraw.Draw(img_pil)
    draw.text((100,50),"S1量子模拟" + arg + "量子油行驶距离",font=font2,fill=(b,g,r,a))
    for i in np.arange(1,x+1):
        #if str(df.iloc[i-1,0])[-1] =="返":
        #    draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(0,128,0,0))
        #    draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(0,128,0,0), width = 20)
        if ("赫-" in df.iloc[i-1,0]) | ("十-" in df.iloc[i-1,0]) | ("微-" in df.iloc[i-1,0]):
            draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(211,0,148,0))
            draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(211,0,148,0), width = 20)
        else:
            draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(b,g,r,a))
            draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(b,g,r,a), width = 20)
    img = np.array(img_pil)
    cv2.imwrite('C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png', img)
    path = os.path.split(os.path.realpath(__file__))[0] + '/DS.png'
    await DFS1.finish(MessageSegment.image(path=path))
    

DFS2=on_command("S2量子",aliases={"s2量子"},priority=1)

@DFS2.handle()
async def handle_function(args: Message = CommandArg()):
    arg = args.extract_plain_text()
    args = pd.to_numeric(args.extract_plain_text())
    a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    df = pd.DataFrame(a)
    df = df.sort_values(by=['DS'],ascending=True)
    x =df.shape[0]
    img = Image.new("RGB",(850,(170+100*x)),(255,248,220))
    img.save("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png")
    date = cv2.imread("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png", cv2.IMREAD_UNCHANGED)
    fontpath = "C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/1637505678825667.ttc"
    b,g,r,a = 19,69,139,0
    font1 = ImageFont.truetype(fontpath,50)
    font2 = ImageFont.truetype(fontpath,40)
    img_pil = Image.fromarray(date)
    draw = ImageDraw.Draw(img_pil)
    draw.text((100,50),"S2量子模拟" + arg + "量子油行驶距离",font=font2,fill=(b,g,r,a))
    for i in np.arange(1,x+1):
        #if str(df.iloc[i-1,0])[-1] =="返":
        #    draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(0,128,0,0))
        #    draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(0,128,0,0), width = 20)
        if ("赫-" in df.iloc[i-1,0]) | ("十-" in df.iloc[i-1,0]) | ("微-" in df.iloc[i-1,0]):
            draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(211,0,148,0))
            draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(211,0,148,0), width = 20)
        else:
            draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(b,g,r,a))
            draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(b,g,r,a), width = 20)
    img = np.array(img_pil)
    cv2.imwrite('C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png', img)
    path = os.path.split(os.path.realpath(__file__))[0] + '/DS.png'
    await DFS2.finish(MessageSegment.image(path=path))


DFS3=on_command("S3量子",aliases={"s3量子"},priority=1)

@DFS3.handle()
async def handle_function(args: Message = CommandArg()):
    arg = args.extract_plain_text()
    args = pd.to_numeric(args.extract_plain_text())
    a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Erebos 102k km/s","民B Impulse 114k km/s","民B Ranger 106k km/s","民B Tyche 98k km/s","民C Fissure 107k km/s","民C Metis 93k km/s","民C Wanderer 100k km/s","民D Drifter 94k km/s","民D Echo 102k km/s","工B Agni 62k km/s","工C Kama 60k km/s","工D Vesta 54k km/s","军A TS-2 208k km/s","军B Balandin 199k km/s","军C Pontes 189k km/s"],'DS':[23,32,39,43,58,60,int(args/49.59),int(args/74.7),int(args/61.18),int(args/54.1),int(args/70.2),int(args/59.89),int(args/64.4),int(args/66.33),int(args/49.59),int(args/36.06),int(args/38.64),int(args/39.93),int(args/141.68),int(args/135.24),int(args/122.36)]}
    df = pd.DataFrame(a)
    df = df.sort_values(by=['DS'],ascending=True)
    x =df.shape[0]
    img = Image.new("RGB",(850,(170+100*x)),(255,248,220))
    img.save("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png")
    date = cv2.imread("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png", cv2.IMREAD_UNCHANGED)
    fontpath = "C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/1637505678825667.ttc"
    b,g,r,a = 19,69,139,0
    font1 = ImageFont.truetype(fontpath,50)
    font2 = ImageFont.truetype(fontpath,40)
    img_pil = Image.fromarray(date)
    draw = ImageDraw.Draw(img_pil)
    draw.text((100,50),"S3量子模拟" + arg + "量子油行驶距离",font=font2,fill=(b,g,r,a))
    for i in np.arange(1,x+1):
        #if str(df.iloc[i-1,0])[-1] =="返":
        #    draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(0,128,0,0))
        #    draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(0,128,0,0), width = 20)
        if ("赫-" in df.iloc[i-1,0]) | ("十-" in df.iloc[i-1,0]) | ("微-" in df.iloc[i-1,0]):
            draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(211,0,148,0))
            draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(211,0,148,0), width = 20)
        else:
            draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(b,g,r,a))
            draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(b,g,r,a), width = 20)
    img = np.array(img_pil)
    cv2.imwrite('C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png', img)
    path = os.path.split(os.path.realpath(__file__))[0] + '/DS.png'
    await DFS3.finish(MessageSegment.image(path=path))




DFship=on_command("量子",priority=1)

@DFship.handle()
async def handle_function(args: Message = CommandArg()):
    arg = args.extract_plain_text()
    if arg =="引擎":
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/量子引擎.png'
        await DFship.finish(MessageSegment.image(path=path))
    if arg.lower() in str(["大青椒","桑托起亚","剃刀","剃刀EX","剃刀LX","325a","350r","箭头","极光CL","极光ES","极光LN","极光MR","复仇","复仇泰坦","复仇追猎","复仇术士","刀锋","掠夺者","大黄蜂","F7C","追黄","超黄","普黄","隐黄","角斗士","短剑","长刀","猎鹰","信使","飓风","卡图","M50","野马阿尔法","野马德尔塔","野马伽马","野马欧米伽","勘探者","信赖","信赖基础","信赖武装","信赖新闻","信赖科考","军刀","军刀彗星","军刀渡鸦","天蝎","天蝎座","死链","利爪","利爪伯劳","秃鹫"]).lower():
        args = 583
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["F7CMK2"]).lower():
        args = 600
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["85X"]).lower():
        args = 625
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["C8","双鱼座","C8X","C8R"]).lower():
        args = 645
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["300i"]).lower():
        args = 680
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["100i","125a","135c","极光LX","野马贝塔"]).lower():
        args = 700
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["游牧"]).lower():
        args = 771
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["蝎心","电蝎"]).lower():
        args = 800
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["315p"]).lower():
        args = 830
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["水龟"]).lower():
        args = 950
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["螳螂"]).lower():
        args = 1000
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["日蚀"]).lower():
        args = 1167
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["小刀","小刀侦察"]).lower():
        args = 1960
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["速伦"]).lower():
        args = 2900
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["F8C"]).lower():
        args = 2500
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}
    elif arg.lower() in str(["货A"]).lower():
        args = 10000
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Atlas 152k km/s","民B Burst 170k km/s","民B Hyperlon 146k km/s","民B Voyage 158k km/s","民C Eos 139k km/s","民C Expedition 149k km/s","民C Rush 160k km/s","民D Flood 152k km/s","民D Wayfare 140k km/s","竞B FoxFire 105k km/s","竞C LightFire 90k km/s","工B Colossus 93k km/s","工C Goliath 90k km/s","工D Vulcan 81k km/s","军A VK-00 283k km/s","军B Siren 269k km/s","军C Beacon 254k km/s","隐A Spectre 202k km/s","隐B Zephyr 187k km/s","隐C Drift 172k km/s"],'DS':[23,32,39,43,58,60,int(args/7.55),int(args/11.37),int(args/8.23),int(args/9.11),int(args/9.11),int(args/9.8),int(args/10.68),int(args/10.09),int(args/10.09),int(args/5.88),int(args/4.9),int(args/5.49),int(args/5.8),int(args/6.08),int(args/21.56),int(args/20.58),int(args/18.62),int(args/18.62),int(args/17.64),int(args/16.66)]}

    if arg.lower() in str(["弯刀","黑弯刀","蓝弯刀","钢弯刀","红弯刀","自由基础","自由枪骑兵","自由","自由MAX","自由MIS","徘徊者","徘徊","报复","报复基础","报复轰炸","女武神","瓦尔基里","先锋","先锋哨兵","先锋重装","先锋典狱长","先锋先驱"]).lower():
        args = 2500
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["巴卫","巴努防卫者"]).lower():
        args = 2750
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["鼹鼠"]).lower():
        args = 2759
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["600i","600i探索","600i旅游","星座","金牛座","凤凰座","天鹰座","仙女座"]).lower():
        args = 3000
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["A1","C1"]).lower():
        args = 3750
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["400i"]).lower():
        args = 4920
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["战神","战神地狱","战神离子","白战神","黑战神","自由DUR"]).lower():
        args = 5000
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["救赎","救赎者"]).lower():
        args = 5700
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["海盗船"]).lower():
        args = 6900
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["水星","墨丘利","水星跑者"]).lower():
        args = 9740
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}
    elif arg.lower() in str(["木筏"]).lower():
        args = 27585
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Hemera 127k km/s","民B Aither 122k km/s","民B Flash 142k km/s","民B Sojourn 132k km/s","民C Khaos 116k km/s","民C Odyssey 125k km/s","民C Torrent 133k km/s","民D Cascade 127k km/s","民D Quest 117k km/s","竞B SunFire 87k km/s","竞C SparkFire 75k km/s","工B Huracan 77k km/s","工C Bolon 75k km/s","工D Yaluk 67k km/s","军A XL-1 261k km/s","军B Yeager 249k km/s","军C Crossfield 236k km/s","隐A Spicule 168k km/s","隐B Bolt 156k km/s","隐C Nova 143k km/s"],'DS':[23,32,39,43,58,60,int(args/8.39),int(args/9.16),int(args/12.64),int(args/10.36),int(args/10.14),int(args/10.9),int(args/11.88),int(args/11.23),int(args/11.23),int(args/6.54),int(args/5.45),int(args/6.1),int(args/6.54),int(args/6.76),int(args/23.98),int(args/22.89),int(args/20.71),int(args/20.71),int(args/19.62),int(args/18.53)]}

    if arg.lower() in str(["毛虫","锤头鲨","回收者","星际远航者","星际远航者双子座","军油","民油"]).lower():
        args = 11000
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Erebos 102k km/s","民B Impulse 114k km/s","民B Ranger 106k km/s","民B Tyche 98k km/s","民C Fissure 107k km/s","民C Metis 93k km/s","民C Wanderer 100k km/s","民D Drifter 94k km/s","民D Echo 102k km/s","工B Agni 62k km/s","工C Kama 60k km/s","工D Vesta 54k km/s","军A TS-2 208k km/s","军B Balandin 199k km/s","军C Pontes 189k km/s"],'DS':[23,32,39,43,58,60,int(args/49.59),int(args/74.7),int(args/61.18),int(args/54.1),int(args/70.2),int(args/59.89),int(args/64.4),int(args/66.33),int(args/49.59),int(args/36.06),int(args/38.64),int(args/39.93),int(args/141.68),int(args/135.24),int(args/122.36)]}
    elif arg.lower() in str(["克拉克"]).lower():
        args = 44000
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Erebos 102k km/s","民B Impulse 114k km/s","民B Ranger 106k km/s","民B Tyche 98k km/s","民C Fissure 107k km/s","民C Metis 93k km/s","民C Wanderer 100k km/s","民D Drifter 94k km/s","民D Echo 102k km/s","工B Agni 62k km/s","工C Kama 60k km/s","工D Vesta 54k km/s","军A TS-2 208k km/s","军B Balandin 199k km/s","军C Pontes 189k km/s"],'DS':[23,32,39,43,58,60,int(args/49.59),int(args/74.7),int(args/61.18),int(args/54.1),int(args/70.2),int(args/59.89),int(args/64.4),int(args/66.33),int(args/49.59),int(args/36.06),int(args/38.64),int(args/39.93),int(args/141.68),int(args/135.24),int(args/122.36)]}
    elif arg.lower() in str(["货C"]).lower():
        args = 76000
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Erebos 102k km/s","民B Impulse 114k km/s","民B Ranger 106k km/s","民B Tyche 98k km/s","民C Fissure 107k km/s","民C Metis 93k km/s","民C Wanderer 100k km/s","民D Drifter 94k km/s","民D Echo 102k km/s","工B Agni 62k km/s","工C Kama 60k km/s","工D Vesta 54k km/s","军A TS-2 208k km/s","军B Balandin 199k km/s","军C Pontes 189k km/s"],'DS':[23,32,39,43,58,60,int(args/49.59),int(args/74.7),int(args/61.18),int(args/54.1),int(args/70.2),int(args/59.89),int(args/64.4),int(args/66.33),int(args/49.59),int(args/36.06),int(args/38.64),int(args/39.93),int(args/141.68),int(args/135.24),int(args/122.36)]}
    elif arg.lower() in str(["A2","M2","C2","大力神","A2大力神","M2大力神","C2大力神","大力神A2","大力神M2","大力神C2"]).lower():
        args = 88000
        a = {'QD':["赫-弧","赫-十","赫-微","十-弧","十-微","微-弧","民A Erebos 102k km/s","民B Impulse 114k km/s","民B Ranger 106k km/s","民B Tyche 98k km/s","民C Fissure 107k km/s","民C Metis 93k km/s","民C Wanderer 100k km/s","民D Drifter 94k km/s","民D Echo 102k km/s","工B Agni 62k km/s","工C Kama 60k km/s","工D Vesta 54k km/s","军A TS-2 208k km/s","军B Balandin 199k km/s","军C Pontes 189k km/s"],'DS':[23,32,39,43,58,60,int(args/49.59),int(args/74.7),int(args/61.18),int(args/54.1),int(args/70.2),int(args/59.89),int(args/64.4),int(args/66.33),int(args/49.59),int(args/36.06),int(args/38.64),int(args/39.93),int(args/141.68),int(args/135.24),int(args/122.36)]}

    if arg != "":
        df = pd.DataFrame(a)
        df = df.sort_values(by=['DS'],ascending=True)
        x =df.shape[0]
        img = Image.new("RGB",(850,(170+100*x)),(255,248,220))
        img.save("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png")
        date = cv2.imread("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png", cv2.IMREAD_UNCHANGED)
        fontpath = "C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/1637505678825667.ttc"
        b,g,r,a = 19,69,139,0
        font1 = ImageFont.truetype(fontpath,50)
        font2 = ImageFont.truetype(fontpath,40)
        img_pil = Image.fromarray(date)
        draw = ImageDraw.Draw(img_pil)
        draw.text((100,50),"量子模拟" + arg + "行驶距离",font=font2,fill=(b,g,r,a))
        for i in np.arange(1,x+1):
            #if str(df.iloc[i-1,0])[-1] =="返":
            #    draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(0,128,0,0))
            #    draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(0,128,0,0), width = 20)
            if ("赫-" in df.iloc[i-1,0]) | ("十-" in df.iloc[i-1,0]) | ("微-" in df.iloc[i-1,0]):
                draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(211,0,148,0))
                draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(211,0,148,0), width = 20)
            else:
                draw.text((20,(20+100*i)),df.iloc[i-1,0] + ":\t" + str(df.iloc[i-1,1]) + "mkm",font=font2,fill=(b,g,r,a))
                draw.line([(20, (70+100*i)), ((20+df.iloc[i-1,1]*800/df.iloc[x-1,1]), (70+100*i))],fill=(b,g,r,a), width = 20)
        img = np.array(img_pil)
        cv2.imwrite('C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/DS.png', img)
        path = os.path.split(os.path.realpath(__file__))[0] + '/DS.png'
        await DFship.finish(MessageSegment.image(path=path))

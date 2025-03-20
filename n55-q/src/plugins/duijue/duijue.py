
from nonebot import on_command, require, get_bots
from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
import datetime
import random
import time
import numpy as np 
import string
import pandas as pd
from random import choice
import cv2
from PIL import ImageFont, ImageDraw, Image
from nonebot.adapters import Bot,Event
from nonebot.params import CommandArg
import os
from pathlib import Path

dayship=on_command("每日舰船",aliases={"每日座驾","今日座驾","每日船只","今日舰船","今日船只"},priority=1)

@dayship.handle()
async def handle_function(event: Event):
    if str(type(event)) =="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
        group_id = "A"
        QQ =event.author.user_openid
    else:
        group_id = event.group_openid
        QQ = event.author.member_openid
    today = datetime.datetime.now()
    time = str(today.year) + "_" + str(today.month) + "_" + str(today.day) + "_" + QQ + group_id
    text = "现在时间：" + str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日"
    f=pd.read_csv("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/dayship.txt")
    if time in np.array(f.loc[:,"A"]).tolist():
        await dayship.finish("今日已抽取过每日船只,输入[查模拟对决]试试运气吧~")
    else:
        shiptable = pd.read_csv("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/战斗船指数.csv")
        shiptable.index = shiptable.iloc[:,0]
        ship = choice(np.array(shiptable.名称).tolist())
        links = shiptable.loc[ship,"资料卡链接"]
        p = pd.DataFrame({"A":[time],"B":[ship]})
        f = f._append(p,ignore_index = True,sort = False)
        f.to_csv("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/dayship.txt",index = False)
        path = "C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins"+links
        await dayship.finish("今天的幸运船只为"+ship+MessageSegment.file_image(Path(__file__).parent / path)+"输入[查模拟对决]试试运气吧~")
        
daybat=on_command("模拟对决",priority=1)

@daybat.handle()
async def handle_function(event: Event):
    if str(type(event)) =="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
        group_id = "A"
        QQ =event.author.user_openid
    else:
        group_id = event.group_openid
        QQ = event.author.member_openid
    today = datetime.datetime.now()
    time = str(today.year) + "_" + str(today.month) + "_" + str(today.day) + "_" + QQ + group_id
    f=pd.read_csv("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/daybat.txt")
    if time in np.array(f.loc[:,"A"]).tolist():
        await daybat.finish("今日次数已用完哦~")
    f=pd.read_csv("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/dayship.txt")
    f.index = f.iloc[:,0]
    if time in np.array(f.loc[:,"A"]).tolist():
        ship1 = f.loc[time,"B"]
        shiptable = pd.read_csv("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/战斗船指数.csv")
        shiptable.index = shiptable.iloc[:,0]
        link1 = shiptable.loc[ship1,"图片链接"]
        ship2 = choice(np.array(shiptable.名称).tolist())
        link2 = shiptable.loc[ship2,"图片链接"]
        type1 = shiptable.loc[ship1,"狗斗机"]
        type2 = shiptable.loc[ship2,"狗斗机"]
        if type1 == 1:
            num2 = shiptable.loc[ship2,"对狗斗机"]
        else:
            num2 = shiptable.loc[ship2,"对炮艇"]
        if type2 == 1:
            num1 = shiptable.loc[ship1,"对狗斗机"]
        else:
            num1 = shiptable.loc[ship1,"对炮艇"]
        num11 = random.uniform(num1*0.7,num1*1.3)
        num22 = random.uniform(num2*0.7,num2*1.3)
        WD1 = shiptable.loc[ship1,"语录"]
        WD2 = shiptable.loc[ship2,"语录"]
        if num11 > num22:
            bat1 = "胜"
            bat2 = "负"
        elif num11 < num22:
            bat1 = "负"
            bat2 = "胜"
        elif num11 == num22:
            bat1 = "势均力敌"
            bat2 = "势均力敌"
    else:
        await daybat.finish("尚未抽取今日船只,输入[查每日舰船]试试运气吧~")
    if num11>num1*1.2:
        biaoxian1 = choice(["全程喝红牛","临时雇了王牌飞行员","人机合一"])
    elif num11>num1*1.1:
        biaoxian1 = choice(["人通宵看攻略","灵光一现","想起保险过期的事实"])
    elif num11>num1:
        biaoxian1 = choice(["正常发挥","常规操作"])
    elif num11<num1*0.8:
        biaoxian1 = choice(["不小心睡着了","第一天上班","对面给的太多了"])
    elif num11<num1*0.9:
        biaoxian1 = choice(["打完回老家结婚","新手飞行员","99新女生自用机"])
    elif num11<num1:
        biaoxian1 = choice(["下饭操作","队友唱歌太难听","抖腿误碰脚舵"])
    
    if num22>num2*1.2:
        biaoxian2 = choice(["全程喝红牛","通透世界+斑纹","人机合一"])
    elif num22>num2*1.1:
        biaoxian2 = choice(["人通宵看攻略","临时雇了王牌飞行员","想起保险过期的事实"])
    elif num22>num2:
        biaoxian2 = choice(["正常发挥","灵光一现","常规操作"])
    elif num22<num2*0.8:
        biaoxian2 = choice(["不小心睡着了","第一天上班","对面给的太多了"])
    elif num22<num2*0.9:
        biaoxian2 = choice(["打完回老家结婚","新手飞行员","99新女生自用机"])
    elif num22<num2:
        biaoxian2 = choice(["下饭操作","队友唱歌太难听","抖腿误碰脚舵"])
    def add_alpha_channel(img):
        b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
        alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 # 创建Alpha通道
        img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
        return img_new
    card_path = "C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/duijuemuban.png"
    card = cv2.imread(card_path, cv2.IMREAD_UNCHANGED)
    shippic1 = cv2.imread("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue"+link1, cv2.IMREAD_UNCHANGED)
    shippic2 = cv2.imread("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue"+link2, cv2.IMREAD_UNCHANGED)
    if card.shape[2] == 3:
        card= add_alpha_channel(card)
    
    if shippic1.shape[2] == 3:
        shippic1= add_alpha_channel(shippic1)

    if shippic2.shape[2] == 3:
        shippic2= add_alpha_channel(shippic2)

    height1, width1, channels1 = shippic1.shape
    height2, width2, channels2 = shippic2.shape
    x1 = 70
    y1 = 260-int(height1/2)
    x2 = x1 + shippic1.shape[1]
    y2 = y1 + shippic1.shape[0]

    yy1 = 0
    yy2 = shippic1.shape[0]
    xx1 = 0
    xx2 = shippic1.shape[1]
 
    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > card.shape[1]:
        xx2 = shippic1.shape[1] - (x2 - card.shape[1])
        x2 = card.shape[1]
    if y2 > card.shape[0]:
        yy2 = shippic1.shape[0] - (y2 - card.shape[0])
        y2 = card.shape[0]
    
    alpha_png = shippic1[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png

    for c in range(0,3):
        card[y1:y2, x1:x2, c] = ( (alpha_jpg*card[y1:y2,x1:x2,c]) + (alpha_png*shippic1[yy1:yy2,xx1:xx2,c]))

    x1 = 630
    y1 = 260-int(height2/2)
    x2 = x1 + shippic2.shape[1]
    y2 = y1 + shippic2.shape[0]

    yy1 = 0
    yy2 = shippic2.shape[0]
    xx1 = 0
    xx2 = shippic2.shape[1]
 
    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > card.shape[1]:
        xx2 = shippic2.shape[1] - (x2 - card.shape[1])
        x2 = card.shape[1]
    if y2 > card.shape[0]:
        yy2 = shippic2.shape[0] - (y2 - card.shape[0])
        y2 = card.shape[0]
    
    alpha_png = shippic2[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png

    for c in range(0,3):
        card[y1:y2, x1:x2, c] = ( (alpha_jpg*card[y1:y2,x1:x2,c]) + (alpha_png*shippic2[yy1:yy2,xx1:xx2,c]))



    fontpath = "C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/143zhengkuchaojihei.ttf"
    b,g,r,a = 0,0,0,0
    font = ImageFont.truetype(fontpath,25)
    img_pil = Image.fromarray(card)
    draw = ImageDraw.Draw(img_pil)
    x0, y0, x1, y1=font.getbbox(bat1)
    w,h =x1-x0, y1-y0
    draw.text((270-w/2,392),bat1,font=font,fill=(b,g,r,a))
    x0, y0, x1, y1=font.getbbox(bat2)
    w,h =x1-x0, y1-y0
    draw.text((830-w/2,392),bat2,font=font,fill=(b,g,r,a))
    x0, y0, x1, y1=font.getbbox(WD1)
    w,h =x1-x0, y1-y0
    draw.text((270-w/2,432),WD1,font=font,fill=(b,g,r,a))
    x0, y0, x1, y1=font.getbbox(WD2)
    w,h =x1-x0, y1-y0
    draw.text((830-w/2,432),WD2,font=font,fill=(b,g,r,a))
    x0, y0, x1, y1=font.getbbox(biaoxian1)
    w,h =x1-x0, y1-y0
    draw.text((270-w/2,472),biaoxian1,font=font,fill=(b,g,r,a))
    x0, y0, x1, y1=font.getbbox(biaoxian2)
    w,h =x1-x0, y1-y0
    draw.text((830-w/2,472),biaoxian2,font=font,fill=(b,g,r,a))
    img = np.array(img_pil)
    cv2.imwrite('C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/duijue.jpg', img)
    path = os.path.split(os.path.realpath(__file__))[0] + "/duijue.jpg"
    f=pd.read_csv("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/daybat.txt")
    p = pd.DataFrame({"A":[time]})
    f = f._append(p,ignore_index = True,sort = False)
    f.to_csv("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/duijue/daybat.txt",index = False)
    await daybat.finish(MessageSegment.file_image(Path(__file__).parent / path)+"仅供娱乐，别问XXX为啥打不过XXX")

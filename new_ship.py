from nonebot.adapters.satori.event import MessageEvent
from nonebot.adapters.satori.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from nonebot.params import CommandArg
from nonebot.rule import startswith
import os

import time

from time import sleep

from PIL import ImageFont, ImageDraw, Image

import cv2

import numpy as np

import pandas as pd

FINDID=on_command("",priority=1)

@FINDID.handle()

async def handle_function(args: Message = CommandArg()):
    arg = args.extract_plain_text()
    table=pd.read_csv("C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\qitajianduitu/shipimg/shipinfotable.txt",sep="\t",encoding="utf-8")
    table.index = table.iloc[:,0]
    card_path = 'C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\qitajianduitu/ship.jpg'
    card = cv2.imread(card_path, cv2.IMREAD_UNCHANGED)

    def add_alpha_channel(img):
        b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
        alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 # 创建Alpha通道
     
        img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
        return img_new
    
    if card.shape[2] == 3:
        card= add_alpha_channel(card)
    
    def img_merge(img1,img2,x1,y1):
        x1 = x1
        y1 = y1
        x2 = x1 +  img1.shape[1]
        y2 = y1 +  img1.shape[0]
        
        yy1 = 0
        yy2 =  img1.shape[0]
        xx1 = 0
        xx2 =  img1.shape[1]
     
        if x1 < 0:
            xx1 = -x1
            x1 = 0
        if y1 < 0:
            yy1 = - y1
            y1 = 0
        if x2 > img2.shape[1]:
            xx2 =  img1.shape[1] - (x2 - img2.shape[1])
            x2 = img2.shape[1]
        if y2 > img2.shape[0]:
            yy2 =  img1.shape[0] - (y2 - img2.shape[0])
            y2 = img2.shape[0]
    
        alpha_png =  img1[yy1:yy2,xx1:xx2,3] / 255.0
        alpha_jpg = 1 - alpha_png
        
        for c in range(0,3):
            img2[y1:y2, x1:x2, c] = ( (alpha_jpg*img2[y1:y2,x1:x2,c]) + (alpha_png* img1[yy1:yy2,xx1:xx2,c]))
        return img2
    ship=str(table.loc[table['匹配名称'].str.contains(arg,case=False),"ship"].to_list()[0])
    try:
        img1 = cv2.imread("C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\qitajianduitu/shipimg/"+table.loc[ship,"图片链接"])
        if img1.shape[2] == 3:
            img1= add_alpha_channel(img1)
        img1 = cv2.resize(img1, (2190, 1170))
    except:
        img1=img1
    try:
        img2 = cv2.imread("C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\qitajianduitu/shipimg/"+table.loc[ship,"Unnamed: 48"])
        if img2.shape[2] == 3:
            img2= add_alpha_channel(img2)
        img2 = cv2.resize(img2, (814, 583))
    except:
        img2=img1
    try:
        img3 = cv2.imread("C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\qitajianduitu/shipimg/"+table.loc[ship,"Unnamed: 49"])
        if img3.shape[2] == 3:
            img3= add_alpha_channel(img3)
        img3 = cv2.resize(img3, (814, 583))
    except:
        img3=img1
    try:
        img4 = cv2.imread("C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\qitajianduitu/shipimg/"+table.loc[ship,"Unnamed: 50"])
        if img4.shape[2] == 3:
            img4= add_alpha_channel(img4)
        img4 = cv2.resize(img4, (814, 583))
    except:
        img4=img1
    card=img_merge(img1,card,69,63)
    card=img_merge(img2,card,2315,63)
    card=img_merge(img3,card,3129,63)
    card=img_merge(img4,card,2315,646)
    ZN = str(table.loc[ship,"中文名称"])
    EN = str(table.loc[ship,"ship"]).replace("_"," ")
    XL = str(table.loc[ship,"血量"])
    LZY = str(table.loc[ship,"量子油"])+" SCU"
    YL = str(table.loc[ship,"油量"])+" SCU"
    ZJS = table.loc[ship,"主驾驶武器挂点"]
    ZDR = str(table.loc[ship,"武器最大电容"])
    DD = table.loc[ship,"导弹挂点"]
    PS = table.loc[ship,"炮手武器挂点"]
    FDJ = table.loc[ship,"发电机"]
    LQQ = table.loc[ship,"冷却器"]
    HD = table.loc[ship,"护盾"]
    LZ = table.loc[ship,"量子驱动"]
    LD = table.loc[ship,"雷达"]
    SM = table.loc[ship,"生命维持"]
    MY = str(table.loc[ship,"美元"])
    YXB = table.loc[ship,"游戏币"]
    if YXB !="-":
        YXB = str(YXB) + " aUEC" 
    GMDD = table.loc[ship,"购买地点"]
    GN = table.loc[ship,"概念"]
    CY = str(table.loc[ship,"船员数"]) + "/" + table.loc[ship,"货舱"]
    CC = table.loc[ship,"尺寸"]
    SP = table.loc[ship,"索赔时间"] + "/" + table.loc[ship,"加急时间"]
    JJP = str(table.loc[ship,"加急价格"])
    if JJP !="-":
        JJP = str(JJP) + " aUEC" 
    XH = table.loc[ship,"加力转向"]
    WL = table.loc[ship,"物理抗性"]
    ZX = table.loc[ship,"转向数据"]
    MAXS = str(table.loc[ship,"最大速度"])
    ZDS = str(table.loc[ship,"战斗速度"]) + "/" + str(table.loc[ship,"最大速度"])
    JLS = str(table.loc[ship,"加力前"]) + "/" + str(table.loc[ship,"加力后"])
    JSD = table.loc[ship,"前向加速度"]
    HJSD = table.loc[ship,"后向加速度"]
    CJSD = table.loc[ship,"侧向加速度"]
    SJSD = table.loc[ship,"上升加速度"]
    XJSD = table.loc[ship,"下降加速度"]
    fontpath = "C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\msyh.ttc"
    fontpath1 = "C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\143zhengkuchaojihei.ttf"
    b,g,r,a = 255,255,255,0
    b1,g1,r1,a1 = 6,203,123,0
    font = ImageFont.truetype(fontpath,70)
    font1 = ImageFont.truetype(fontpath1,100)
    font2 = ImageFont.truetype(fontpath,int(table.loc[ship,"炮手字号"]))
    font4 = ImageFont.truetype(fontpath,50)
    img_pil = Image.fromarray(card)
    draw = ImageDraw.Draw(img_pil)
    x0, y0, x1, y1=font.getbbox(ZN)
    w, h = x1-x0, y1-y0
    draw.text((63,1300),ZN,font=font1,fill=(b1,g1,r1,a1))
    x0, y0, x1, y1=font.getbbox(EN)
    w, h = x1-x0, y1-y0
    draw.text((63,1430),EN,font=font,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(MY)
    w, h = x1-x0, y1-y0
    draw.text((1230-w,1785),MY,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(YXB)
    w, h = x1-x0, y1-y0
    draw.text((1230-w,1865),YXB,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(GMDD)
    w, h = x1-x0, y1-y0
    draw.text((1230-w,1945),GMDD,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(GN)
    w, h = x1-x0, y1-y0
    draw.text((1230-w,2030),GN,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(CC)
    w, h = x1-x0, y1-y0
    draw.text((1230-w,2120),CC,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(CY)
    w, h = x1-x0, y1-y0
    draw.text((1230-w,2210),CY,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(SP)
    w, h = x1-x0, y1-y0
    draw.text((1230-w,2300),SP,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(JJP)
    w, h = x1-x0, y1-y0
    draw.text((1230-w,2385),JJP,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(JJP)
    w, h = x1-x0, y1-y0
    draw.text((1230-w,2385),JJP,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(FDJ)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,1460),FDJ,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(LQQ)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,1545),LQQ,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(HD)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,1630),HD,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(LZ)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,1715),LZ,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(LD)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,1805),LD,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(SM)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,1890),SM,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(ZJS)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,2120),ZJS,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(DD)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,2210),DD,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(PS)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,2295),PS,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(ZDR)
    w, h = x1-x0, y1-y0
    draw.text((2580-w,2385),ZDR,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(XL)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,1460),XL,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(WL)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,1545),WL,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(LZY)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,1630),LZY,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(YL)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,1715),YL,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(ZDS)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,1950),ZDS,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(JLS)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,2040),JLS,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(ZX)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,2125),ZX,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(XH)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,2210),XH,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(JSD)
    w, h = x1-x0, y1-y0
    draw.text((3565-w,2295),JSD,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(HJSD)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,2295),HJSD,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(CJSD)
    w, h = x1-x0, y1-y0
    draw.text((3180-w,2385),CJSD,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(SJSD)
    w, h = x1-x0, y1-y0
    draw.text((3565-w,2385),SJSD,font=font4,fill=(b,g,r,a))
    x0, y0, x1, y1=font4.getbbox(XJSD)
    w, h = x1-x0, y1-y0
    draw.text((3940-w,2385),XJSD,font=font4,fill=(b,g,r,a))
    img = np.array(img_pil)
    cv2.imwrite('C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\tmp.jpg', img)
    image = Image.open("C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\tmp.jpg")
    resized_image = image.resize((1440, int(image.size[1] * 1440 / image.size[0])))
    resized_image.save("C:\\Users\\Administrator\\Desktop\\bot\\bot01\\src\\plugins\\ship.jpg")
    path = os.path.split(os.path.realpath(__file__))[0] + '/ship.jpg'

    await FINDID.finish(MessageSegment.image(path=path))
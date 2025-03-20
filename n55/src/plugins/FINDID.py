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
import urllib
import requests
from urllib import error
import random
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from numpy import take
import cv2
from io import BytesIO
import sys
from urllib.request import urlopen
import random

FINDID=on_command("ID",aliases={"id","iD","Id"},priority=1)

@FINDID.handle()
async def handle_function(args: Message = CommandArg()):
#    await FINDID.finish("官网查ID需要先登陆，正在想办法解决这个问题")
    args = args.extract_plain_text()
    def request_html(url):
        ua=UserAgent()
        headers={'Cookie':'wsc_hide=false; _rsi_device=kcu9x7yqnmsm06229t42pte27s; __stripe_mid=325339c5-b4bc-42ae-8aaf-2d86f3c6bc3dedd0eb; wsc_view_count=5; _gcl_au=1.1.29601470.1712535858; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1713832989422%2Cregion:%27CN%27}; _ga_FBVH2Q6FPF=GS1.1.1714975046.7.1.1714975082.0.0.0; _ga_V6MWYXRQNP=GS1.1.1715323822.2.1.1715323872.10.0.0; _ga=GA1.2.1931267318.1704690994; _ga_XGSMCBZNFM=GS1.2.1715387275.18.1.1715389034.60.0.0; _gid=GA1.2.587038219.1715665840; Rsi-XSRF=fVdFZg%3Avgrzznp%2Bfqthb2hkupQa0w%3AL%2Bx%2Bc0s6wnahtOFgCpArSw%3A1715822217632; moment_timezone=Asia%2FHong_Kong; _gat_UA-39586040-1=1; Rsi-Token=7b25f6ff5beb8d482133ae22b98b64a0'}
        request = urllib.request.Request(url, headers=headers)
        return request

    url='https://robertsspaceindustries.com/citizens/' + args
    print(url)
    request = request_html(url)
    try:
        i=0
        while i<3:
            try:
                html = urllib.request.urlopen(request,timeout=10).read().decode('utf8')
                break
            except requests.exceptions.RequestException:
                i += 1
    except:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/查找失败.jpg'
        await FINDID.finish("未找到玩家，是不是输错啦？"+MessageSegment.image(path))
    else:
        await FINDID.send("图片合成中。。请稍后。。。")
#        await FINDID.send("图片合成中。。请稍后。。。\n图片为7种主题颜色和432种背景随机组合而成，让每一次查询都与众不同~")
    #html = urllib.request.urlopen(request).read().decode('utf8')
    
    soup =BeautifulSoup(html, 'lxml')
    links = soup.find_all('img')[0:5]
    imgs=[]
    for data in links:
        imgs.append(data.get('src'))
    print(imgs)
    list_name = soup.select('.value')
    info=[p.get_text() for p in list_name]
    print("".join(info[3].split())+"a")
#    if np.array(imgs).size==4:
#        if "".join(info[3].split())=="":
#            imgs=np.array(imgs).take([2,3,3]).tolist()
#            print(imgs)
#            for i in np.arange(3):
#                if imgs[i].split('/')[0]=='https:':
#                    print(imgs[i])
#                else:
#                    imgs[i]='https://robertsspaceindustries.com'+imgs[i]
#                    print(imgs[i])
#            imgs[2]="C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/NONEdes.png"
#        else:
#            imgs=np.array(imgs).take([2,1,3]).tolist()
#            print(imgs)
#            for i in np.arange(3):
#                if imgs[i].split('/')[0]=='https:':
#                    print(imgs[i])
#                else:
#                    imgs[i]='https://robertsspaceindustries.com'+imgs[i]
#                    print(imgs[i])
#            imgs[1]="C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/NONEORG.png"
#    elif np.array(imgs).size==3:
#        imgs=np.array(imgs).take([2,1,0]).tolist()
#        print(imgs)
#        for i in np.arange(3):
#            if imgs[i].split('/')[0]=='https:':
#                print(imgs[i])
#            else:
#                imgs[i]='https://robertsspaceindustries.com'+imgs[i]
#                print(imgs[i])
#        imgs[1]="C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/NONEORG.png"
#    else:
#        imgs=np.array(imgs).take([2,4,3]).tolist()
#        print(imgs)
#        for i in np.arange(3):
#            if imgs[i].split('/')[0]=='https:':
#                print(imgs[i])
#            else:
#                imgs[i]='https://robertsspaceindustries.com'+imgs[i]
#                print(imgs[i])
    leftlabel=soup.select('div.profile.left-col img')
    rightlabel=soup.select('div.main-org.right-col.visibility-V img')
    redactlabel=soup.select('div.main-org.right-col.visibility-R img')
    imgs=[]
    for data in leftlabel:
        imgs.append(data.get('src'))
    for data in rightlabel:
        imgs.append(data.get('src'))
    for data in redactlabel:
        imgs.append(data.get('src'))

    if rightlabel==[] and redactlabel==[]:
        imgs.append("img/NONEORG.png")

    for i in np.arange(3):
        if imgs[i].split('/')[0]=='https:':
            print(imgs[i])
        elif imgs[i].split('\\')[0]=='C:':
            print(imgs[i])
        else:
            imgs[i]='https://robertsspaceindustries.com'+imgs[i]
            print(imgs[i])
    list_name = soup.select('.value')
    info=[p.get_text() for p in list_name]
    labellist=soup.select('.label')
    label=[p.get_text() for p in labellist]
    if "Organization rank" not in label:
        info = [info[0],info[1],info[2],info[3],"未加入舰队","无","无"] + info[4:]
        if imgs[2]=="https://cdn.robertsspaceindustries.com/static/images/organization/public-orgs-thumb-redacted-bg.png":
            info[4]="舰队已隐藏"
    n=random.randint(0,16)
    card_path = 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/cardmuban'+str(n)+'.jpg'
    
    #n=9
    if n>13:
        card_path = 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/55jiID.jpg'
    else:
        card_path = 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/cardmuban'+str(n)+'.jpg'
    ID_path = imgs[0]
    org_path = imgs[2]
    des_path= imgs[1]
    print(des_path)
    def add_alpha_channel(img):
        b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
        alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 # 创建Alpha通道
 
        img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
        return img_new
    def addpic_alpha_channel(img):
        b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
        alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 # 创建Alpha通道
     
        img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
        return img_new

    card = cv2.imread(card_path, cv2.IMREAD_UNCHANGED)
    try:
        response = requests.get(ID_path, timeout=5)
    except:
        await FINDID.send("与官网连接不稳定，请稍后重试。。。")
    try:
        image = Image.open(BytesIO(response.content))
        if image.mode=="L":
            image=image.convert("RGB")
    except:
        image = Image.open("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/NONEID.png")
        await FINDID.send("官网头像异常，使用默认图片代替。。。")
    radii=33
    def circle_corner(img, radii,path):
        circle = Image.new('L', (radii * 2, radii * 2), 0)  # 创建黑色方形
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, radii * 2, radii * 2), fill=255)  # 黑色方形内切白色圆形
        img = img.convert("RGBA")
        w, h = img.size
        alpha = Image.new('L', img.size, 255)	#与img同大小的白色矩形，L 表示黑白图
        alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))  # 左上角
        alpha.paste(circle.crop((radii, 0, radii * 2, radii)), (w - radii, 0))  # 右上角
        alpha.paste(circle.crop((radii, radii, radii * 2, radii * 2)), (w - radii, h - radii))  # 右下角
        alpha.paste(circle.crop((0, radii, radii, radii * 2)), (0, h - radii))  # 左下角
        img.putalpha(alpha)		# 白色区域透明可见，黑色区域不可见、
        w = img.size[0]
        h = img.size[1]
        w += 2*2
        h += 2*2
        img_new = Image.new('RGB', (w, h), 0)
        img_new.paste(img, (2, 2))
        img.save(path,'PNG',qulity=100)
        return img
    if card_path == 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/55jiID.jpg':
        radii=20
    if n>6 :
        img = circle_corner(image, radii,'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/ID.png')
    else:
        image.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/ID.png','PNG',qulity=100)
    ID = cv2.imread('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/ID.png', cv2.IMREAD_UNCHANGED)
    if card_path == 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/55jiID.jpg':
        ID = cv2.resize(ID, (210, 210))
    else:
        ID = cv2.resize(ID, (312, 312))
    ID = cv2.copyMakeBorder(ID,2,2,2,2,cv2.BORDER_CONSTANT)
    print("ID读取成功")
    try:
        response = requests.get(org_path, timeout=5)
    except:
        print("与官网连接不稳定，请稍后重试。。。")
        response=0
    try:
        img = Image.open(BytesIO(response.content))
    except:
        img = Image.open("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/NONEORG.png")
    w = img.size[0]
    h = img.size[1]
    w += 2*2
    h += 2*2
    img_new = Image.new('RGB', (w, h), 0)
    img_new.paste(img, (2, 2))
    if img.mode=="L":
        img=img.convert("RGB")
    img.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/org.png')
    print("ID处理完成")
    org = cv2.imread('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/org.png', cv2.IMREAD_UNCHANGED)
    if card_path == 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/55jiID.jpg':
        org = cv2.resize(org, (135, 135))
    else:
         org = cv2.resize(org, (230, 230))
    org = cv2.copyMakeBorder(org,2,2,2,2,cv2.BORDER_CONSTANT)
    print("舰队读取成功")
    try:
        response1 = requests.get(des_path, timeout=5)
    except:
        print("与官网连接不稳定，请稍后重试。。。")
        response1=0
    try:
        image = Image.open(BytesIO(response1.content))
    except:
        image = Image.open("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/NONEdes.png")
    image.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/des.png')
    des = cv2.imread('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/des.png', cv2.IMREAD_UNCHANGED)
    if args.lower()=="MolaACG".lower():
        des = cv2.imread('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/molacg.png', cv2.IMREAD_UNCHANGED)
    if card_path == 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/55jiID.jpg':
        des = cv2.resize(des, (80, 80))
    else:
        des = cv2.resize(des, (50, 50))
    print("成就读取成功")
    if card.shape[2] == 3:
        card= add_alpha_channel(card)
    
    if ID.shape[2] == 3:
        ID= add_alpha_channel(ID)

    if org.shape[2] == 3:
        org= add_alpha_channel(org)
    
    if des.shape[2] == 3:
        des= add_alpha_channel(des)

    if card_path == 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/55jiID.jpg':
        x1 = 602
        y1 = 82
    else:
        x1 = 55
        y1 = 220
    x2 = x1 + ID.shape[1]
    y2 = y1 + ID.shape[0]

    yy1 = 0
    yy2 = ID.shape[0]
    xx1 = 0
    xx2 = ID.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > card.shape[1]:
        xx2 = ID.shape[1] - (x2 - card.shape[1])
        x2 = card.shape[1]
    if y2 > card.shape[0]:
        yy2 = ID.shape[0] - (y2 - card.shape[0])
        y2 = card.shape[0]

    alpha_png = ID[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png

    for c in range(0,3):
        card[y1:y2, x1:x2, c] = ( (alpha_jpg*card[y1:y2,x1:x2,c]) + (alpha_png*ID[yy1:yy2,xx1:xx2,c]))
    
    if card_path == 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/55jiID.jpg':
        x1 = 1003
        y1 = 517
    else:
        x1 = 30
        y1 = 605
    x2 = x1 + org.shape[1]
    y2 = y1 + org.shape[0]

    yy1 = 0
    yy2 = org.shape[0]
    xx1 = 0
    xx2 = org.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > card.shape[1]:
        xx2 = org.shape[1] - (x2 - card.shape[1])
        x2 = card.shape[1]
    if y2 > card.shape[0]:
        yy2 = org.shape[0] - (y2 - card.shape[0])
        y2 = card.shape[0]

    alpha_png = org[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png

    for c in range(0,3):
        card[y1:y2, x1:x2, c] = ((alpha_png*org[yy1:yy2,xx1:xx2,c]) + (alpha_jpg*card[y1:y2,x1:x2,c]))

    if card_path == 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/55jiID.jpg':
        x1=340
        y1=420
    else:
        x1 =50
        y1 = 10
    x2 = x1 + des.shape[1]
    y2 = y1 + des.shape[0]

    yy1 = 0
    yy2 = des.shape[0]
    xx1 = 0
    xx2 = des.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > card.shape[1]:
        xx2 = des.shape[1] - (x2 - card.shape[1])
        x2 = card.shape[1]
    if y2 > card.shape[0]:
        yy2 = des.shape[0] - (y2 - card.shape[0])
        y2 = card.shape[0]

    alpha_png = des[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png

    for c in range(0,3):
        card[y1:y2, x1:x2, c] = ((alpha_png*des[yy1:yy2,xx1:xx2,c]) + (alpha_jpg*card[y1:y2,x1:x2,c]))

    labellist=soup.select('.label')
    label=[p.get_text() for p in labellist]
    label = [item for item in label if item != "Website"]
    print(info)
    print(label)
    print(len(info))
    text1 =  info[2]
    text2 = info[3]
    try:
        text3=info[-(len(label)-label.index("Enlisted"))]
    except:
        text3="史前生物"
    try:
        text4=info[-(len(label)-label.index("Location"))].replace(' ', '').replace('\n', '').replace('\r', '').strip()
    except:
        text4="斯坦顿,新巴贝奇"
    try:
        text5=info[-(len(label)-label.index("Fluency"))].replace(' ', '').replace('\n', '').replace('\r', '').strip()
    except:
        text5="斯坦顿,新巴贝奇"
    text6 = info[4]
    text7 = info[5]
    text8 = info[6]

    if args.lower()=="asdda".lower():
        text4 = "提瓦特大陆，净善宫"
    if args.lower()=="captainyuki".lower():
        text4 = "神圣泰拉"
        text5 = "Shtibidi! dabudu! bidid!"
    elif args.lower()=="tiwate_C1G".lower():
        text4 = "提瓦特大陆，望舒客栈"
    elif args.lower()=="wumingshi62606".lower():
        text4 = "提瓦特大陆，往生堂"
    elif args.lower()=="VGWE543".lower():
        text4 = "南极"
    elif args.lower()=="UEE_TianXing".lower():
        text4 = "卡拉克·八峰山"
        text5 = "Skaven! Yes! Yes!"
    elif args.lower()=="Hunter-Zhao".lower():
        text4 = "苏维埃社会主义联盟"
        text8 = "政委"

    print("绘图开始")
    if card_path == 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/55jiID.jpg':
        fontpath1 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/FZYHJW.TTF"
        fontpath12 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/FZYHJW.TTF"
        fontpath2 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/Banu-Regular.otf"
        fontpath3 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/FZYHJW.TTF"
        b,g,r,a = 255,255,255,0
        b2,g2,r2,a2 = 255,255,255,0
        font1 = ImageFont.truetype(fontpath1,45)
        font11 = ImageFont.truetype(fontpath1,45)
        font12 = ImageFont.truetype(fontpath1,60)
        font2 = ImageFont.truetype(fontpath2,45)
        font3 = ImageFont.truetype(fontpath12,65)
        img_pil = Image.fromarray(card)
        x0, y0, x1, y1=font1.getbbox(text2)
        w,h =x1-x0, y1-y0
        draw = ImageDraw.Draw(img_pil)
        draw.text((550,540),text1,font=font3,fill=(b2,g2,r2,a2))
        x0, y0, x1, y1=font2.getbbox("".join(info[2].split("_")).lower())
        w,h =x1-x0, y1-y0
        draw.text((260,630),"".join(info[2].split("_")).lower(),font=font2,fill=(b,g,r,a))
        x0, y0, x1, y1=font1.getbbox(text3)
        w,h =x1-x0, y1-y0
        draw.text((363,735),text3,font=font1,fill=(b,g,r,a))
        draw.text((450,440),text2,font=font11,fill=(b2,g2,r2,a2))
        x0, y0, x1, y1=font1.getbbox(text4)
        w,h =x1-x0, y1-y0
        draw.text((390,840),text4,font=font1,fill=(b,g,r,a))
        x0, y0, x1, y1=font1.getbbox(text5)
        w,h =x1-x0, y1-y0
        draw.text((315,920),text5,font=font1,fill=(b,g,r,a))
        x0, y0, x1, y1=font12.getbbox(text6)
        w,h =x1-x0, y1-y0
        draw.text((1070,658),text6,font=font12,fill=(b,g,r,a))
        x0, y0, x1, y1=font11.getbbox(text7)
        w,h =x1-x0, y1-y0
        draw.text((1005,775),text7,font=font11,fill=(b,g,r,a))
        x0, y0, x1, y1=font11.getbbox(text8)
        w,h =x1-x0, y1-y0
        draw.text((1080,895),text8,font=font11,fill=(b,g,r,a))
        x0, y0, x1, y1=font1.getbbox(info[1])
        w,h =x1-x0, y1-y0
        draw.text((625,315),info[1],font=font3,fill=(b2,g2,r2,a2))
    else:
        fontpath1 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/msyh.ttc"
        fontpath12 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/msyhbd.ttc"
        fontpath2 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/Banu-Regular.otf"
        fontpath3 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/ROGFONTS-REGULAR_0.OTF"
        b,g,r,a = 0,0,0,0
        b2,g2,r2,a2 = 255,255,255,0
        font1 = ImageFont.truetype(fontpath1,40)
        font11 = ImageFont.truetype(fontpath1,30)
        font12 = ImageFont.truetype(fontpath1,60)
        font2 = ImageFont.truetype(fontpath2,40)
        font3 = ImageFont.truetype(fontpath12,60)
        img_pil = Image.fromarray(card)
        x0, y0, x1, y1=font1.getbbox(text2)
        w,h =x1-x0, y1-y0
        draw = ImageDraw.Draw(img_pil)
        draw.text((400,45),text1,font=font3,fill=(b2,g2,r2,a2))
        x0, y0, x1, y1=font2.getbbox("".join(info[2].split("_")).lower())
        w,h =x1-x0, y1-y0
        draw.text((1180-w,290),"".join(info[2].split("_")).lower(),font=font2,fill=(b,g,r,a))
        x0, y0, x1, y1=font1.getbbox(text3)
        w,h =x1-x0, y1-y0
        draw.text((1180-w,350),text3,font=font1,fill=(b,g,r,a))
        draw.text((120,15),text2,font=font11,fill=(b2,g2,r2,a2))
        x0, y0, x1, y1=font1.getbbox(text4)
        w,h =x1-x0, y1-y0
        if w>560:
            font13 = ImageFont.truetype(fontpath1,40*(560/w))
            x0, y0, x1, y1=font13.getbbox(text4)
            w,h =x1-x0, y1-y0
            draw.text((1180-w,415),text4,font=font13,fill=(b,g,r,a))
        else:
            draw.text((1180-w,415),text4,font=font1,fill=(b,g,r,a))
        x0, y0, x1, y1=font1.getbbox(text5)
        w,h =x1-x0, y1-y0
        draw.text((1180-w,480),text5,font=font1,fill=(b,g,r,a))
        x0, y0, x1, y1=font12.getbbox(text6)
        w,h =x1-x0, y1-y0
        if w>870:
            font12 = ImageFont.truetype(fontpath1,60*(870/w))
            x0, y0, x1, y1=font12.getbbox(text6)
            w,h =x1-x0, y1-y0
            draw.text((755-w/2,690-h/2),text6,font=font12,fill=(b,g,r,a))
        else:
            draw.text((755-w/2,658),text6,font=font12,fill=(b,g,r,a))
        x0, y0, x1, y1=font11.getbbox(text7)
        w,h =x1-x0, y1-y0
        draw.text((1180-w,745),text7,font=font11,fill=(b,g,r,a))
        x0, y0, x1, y1=font11.getbbox(text8)
        w,h =x1-x0, y1-y0
        draw.text((1180-w,785),text8,font=font11,fill=(b,g,r,a))
        draw.text((400,115),info[1],font=font1,fill=(b2,g2,r2,a2))
    
    img = np.array(img_pil)
    image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    image.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/findID.png')
    
    path = os.path.split(os.path.realpath(__file__))[0] + '/findID.png'
    await FINDID.finish(MessageSegment.image(path))

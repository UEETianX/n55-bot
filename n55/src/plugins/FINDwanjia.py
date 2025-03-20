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

FINDwanjia=on_command("玩家",priority=1)

@FINDwanjia.handle()
async def handle_function(args: Message = CommandArg()):
#    await FINDwanjia.finish("官网查ID需要先登陆，正在想办法解决这个问题")
    args = args.extract_plain_text()
    def request_html(url):
        ua=UserAgent()
        headers={'User-Agent':str(UserAgent("C:\\Users/Administrator/Desktop/Qbot/n55/src/plugins/fake_useragent_0.1.11.json").random),
                       'Cookie':'wsc_hide=false; _rsi_device=kcu9x7yqnmsm06229t42pte27s; __stripe_mid=325339c5-b4bc-42ae-8aaf-2d86f3c6bc3dedd0eb; wsc_view_count=5; _gcl_au=1.1.29601470.1712535858; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1713832989422%2Cregion:%27CN%27}; _ga_FBVH2Q6FPF=GS1.1.1714975046.7.1.1714975082.0.0.0; _ga_V6MWYXRQNP=GS1.1.1715323822.2.1.1715323872.10.0.0; _ga=GA1.2.1931267318.1704690994; _ga_XGSMCBZNFM=GS1.2.1715387275.18.1.1715389034.60.0.0; _gid=GA1.2.587038219.1715665840; Rsi-XSRF=fVdFZg%3Avgrzznp%2Bfqthb2hkupQa0w%3AL%2Bx%2Bc0s6wnahtOFgCpArSw%3A1715822217632; moment_timezone=Asia%2FHong_Kong; _gat_UA-39586040-1=1; Rsi-Token=7b25f6ff5beb8d482133ae22b98b64a0'}
        request = urllib.request.Request(url, headers=headers)
        return request

    url='https://robertsspaceindustries.com/citizens/' + args
    print(url)
    request = request_html(url)
    try:
        html = urllib.request.urlopen(request).read().decode('utf8')
    except:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/查找失败.jpg'
        await FINDwanjia.finish("未找到玩家，是不是输错啦？"+MessageSegment.image(path))
    else:
        await FINDwanjia.send("图片合成中。。请稍后。。。")
#        await FINDwanjia.send("图片合成中。。请稍后。。。\n图片为7种主题颜色和432种背景随机组合而成，让每一次查询都与众不同~")
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
    imgs=[]
    for data in leftlabel:
        imgs.append(data.get('src'))
    for data in rightlabel:
        imgs.append(data.get('src'))


    if rightlabel==[]:
        imgs.append("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/NONEORG.png")


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
    n=random.randint(0,6)
    if args.lower()=="asdda".lower():
        n=4
    card_path = 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/cardmuban_old'+str(n)+'.png'
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
        await FINDwanjia.send("与官网连接不稳定，请稍后重试。。。")
    try:
        image = Image.open(BytesIO(response.content))
        if image.mode=="L":
            image=image.convert("RGB")
    except:
        image = Image.open("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/NONEID.png")
        await FINDwanjia.send("官网头像异常，使用默认图片代替。。。")
    radii=33
    def circle_corner(img, radii):
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
        img.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/ID.png','PNG',qulity=100)
        return img

    img = circle_corner(image, radii)
    ID = cv2.imread('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/ID.png', cv2.IMREAD_UNCHANGED)
    ID = cv2.resize(ID, (450, 450))
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
    org = cv2.resize(org, (300, 300))
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
    des = cv2.resize(des, (200, 200))
    print("成就读取成功")
    if card.shape[2] == 3:
        card= add_alpha_channel(card)
    
    if ID.shape[2] == 3:
        ID= add_alpha_channel(ID)

    if org.shape[2] == 3:
        org= add_alpha_channel(org)
    
    if des.shape[2] == 3:
        des= add_alpha_channel(des)

    bai = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/bai.png", cv2.IMREAD_UNCHANGED)
    pic_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/idimg/"+str(random.randint(1,432))+".jpg"
    if args.lower()=="PMC_HK416".lower():
        pic_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/hk416.jpg"
    elif args.lower()=="DeathAngle".lower():
        pic_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/shichen.jpg"
    elif args.lower()=="UEE_TianXing".lower():
        pic_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/tianxingid.jpg"
    elif args.lower()=="Hunter-Zhao".lower():
        pic_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/zhaoid.jpg"
    elif args.lower()=="asdda".lower():
        pic_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/asddaid.jpg"
    elif args.lower()=="captainyuki".lower():
        pic_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/img/CaptainYuki.jpg"
    pic = cv2.imread(pic_path, cv2.IMREAD_UNCHANGED)
    pic = cv2.resize(pic, (1763, 1246))
    if bai.shape[2] == 3:
        bai= add_alpha_channel(bai)
    if pic.shape[2] == 3:
        pic= addpic_alpha_channel(pic)
    
    x1 = 0
    y1 = 0
    x2 = x1 +  pic.shape[1]
    y2 = y1 +  pic.shape[0]
    
    yy1 = 0
    yy2 =  pic.shape[0]
    xx1 = 0
    xx2 =  pic.shape[1]
     
    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > bai.shape[1]:
        xx2 =  pic.shape[1] - (x2 - bai.shape[1])
        x2 = bai.shape[1]
    if y2 > bai.shape[0]:
        yy2 =  pic.shape[0] - (y2 - bai.shape[0])
        y2 = bai.shape[0]
        
    alpha_png =  pic[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png
    
    for c in range(0,3):
        bai[y1:y2, x1:x2, c] = ( (alpha_jpg*bai[y1:y2,x1:x2,c]) + (alpha_png* pic[yy1:yy2,xx1:xx2,c]))
    
    x1 = 0
    y1 = 0
    x2 = x1 +  card.shape[1]
    y2 = y1 +  card.shape[0]
    
    yy1 = 0
    yy2 =  card.shape[0]
    xx1 = 0
    xx2 =  card.shape[1]
     
    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > bai.shape[1]:
        xx2 =  card.shape[1] - (x2 - bai.shape[1])
        x2 = bai.shape[1]
    if y2 > bai.shape[0]:
        yy2 =  card.shape[0] - (y2 - bai.shape[0])
        y2 = bai.shape[0]
        
    alpha_png =  card[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png
    
    for c in range(0,3):
        card[y1:y2, x1:x2, c] = ( (alpha_jpg*bai[y1:y2,x1:x2,c]) + (alpha_png* card[yy1:yy2,xx1:xx2,c]))
    

    x1 = 50
    y1 = 200
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
    
    x1 = 730
    y1 = 930
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

    x1 =1330
    y1 = 800
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
    print(info)
    print(label)
    print(len(info))
    if "Fluency" in label and "Location" in label:
        if len(info)==13:
            text1 = "玩家ID:  " + info[2]
            text2 = info[3]
            text3 = "注册时间:  " + info[9]
            text4 = "地区:  " + info[10].replace(' ', '').replace('\n', '').replace('\r', '').strip()
            text5 = "语言:  " + info[11].replace(' ', '').replace('\n', '').replace('\r', '').strip()
            text6 = "舰队名称:  " + info[4]
            text7 = "舰队编号:  " + info[5]
            text8 = "成员职位:  " + info[6]
            text9 = "社区ID:"
        else:
            text1 = "玩家ID:  " + info[2]
            text2 = info[3]
            text3 = "注册时间:  " + info[7]
            text4 = "地区:  " + info[8].replace(' ', '').replace('\n', '').replace('\r', '').strip()
            text5 = "语言:  " + info[9].replace(' ', '').replace('\n', '').replace('\r', '').strip()
            text6 = "舰队名称:  " + info[4]
            text7 = "舰队编号:  " + info[5]
            text8 = "成员职位:  " + info[6]
            text9 = "社区ID:"

    if "Fluency" in label and "Location" not in label:
        if len(info)==8:
            text1 = "玩家ID:  " + info[2]
            text2 = info[2]
            text3 = "注册时间:  " + info[3]
            text4 = "地区:  " + "斯坦顿,新巴贝奇"
            text5 = "语言:  " + info[7].replace(' ', '').replace('\n', '').replace('\r', '').strip()
            text6 = "舰队名称:  " + info[4]
            text7 = "舰队编号:  " + info[5]
            text8 = "成员职位:  " + info[6]
            text9 = "社区ID:  "
        else:
            text1 = "玩家ID:  " + info[2]
            text2 = info[3]
            text3 = "注册时间:  " + info[7]
            text4 = "地区:  " + "斯坦顿,新巴贝奇"
            text5 = "语言:  " + info[8].replace(' ', '').replace('\n', '').replace('\r', '').strip()
            text6 = "舰队名称:  " + info[4]
            text7 = "舰队编号:  " + info[5]
            text8 = "成员职位:  " + info[6]
            text9 = "社区ID:  "
    
    if "Fluency" not in label and "Location" in label:
        text1 = "玩家ID:  " + info[2]
        text2 = info[3]
        text3 = "注册时间:  " + info[7]
        text4 = "地区:  " + info[8].replace(' ', '').replace('\n', '').replace('\r', '').strip()
        text5 = "语言:  " + "巴努语"
        text6 = "舰队名称:  " + info[4]
        text7 = "舰队编号:  " + info[5]
        text8 = "成员职位:  " + info[6]
        text9 = "社区ID:  "

    if args.lower()=="asdda".lower():
        text4 = "地区:  提瓦特大陆，净善宫"
    if args.lower()=="captainyuki".lower():
        text4 = "地区:  神圣泰拉"
        text5 = "语言:  Shtibidi! dabudu! bidid!"
    elif args.lower()=="tiwate_C1G".lower():
        text4 = "地区:  提瓦特大陆，望舒客栈"
    elif args.lower()=="wumingshi62606".lower():
        text4 = "地区:  提瓦特大陆，往生堂"
    elif args.lower()=="VGWE543".lower():
        text4 = "地区:  南极"
    elif args.lower()=="UEE_TianXing".lower():
        text4 = "地区:  卡拉克·八峰山"
        text5 = "语言:  Skaven! Yes! Yes!"
    elif args.lower()=="Hunter-Zhao".lower():
        text4 = "地区:  苏维埃社会主义联盟"
        text8 = "成员职位:  政委"

    print("绘图开始")
    fontpath1 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/1637505678825667.ttc"
    fontpath2 = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/Banu-Regular.otf"
    if n==0:
        b,g,r,a = 77,0,128,0
    elif n==1:
        b,g,r,a = 34,34,178,0
    elif n==2:
        b,g,r,a = 30,105,210,0
    elif n==3:
        b,g,r,a = 32,165,218,0
    elif n==4:
        b,g,r,a = 35,142,107,0
    elif n==5:
        b,g,r,a = 139,139,0,0
    elif n==6:
        b,g,r,a = 237,149,100,0
    b2,g2,r2,a2 = 255,255,255,0
    font1 = ImageFont.truetype(fontpath1,50)
    font2 = ImageFont.truetype(fontpath2,70)
    font3 = ImageFont.truetype(fontpath1,70)
    img_pil = Image.fromarray(card)
    x0, y0, x1, y1=font1.getbbox(text2)
    w,h =x1-x0, y1-y0
    draw = ImageDraw.Draw(img_pil)
    draw.text((750,130),text1,font=font3,fill=(b,g,r,a))
    draw.text((750,250),"巴努语:",font=font3,fill=(b,g,r,a))
    draw.text((1070,250),"".join(info[2].split("_")).lower(),font=font2,fill=(b,g,r,a))
    draw.text((1430-w/2,1030),text2,font=font1,fill=(b,g,r,a))
    draw.text((750,370),text3,font=font3,fill=(b,g,r,a))
    draw.text((750,490),text4,font=font3,fill=(b,g,r,a))
    draw.text((750,610),text5,font=font3,fill=(b,g,r,a))
    x0, y0, x1, y1=font1.getbbox(text6)
    w,h =x1-x0, y1-y0
    if w>1000:
        try:
            text6 = text6[0:30] + "\n                    "+ text6[30:]
        except:
            text6 = text6[0:16] + "\n                    "+ text6[16:]
    draw.text((50,850),text6,font=font1,fill=(b2,g2,r2,a))
    draw.text((50,980),text7,font=font1,fill=(b2,g2,r2,a))
    x0, y0, x1, y1=font1.getbbox(text8)
    w,h =x1-x0, y1-y0
    if w> 700:
        try:
            text8 = text8[0:20] + "\n           "+ text8[20:]
        except:
            text8 = text8[0:15] + "\n           "+ text8[15:]
    draw.text((50,1110),text8,font=font1,fill=(b2,g2,r2,a))
    draw.text((50,100),text9,font=font1,fill=(b,g,r,a))
    draw.text((220,100),info[1],font=font1,fill=(b,g,r,a))
    img = np.array(img_pil)
    image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    image.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/FINDwanjia.png')
    
    path = os.path.split(os.path.realpath(__file__))[0] + '/FINDwanjia.png'
    await FINDwanjia.finish(MessageSegment.image(path))

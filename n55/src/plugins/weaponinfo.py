from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
import requests
import os
import random
from time import sleep
import pandas as pd
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import os
from nonebot.params import CommandArg

weaponinfo=on_command("",aliases={"武器"},priority=2)

@weaponinfo.handle()
async def handle_function(bot:Bot,event:Event,state:T_State,args: Message = CommandArg()):
    args = args.extract_plain_text().replace(" ","").replace(".","#")
    if args =="武器": 
        await weaponinfo.finish("查询单个武器数据，输入:查武器+[武器名/尺寸类型]\n例：查武器CF227\n查武器S1激光速射\n\n查询武器列表输入：查舰船武器\n查询导弹鱼雷输入：查导弹\n查询单兵武器输入：查FPS")
    df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/weapons.csv',index_col=None,header=0)
    if  args.lower()=="wb":
        args="asdsadawea"
    try:
        text0 = str(df.loc[df['CN-Name'].str.contains(args,case=False),"CN"].to_list()[0])
        text1 = str(df.loc[df['CN-Name'].str.contains(args,case=False),"Name"].to_list()[0])
    except:
        try:
            df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/weapons.csv',index_col=None,header=0)
            df["add"] = "S"+df["Size"].astype(str).str.cat(df["Type"])+"S"+df["Size"].astype(str).str.cat(df["Type"].apply(lambda x:x[2:]))
            tmp = df.loc[df['add'].str.contains(args,case=False),["Name","Size","Type","Burst DPS","Speed","Base price"]]
            print(tmp.iloc[0])
        except:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/查找失败.jpg'
            return
#            await weaponinfo.finish("是不是输错啦?如果发现武器没收录可以@UEE_TianXing哦~"+MessageSegment.image(path))
        tmp = tmp.sort_values(by="Size",ascending=True)
        x =tmp.shape[0]
        if x>0:
            text01 = "武器名称"
            text02 = "尺寸"
            text03 = "类型"
            text04 = "爆发DPS"
            text05 = "子弹飞行速度"
            text06 = "武器价格"
            text1 = "\n".join([str(i) for i in tmp["Name"].tolist()])
            text2 = "\n".join([str(i) for i in tmp["Size"].tolist()])
            text3 = "\n".join([str(i) for i in tmp["Type"].tolist()])
            text4 = "\n".join([str(i) for i in tmp["Burst DPS"].tolist()])
            text5 = "\n".join([str(i) for i in tmp["Speed"].tolist()])
            text6 = "\n".join([str(i) for i in tmp["Base price"].tolist()])
            img = Image.new("RGB",(1800,(90+40*x)),(255,248,220))
            img.save("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/p.jpg")
            date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/p.jpg", cv2.IMREAD_UNCHANGED)
            fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/1637505678825667.ttc"
            b,g,r,a = 19,69,139,0
            font1 = ImageFont.truetype(fontpath,50)
            font2 = ImageFont.truetype(fontpath,40)
            img_pil = Image.fromarray(date)
            draw = ImageDraw.Draw(img_pil)
            draw.text((20,20),text01,font=font1,fill=(b,g,r,a))
            draw.text((450,20),text02,font=font1,fill=(b,g,r,a))
            draw.text((660,20),text03,font=font1,fill=(b,g,r,a))
            draw.text((920,20),text04,font=font1,fill=(b,g,r,a))
            draw.text((1150,20),text05,font=font1,fill=(b,g,r,a))
            draw.text((1520,20),text06,font=font1,fill=(b,g,r,a))
            draw.text((20,70),text1,font=font2,fill=(b,g,r,a))
            draw.text((490,70),text2,font=font2,fill=(b,g,r,a))
            draw.text((620,70),text3,font=font2,fill=(b,g,r,a))
            draw.text((970,70),text4,font=font2,fill=(b,g,r,a))
            draw.text((1250,70),text5,font=font2,fill=(b,g,r,a))
            draw.text((1570,70),text6,font=font2,fill=(b,g,r,a))
            img = np.array(img_pil)
            cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/p.jpg', img)
            path=os.path.split(os.path.realpath(__file__))[0] + '/p.jpg'
            await weaponinfo.finish( MessageSegment.image(path))
    if len(args) >0:
        text2 = "制造商：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Manufacturer"].to_list()[0])
        text3 = "武器类型：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Type"].to_list()[0])
        text4 = "尺寸：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Size"].to_list()[0])
        text5 = "出售地点：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"loc"].to_list()[0]).split(" ")[0]
        text6 = "售价：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Base price"].to_list()[0]) +" aUEC"
        text7 = "爆发DPS：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Burst DPS"].to_list()[0])
        text8 = "单发伤害：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Alpha"].to_list()[0])
        text9 = "射速：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Fire rate"].to_list()[0])
        text10 = "射程：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Range"].to_list()[0]) + " m"
        
        text11 = "子弹飞行速度：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Speed"].to_list()[0]) + " m/s"
        text12 = "备弹量：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Ammo count"].to_list()[0])
        text13 = "血量：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Health"].to_list()[0])
        
        text14 = "畸变容量：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Distortion shutdwon dmg"].to_list()[0])
        text15 = "畸变恢复延迟：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Distortion decay delay"].to_list()[0])
        text16 = "恢复速率：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Distortion decay rate"].to_list()[0])
        text17 = "畸变恢复比：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Distortion recovery ratio"].to_list()[0])
        text18 = "电量消耗：" + str(df.loc[df['CN-Name'].str.contains(args,case=False),"Power consumption"].to_list()[0])
        date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/wuqimoban.png", cv2.IMREAD_UNCHANGED)
        def add_alpha_channel(img):
            b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
            alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 # 创建Alpha通道
            img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
            return img_new
    
        def imgadd(img1,img2,x1,y1):
            x2 = x1 + img2.shape[1]
            y2 = y1 + img2.shape[0]
            yy1 = 0
            yy2 = img2.shape[0]
            xx1 = 0
            xx2 = img2.shape[1]
            if x1 < 0:
                xx1 = -x1
                x1 = 0
            if y1 < 0:
                yy1 = - y1
                y1 = 0
            if x2 > img1.shape[1]:
                xx2 = img2.shape[1] - (x2 - img1.shape[1])
                x2 = img1.shape[1]
            if y2 > img1.shape[0]:
                yy2 = img2.shape[0] - (y2 - img1.shape[0])
                y2 = img1.shape[0]
            alpha_png = img2[yy1:yy2,xx1:xx2,3] / 255.0
            alpha_jpg = 1 - alpha_png
            for c in range(0,3):
                img1[y1:y2, x1:x2, c] = ( (alpha_jpg*img1[y1:y2,x1:x2,c]) + (alpha_png*img2[yy1:yy2,xx1:xx2,c]))
            return(img1)
    
        if date.shape[2] == 3:
            date= add_alpha_channel(date)
        fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/1637505678825667.ttc"
        link = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins"+str(df.loc[df['CN-Name'].str.contains(args,case=False),"pic"].to_list()[0])
        pic = cv2.imread(link, cv2.IMREAD_UNCHANGED)
        pic = cv2.resize(pic, (480, 270))
        if pic.shape[2] == 3:
            pic= add_alpha_channel(pic)
        height, width, channels1 = pic.shape
        pic = cv2.resize(pic, (500,int(height*500/width)))
        date = imgadd(date,pic,1233-500-100,190)
    
        b,g,r,a = 19,69,139,0
        font1 = ImageFont.truetype(fontpath,70)
        font2 = ImageFont.truetype(fontpath,35)
        img_pil = Image.fromarray(date)
        draw = ImageDraw.Draw(img_pil)
        x0, y0, x1, y1 =font1.getbbox(text0)
        w, h = x1-x0, y1-y0
        draw.text((616-w/2,40),text0,font=font1,fill=(b,g,r,a))
        x0, y0, x1, y1 =font2.getbbox(text1)
        w, h = x1-x0, y1-y0
        draw.text((616-w/2,110),text1,font=font2,fill=(b,g,r,a))
        #draw.text((130,220),text2,font=font2,fill=(b,g,r,a))
        draw.text((130,255),text3,font=font2,fill=(b,g,r,a))
        draw.text((130,205),text4,font=font2,fill=(b,g,r,a))
        draw.text((130,305),text6,font=font2,fill=(b,g,r,a))
        x0, y0, x1, y1 =font1.getbbox(text5)
        w, h = x1-x0, y1-y0
        if w>1000:
            text5 = text5[0:16] + "\n"+ text5[16:]
        x0, y0, x1, y1 =font1.getbbox(text5)
        w, h = x1-x0, y1-y0
        if w>2080:
            text5 = text5[0:32] + "\n"+ text5[32:]
        if w>3080:
            text5 = text5[0:48] + "\n"+ text5[48:]
            
        if w>5080:
            text5 = text5[0:81] + "\n"+ text5[81:]
        
        draw.text((130,365),text5,font=font2,fill=(b,g,r,a))
        draw.text((130,560+70),text7,font=font2,fill=(b,g,r,a))
        draw.text((130,620+70),text8,font=font2,fill=(b,g,r,a))
        draw.text((130,680+70),text9,font=font2,fill=(b,g,r,a))
        draw.text((130,740+70),text10,font=font2,fill=(b,g,r,a))
        draw.text((130,800+70),text11,font=font2,fill=(b,g,r,a))
        draw.text((130,860+70),text12,font=font2,fill=(b,g,r,a))
        draw.text((130,920+70),text18,font=font2,fill=(b,g,r,a))
        draw.text((720,560+70),text13,font=font2,fill=(b,g,r,a))
        draw.text((720,645+70),text14,font=font2,fill=(b,g,r,a))
        draw.text((720,730+70),text15,font=font2,fill=(b,g,r,a))
        draw.text((720,815+70),text16,font=font2,fill=(b,g,r,a))
        draw.text((720,900+70),text17,font=font2,fill=(b,g,r,a))
        img = np.array(img_pil)
        cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/wuqi.jpg', img)
        path=os.path.split(os.path.realpath(__file__))[0] + '/wuqi.jpg'
        await weaponinfo.finish( MessageSegment.image(path))

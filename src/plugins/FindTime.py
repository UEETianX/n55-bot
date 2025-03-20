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
from win32com.client import Dispatch
import openpyxl
from datetime import datetime, timezone

findtime=on_command("时间",priority=1)

@findtime.handle()
async def handle_function(args: Message = CommandArg()):
    alist=pd.read_table("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/alist.xls",encoding="gbk")
    msg=str(args)
    utc_now = datetime.now(timezone.utc)
    today = datetime.now()
    if msg=="":
        await findtime.finish("要加上星球/地点名称哦~")
    def just_open(filename):
        xlApp = Dispatch("Excel.Application")
        xlApp.Visible = False
        xlBook = xlApp.Workbooks.Open(filename)
        xl=xlBook.Worksheets(1)
        xl.Range('D3').Value=utc_now
        xl.Range('B1').Value=pla
        xlBook.Save()
        xlBook.Close()
    if any(msg in item for item in alist.PLACN):
        await findtime.send("让我去看看~")
        flist=alist[alist.PLACN.str.contains(msg)]
        pla=flist.PLA.tolist()[0]
        loccn=flist.LOCCN.tolist()
        loc=flist.LOC.tolist()
        cla=flist.CLA.tolist()
        linenum=len(loc)
        just_open("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/test.xlsx")
        wb = openpyxl.load_workbook("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/test.xlsx",data_only=True)
        sheet = wb.active
        llist=[]
        for cell in sheet["A"]:
            llist=llist+[cell.value]
        img = Image.new("RGB",(1750,(100+100*linenum)),(255,248,220))
        img.save("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/time.jpg")
        date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/time.jpg", cv2.IMREAD_UNCHANGED)
        fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/1637505678825667.ttc"
        b,g,r,a = 19,69,139,0
        font1 = ImageFont.truetype(fontpath,50)
        font2 = ImageFont.truetype(fontpath,40)
        img_pil = Image.fromarray(date)
        draw = ImageDraw.Draw(img_pil)
        for i in np.arange(linenum):
            n=loc[i]
            num=llist.index([s for s in llist if n in str(s)][0])
            text=msg+"的时间概况如下："
            text1=loccn[i]
            text2=sheet['O' + str(num+1)].value
            text3=cla[i]
            draw.text((20,20),text,font=font1,fill=(b,g,r,a))
            draw.text((20,20+100*i+100),text1,font=font2,fill=(b,g,r,a))
            draw.text((900,20+100*i+100),text2,font=font2,fill=(b,g,r,a))
            draw.text((1500,20+100*i+100),text3,font=font2,fill=(b,g,r,a))
        img = np.array(img_pil)
        cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/time.jpg', img)
        path = os.path.split(os.path.realpath(__file__))[0] + '/time.jpg'
        await findtime.finish(MessageSegment.image(path))
    elif any(msg in item for item in alist.LOCCN):
        await findtime.send("让我去看看~")
        flist=alist[alist.LOCCN.str.contains(msg)]
        if len(flist)==1:
            pla=flist.PLA.tolist()[0]
            placn=flist.PLACN.tolist()[0]
            loc=flist.LOC.tolist()[0]
            just_open("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/test.xlsx")
            wb = openpyxl.load_workbook("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/test.xlsx",data_only=True)
            sheet = wb.active
            llist=[]
            for cell in sheet["A"]:
                llist=llist+[cell.value]
            num=llist.index([s for s in llist if loc in str(s)][0])
            if len(sheet['O' + str(num+1)].value.split("/"))==2:
                text="当前"+placn+"-"+msg+"的时间为：\n"+str(sheet['O' + str(num+1)].value).split("/")[0]+"距离"+str(sheet['O' + str(num+1)].value).split("/")[1].split("in")[0].replace(' Rises ', '日出').replace(' Sets ', '日落')+"还有"+sheet['O' + str(num+1)].value.split("/")[1].split("in")[1]
                text=text+"\n"+placn+"-"+msg+"的位置为：\nOM1 "+str(sheet['E' + str(num+1)].value)+"\nOM2 "+str(sheet['F' + str(num+1)].value)+"\nOM3 "+str(sheet['G' + str(num+1)].value)+"\nOM4 "+str(sheet['H' + str(num+1)].value)+"\nOM5 "+str(sheet['I' + str(num+1)].value)+"\nOM6 "+str(sheet['J' + str(num+1)].value)
            else:
                text="当前"+msg+"的时间为：\n"+str(sheet['O' + str(num+1)].value).split("/")[0]
                text=text+"\n"+placn+"-"+msg+"的位置为：\nOM1 "+str(sheet['E' + str(num+1)].value)+"\nOM2 "+str(sheet['F' + str(num+1)].value)+"\nOM3 "+str(sheet['G' + str(num+1)].value)+"\nOM4 "+str(sheet['H' + str(num+1)].value)+"\nOM5 "+str(sheet['I' + str(num+1)].value)+"\nOM6 "+str(sheet['J' + str(num+1)].value)
            text=text+"\n"+"当前现实时间为："+ str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日"+str(today.hour).rjust(2,'0')+":"+str(today.minute).rjust(2,'0')+":"+str(today.second).rjust(2,'0')
            await findtime.finish(text)
        else:
            text="地点不唯一，请检查输入名称\n以下包含["+msg+"]:\n"+"\n".join(flist.LOCCN)
            await findtime.finish(text)
    else:
        await findtime.finish("未找到该地点，请检查输入名称")
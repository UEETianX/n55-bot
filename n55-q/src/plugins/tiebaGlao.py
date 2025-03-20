
from nonebot import on_command, require, get_bots
from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message
from nonebot.params import CommandArg
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
import asyncio
import os
from time import sleep
from random import randint
import requests
from random import choice
import urllib.request
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
import xml.etree.ElementTree as ET
import math
from pathlib import Path

__plugin_name__ = 'timing'
__plugin_usage__ = '用法：在规定时间触发发送的信息。'

# 发送图片时用到的函数, 返回发送图片所用的编码字符串
def send_img(img_name):
    return MessageSegment.image(path=img_name)

# 设置一个定时器
tieba = require("nonebot_plugin_apscheduler").scheduler


# 设置在15:00发送信息
#@tieba.scheduled_job("cron", hour='*/2', id="glao")
#async def glao():
#    bot, = get_bots().values()
#    assert isinstance(bot, Bot)
#    # 发送一条群聊信息
#    def request_html(url):
#        ua=UserAgent()
#        headers={'User-Agent':str(UserAgent("C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/fake_useragent_0.1.11.json").random)}
#        request = urllib.request.Request(url, headers=headers)
#        return request
#    url='https://tieba.baidu.com/home/main/?id=tb.1.c71983a8._2RHIWDtaJALopgO4mFVeg&fr=frs'
#    request = request_html(url)
#    html = urllib.request.urlopen(request).read().decode('utf8')
#    soup =BeautifulSoup(html, 'lxml')
#    list_name = soup.select('.title')
#    links = [p.get("href").split("?")[0] for p in list_name]
#    f=open("C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/tiebalist.txt","r+")
#    linktext = f.readline()
#    if links[0] in linktext:
#        f.close()
#    else:
#        f.seek(0)	# 定位
#        f.truncate()
#        f.write(str(links))
#        f.close()
#        print("G佬更新啦")
#        path = "https://tieba.baidu.com" + links[0] + "?see_lz=1"
#        request = request_html(path)
#        html = urllib.request.urlopen(request).read().decode('utf8')
#        soup =BeautifulSoup(html, 'lxml')
#        title = soup.select('.core_title_txt.pull-left.text-overflow.vip_red')[0].get_text().strip(" ")
#        article = soup.select('.d_post_content.j_d_post_content')
#        sendwd = ""
#        for x in range(len(article)):
#            cmdstr = " "
#            part1 = str(article[x]).replace("<img class=","imgplace<img class=")
#            part1 = str(part1).replace("<br/>","\n<br/>")
#            text_list = BeautifulSoup(part1).get_text().strip(" ").split("imgplace")
#            imglinks = article[x].find_all("img")
#            imglinks = [p.get("src") for p in imglinks]
#            text_list[0] = "\n" + text_list[0]
#            if len(imglinks) == 0:
#                cmdstr ="text_list[-1]"
#            else:
#                for i in range(len(imglinks)):
#                    if i == 0:
#                        cmdstr = "text_list[" + str(i) + "]" + " + MessageSegment.image(path=imglinks[" + str(i) + "])"
#                    else:
#                        cmdstr = cmdstr + " + text_list[" + str(i) + "]" + " + MessageSegment.image(path=imglinks[" + str(i) + "])"
#                if len(imglinks) < len(text_list):
#                    cmdstr = cmdstr + " + text_list[-1]"
#            sendwd = sendwd + eval(cmdstr)
#        groups = [955342491,473081444,762792972,959233317,74821097,569705657,745131656,472786437,691702096,774655949,751972290,477726252,798762938,691311516,943088969,849535523,924584753]
#        for group in groups:
#            await bot.send_group_message(
#                target=group,
#                message="G-lao最新帖子：\n\n"+title + sendwd
#            )
#            await asyncio.sleep(randint(2, 5))

tiebafind=on_command("最新帖子",priority=1)

@tiebafind.handle()
async def handle_function():
    await tiebafind.send("正在查找帖子。。。")
    def request_html(url):
        ua=UserAgent()
        headers={'User-Agent':str(UserAgent("C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/fake_useragent_0.1.11.json").random)}
        request = urllib.request.Request(url, headers=headers)
        return request
    url='https://tieba.baidu.com/home/main/?id=tb.1.c71983a8._2RHIWDtaJALopgO4mFVeg&fr=frs'
    request = request_html(url)
    html = urllib.request.urlopen(request).read().decode('utf8')
    soup =BeautifulSoup(html, 'lxml')
    list_name = soup.select('.title')
    links = [p.get("href").split("?")[0] for p in list_name]
    path = "https://tieba.baidu.com" + links[0] + "?see_lz=1"
    print(path)
    request = request_html(path)
    html = urllib.request.urlopen(request).read().decode('utf8')
    soup =BeautifulSoup(html, 'lxml')
    title = soup.select('.core_title_txt.pull-left.text-overflow.vip_red')[0].get_text().strip(" ")
    data=soup.select('.tail-info')
    article = soup.select('.d_post_content.j_d_post_content')
    sendwd = ""
    l = [s.get_text().strip(" ") for s in data if ':' in s.get_text().strip(" ")][0]
#    await tiebafind.send("G-lao帖子：\n"+l +"\n"+title)
    for x in range(len(article)):
        cmdstr = " "
        part1 = str(article[x]).replace("<img class=","imgplace<img class=")
        part1 = str(part1).replace("<br/>","\n<br/>")
        text_list = BeautifulSoup(part1).get_text().strip(" ").split("imgplace")
        imglinks = article[x].find_all("img")
        imglinks = [p.get("src") for p in imglinks]
        text_list[0] = "\n" + text_list[0]
        if len(imglinks) == 0:
            cmdstr ="text_list[-1]"
        else:
            for i in range(len(imglinks)):
                try:
                    text_list[i]==None
                except:
                    text_list=text_list+[""]
                if i == 0:
                    pic = requests.get(imglinks[i], timeout=8)
                    image = Image.open(BytesIO(pic.content))
                    image.save('C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/tiebaimg'+str(i)+'.png')
                    imgstr="path"+str(i)+"='C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/tiebaimg"+str(i)+".png'"
                    exec(imgstr)
                    cmdstr = "text_list[" + str(i) + "]" + " + MessageSegment.image(path=path"+str(i)+ ")"
                else:
                    pic = requests.get(imglinks[i], timeout=8)
                    image = Image.open(BytesIO(pic.content))
                    image.save('C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/tiebaimg'+str(i)+'.png')
                    imgstr="path"+str(i)+"='C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/tiebaimg"+str(i)+".png'"
                    exec(imgstr)
                    cmdstr = cmdstr + " + text_list[" + str(i) + "]" + " + MessageSegment.file_image(Path(__file__).parent / path" + str(i) + ")"
            if len(imglinks) < len(text_list):
                cmdstr = cmdstr + " + text_list[-1]"
        sendwd = sendwd + eval(cmdstr)
        if x==0:
            await tiebafind.send("G-lao帖子：\n"+l +"\n"+title+eval(cmdstr))
        else:
            await tiebafind.send(eval(cmdstr))
        sleep(1)
    await tiebafind.finish("G佬如是说~")

tiezi=on_command("帖子",priority=1)
@tiezi.handle()
async def handle_function(args: Message = CommandArg()):
    await tiezi.send("正在查找帖子。。。")
    arg = args.extract_plain_text()
    def request_html(url):
        ua=UserAgent()
        headers={'User-Agent':str(UserAgent("C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/fake_useragent_0.1.11.json").random)}
        request = urllib.request.Request(url, headers=headers)
        return request
    url='https://tieba.baidu.com/home/main/?id=tb.1.c71983a8._2RHIWDtaJALopgO4mFVeg&fr=frs'
    request = request_html(url)
    html = urllib.request.urlopen(request).read().decode('utf8')
    soup =BeautifulSoup(html, 'lxml')
    list_name = soup.select('.title')
    timelist=soup.select('.n_post_time')
    timelist=[s.get_text().strip(" ") for s in timelist]
    if arg:
        print(arg)
    else:
        arg = 0
    if arg == "列表" or arg == "编号":
        name=[p.get_text() for p in list_name]
        for i in range(len(name)):
            name[i] = str(i) + ". " + name[i]+"  "+timelist[i]
        name = "输入[查帖子<编号>]可查看帖子内容" + "\n\n" + "\n\n".join(name)
        await tiezi.finish(name)
    if int(arg) not in range(20):
        tiezi.finish("不支持该参数，请输入0-19的数字，例如：查帖子0")
    links = [p.get("href").split("?")[0] for p in list_name]
    path = "https://tieba.baidu.com" + links[int(arg)] + "?see_lz=1"
    print(path)
    request = request_html(path)
    html = urllib.request.urlopen(request).read().decode('utf8')
    soup =BeautifulSoup(html, 'lxml')
    title = soup.select('.core_title_txt.pull-left.text-overflow.vip_red')[0].get_text().strip(" ")
    data=soup.select('.tail-info')
    article = soup.select('.d_post_content.j_d_post_content')
    sendwd = ""
    l = [s.get_text().strip(" ") for s in data if ':' in s.get_text().strip(" ")][0]
#    await tiezi.send("G-lao帖子：\n"+l +"\n"+title)
    for x in range(len(article)):
        cmdstr = " "
        part1 = str(article[x]).replace("<img class=","imgplace<img class=")
        part1 = str(part1).replace("<br/>","\n<br/>")
        text_list = BeautifulSoup(part1).get_text().strip(" ").split("imgplace")
        imglinks = article[x].find_all("img")
        imglinks = [p.get("src") for p in imglinks]
        text_list[0] = "\n" + text_list[0]
        if len(imglinks) == 0:
            cmdstr ="text_list[-1]"
        else:
            for i in range(len(imglinks)):
                try:
                    text_list[i]==None
                except:
                    text_list=text_list+[""]
                if i == 0:
                    pic = requests.get(imglinks[i], timeout=8)
                    image = Image.open(BytesIO(pic.content))
                    image.save('C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/tiebaimg'+str(i)+'.png')
                    imgstr="path"+str(i)+"='C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/tiebaimg"+str(i)+".png'"
                    exec(imgstr)
                    cmdstr = "text_list[" + str(i) + "]" + " + MessageSegment.file_image(Path(__file__).parent / path"+str(i)+ ")"
                else:
                    pic = requests.get(imglinks[i], timeout=8)
                    image = Image.open(BytesIO(pic.content))
                    image.save('C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/tiebaimg'+str(i)+'.png')
                    imgstr="path"+str(i)+"='C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/tiebaimg"+str(i)+".png'"
                    exec(imgstr)
                    cmdstr = cmdstr + " + text_list[" + str(i) + "]" + " + MessageSegment.file_image(Path(__file__).parent / path" + str(i) + ")"
            if len(imglinks) < len(text_list):
                cmdstr = cmdstr + " + text_list[-1]"
        sendwd = sendwd + eval(cmdstr)
        if x == 0 :
            await tiezi.send("G-lao帖子：\n"+l +"\n"+title+eval(cmdstr))
        else:
            await tiezi.send(eval(cmdstr))
        sleep(1)
    await tiezi.finish("G佬如是说~")
#    if len(str(sendwd).split("\n"))>47:
#        for i in range(math.ceil((len(str(sendwd).split("\n"))+1)/47)):
#            await tiezi.send("\n".join(str(sendwd).split("\n")[(0+47*i):(47+47*i)]))
#            await asyncio.sleep(1)
#    else:
#        await tiezi.finish(sendwd)

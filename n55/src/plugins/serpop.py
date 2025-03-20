from nonebot.adapters.satori.event import MessageEvent
from nonebot.adapters.satori.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from time import sleep
import datetime
from pytz import timezone
import pandas as pd
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import os
import requests
import sys
from io import BytesIO
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib import error
import urllib
import json
import random

serpop=on_command("服务器",priority=1)
@serpop.handle()
async def handle_function(bot:Bot,event:Event,state:T_State):
    def request_html(url):
        ua=UserAgent()
        headers={'User-Agent':str(UserAgent("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/fake_useragent_0.1.11.json").random)}
        request = urllib.request.Request(url, headers=headers)
        return request

    url='https://status.robertsspaceindustries.com/index.json'
    request = request_html(url)
    html = urllib.request.urlopen(request).read().decode('utf8')
    soup =json.loads(html)
    def trans(x):
        if x.lower() =="operational":
            info = "正常"
        elif x.lower() =="partial outage":
            info = "部分中断"
        elif x.lower() =="under maintenance":
            info = "维护中"
        elif x.lower() =="degraded performance":
            info = "性能下降"
        elif x.lower() =="major outage":
            info = "重大中断"
        elif x.lower() =="degraded":
            info = "性能下降"
        return info
    hexagram_texts = {
    (7, 7, 7, 7, 7, 7): "乾：元亨，利贞。",
    (8, 8, 8, 8, 8, 8): "坤：元亨，利牝马之贞。",
    (8, 7, 8, 8, 8, 8): "屯：元亨，利贞。勿用有攸往，利建侯。",
    (7, 8, 8, 8, 8, 8): "蒙：亨。匪我求童蒙，童蒙求我。初筮告，再三渎，渎则不告。利贞。",
    (7, 7, 8, 8, 8, 8): "需：有孚，光亨，贞吉。利涉大川。",
    (8, 8, 8, 7, 7, 8): "讼：有孚窒惕，中吉，终凶。利见大人，不利涉大川。",
    (8, 7, 7, 7, 7, 8): "师：贞，丈人吉，无咎。",
    (8, 8, 8, 8, 7, 7): "比：吉。原筮，元永贞，无咎。不宁方来，后夫凶。",
    (7, 8, 7, 8, 8, 8): "小畜：亨。柔顺而志行，小畜以柔，亨，柔顺而志行。",
    (8, 8, 7, 8, 7, 8): "履：履虎尾，不咥人，亨。",
    (8, 7, 7, 8, 7, 8): "泰：小往大来，吉亨。",
    (7, 8, 7, 7, 8, 7): "否：否之匪人，不利君子贞，大往小来。",
    (7, 7, 8, 7, 8, 8): "同人：同人于野，亨。利涉大川，利君子贞。",
    (8, 8, 7, 8, 7, 7): "大有：元亨。",
    (8, 7, 8, 8, 7, 8): "谦：亨，君子有终。",
    (8, 7, 8, 7, 8, 7): "豫：利建侯行师。",
    (7, 7, 8, 8, 7, 7): "随：元亨，利贞，无咎。",
    (7, 7, 8, 7, 7, 8): "蛊：元亨，利涉大川，先甲三日，后甲三日。",
    (8, 7, 7, 8, 8, 7): "临：元，亨，利，贞。至于八月有凶。",
    (7, 8, 8, 7, 7, 8): "观：盥而不荐，有孚顒若。",
    (8, 8, 8, 7, 8, 7): "噬嗑：亨。利用狱。",
    (7, 8, 7, 8, 8, 7): "贲：亨。小利有所往。",
    (8, 7, 8, 7, 7, 7): "剥：不利有攸往。",
    (7, 7, 7, 8, 7, 8): "复：亨。出入无疾，朋来无咎。反复其道，七日来复。利有攸往。",
    (7, 8, 8, 8, 8, 7): "无妄：元亨，利贞。其匪正有眚，不利有攸往。",
    (8, 7, 7, 7, 8, 8): "大畜：利贞。不家食吉，利涉大川。",
    (8, 8, 7, 7, 7, 8): "颐：贞吉。观颐，自求口实。",
    (7, 8, 7, 7, 7, 7): "大过：栋桡，利有攸往，亨。",
    (7, 7, 7, 8, 8, 8): "坎：习坎，有孚维心，亨。行有尚。",
    (8, 8, 8, 7, 7, 7): "离：利贞，亨。畜牝牛，吉。",
    (7, 7, 8, 8, 8, 7): "咸：亨，利贞。取女吉。",
    (7, 8, 8, 8, 7, 7): "恒：亨，无咎。利贞，利有攸往。",
    (8, 7, 8, 8, 7, 7): "遯：亨，小利贞。",
    (7, 7, 8, 8, 7, 8): "大壮：利贞。",
    (8, 7, 7, 7, 8, 7): "晋：康侯用锡马蕃庶，昼日三接。",
    (7, 8, 7, 7, 8, 8): "明夷：利艰贞。",
    (8, 8, 7, 8, 8, 8): "家人：利女贞。",
    (8, 8, 8, 7, 8, 8): "睽：小事吉。",
    (7, 8, 8, 7, 8, 8): "蹇：利西南，不利东北。利见大人，贞吉。",
    (8, 8, 7, 8, 8, 7): "解：利西南，无所往，其来复吉。有攸往，夙吉。",
    (7, 8, 7, 8, 8, 8): "损：有孚，元吉，无咎，可贞。利有攸往。曷之用，二簋可用享。",
    (8, 8, 8, 7, 8, 7): "益：利有攸往，利涉大川。",
    (7, 8, 8, 7, 8, 7): "夬：扬于王庭，孚号有厉。告自邑，不利即戎，利有攸往。",
    (8, 7, 8, 7, 8, 8): "姤：女壮，勿用取女。",
    (7, 8, 8, 8, 7, 8): "萃：亨。王假有庙，利见大人，亨，利贞。用大牲吉，利有攸往。",
    (8, 7, 8, 8, 8, 7): "升：元亨。用见大人，勿恤。南征吉。",
    (7, 8, 8, 7, 7, 7): "困：亨。贞，大人吉，无咎。有言不信。",
    (7, 7, 7, 8, 8, 7): "井：改邑不改井，无丧无得。往来井井。汔至亦未繘井，羸其瓶，凶。",
    (8, 7, 7, 7, 7, 8): "革：己日乃孚。元亨，利贞，悔亡。",
    (7, 8, 7, 7, 8, 7): "鼎：元吉，亨。",
    (8, 8, 7, 7, 8, 8): "震：亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。",
    (8, 8, 8, 7, 7, 8): "艮：艮其背，不获其身，行其庭，不见其人，无咎。",
    (7, 7, 8, 7, 8, 8): "渐：女归吉，利贞。",
    (8, 8, 7, 8, 7, 7): "归妹：征凶，无攸利。",
    (7, 7, 7, 8, 7, 8): "丰：亨。王假之，勿忧，宜日中。",
    (8, 7, 8, 7, 7, 8): "旅：小亨，旅贞吉。",
    (7, 8, 8, 8, 8, 8): "巽：小亨，利有攸往，利见大人。",
    (8, 8, 8, 8, 7, 8): "兑：亨，利贞。",
    (7, 8, 8, 8, 7, 8): "涣：亨。王假有庙，利涉大川，利贞。",
    (8, 7, 8, 8, 8, 8): "节：亨。苦节不可贞。",
    (8, 8, 7, 7, 7, 7): "中孚：豚鱼，吉。利涉大川，利贞。",
    (7, 7, 7, 7, 8, 8): "小过：亨，利贞。可小事，不可大事。飞鸟遗之音，不宜上，宜下，大吉。",
    (8, 7, 7, 8, 7, 8): "既济：亨小，利贞。初吉终乱。",
    (7, 8, 7, 8, 7, 7): "未济：亨。小狐汔济，濡其尾，无攸利。",
    }

    def random_hexagram():
        # 从六十四卦中随机选择一个
        hexagram = random.choice(list(hexagram_texts.keys()))
        return hexagram_texts[hexagram]

    text = random_hexagram()
    path = os.path.split(os.path.realpath(__file__))[0] + '/img/云端.jpg'
    await serpop.send("当前服务器状态使用时差推算已无意义，建议广加好友，右键好友加入更为稳妥。\n平台状态："+trans(soup['systems'][0]['status'])+"\nPU状态："+trans(soup['systems'][1]['status'])+"\nAC状态："+trans(soup['systems'][2]['status']))
    #await serpop.finish("来都来啦55姬送你一卦~\n(掐指中)安巴尼莱蒙~\n(翻白眼)安巴尼莱蒙~\n六十四卦卦象："+text)
    #date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/serpop.png", cv2.IMREAD_UNCHANGED)
    #text1 = "建议服务器：" + sug
    #text2 = "USA时间:" + str(USA_now.hour) + ":" + str(USA_now.minute)
    #text25 = "当前人数：" + USA_pop
    #text3 = "EU 时间:" + str(EU_now.hour) + ":" + str(EU_now.minute)
    #text35 = "当前人数：" + EU_pop
    #text4 = "CN 时间:" + str(CN_now.hour) + ":" + str(CN_now.minute)
    #text45 = "当前人数：" + CN_pop
    #text5 = "AUS时间:" + str(AUS_now.hour) + ":" + str(AUS_now.minute)
    #text55 = "当前人数：" + AUS_pop
    #text6 = "当前服务器状态：" + info
    #text7 = "人数为时差推测"
    #text12 = "现在时间：" + str(CN_now.hour) + ":" + str(CN_now.minute) + ":" + str(CN_now.second)
    #fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/1637505678825667.ttc"
    #b,g,r,a = 19,69,139,0
    #font1 = ImageFont.truetype(fontpath,50)
    #font2 = ImageFont.truetype(fontpath,40)
    #font3 = ImageFont.truetype(fontpath,25)
    #img_pil = Image.fromarray(date)
    #draw = ImageDraw.Draw(img_pil)
    #draw.text((100,80),text1,font=font1,fill=(b,g,r,a))
    #draw.text((100,130),text7,font=font3,fill=(b,g,r,a))
    #draw.text((100,200),text2,font=font2,fill=(b,g,r,a))
    #draw.text((450,200),text25,font=font2,fill=(b,g,r,a))
    #draw.text((100,300),text3,font=font2,fill=(b,g,r,a))
    #draw.text((450,300),text35,font=font2,fill=(b,g,r,a))
    #draw.text((100,400),text4,font=font2,fill=(b,g,r,a))
    #draw.text((450,400),text45,font=font2,fill=(b,g,r,a))
    #draw.text((100,500),text5,font=font2,fill=(b,g,r,a))
    #draw.text((450,500),text55,font=font2,fill=(b,g,r,a))
    #draw.text((180,580),text6,font=font2,fill=(b,g,r,a))
    #draw.text((220,650),text12,font=font2,fill=(b,g,r,a))
    #img = np.array(img_pil)
    #cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/serpop.jpg', img)
    #path = os.path.split(os.path.realpath(__file__))[0] + '/serpop.jpg'
    #await serpop.finish(MessageSegment.image(path=path))


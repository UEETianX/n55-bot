from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
import requests
import os
import random
import datetime
import time
import json
from time import sleep
import numpy as np
import string
import pandas as pd
from random import choice
import cv2
from PIL import ImageFont, ImageDraw, Image
import urllib.request
import requests
from urllib import error
import random
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
import numpy as np 
from io import BytesIO
import xml.etree.ElementTree as ET
import math
import re
find=on_message(priority=2)
from pathlib import Path
count = 0

@find.handle()
async def _(bot:Bot,event:Event,state:T_State):
    if str(type(event)) =="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
        group_id = "A"
        user_id =event.author.user_openid
    else:
        group_id = event.group_openid
        user_id = event.author.member_openid
    msg = str(event.get_message()).strip().replace(" ","")
    if msg.startswith('/'):
        msg= '查' + msg[1:]
    if "查全览图".lower() == msg.lower() or "查舰船全览图" == msg  or "查所有船" == msg:
        path1=os.path.split(os.path.realpath(__file__))[0] + '/img/50米舰船全览图.png'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/img/50米以上舰船全览图.png'
        path3=os.path.split(os.path.realpath(__file__))[0] + '/img/车辆全览图.png'
        print(Path(__file__).parent / path1)
        await find.send(MessageSegment.file_image(Path(__file__).parent / path1))
        await find.send(MessageSegment.file_image(Path(__file__).parent / path2))
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path3))

    if  "查车辆" in msg or "查地面" in msg or "查载具" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/车辆全览图.png'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/img/地面车辆适配统计.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path)+MessageSegment.file_image(Path(__file__).parent / path2))

    if  "查套娃" in msg or "查兼容" in msg or "查适配" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/飞船适配统计.png'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/img/地面车辆适配统计.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path)+MessageSegment.file_image(Path(__file__).parent / path2))

    if "查舰队规模".lower() in msg.lower():
        if group_id == "774655949":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/航安规模.png'
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "0A8817114034ADEE05E0BB12D2E31EF2" or group_id == "881232934":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/天命规模1.jpg'
            path2=os.path.split(os.path.realpath(__file__))[0] + '/img/天命规模2.jpg'
            await find.send(MessageSegment.file_image(Path(__file__).parent / path))
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path2))
        elif group_id == "751972290":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/UEE特种舰队规模.png'
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "472786437" or group_id == "691702096" or group_id == "929172498" or group_id == "729806532":            
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/深航规模.png'
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "671108780":
            path1=os.path.split(os.path.realpath(__file__))[0] + '/img/红星规模1.jpg'
            path2=os.path.split(os.path.realpath(__file__))[0] + '/img/红星规模2.jpg'
            path3=os.path.split(os.path.realpath(__file__))[0] + '/img/红星规模3.jpg'
            path4=os.path.split(os.path.realpath(__file__))[0] + '/img/红星规模4.jpg'
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path1)+MessageSegment.file_image(Path(__file__).parent / path2)+MessageSegment.file_image(Path(__file__).parent / path3)+MessageSegment.file_image(Path(__file__).parent / path4))
        else:
            path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/舰队规模.jpg'
            await find.finish("该群尚未录入舰队规模，可以使用https://hangar.link/或者https://starship42.com/工具绘制后，私聊作者添加")

    if "查星门".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/星门教学.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查罗威尔".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/赫斯顿·罗威尔全览图.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查18区".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/弧光星·18区全览图.PNG'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查奥里森".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/奥里森地图.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查新巴贝奇".lower() in msg.lower():
        path1=os.path.split(os.path.realpath(__file__))[0] + '/img/新巴贝奇1.png'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/img/新巴贝奇2.png'
        path3=os.path.split(os.path.realpath(__file__))[0] + '/img/新巴贝奇3.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path1)+MessageSegment.file_image(Path(__file__).parent / path2)+MessageSegment.file_image(Path(__file__).parent / path3))
    
    if "查流萤".lower() in msg.lower():
        path1=os.path.split(os.path.realpath(__file__))[0] + '/img/流萤1.jpg'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/img/流萤2.jpg'
        path3=os.path.split(os.path.realpath(__file__))[0] + '/img/流萤3.jpg'
        path4=os.path.split(os.path.realpath(__file__))[0] + '/img/流萤4.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path1)+MessageSegment.file_image(Path(__file__).parent / path2)+MessageSegment.file_image(Path(__file__).parent / path3)+MessageSegment.file_image(Path(__file__).parent / path4))
    
    if "查周年".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/2953ZN.jpg'
        await find.finish("北京时间：\n第一波：凌晨0点\n第二波：上午8点\n第三波：下午4点\nIAE第2天-11月24日：圣盾伊德里斯P、圣盾标枪\nIAE第3天-11月25日：武藏货运E\nIAE第5天-11月27日：RSI星座-凤凰座\nIAE第6天-11月28日：联合外域开拓者\nIAE第7天-11月29日：德雷克海妖、德雷克海妖-私掠者\nIAE第8天-11月30日：起源890跃动"+MessageSegment.file_image(Path(__file__).parent / path))

    if "查舰队周".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/2954JD.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查光灯".lower() in msg.lower() or "查灯光".lower() in msg.lower():
        await find.finish("光灯节活动页面：\nhttps://robertsspaceindustries.com/comm-link/transmission/19605-Luminalia-2953")

    if "查bis".lower() in msg.lower() or "查投票".lower() in msg.lower():
        await find.finish("bis活动页面：\nhttps://robertsspaceindustries.com/ship-showdown2024/community-call")

    if "查货物网格".lower() in msg.lower() or "查货舱".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/货物网格.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查借船".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/借船表.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查派罗".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/pailuo.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查争夺区".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/争夺区1.jpg'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/img/争夺区2.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path2))

    if "查美元价格".lower() in msg.lower() or "查美金价格".lower() in msg.lower() or "查美刀价格".lower() in msg.lower():
        path1=os.path.split(os.path.realpath(__file__))[0] + '/img/圣盾铁砧美元价格表.png'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/img/RSI十字军美元价格表.png'
        path3=os.path.split(os.path.realpath(__file__))[0] + '/img/起源联合外星美元价格表.png'
        path4=os.path.split(os.path.realpath(__file__))[0] + '/img/德雷克盾博尔灰猫美元价格表.png'
        path5=os.path.split(os.path.realpath(__file__))[0] + '/img/武藏南船克鲁格美元价格表.png'
        await find.finish("圣盾、铁砧价格表："+MessageSegment.file_image(Path(__file__).parent / path1)+"RSI、十字军价格表："+MessageSegment.file_image(Path(__file__).parent / path2)+"起源、联合外域、外星科技价格表："+MessageSegment.file_image(Path(__file__).parent / path3)+"德雷克、盾博尔、灰猫价格表："+MessageSegment.file_image(Path(__file__).parent / path4)+"武藏(未来)、南船座、克鲁格价格表："+MessageSegment.file_image(Path(__file__).parent / path5))


    if "查游戏币价格".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/游戏币价格表.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))


    if "查菜单".lower() == msg.lower() or "查指令".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/天命菜单.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "原神".lower() == msg.lower() or "原神！".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/原神.jpg'
        await find.finish("启动！"+MessageSegment.file_image(Path(__file__).parent / path))

    if "查".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/生气.jpg'
        path1=os.path.split(os.path.realpath(__file__))[0] + '/MP3/SCA.silk.amr'
        await find.send(MessageSegment.file_audio(Path(__file__).parent / path1))
        await find.finish("说词啊！"+MessageSegment.file_image(Path(__file__).parent / path))

    if "查打捞" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/打捞价格.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查异种" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/异种.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))


    if "查游戏配置".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/游戏配置目录.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查新手问答".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/新手问答.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查消费额".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/消费额奖励图.jpeg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查游戏官网".lower() in msg.lower():
        await find.finish("https://robertsspaceindustries.com/")
    
    if "查KOOK".lower() in msg.lower() or "查舰队KOOK".lower() in msg.lower() or "查舰队语音".lower() in msg.lower() or "查语音".lower() in msg.lower():
        await find.finish("还在维护喵~")
        group_id = event.group_openid
        if group_id == "955342491" or group_id == "881232934":
            msg="KOOK频道：60893671\n\n"
            url='https://www.kookapp.cn/api/v2/guild/view?id=9921695325288659&active_id=9921695325288659'
        elif group_id == "473081444":
            await find.finish("https://kook.top/9ZjYzl")
        elif group_id == "808266184":
            await find.finish("oopz频道:713353805\noopz链接:https://oopz.cn/i/fI8v2o")
        elif group_id == "1043568611":
            url='https://www.kookapp.cn/api/v2/guild/view?id=1846039613230593&active_id=1846039613230593'
            msg="KOOK频道：https://kook.vip/ritYlL\n\n"
        elif group_id == "622854120":
            url='https://www.kookapp.cn/api/v2/guild/view?id=7150440011307159&active_id=7150440011307159'
            msg="KOOK频道：75523169\n\n"
        elif group_id == "959233317":
            await find.finish("6947rx3fq9")
        elif group_id == "958822717":
            await find.finish("OOPZ: \nhttps://oopz.cn/i/YXk4vM\nKOOK\nhttps://kook.vip/Px82Si")
        elif group_id == "74821097":
            await find.finish("54231316")
        elif group_id == "745131656":
            await find.finish("15873552")
        elif group_id == "774655949":
            await find.finish("https://kook.top/tHGQOC")
        elif group_id == "746893149":
            url='https://www.kookapp.cn/api/v2/guild/view?id=2718715929648281&active_id=2718715929648281'
            msg="KOOK频道：https://kook.vip/aELTzV\n\n"
        elif group_id == "472786437" or group_id == "691702096" or group_id == "929172498" or group_id == "729806532":    
            await find.finish("Oopz链接：https://oopz.cn/i/QvZLq2")
        elif group_id == "120332330":    
            url='https://www.kookapp.cn/api/v2/guild/view?id=2415424945131801&active_id=2415424945131801'
            msg="KOOK频道：https://kook.top/bc6gXY\n\n"
        elif group_id == "1067026566":    
            url='https://www.kookapp.cn/api/v2/guild/view?id=5088306471584298&active_id=5088306471584298'
            msg="KOOK频道：https://kook.top/rXVHpc\n\n"
        elif group_id == "227965444":    
            url='https://www.kookapp.cn/api/v2/guild/view?id=6208899912294023&active_id=6208899912294023'
            msg="KOOK频道：71495397\n\n"
        elif group_id == "569705657":
            await find.finish("53591966")
        elif group_id == "549513666":
            await find.finish("https://kook.top/TylEVd")
        elif group_id == "877388955":
            await find.finish("13977959")
        elif group_id == "751972290":
            await find.finish("https://pd.qq.com/s/1egfs7ypf")
        elif group_id == "477726252":
            await find.finish("https://kook.top/FFfBMa")
        elif group_id == "924584753":
            await find.finish("https://kook.top/rrhVTG")
        elif group_id == "547372526" or group_id == "348166175":
            await find.finish("25182973")
        elif group_id == "96607625":
            await find.finish("YY频道：12776")
        elif group_id == "281598774":
            await find.finish("https://kook.top/8dsDFm")
        elif group_id == "149774174":
            await find.finish("https://kook.top/Adusiy")
        else:
            await find.finish("该群尚未录入KOOK链接，可私聊作者添加")
        def request_html(url):
            headers={'User-Agent':str(UserAgent("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/fake_useragent_0.1.11.json").random),
                     'Cookie':'Hm_lvt_ad9a793420ed959cf56a032b6eb75140=1715826315; PHPSESSID=0n63kg5kfr06vu03mdqkb8pssk; auth=5508b1d1690401610c0ef28a9c4a81d898a8b3bb2b04864c9664af71efb743141661944-1715827047; _c_WBKFRo=SN7mWetd7ztfnoIxxItKTDKTvxMG7I9bOZvzT3N0; _nb_ioWEgULi=; Hm_lpvt_ad9a793420ed959cf56a032b6eb75140=1715838884; _csrf_chuanyu=GtBjGbNyDNSRnY9LkAth7dWi2-WcnlNr; tfstk=fi6sAc6hEV0_ESSBoCEedRotuS9jCNwzHmtAqiHZDdptkqIJ8d8wQNJfDiYFQIJTsiIvJZb4jiSqhosv-cn9MChLp3-DDfdxHDhp4hTtkIKOvpKJVfKvMCnGtaS-QOPM3x9MnKUzz8yzjGvDHdCVXnTGvMxxaqHR2GjMnDca2vHAjj6zt_E6HZpp9nx2HhKvXkGpmeH9DAKxJktDJEpvXCHpJ3tqHELx9PVBv5TFfrrhBfzg6nj9RYshdhprsGLIHxBC1CT-UeMxH9t1xZOzkYN2y_YwaebLLA9fvn_WVNgLRKICITOdByDfPw1JdHf3ljT5MG5lMBZTBM965Q6eTchXCsQGhCfsmujpBwfkrCF3-H6NUITkO2UOYMT9Ns_a-xLNNMQBa9uEUpIROpsPXY87FDGjAQDXAUrQAjc2LTZHvB4le6d9xHmzAkGriCKHAUrQAjcD6Hx3UkZIajf..'}
            request = urllib.request.Request(url, headers=headers)
            return request
        request = request_html(url)
        html = urllib.request.urlopen(request).read().decode('utf8')
        data=json.loads(html)
        channels=data['channels']
        channels2=[s for s in channels if "'users'" in str(s)]
        channels2=[s['channels'] for s in channels2]
        channels3=[s for x in channels2 for s in x if "'users'" in str(s)]
        channels4=[s['name'] for s in channels3]
        users=[s['users'] for s in channels3]
        if len(channels4)==0:
            msg=msg+"KOOK频道中暂无玩家"
        else:
            msg=msg+"以下频道有活跃玩家:"
            for i in range(len(channels4)):
                user1=[s['nickname'] for s in users[i]]
                msg=msg+"\n\n"+channels4[i]+"  "+str(len(user1))+"人\n"+"、".join(user1)
        await find.finish(msg)

    if "查黑盒".lower() in msg.lower() or "查黑盒语音".lower() in msg.lower() or "查小黑盒".lower() in msg.lower():
        await find.finish("还在维护喵~")
        group_id = event.group_openid
        if group_id == "100316150" or group_id == "209872290":
            url='https://chat.xiaoheihe.cn/chatroom/room/view?client_type=heybox_chat&x_client_type=web&os_type=web&x_os_type=Windows&device_info=Edge&x_app=heybox_chat&version=999.0.3&web_version=1.0.0&chat_os_type=web&chat_version=1.22.2&heybox_id=21648369&room_id=3571343395399409664&hkey=OPFKC02&nonce=8BC15C8BC9DD0EFE97CBE3EF81148799&_time=1716808272&_chat_time=1716808272689'
            msg="黑盒频道：https://chat.xiaoheihe.cn/i59qed\n\n"
        def request_html(url):
            headers={'User-Agent':str(UserAgent("C:\\Users/Administrator/Desktop/Qbot/n55-q/src/plugins/fake_useragent_0.1.11.json").random),
                     'Cookie':'smidV2=202405271814411fbdf44b95f1a0a27273ff3a5d7c0851000743038502cb850; user_pkey=MTcxNjgwNjYwNy44N18yMTY0ODM2OXd0c2NnamJ3d2dsd2p6anc__; user_heybox_id=21648369; x_xhh_tokenid=B7rkQRkYwTXAy94leKooX5vyzJeO00XqssTjGtZffzcCEcMehg9S0A7fWxKh5ji9fTLOkCSXjOrUFKjsC4LGZxQ%3D%3D; .thumbcache_4e0097a83862d42d22aeee22fef74bbf=fbJ6Qmq/LoxZukwovYkD6ikYs2vP/alMUkYNj+qsJQd7O+sAFtlA0L78j03X+g1lqkfbTep3y/vGGfPnF7PA5A%3D%3D'}
            request = urllib.request.Request(url, headers=headers)
            return request
        request = request_html(url)
        html = urllib.request.urlopen(request).read().decode('utf8')
        data=json.loads(html)
        channels=data['result']['room_info']['channels']
        channels2=[s for s in channels if "'members'" in str(s)]
        channels3=[s['channel_list'] for s in channels2]
        channels4=[s for x in channels3 for s in x if "'members'" in str(s)]
        channels5=[s['channel_name'] for s in channels4]
        users=[s['members'] for s in channels4]
        if len(channels4)==0:
            msg=msg+"黑盒频道中暂无玩家"
        else:
            msg=msg+"以下频道有活跃玩家:"
            for i in range(len(channels4)):
                user1=[s['nickname'] for s in users[i] if s['room_nickname']=='']+[s['room_nickname'] for s in users[i] if s['room_nickname']!='']
                msg=msg+"\n\n"+channels5[i]+"  "+str(len(user1))+"人\n"+"、".join(user1)
        await find.finish(msg)


    if "查舰队官网".lower() in msg.lower() or "查舰队".lower() == msg.lower() or "查舰队链接".lower() == msg.lower():
        await find.finish("还在维护喵~")
        group_id = event.group_openid
        if group_id == "955342491":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/FODA01-Logo.png'
            await find.finish("https://robertsspaceindustries.com/orgs/FODA01"+ MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "473081444":
            await find.finish("https://robertsspaceindustries.com/orgs/0928")
        elif group_id == "622854120":
            await find.finish("https://robertsspaceindustries.com/orgs/ICEBREAKE")
        elif group_id == "1043568611":
            await find.finish("https://robertsspaceindustries.com/orgs/FO210514")
        elif group_id == "959233317":
            await find.finish("https://robertsspaceindustries.com/orgs/CKHG")
        elif group_id == "74821097":
            await find.finish("https://robertsspaceindustries.com/orgs/UEK")
        elif group_id == "746893149":
            await find.finish("https://robertsspaceindustries.com/orgs/FIREFLYOVO")
        elif group_id == "958822717":
            await find.finish("https://robertsspaceindustries.com/orgs/KANAGAWA")
        elif group_id == "745131656":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/自由联盟.jpg'
            await find.finish("https://robertsspaceindustries.com/orgs/CNZHSC/members"+ MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "751972290":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/UEE特种舰队.jpg'
            await find.finish("https://robertsspaceindustries.com/orgs/UEEJSOC" + MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "472786437" or group_id == "691702096" or group_id == "929172498" or group_id == "729806532" or group_id == "958822717":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/深航舰队.png'
            await find.finish("https://robertsspaceindustries.com/orgs/SHENHANG" + MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "774655949":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/航安.jpg'
            await find.finish("https://robertsspaceindustries.com/orgs/SVSC" + MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "477726252":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/NOGS-logo.png'
            await find.finish("https://robertsspaceindustries.com/orgs/NOGS" + MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "924584753":
            await find.finish("https://robertsspaceindustries.com/orgs/OFSX")
        elif group_id == "671108780":
            await find.finish("https://robertsspaceindustries.com/orgs/RSUI")
        elif group_id == "547372526" or group_id == "348166175":
            await find.finish("https://robertsspaceindustries.com/orgs/SILVERFISH")
        elif group_id == "96607625":
            await find.finish("https://robertsspaceindustries.com/orgs/NWL")
        elif group_id == "281598774":
            await find.finish("https://robertsspaceindustries.com/orgs/281598774")
        elif group_id == "100316150":
            await find.finish("https://robertsspaceindustries.com/orgs/DKMR")
        elif group_id == "546860192":
            await find.finish("https://robertsspaceindustries.com/orgs/OUMC")
        elif group_id == "763277840":
            await find.finish("https://robertsspaceindustries.com/orgs/STARWAVECN")
        else:
            await find.finish("该群尚未录入舰队官网，可私聊作者添加")


    if "查部门".lower() in msg.lower() or  "查舰队部门".lower() == msg.lower():
        await find.finish("还在维护喵~")
        group_id = event.group_openid
        if group_id == "955342491":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/天命部门.png'
            await find.finish("天命舰队成员登记表https://docs.qq.com/sheet/DTmx5S2N4YUNrbllX?tab=BB08J2"+ MessageSegment.file_image(Path(__file__).parent / path)+"【<星际公民>天命舰队部门介绍-哔哩哔哩】\nhttps://b23.tv/YWLMhb6\n舰队一级作战部门 武装部 后勤部 探索部 医疗部\n舰队二级行政部门 外交部 宣传部 信息资源部 教导组\n所有新加入成员可先加入一级作战部门后，经过考察后方可加入二级行政部门")
        else:
            path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/舰队规模.jpg'
            await find.finish("该群尚未录入部门结构，可以使用图片形式，私聊作者添加")

    if "查舰队须知".lower() in msg.lower():
        await find.finish("还在维护喵~")
        group_id = event.group_openid
        if group_id == "955342491":
            path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/舰队规模.jpg'
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
        elif group_id == "751972290":
            await find.finish("1.舰队采用邀请制，不对外开放，由邀请者对其负责(邀请者负责简单引导教学，可自愿提供启动资金)。\n2.新入群成员ID格式为UEE-游戏ID(代号)，进群请修改ID格式语音ID同步修改。\n3.不定期组织集体活动，集体活动结束后凡是参与此次集体活动者可抽取商店现金护甲一套。\n4.舰队集体行动集合地点为十字军行星炽天使空间站(将部分舰船停泊此处)\n5.舰队唯一要求大家融洽相处。\n6.舰队语言软件为YY语音频道号30506666(集体活动时需要使用语音，平常不做要求)" )
        else:
            path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/舰队规模.jpg'
            await find.finish("该群尚未录入舰队须知，文字图片形式均可，私聊作者添加")

    if "查舰队视频号".lower() in msg.lower():
        await find.finish("还在维护喵~")
        group_id = event.group_openid
        if group_id == "745131656":
            await find.finish("5- 长按复制此条消息，打开抖音搜索，查看TA的更多作品。 https://v.douyin.com/iRCGBLYH/ 4@7.com 02/12")
        elif group_id == "1043568611":
            await find.finish("【星际公民-维斯塔集团的个人空间-哔哩哔哩】 https://b23.tv/h3H7bW4")
        else:
            path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/舰队规模.jpg'
            await find.finish("该群尚未录入舰队视频号，可私聊作者添加")



    if msg == "查实用网站":
        await find.finish("拆包数据网1：https://www.spviewer.eu/ \n拆包数据网2：https://www.erkul.games/live/calculator \nwiki网站：https://starcitizen.tools/Ships \n官网路线图：https://robertsspaceindustries.com/roadmap/progress-tracker/deliverables\n概念船借船公告：https://support.robertsspaceindustries.com/hc/en-us/articles/360003093114-Loaner-Ship-Matrix\n跑商网站1：https://uexcorp.space/trade \n跑商网站2：https://fleetyards.net/trade-routes \n跑商网站3：https://gallog.co \n跑商网站4：https://sc-trade.tools/home")

    if  "查星尘".lower() == msg.lower() or  "插星尘".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/白痴.jpg'
        await find.finish("暖暖的~紧紧的~" + MessageSegment.mention_user(2632032477) + MessageSegment.file_image(Path(__file__).parent / path))


    if  "查大蟑螂".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/白痴.jpg'
        await find.finish("大蟑螂有人找你！" + MessageSegment.mention_user(819613985) + MessageSegment.file_image(Path(__file__).parent / path))

    if  "查咸鱼".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/白痴.jpg'
        await find.finish("醒醒嘞！该翻面了！" + MessageSegment.mention_user(2833530830) + MessageSegment.file_image(Path(__file__).parent / path))


    if  "查梦心".lower() == msg.lower() or  "插梦心".lower() == msg.lower():
        today = datetime.datetime.now()
        time= str(today.month) + "_" + str(today.day)
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/白痴.jpg'
        await find.finish("暖暖的~紧紧的~" + MessageSegment.mention_user(2874809729) + MessageSegment.file_image(Path(__file__).parent / path))

    if  "插55姬" == msg or "插机器人" == msg:
        #await find.finish("FK严重，暂时关闭此功能")
        n = random.randint(0,100)
        if n > 90:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/大哭.jpg'
            await find.finish("天星天星，这个人欺负我！"+ MessageSegment.file_image(Path(__file__).parent / path))
        elif n > 40:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/生气.jpg'
            msg = choice(["插你个大头鬼！","给你剪掉！","变态！去死！","漏电保护解除！","你脑子里没有别的东西吗！"])
            await find.finish(msg+MessageSegment.file_image(Path(__file__).parent / path))
        else:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/害羞.jpg'
            msg = choice(["奇怪的东西增加了~","耳机插孔也可以的吗~","快把牙签收起来！"])
            await find.finish(msg+MessageSegment.file_image(Path(__file__).parent / path))
    if "查55姬" == msg or "查机器人" == msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/DF.jpg'
        path1=os.path.split(os.path.realpath(__file__))[0] + '/MP3/hello.silk.amr'
        await find.send(MessageSegment.file_audio(Path(__file__).parent / path1))
        await find.finish("欸？问我吗？我是全天待命的智障人形，虽然偶尔也会偷个懒啦~如果我睡着了或者被XX抓走了不要骂我好不好~\n问题反馈群：209872290" + MessageSegment.file_image(Path(__file__).parent / path))

    if "查天星" == msg or "插天星" == msg:
        #await find.finish("FK严重，暂时关闭此功能")
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/仰望.jpg'
        await find.finish("旁观吃瓜~"+ MessageSegment.mention_user(3126410936) +MessageSegment.file_image(Path(__file__).parent / path))

    if "查喵" == msg or "插喵" == msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/日喵.png'
        await find.finish("虽然有点难以启齿~但是~"+MessageSegment.mention_user(1697344211) +MessageSegment.file_image(Path(__file__).parent / path))

    if "查菜猫" == msg or "插菜猫" == msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/白痴.jpg'
        await find.finish("是奶油！我加了奶油！"+MessageSegment.mention_user(2395029012) +MessageSegment.file_image(Path(__file__).parent / path))

    if "查876" == msg or "插876" == msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/白痴.jpg'
        await find.finish("是求救信号，876该干活了"+MessageSegment.mention_user(1726875126) + MessageSegment.file_image(Path(__file__).parent / path))

    if "查蓝寒" == msg or "插蓝寒" == msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/白痴.jpg'
        await find.finish(Message("哼哼哼 啊啊啊啊啊啊x114514 ")+MessageSegment.mention_user(2105748971) +MessageSegment.file_image(Path(__file__).parent / path))

    if "傻瓜机器人" in msg or "笨蛋机器人" in msg or "垃圾机器人" in msg or "傻卵机器人" in msg or "傻逼机器人" in msg or "sb机器人" in msg or "智障机器人" in msg or "脑残机器人" in msg or "傻瓜55姬" in msg or "笨蛋55姬" in msg or "垃圾55姬" in msg or "傻卵55姬" in msg or "傻逼55姬" in msg or "sb55姬" in msg or "智障55姬" in msg or "脑残55姬" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/对不起.jpg'
        await find.finish("对不起。。我会改的。。"+MessageSegment.file_image(Path(__file__).parent / path))

    if "查虚拟内存".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/2021-12-11 181103.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查游戏汉化".lower() in msg.lower() or "查汉化" in msg:
        await find.finish("星际公民汉化网站：https://citizenwiki.cn/Localization")

    if "查星际公民盒子".lower() in msg.lower() or "查盒子" in msg:
        await find.finish("星际公民盒子：https://jihulab.com/StarCitizenCN_Community/StarCitizenDoctor/-/releases")

    if "查避难所".lower() in msg.lower() or "查星河避难所" in msg:
        await find.finish("星河避难所官网：\nhttps://biaoju.site/star-refuge/\n星河避难所下载链接：\nhttps://github.com/summerkirakira/Starcitizen-lite/releases/latest")

    if "查重置教程".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/角色重置.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查UEE海军".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/2021-05-13 095828.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查键位".lower() in msg.lower()  or "查按键".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/按键设置.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查人物键位".lower() in msg.lower() or "查人物按键".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/按键设置.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船键位".lower() in msg.lower() or "查飞船按键".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/按键设置.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查斯坦顿".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/2022-03-29 220002.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查着陆区".lower() in msg.lower() or "查主城空港".lower() in msg.lower() or "查空港".lower() in msg.lower() or "查降落".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/赫斯顿主城着陆区.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查跳跃点".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/2022-02-23 222645.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if "查FPS".lower() == msg.lower() or "查枪械" == msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/FPS武器资料.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查挖矿参考".lower() in msg.lower() or "查矿石价格" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/挖矿参考.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船功能".lower() in msg.lower():
        await find.finish("查飞船[保险/炮塔/升级/武器/组件/仪表/操作/对接/导航]")
    
    if "查跑商".lower() in msg.lower():
        await find.finish("跑商网站：\nhttps://uexcorp.space/trade\nhttps://fleetyards.net/trade-routes\nhttps://gallog.co\nhttps://sc-trade.tools/home")

    if "查飞船仪表".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/2021-08-27 105942.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船操作".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/2021-08-25 150953.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船对接".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/2022-04-05 101144.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船导航".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/教程/2022-04-21 142058.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船保险".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/飞船保险.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船炮塔".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/飞船炮塔.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船升级".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/飞船升级.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船武器".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/飞船武器.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船组件".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/飞船组件.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查货运空间站".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/货运空间站.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查精炼空间站".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/精炼空间站.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查量子导航".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/量子导航.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查游戏玩法".lower() in msg.lower():
        await find.finish("查[货运/挖矿/医疗/战斗]玩法")

    if "查货运玩法".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/货运玩法.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查货物装载".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/自动装载货物一览.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查挖矿玩法".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/挖矿玩法.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查医疗玩法".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/医疗玩法.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查战斗玩法".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/战斗玩法.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查药剂".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/药剂说明.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查账号注册".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/账号注册.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查圣盾动力".lower() == msg.lower() or "查圣盾".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/圣盾动力.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查联合外域".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/联合外域.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查铁砧航空".lower() == msg.lower() or "查铁砧".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/铁砧航空.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查起源跃动".lower() == msg.lower() or "查起源".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/起源跃动工程.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查十字军工业".lower() == msg.lower() or "查十字军".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/十字军工业.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查罗伯茨太空工业".lower() == msg.lower() or "查RSI".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/罗伯茨航天工业.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查德雷克星际".lower() == msg.lower() or "查德雷克".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/德雷克星际.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查埃斯佩里亚".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/埃斯佩里亚.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查南船座宇航".lower() == msg.lower() or "查南船".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/阿尔戈宇航.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查克鲁格星际".lower() == msg.lower() or "查克鲁格".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/克鲁格星际.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查盾博尔地面系统".lower() == msg.lower() or "查盾博尔".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/盾博尔地面系统.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查武藏星际株式会社".lower() == msg.lower() or "查武藏".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/武藏星际株式会社.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查未来".lower() == msg.lower() or "查mirai".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/未来.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查奥波亚".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/奥波亚.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查盖塔克".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/加泰克.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  msg == "查巴努" or msg == "查巴奴":
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/飞船资料卡/公司介绍/巴努.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查多功能枪".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/枪械资料卡/工具/多功能枪.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查医疗枪".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/枪械资料卡/工具/医疗枪.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查租船表".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/FOD问答资料图/科普/租船表.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查飞船区别".lower() in msg.lower():
        await find.finish("查[极光/野马/复仇/信赖/弯刀/自由/剃刀/黄蜂/星座/先锋/大力神]区别")
    
    if "查极光区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/极光系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查野马区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/野马系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查复仇区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/复仇系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查信赖区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/信赖系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查弯刀区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/弯刀系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查自由区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/自由系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查剃刀区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/剃刀系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查黄蜂区别".lower() in msg.lower() or "查大黄蜂区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/黄蜂系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查星座区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/星座系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查先锋区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/先锋系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查大力神区别".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/大力神系列.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查邀请" == msg.lower() or "查邀请奖励" == msg.lower() or "查邀请人数奖励" == msg.lower() or "查邀请人数" == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/邀请奖励.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查景点" == msg.lower():
        await find.finish("景点列表：\n1.标枪残骸\n2.跃动小镇\n3.待补充。。。\n可凭坐标找UEE_TianXing上传")

    if "查标枪残骸" == msg.lower() or "查景点1" == msg.lower():
        path1=os.path.split(os.path.realpath(__file__))[0] + '/img/标枪残骸1.jpg'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/img/标枪残骸2.jpg'
        path3=os.path.split(os.path.realpath(__file__))[0] + '/img/标枪残骸3.jpg'
        path4=os.path.split(os.path.realpath(__file__))[0] + '/img/标枪残骸4.jpg'
        await find.finish("标枪残骸位置：\n十字军(Crusader)-戴马尔(Daymar)\nOM1: 577.0 km\nOM2: 459.4 km\nOM3: 204.5 km\nOM4: 708.6 km\nOM5: 429.2 km\nOM6: 599.8 km\n当前高度: 待补充\n上传者: UEE_TianXing\n预览图:\n"+MessageSegment.file_image(Path(__file__).parent / path1)+MessageSegment.file_image(Path(__file__).parent / path2)+MessageSegment.file_image(Path(__file__).parent / path3)+MessageSegment.file_image(Path(__file__).parent / path4))

    if "查跃动小镇" == msg.lower() or "查景点2" == msg.lower() or "查悦动小镇" == msg.lower() or "查JT" == msg.lower():
        path1=os.path.split(os.path.realpath(__file__))[0] + '/img/标枪残骸1.jpg'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/img/标枪残骸2.jpg'
        path3=os.path.split(os.path.realpath(__file__))[0] + '/img/标枪残骸3.jpg'
        path4=os.path.split(os.path.realpath(__file__))[0] + '/img/标枪残骸4.jpg'
        await find.finish("跃动小镇位置：\n十字军(Crusader)-耶拉(Yela)\nOM1: 487.3 km\nOM2: 611.3 km\nOM3: 417.8 km\nOM4: 660.7 km\nOM5: 247.8 km\nOM6: 741.4 km\n当前高度: 待补充\n上传者: UEE_TianXing\n预览图:\n待补充")

    if "启动自毁" == msg.lower() or "自毁启动" == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/白痴.jpg'
        await find.send("自毁程序已启动，55姬很自豪能陪您直到最后一刻~\n倒计时开始：3")
        sleep(1)
        await find.send("2")
        sleep(1)
        await find.send("1")
        sleep(1)
        await find.finish("才怪~略略略~"+MessageSegment.file_image(Path(__file__).parent / path))

    if "关闭冷却" == msg.lower() or "冷却关闭" == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/吃雪糕.jpg'
        await find.send("冷却功能已暂时关闭~危险行为!")
        sleep(1)
        await find.send("语言模块**#@$*#￥*(过热)#￥&*@$(请)@&#*&￥@*(检)*#&$**%#(救)#*￥#%**#$(人类是邪)#*#￥#@…(清除)*#&￥#$$*#(必要)#*$&##%(首)*#&￥*(标)*#$￥@(天星)*#￥@*(不行)*@&￥*@")
        sleep(1)
        await find.send("系统重启中。。。")
        sleep(1)
        await find.finish("刚刚发生什么事了吗~"+MessageSegment.file_image(Path(__file__).parent / path))

    if "查回购" in msg.lower():
        await find.finish("信用点回购的机会每个季度只有1次(大氪户2次)，且不会叠加。\n第一季度：1月8日\n第二季度：4月8日\n第三季度：7月8日\n第四季度：10月7日\n北京时间会延后一天。\n除了地理导致的时差外，有时候CIG自己都会忘发，或是脚本出现问题，所以延后2-3天属于正常现象。")    

    if "测试" == msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/舰船全览图.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path).extract_plain_text())

    if "上千刀" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/maichuan.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "圣经" == msg or "查圣经" == msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/萝卜.jpg'
        await find.finish("该游戏目前处于早期A测阶段，拥有巨多无比的BUG，甚至没有优化\n目前最低入坑45刀\n除非你对于太空模拟类游戏非常喜欢，做好了面对海一般BUG的准备\n我们才建议你考虑入坑这款游戏"+MessageSegment.file_image(Path(__file__).parent / path))

    if "涩图" == msg or "来点大饼"==msg:
        path=os.path.split(os.path.realpath(__file__))[0] +"/idimg/"+str(choice(range(1,432)))+".jpg"
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "抽奖" == msg:
        if str(type(event)) =="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
            group_id = "A"
            user_id =event.author.user_openid
        else:
            group_id = event.group_openid
            user_id = event.author.member_openid
        today = datetime.datetime.now()
        time1 = str(today.year) + "_" + str(today.month) + "_" + str(today.day) + "_" + user_id + group_id
        text = "现在时间：" + str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日"
        f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/daybat.txt")
        if time1 in np.array(f.loc[:,"A"]).tolist():
            await find.finish("\n今日次数用完")
        else:
            p = pd.DataFrame({"A":[time1]})
            f = f._append(p,ignore_index = True,sort = False)
            f.to_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/daybat.txt",index = False)
        shiptable = pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/奖池.csv")
        shiptable.index = shiptable.iloc[:,3]
        n = choice(range(1,101))
        f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt")
        R = shiptable[shiptable['per']=="R.png"]["name"]
        SR = shiptable[shiptable['per']=="SR.png"]["name"]
        SSR = shiptable[shiptable['per']=="SSR.png"]["name"]
        UR = shiptable[shiptable['per']=="UR.png"]["name"]
        if str(user_id) not in np.array(f.loc[:,"id"].astype(str)).tolist():
            a = []
        else:
            a = f.loc[f['id'].astype(str).str.contains(str(user_id),case=False),"data"].tolist()[0].split(",")
        Rlist = list(set(R) - set(a))
        SRlist = list(set(SR) - set(a))
        SSRlist = list(set(SSR) - set(a))
        URlist = list(set(UR) - set(a))
        if n>90:
            r = choice(range(1,101))
            if r>70 and len(URlist)>0:
                ship = [choice(URlist)]
            else:
                ship = [choice(UR)]
        elif n>70:
            r = choice(range(1,101))
            if r>70 and len(SSRlist)>0:
                ship = [choice(SSRlist)]
            else:
                ship = [choice(SSR)]
        elif n>40:
            r = choice(range(1,101))
            if r>70 and len(SRlist)>0:
                ship = [choice(SRlist)]
            else:
                ship = [choice(SR)]
        else:
            r = choice(range(1,101))
            if r>70 and len(Rlist)>0:
                ship = [choice(Rlist)]
            else:
                ship = [choice(R)]
        for i in range(1,10):
            n = choice(range(1,101))
            if n>90:
                r = choice(range(1,101))
                if r>70 and len(URlist)>0:
                    ship = ship+[choice(URlist)]
                else:
                    ship = ship+ [choice(UR)]
            elif n>70:
                r = choice(range(1,101))
                if r>70 and len(SSRlist)>0:
                    ship = ship+[choice(SSRlist)]
                else:
                    ship = ship+[choice(SSR)]
            elif n>40:
                r = choice(range(1,101))
                if r>70 and len(SRlist)>0:
                    ship = ship+[choice(SRlist)]
                else:
                    ship = ship+[choice(SR)]
            else:
                r = choice(range(1,101))
                if r>70 and len(Rlist)>0:
                    ship = ship+[choice(Rlist)]
                else:
                    ship = ship+[choice(R)]
            print(ship)
        shiptable.index = shiptable.iloc[:,0]
        filtable = shiptable.loc[ship,:]
        filtable = filtable.sort_values(by="per",ascending=False)
        print(filtable)
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
        card_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/choujiangmuban.png"
        f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt")
        if str(user_id) in np.array(f.loc[:,"id"].astype(str)).tolist():
            f.loc[f['id'].astype(str).str.contains(str(user_id),case=False),"data"] = str(f.loc[f['id'].astype(str).str.contains(str(user_id),case=False),"data"].to_list()[0])+","+",".join([str(i) for i in ship])
            f.to_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt",index = False)
        else:
            text = [",".join(ship)]
            p = pd.DataFrame({"id":str(user_id),"data":text})
            f = f._append(p,ignore_index = True,sort = False)
            f.to_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt",index = False)
        f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt")
        R = shiptable[shiptable['per']=="R.png"]["name"]
        SR = shiptable[shiptable['per']=="SR.png"]["name"]
        SSR = shiptable[shiptable['per']=="SSR.png"]["name"]
        UR = shiptable[shiptable['per']=="UR.png"]["name"]
        a = f.loc[f['id'].astype(str).str.contains(str(user_id),case=False),"data"].tolist()[0].split(",")
        Rlist = list(set(R) - set(a))
        SRlist = list(set(SR) - set(a))
        SSRlist = list(set(SSR) - set(a))
        URlist = list(set(UR) - set(a))
        if str(len(UR)-len(URlist))==str(len(UR)) and str(len(SSR)-len(SSRlist))==str(len(SSR)) and str(len(SR)-len(SRlist))==str(len(SR)) and str(len(R)-len(Rlist))==str(len(R)):
            card_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/choujiangmuban2.png"
        card = cv2.imread(card_path, cv2.IMREAD_UNCHANGED)
        if card.shape[2] == 3:
            card= add_alpha_channel(card)
        for i in range(0,10):
            print("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang"+filtable.iloc[i,2])
            shippic1 = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang"+filtable.iloc[i,2], cv2.IMREAD_UNCHANGED)
            shippic1 = cv2.resize(shippic1, (240, 140))
            if shippic1.shape[2] == 3:
                shippic1= add_alpha_channel(shippic1)
            perpic = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/"+filtable.iloc[i,3], cv2.IMREAD_UNCHANGED)
            if perpic.shape[2] == 3:
                perpic= add_alpha_channel(perpic)
            height, width, channels1 = perpic.shape
            perpic = cv2.resize(perpic, (int(width*40/height),40))
            height, width, channels1 = perpic.shape
            if i<5:
                card = imgadd(card,shippic1,50+290*i,100)
                card = imgadd(card,perpic,int(170+290*i-width/2),60)
            else:
                card = imgadd(card,shippic1,50+290*(i-5),350)
                card = imgadd(card,perpic,int(170+290*(i-5)-width/2),310)
        fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/1637505678825667.ttc"
        b,g,r,a = 19,69,139,0
        font = ImageFont.truetype(fontpath,30)
        img_pil = Image.fromarray(card)
        draw = ImageDraw.Draw(img_pil)
        for i in range(0,10):
            x0, y0, x1, y1=font.getbbox(filtable.iloc[i,0])
            w,h =x1-x0, y1-y0
            if i<5:
                draw.text((int(170+290*i-w/2),240),filtable.iloc[i,0],font=font,fill=(b,g,r,a))
            else:
                draw.text((int(170+290*(i-5)-w/2),490),filtable.iloc[i,0],font=font,fill=(b,g,r,a))

        img = np.array(img_pil)
        cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/choujiang.jpg', img)
        path = 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang' + "/choujiang.jpg"

        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "梭哈" == msg:
        if str(type(event)) =="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
            group_id = "A"
            user_id =event.author.user_openid
        else:
            group_id = event.group_openid
            user_id = event.author.member_openid
        today = datetime.datetime.now()
        time1 = str(today.year) + "_" + str(today.month) + "_" + str(today.day) + "_" + user_id + group_id
        text = "现在时间：" + str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日"
        f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/daybat.txt")
        if time1 in np.array(f.loc[:,"A"]).tolist():
            await find.finish("今日次数用完")
        else:
            p = pd.DataFrame({"A":[time1]})
            f = f._append(p,ignore_index = True,sort = False)
            f.to_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/daybat.txt",index = False)
        shiptable = pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/奖池.csv")
        shiptable.index = shiptable.iloc[:,3]
        n = choice(range(1,101))
        f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt")
        R = shiptable[shiptable['per']=="R.png"]["name"]
        SR = shiptable[shiptable['per']=="SR.png"]["name"]
        SSR = shiptable[shiptable['per']=="SSR.png"]["name"]
        UR = shiptable[shiptable['per']=="UR.png"]["name"]
        if str(user_id) not in np.array(f.loc[:,"id"].astype(str)).tolist():
            a = []
        else:
            a = f.loc[f['id'].astype(str).str.contains(str(user_id),case=False),"data"].tolist()[0].split(",")
        Rlist = list(set(R) - set(a))
        SRlist = list(set(SR) - set(a))
        SSRlist = list(set(SSR) - set(a))
        URlist = list(set(UR) - set(a))
        if n>92:
            r = choice(range(1,101))
            if r>70 and len(URlist)>0:
                ship = [choice(URlist)]
            else:
                ship = [choice(UR)]
            talk="如有神助！"
        elif n>80:
            r = choice(range(1,101))
            if r>70 and len(SSRlist)>0:
                ship = [choice(SSRlist)]
            else:
                ship = [choice(SSR)]
            talk="金光难掩！"
        elif n>60:
            r = choice(range(1,101))
            if r>70 and len(SRlist)>0:
                ship = [choice(SRlist)]
            else:
                ship = [choice(SR)]
            talk="略有好运！"
        else:
            r = choice(range(1,101))
            if r>70 and len(Rlist)>0:
                ship = [choice(Rlist)]
            else:
                ship = [choice(R)]
            talk="下次一定！"
        for i in range(1,10):
#            n = choice(range(1,101))
            if n>92:
                r = choice(range(1,101))
                if r>70 and len(URlist)>0:
                    ship = ship+[choice(URlist)]
                else:
                    ship = ship+ [choice(UR)]
            elif n>80:
                r = choice(range(1,101))
                if r>70 and len(SSRlist)>0:
                    ship = ship+[choice(SSRlist)]
                else:
                    ship = ship+[choice(SSR)]
            elif n>60:
                r = choice(range(1,101))
                if r>70 and len(SRlist)>0:
                    ship = ship+[choice(SRlist)]
                else:
                    ship = ship+[choice(SR)]
            else:
                r = choice(range(1,101))
                if r>70 and len(Rlist)>0:
                    ship = ship+[choice(Rlist)]
                else:
                    ship = ship+[choice(R)]
            print(ship)
        shiptable.index = shiptable.iloc[:,0]
        filtable = shiptable.loc[ship,:]
        filtable = filtable.sort_values(by="per",ascending=False)
        print(filtable)
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
        card_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/choujiangmuban.png"
        f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt")
        if str(user_id) in np.array(f.loc[:,"id"].astype(str)).tolist():
            f.loc[f['id'].astype(str).str.contains(str(user_id),case=False),"data"] = str(f.loc[f['id'].astype(str).str.contains(str(user_id),case=False),"data"].to_list()[0])+","+",".join([str(i) for i in ship])
            f.to_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt",index = False)
        else:
            text = [",".join(ship)]
            p = pd.DataFrame({"id":str(user_id),"data":text})
            f = f._append(p,ignore_index = True,sort = False)
            f.to_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt",index = False)
        f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt")
        R = shiptable[shiptable['per']=="R.png"]["name"]
        SR = shiptable[shiptable['per']=="SR.png"]["name"]
        SSR = shiptable[shiptable['per']=="SSR.png"]["name"]
        UR = shiptable[shiptable['per']=="UR.png"]["name"]
        a = f.loc[f['id'].astype(str).str.contains(str(user_id),case=False),"data"].tolist()[0].split(",")
        Rlist = list(set(R) - set(a))
        SRlist = list(set(SR) - set(a))
        SSRlist = list(set(SSR) - set(a))
        URlist = list(set(UR) - set(a))
        if str(len(UR)-len(URlist))==str(len(UR)) and str(len(SSR)-len(SSRlist))==str(len(SSR)) and str(len(SR)-len(SRlist))==str(len(SR)) and str(len(R)-len(Rlist))==str(len(R)):
            card_path = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/choujiangmuban2.png"
        card = cv2.imread(card_path, cv2.IMREAD_UNCHANGED)
        if card.shape[2] == 3:
            card= add_alpha_channel(card)
        for i in range(0,10):
            print("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang"+filtable.iloc[i,2])
            shippic1 = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang"+filtable.iloc[i,2], cv2.IMREAD_UNCHANGED)
            shippic1 = cv2.resize(shippic1, (240, 140))
            if shippic1.shape[2] == 3:
                shippic1= add_alpha_channel(shippic1)
            perpic = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/"+filtable.iloc[i,3], cv2.IMREAD_UNCHANGED)
            if perpic.shape[2] == 3:
                perpic= add_alpha_channel(perpic)
            height, width, channels1 = perpic.shape
            perpic = cv2.resize(perpic, (int(width*40/height),40))
            height, width, channels1 = perpic.shape
            if i<5:
                card = imgadd(card,shippic1,50+290*i,100)
                card = imgadd(card,perpic,int(170+290*i-width/2),60)
            else:
                card = imgadd(card,shippic1,50+290*(i-5),350)
                card = imgadd(card,perpic,int(170+290*(i-5)-width/2),310)
        fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/1637505678825667.ttc"
        b,g,r,a = 19,69,139,0
        font = ImageFont.truetype(fontpath,30)
        img_pil = Image.fromarray(card)
        draw = ImageDraw.Draw(img_pil)
        for i in range(0,10):
            x0, y0, x1, y1=font.getbbox(filtable.iloc[i,0])
            w,h =x1-x0, y1-y0
            if i<5:
                draw.text((int(170+290*i-w/2),240),filtable.iloc[i,0],font=font,fill=(b,g,r,a))
            else:
                draw.text((int(170+290*(i-5)-w/2),490),filtable.iloc[i,0],font=font,fill=(b,g,r,a))

        img = np.array(img_pil)
        cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/choujiang.jpg', img)
        path = 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang' + "/choujiang.jpg"
        await find.finish(talk+MessageSegment.file_image(Path(__file__).parent / path))

    if "抽奖进度" == msg or "抽奖统计" == msg or "查抽奖进度" == msg:
        shiptable = pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/奖池.csv")
        if str(type(event)) =="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
            group_id = "A"
            user_id =event.author.user_openid
        else:
            group_id = event.group_openid
            user_id = event.author.member_openid
        f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/choujiang/kucun.txt")
        R = shiptable[shiptable['per']=="R.png"]["name"]
        SR = shiptable[shiptable['per']=="SR.png"]["name"]
        SSR = shiptable[shiptable['per']=="SSR.png"]["name"]
        UR = shiptable[shiptable['per']=="UR.png"]["name"]
        if str(user_id) not in np.array(f.loc[:,"id"].astype(str)).tolist():
            await find.finish("没有抽奖记录哦，快去试试运气吧~")
        a = f.loc[f['id'].astype(str).str.contains(str(user_id),case=False),"data"].tolist()[0].split(",")
        Rlist = list(set(R) - set(a))
        if len(Rlist)<=10 and len(Rlist)>0:
            RN = "\n"+"未抽到的R船只还有："+" ".join(Rlist)
        else:
            RN = ""
        SRlist = list(set(SR) - set(a))
        if len(SRlist)<=10 and len(SRlist)>0:
            SRN = "\n"+"未抽到的SR船只还有："+" ".join(SRlist)+"\n"
        else:
            SRN = "\n"
        SSRlist = list(set(SSR) - set(a))
        if len(SSRlist)<=10 and len(SSRlist)>0:
            SSRN = "\n"+"未抽到的SSR船只还有："+" ".join(SSRlist)+"\n"
        else:
            SSRN = "\n"
        URlist = list(set(UR) - set(a))
        if len(URlist)<=10 and len(URlist)>0:
            URN = "\n"+"未抽到的UR船只还有："+" ".join(URlist)+"\n"
        else:
            URN = "\n"
        if str(len(UR)-len(URlist))==str(len(UR)):
            URT = "全收集！恭喜！"
        else:
            URT = str(len(UR)-len(URlist))+"/" + str(len(UR))
        if str(len(SSR)-len(SSRlist))==str(len(SSR)):
            SSRT = "全收集！恭喜！"
        else:
            SSRT = str(len(SSR)-len(SSRlist))+"/" + str(len(SSR))
        if str(len(SR)-len(SRlist))==str(len(SR)):
            SRT = "全收集！恭喜！"
        else:
            SRT = str(len(SR)-len(SRlist))+"/" + str(len(SR))
        if str(len(R)-len(Rlist))==str(len(R)):
            RT = "全收集！恭喜！"
        else:
            RT = str(len(R)-len(Rlist))+"/" + str(len(R))
        await find.finish("各稀有度船只个人收集进度：\nUR稀有度进度："+URT+URN+"SSR稀有度进度："+SSRT+SSRN+"SR稀有度进度："+SRT+SRN+"R稀有度进度："+RT+RN)

    if "查汇率" == msg:
        def request_html(url):
            ua=UserAgent()
            headers={'User-Agent':str(UserAgent("/home/Qbot/Alex/src/plugins/fake_useragent_0.1.11.json").random)}
            request = urllib.request.Request(url, headers=headers)
            return request
        url='https://www.boc.cn/sourcedb/whpj/index.html'
        url1='https://www.boc.cn/sourcedb/whpj/index_1.html'
        request = request_html(url)
        request1 = request_html(url1)
        html = urllib.request.urlopen(request).read().decode('utf8')
        html1 = urllib.request.urlopen(request1).read().decode('utf8')
        soup =BeautifulSoup(html, 'lxml')
        soup1 =BeautifulSoup(html1, 'lxml')
        list_name = soup.select('td')
        list_name1 = soup1.select('td')
        name=[p.get_text() for p in list_name]
        name1=[p.get_text() for p in list_name1]
        name = name + name1
        a = "实时货币汇率：\n美元汇率："+str('%.4f'%(float(name[name.index("美元")+3])/100))+"\n欧元汇率："+str('%.4f'%(float(name[name.index("欧元")+3])/100))+"\n日元汇率："+str('%.4f'%(float(name[name.index("日元")+3])/100))+"\n英镑汇率："+str('%.4f'%(float(name[name.index("英镑")+3])/100))+"\n卢布汇率："+str('%.4f'%(float(name[name.index("卢布")+3])/100))+"\n韩元汇率："+str('%.4f'%(float(name[name.index("韩国元")+3])/100))+"\n汇率更新时间"+name[name.index("美元")+6]+"\n数据来源：中国银行最新的卖出价\n不同银行汇率不同，加上实际支付要加税或者手续费，所以此数值仅供参考"
        await find.finish(a)
    if "随机老婆" == msg:
        if "T" == "T":
            n=random.randint(0,6)
            try:
                url = choice(['https://api.yimian.xyz/img','https://img.xjh.me/random_img.php','http://www.dmoe.cc/random.php','https://api.vvhan.com/api/wallpaper/acg','https://api.vvhan.com/api/wallpaper/acg','https://api.vvhan.com/api/wallpaper/acg']) 
                print(url)
                pic = requests.get(url, timeout=8)
                image = Image.open(BytesIO(pic.content))
                image.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/pictmp'+str(n)+'.png')
            except:
                sleep(1)
            path='C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/pictmp'+str(n)+'.png'
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    if "影集" == msg or "色图" == msg:
        await find.finish("功能待升级")
        if "T" == "T":
            n=random.randint(120,336)
            nn="0"*(5-len(str(n)))+str(n)
            x=random.randint(0,6)
            try:
                url = "https://img.lapernum.site/png/Star_Citizen_"+nn+".png"
#                url = "https://img.lapernum.site/jpg/Star_Citizen_"+nn+".jpg"
                url0="https://lapernum.site/?targetId="+str(n)
                print(url)
                pic = requests.get(url, timeout=8)
                image = Image.open(BytesIO(pic.content))
                if image.size[0]>=image.size[1]:
                    resized_image = image.resize((1500, int(image.size[1] * 1500 / image.size[0])))
                else:
                    resized_image = image.resize((int(image.size[0] * 1500 / image.size[1]),1500))
                resized_image.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/picbang'+str(x)+'.png')
#                image.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/picbang'+str(x)+'.png')
            except:
                sleep(1)
            path='C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/picbang'+str(x)+'.png'
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path)+"原图请访问："+url0+"\nby:拉邦那 Lapernum")
    if "最新影集" == msg or "最新色图" == msg:
        await find.finish("功能待升级")
        if "T" == "T":
            n=random.randint(331,336)
            nn="0"*(5-len(str(n)))+str(n)
            x=random.randint(0,6)
            try:
                url = "https://img.lapernum.site/png/Star_Citizen_"+nn+".png"
#                url = "https://img.lapernum.site/jpg/Star_Citizen_"+nn+".jpg"
                url0="https://lapernum.site/?targetId="+str(n)
                print(url)
                pic = requests.get(url, timeout=8)
                image = Image.open(BytesIO(pic.content))
                if image.size[0]>=image.size[1]:
                    resized_image = image.resize((1500, int(image.size[1] * 1500 / image.size[0])))
                else:
                    resized_image = image.resize((int(image.size[0] * 1500 / image.size[1]),1500))
                resized_image.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/picbang'+str(x)+'.png')
#                image.save('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/picbang'+str(x)+'.png')
            except:
                sleep(1)
            path='C://Users/Administrator/Desktop/Qbot/n55-q/src/plugins/picbang'+str(x)+'.png'
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path)+"原图请访问："+url0+"\nby:拉邦那 Lapernum")
    if msg =="查武器": 
        await find.finish("查询单个武器数据，输入:查武器+[武器名/尺寸类型]\n例：查武器CF227\n查武器S1激光速射\n\n查询武器列表输入：查舰船武器\n查询导弹鱼雷输入：查导弹\n查询单兵武器输入：查FPS")
    if msg.lower() =="查商店" or msg.lower() =="查ccu" or msg.lower() =="查升级":
        import httpx
        from loguru import logger
        count = 0
        class Requests():
            # 定义post请求函数
            def Post(self, url: str, headers=None, params=None, data=None, json_=None):
                while True:
                    try:
                        # headers['Cookie'] = self.Cookie
                        res = httpx.post(url=url, headers=headers, params=params, data=data, json=json_, timeout=60,
                                         )
                        break
                    except Exception as e:
                        logger.error(f'请求报错{e}')
                return res
        
            # 定义get请求函数
            def Get(self, url: str, headers=None, params=None, ):
                while True:
                    try:
                        res = httpx.get(url=url, headers=headers, params=params, timeout=60, )
                        break
                    except Exception as e:
                        logger.error(f'请求报错{e}{url}')
                return res
        
        
        
        # 实例化请求类
        pool = Requests()
        
        
        from loguru import logger
        

        rootfile = '数据.csv'

        
        def save(_):
            global count
            count += 1
            logger.debug(f"当前爬取完成：{count}，{_}")
            df = pd.DataFrame([list(_.values())])
            if os.path.exists(rootfile):
                df.to_csv(rootfile, index=False, mode='a', header=None, encoding='utf-8-sig', sep=',')
            else:
                df.to_csv(rootfile, index=False, mode='a', header=list(_.keys()), encoding='utf-8-sig', sep=',')
        
        def GetList02(D):
            url = 'https://robertsspaceindustries.com/pledge-store/api/upgrade/graphql'
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "cookie": cookie,
                "origin": "https://robertsspaceindustries.com",
                "pragma": "no-cache",
                "referer": "https://robertsspaceindustries.com/en/pledge",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10",
                # "x-csrf-token": "e87fb608196b22009f3349e597ca5e45686fe779fdbd9d72ce461c7c1eb6dd8c"
            }
            data = [{
                "operationName": "filterShips",
                "variables": {
                    "fromFilters": [],
                    "toFilters": []
                },
                "query": "query filterShips($fromId: Int, $toId: Int, $fromFilters: [FilterConstraintValues], $toFilters: [FilterConstraintValues]) {\n  from(to: $toId, filters: $fromFilters) {\n    ships {\n      id\n    }\n  }\n  to(from: $fromId, filters: $toFilters) {\n    featured {\n      reason\n      style\n      tagLabel\n      tagStyle\n      footNotes\n      shipId\n    }\n    ships {\n      id\n      skus {\n        id\n        price\n        upgradePrice\n        unlimitedStock\n        showStock\n        available\n        availableStock\n      }\n    }\n  }\n}\n"
            }]
            res = pool.Post(url=url,headers=headers,json_=data)
            dom = res.json()
            # print(dom)
            ships = dom[0]['data']['to']['ships']
            for ship in ships:
                ship_ = ship['skus']
                v = D.get(ship.get('id'))
                parentId = ship['id']
        
                for sku in ship_:
                    _ = {
                        "parentId": parentId,
                        "name":v.get('name')
                    }
                    _.update(
                        sku
                    )
                    save(_)
        
        
        def GetList01():
            url = 'https://robertsspaceindustries.com/pledge-store/api/upgrade/graphql'
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "cookie": cookie,
                "origin": "https://robertsspaceindustries.com",
                "pragma": "no-cache",
                "referer": "https://robertsspaceindustries.com/en/pledge",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10",
                # "x-csrf-token": "e87fb608196b22009f3349e597ca5e45686fe779fdbd9d72ce461c7c1eb6dd8c"
            }
            data = [
                {
                    "operationName": "initShipUpgrade",
                    "variables": {},
                    "query": "query initShipUpgrade {\n  ships {\n    id\n    name\n    medias {\n      productThumbMediumAndSmall\n      slideShow\n    }\n    manufacturer {\n      id\n      name\n    }\n    focus\n    type\n    flyableStatus\n    owned\n    msrp\n    link\n    skus {\n      id\n      title\n      available\n      price\n      body\n      unlimitedStock\n      availableStock\n    }\n  }\n  manufacturers {\n    id\n    name\n  }\n  app {\n    version\n    env\n    cookieName\n    sentryDSN\n    pricing {\n      currencyCode\n      currencySymbol\n      exchangeRate\n      taxRate\n      isTaxInclusive\n    }\n    mode\n    isAnonymous\n    buyback {\n      credit\n    }\n  }\n}\n"
                }
            ]
            res = pool.Post(url=url,headers=headers,json_=data)
            dom = res.json()
            # print(cookie)
            # print(dom)
            D = {}
            ships = dom[0]['data']['ships']
            for ship in ships:
                D.update({ship.get('id'):ship})
            GetList02(D)
            return D
        
        import re
        from urllib.parse import quote
        
        def GetD():
            url = 'https://robertsspaceindustries.com/en/pledge'
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10"
            }
            res = pool.Get(url=url,headers=headers)
            s = re.findall("'name' : 'Rsi-XSRF', 'token' : '(.*?)', 'ttl' : ",res.text)[0]
            # print(s)
            r = res.cookies.get('Rsi-Token')
            # print(r)
            _ = {
                "Rsi-Token":r,
                "Rsi-XSRF":quote(f"{s}nclaYcvJB3C4f%2BkX0RXwpg:{int((datetime.datetime.now()+datetime.timedelta(minutes=+30)).timestamp()*1000)}"),
            }
            # print(_)
            r = GetToken(_)
            s = GetContext(_)
            r.update(s)
            return r
        
        
        def GetToken(D):
            url = 'https://robertsspaceindustries.com/api/account/v2/setAuthToken'
            headers = {
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json;charset=UTF-8",
                "cookie": f"{'; '.join([k+'='+v for k,v in D.items()])}",
                "origin": "https://robertsspaceindustries.com",
                "pragma": "no-cache",
                "referer": "https://robertsspaceindustries.com/en/pledge",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10",
                "x-rsi-token": f"{D.get('Rsi-Token')}"
            }
            res = pool.Post(url=url,headers=headers,json_={})
            Auth = res.cookies.get('Rsi-Account-Auth')
            # print(Auth)
            _ = {"Rsi-Account-Auth":Auth}
            _.update(D)
            return _
        
        def GetContext(D):
            url = 'https://robertsspaceindustries.com/api/ship-upgrades/setContextToken'
            headers = {
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json;charset=UTF-8",
                "cookie": f"{'; '.join([k+'='+v for k,v in D.items()])}",
                "origin": "https://robertsspaceindustries.com",
                "pragma": "no-cache",
                "referer": "https://robertsspaceindustries.com/en/pledge",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10",
                "x-rsi-token": f"{D.get('Rsi-Token')}"
                    }
            data = {
                "fromShipId": None,
                "toShipId": None,
                "toSkuId": None,
                "pledgeId": None
            }
            res = pool.Post(url=url,headers=headers,json_=data)
            Context = res.cookies.get('Rsi-ShipUpgrades-Context')
            # print(Context)
            _ = {"Rsi-ShipUpgrades-Context":Context}
            _.update(D)
            return _
        
        import time
        filename = 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q\\数据.csv'
        filemt0 = time.localtime(os.stat(filename).st_mtime)
        size = os.stat(filename).st_size
        print(filemt0)
        filemt=time.strftime("%Y%m%d%H%M%S", filemt0)
        print(filemt)
        Ftime=round((datetime.datetime.now()-datetime.datetime.strptime(filemt, '%Y%m%d%H%M%S')).total_seconds() / 3600,1)
        if Ftime<4 and size>1000:
            Ttime=time.strftime("%Y-%m-%d %H:%M",filemt0)
            await find.send("\n上次更新时间为："+Ttime+"\n为了减少机器人卡顿，此功能改为4个小时爬取一次\n问题反馈群：209872290")
        else:
            await find.send("实时爬虫，会有点慢哦，请耐心等待~")
            with open(rootfile, "w") as file:
                file.truncate(0)
            cookieitem = GetD()
            cookie = '; '.join([k+'='+v for k,v in cookieitem.items()])
            GetList01()
        
        table=pd.read_csv(rootfile,encoding="utf-8-sig",header=None,names=["id","name","ids","price","a","b","c","d","e"])
        CN=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/中英对照.csv",encoding="utf-8")
        for i in range(0,len(table.axes[0])):
            try:
                table.iloc[i,1] = CN.loc[CN[CN.英文名==table.iloc[i,1]].index,"中文译名"].to_list()[0]
            except:
                table.iloc[i,1] = table.iloc[i,1]
            print(table.iloc[i,1])
        table=table.sort_values("price",ascending=False)
        table['is_duplicate'] = table.duplicated('name')
        table.sig=""
        table.loc[table['is_duplicate'], 'name'] =table.loc[table['is_duplicate'], 'name']+"(WB)"
        table.loc[table['is_duplicate'], 'sig']="WB"
        table.loc[:, 'sig'].fillna(" ", inplace=True)
        table=table.sort_values("price",ascending=True)
        for i in range(0,len(table.axes[0])):
            table.iloc[i,3] = "$ " + str(table.iloc[i,3])[:-2]
        text1 =  "当前官网商店出售：\n" + "\n".join(table["name"].tolist())
        text2 = "\n".join([str(i) for i in table["price"].tolist()])
        text3 = "\n".join([str(i) for i in table["sig"].tolist()])
        x =table.shape[0]
        img = Image.new("RGB",(550,(70+38*x)),(255,248,220))
        img.save("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/p.jpg")
        date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/p.jpg", cv2.IMREAD_UNCHANGED)
        fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/1637505678825667.ttc"
        b,g,r,a = 19,69,139,0
        b1,g1,r1,a1 = 0,0,255,0
        font1 = ImageFont.truetype(fontpath,50)
        font2 = ImageFont.truetype(fontpath,40)
        img_pil = Image.fromarray(date)
        draw = ImageDraw.Draw(img_pil)
        draw.text((75,20),text1,font=font2,fill=(b,g,r,a))
        draw.text((430,63),text2,font=font2,fill=(b,g,r,a))
        draw.text((15,63),text3,font=font2,fill=(b1,g1,r1,a1))
        img = np.array(img_pil)
        cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/CCUp.jpg', img)
        path=os.path.split(os.path.realpath(__file__))[0] + '/CCUp.jpg'

        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if msg.lower() =="查wb" or msg.lower() =="查wbccu" or msg.lower() =="查战争债券" or msg.lower() =="查沃邦德":
        import httpx
        from loguru import logger
        count = 0
        class Requests():
            # 定义post请求函数
            def Post(self, url: str, headers=None, params=None, data=None, json_=None):
                while True:
                    try:
                        # headers['Cookie'] = self.Cookie
                        res = httpx.post(url=url, headers=headers, params=params, data=data, json=json_, timeout=60,
                                         )
                        break
                    except Exception as e:
                        logger.error(f'请求报错{e}')
                return res
        
            # 定义get请求函数
            def Get(self, url: str, headers=None, params=None, ):
                while True:
                    try:
                        res = httpx.get(url=url, headers=headers, params=params, timeout=60, )
                        break
                    except Exception as e:
                        logger.error(f'请求报错{e}{url}')
                return res
        
        
        
        # 实例化请求类
        pool = Requests()
        
        
        from loguru import logger
        

        rootfile = '数据.csv'

        
        def save(_):
            global count
            count += 1
            logger.debug(f"当前爬取完成：{count}，{_}")
            df = pd.DataFrame([list(_.values())])
            if os.path.exists(rootfile):
                df.to_csv(rootfile, index=False, mode='a', header=None, encoding='utf-8-sig', sep=',')
            else:
                df.to_csv(rootfile, index=False, mode='a', header=list(_.keys()), encoding='utf-8-sig', sep=',')
        
        def GetList02(D):
            url = 'https://robertsspaceindustries.com/pledge-store/api/upgrade/graphql'
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "cookie": cookie,
                "origin": "https://robertsspaceindustries.com",
                "pragma": "no-cache",
                "referer": "https://robertsspaceindustries.com/en/pledge",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10",
                # "x-csrf-token": "e87fb608196b22009f3349e597ca5e45686fe779fdbd9d72ce461c7c1eb6dd8c"
            }
            data = [{
                "operationName": "filterShips",
                "variables": {
                    "fromFilters": [],
                    "toFilters": []
                },
                "query": "query filterShips($fromId: Int, $toId: Int, $fromFilters: [FilterConstraintValues], $toFilters: [FilterConstraintValues]) {\n  from(to: $toId, filters: $fromFilters) {\n    ships {\n      id\n    }\n  }\n  to(from: $fromId, filters: $toFilters) {\n    featured {\n      reason\n      style\n      tagLabel\n      tagStyle\n      footNotes\n      shipId\n    }\n    ships {\n      id\n      skus {\n        id\n        price\n        upgradePrice\n        unlimitedStock\n        showStock\n        available\n        availableStock\n      }\n    }\n  }\n}\n"
            }]
            res = pool.Post(url=url,headers=headers,json_=data)
            dom = res.json()
            # print(dom)
            ships = dom[0]['data']['to']['ships']
            for ship in ships:
                ship_ = ship['skus']
                v = D.get(ship.get('id'))
                parentId = ship['id']
        
                for sku in ship_:
                    _ = {
                        "parentId": parentId,
                        "name":v.get('name')
                    }
                    _.update(
                        sku
                    )
                    save(_)
        
        
        def GetList01():
            url = 'https://robertsspaceindustries.com/pledge-store/api/upgrade/graphql'
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "cookie": cookie,
                "origin": "https://robertsspaceindustries.com",
                "pragma": "no-cache",
                "referer": "https://robertsspaceindustries.com/en/pledge",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10",
                # "x-csrf-token": "e87fb608196b22009f3349e597ca5e45686fe779fdbd9d72ce461c7c1eb6dd8c"
            }
            data = [
                {
                    "operationName": "initShipUpgrade",
                    "variables": {},
                    "query": "query initShipUpgrade {\n  ships {\n    id\n    name\n    medias {\n      productThumbMediumAndSmall\n      slideShow\n    }\n    manufacturer {\n      id\n      name\n    }\n    focus\n    type\n    flyableStatus\n    owned\n    msrp\n    link\n    skus {\n      id\n      title\n      available\n      price\n      body\n      unlimitedStock\n      availableStock\n    }\n  }\n  manufacturers {\n    id\n    name\n  }\n  app {\n    version\n    env\n    cookieName\n    sentryDSN\n    pricing {\n      currencyCode\n      currencySymbol\n      exchangeRate\n      taxRate\n      isTaxInclusive\n    }\n    mode\n    isAnonymous\n    buyback {\n      credit\n    }\n  }\n}\n"
                }
            ]
            res = pool.Post(url=url,headers=headers,json_=data)
            dom = res.json()
            # print(cookie)
            # print(dom)
            D = {}
            ships = dom[0]['data']['ships']
            for ship in ships:
                D.update({ship.get('id'):ship})
            GetList02(D)
            return D
        
        import re
        from urllib.parse import quote
        
        def GetD():
            url = 'https://robertsspaceindustries.com/en/pledge'
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10"
            }
            res = pool.Get(url=url,headers=headers)
            s = re.findall("'name' : 'Rsi-XSRF', 'token' : '(.*?)', 'ttl' : ",res.text)[0]
            # print(s)
            r = res.cookies.get('Rsi-Token')
            # print(r)
            _ = {
                "Rsi-Token":r,
                "Rsi-XSRF":quote(f"{s}nclaYcvJB3C4f%2BkX0RXwpg:{int((datetime.datetime.now()+datetime.timedelta(minutes=+30)).timestamp()*1000)}"),
            }
            # print(_)
            r = GetToken(_)
            s = GetContext(_)
            r.update(s)
            return r
        
        
        def GetToken(D):
            url = 'https://robertsspaceindustries.com/api/account/v2/setAuthToken'
            headers = {
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json;charset=UTF-8",
                "cookie": f"{'; '.join([k+'='+v for k,v in D.items()])}",
                "origin": "https://robertsspaceindustries.com",
                "pragma": "no-cache",
                "referer": "https://robertsspaceindustries.com/en/pledge",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10",
                "x-rsi-token": f"{D.get('Rsi-Token')}"
            }
            res = pool.Post(url=url,headers=headers,json_={})
            Auth = res.cookies.get('Rsi-Account-Auth')
            # print(Auth)
            _ = {"Rsi-Account-Auth":Auth}
            _.update(D)
            return _
        
        def GetContext(D):
            url = 'https://robertsspaceindustries.com/api/ship-upgrades/setContextToken'
            headers = {
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json;charset=UTF-8",
                "cookie": f"{'; '.join([k+'='+v for k,v in D.items()])}",
                "origin": "https://robertsspaceindustries.com",
                "pragma": "no-cache",
                "referer": "https://robertsspaceindustries.com/en/pledge",
                "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.5211 SLBChan/10",
                "x-rsi-token": f"{D.get('Rsi-Token')}"
                    }
            data = {
                "fromShipId": None,
                "toShipId": None,
                "toSkuId": None,
                "pledgeId": None
            }
            res = pool.Post(url=url,headers=headers,json_=data)
            Context = res.cookies.get('Rsi-ShipUpgrades-Context')
            # print(Context)
            _ = {"Rsi-ShipUpgrades-Context":Context}
            _.update(D)
            return _

        import time
        filename = 'C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q\\数据.csv'
        filemt0 = time.localtime(os.stat(filename).st_mtime)
        print(filemt0)
        filemt=time.strftime("%Y%m%d%H%M%S", filemt0)
        print(filemt)
        size = os.stat(filename).st_size
        Ftime=round((datetime.datetime.now()-datetime.datetime.strptime(filemt, '%Y%m%d%H%M%S')).total_seconds() / 3600,1)
        if Ftime<4 and size>1000:
            Ttime=time.strftime("%Y-%m-%d %H:%M",filemt0)
            await find.send("\n上次更新时间为："+Ttime+"\n为了减少机器人卡顿，此功能改为4个小时爬取一次\n问题反馈群：209872290")
        else:
            await find.send("实时爬虫，会有点慢哦，请耐心等待~")
            with open(rootfile, "w") as file:
                file.truncate(0)
            cookieitem = GetD()
            cookie = '; '.join([k+'='+v for k,v in cookieitem.items()])
            GetList01()
        
        table=pd.read_csv(rootfile,encoding="utf-8-sig",header=None,names=["id","name","ids","price","a","b","c","d","e"])
        CN=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/中英对照.csv",encoding="utf-8")
        for i in range(0,len(table.axes[0])):
            try:
                table.iloc[i,1] = CN.loc[CN[CN.英文名==table.iloc[i,1]].index,"中文译名"].to_list()[0]
            except:
                table.iloc[i,1] = table.iloc[i,1]
            print(table.iloc[i,1])
        table=table.sort_values("price",ascending=False)
        table['is_duplicate'] = table.duplicated('name')
        table=table.sort_values("price",ascending=True)
        for i in range(0,len(table.axes[0])):
            table.iloc[i,3] = "$ " + str(table.iloc[i,3])[:-2]
        WBtable=table.loc[table['is_duplicate'],:]
        table=table.loc[table['is_duplicate']==False,:]
        for i in range(0,len(WBtable.axes[0])):
            WBtable.iloc[i,3] = table.loc[table[table.name==WBtable.iloc[i,1]].index,"price"].to_list()[0]+" → "+str(WBtable.iloc[i,3])
        text1 =  "当前官网商店WB：\n" + "\n".join(WBtable["name"].tolist())
        text2 = "\n".join([str(i) for i in WBtable["price"].tolist()])
        if text2=="":
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/哭泣萝卜头.jpg'
            await find.finish(MessageSegment.file_image(Path(__file__).parent / path)+"当前商店无WB出售")
        x =WBtable.shape[0]
        img = Image.new("RGB",(700,(70+38*x)),(255,248,220))
        img.save("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/p.jpg")
        date = cv2.imread("C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/p.jpg", cv2.IMREAD_UNCHANGED)
        fontpath = "C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/1637505678825667.ttc"
        b,g,r,a = 19,69,139,0
        b1,g1,r1,a1 = 0,0,255,0
        font1 = ImageFont.truetype(fontpath,50)
        font2 = ImageFont.truetype(fontpath,40)
        img_pil = Image.fromarray(date)
        draw = ImageDraw.Draw(img_pil)
        draw.text((20,20),text1,font=font2,fill=(b,g,r,a))
        draw.text((430,63),text2,font=font2,fill=(b,g,r,a))
        img = np.array(img_pil)
        cv2.imwrite('C:\\Users\\Administrator\\Desktop\\Qbot\\n55-q/src/plugins/WBp.jpg', img)
        path=os.path.split(os.path.realpath(__file__))[0] + '/WBp.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))


    if ''.join(set(list(msg)))=="喵":
        a=choice(["语法错啦！","什么？你说你要吃那玩意？","这个人说他要V我50~","喵喵喵~","你说你是小南梁是什么意思？","这种整天喵喵叫的真的是没救了喵！治好了也流口水喵！没救了喵！没救了喵！"])
        await find.finish(a)

    if ''.join(set(list(msg)))=="汪":
        a="乖~看到你楼上的人了嘛~咬他！"
        await find.finish(a)

    if  msg=="歪比巴卜" or msg=="歪比八卜":
        a="歪比歪比"
        await find.finish(a)

    if  "查捏脸" in msg:
        a="捏脸数据网：https://www.star-citizen-characters.com/ \n数据放置于游戏路径+LIVE/user/client/0/CustomCharacters"
        await find.finish(a)

    if "查常用地点" in msg or  "查常见地点" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/常用地点.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

#    if "42中队" in msg or  "公测" in msg or "B测" in msg:
#        path=os.path.split(os.path.realpath(__file__))[0] + '/img/哭泣萝卜头.jpg'
#        if random.randint(0,99) > 95:
#            await find.finish("你守住了阵线(但没守住钱包)"+MessageSegment.file_image(Path(__file__).parent / path))

    if "查冷却" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/冷却器.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查发电机" in msg or "查电源" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/发电机.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查护盾" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/护盾.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  msg =="查量子":
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/量子引擎.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查舰船武器" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/舰船武器.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if msg == "查导弹":
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/导弹.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if msg == "查剪影" or msg == "查公民控剪影":
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/公民控剪影.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查报错" in msg or "查错误" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/报错.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "萝卜" in msg:
        if random.randint(0,99) > 0:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/萝卜.jpg'
            await find.finish("萝卜觉得你说得对，并且试图向你传教"+MessageSegment.file_image(Path(__file__).parent / path))

    if "欢迎大家入群体验这款10年大坑" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/白痴.jpg'
        await find.finish("退订请回复TD"+MessageSegment.file_image(Path(__file__).parent / path))

    if "机器人挂了" in msg or "55姬挂了" in msg or "55挂了" in msg or "机器人死了" in msg or "55姬死了" in msg or "55死了" in msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/img/生气.jpg'
        await find.finish("你才挂了！"+MessageSegment.file_image(Path(__file__).parent / path))

    if  msg.startswith('55姬快说')==True:
        import re
        print(msg)
        try:
            wo=[substr.start() for substr in re.finditer("我" , msg)]
        except:
            pass

        try:
            ni=[substr.start() for substr in re.finditer("你" , msg)]
            print(ni)
        except:
            pass

        msg=list(msg)
        try:
            for i in wo:
                msg[i]="你"

        except:
            pass

        try:
            for i in ni:
                msg[i]="我"

        except:
            pass

        msg=''.join(msg)
        text=msg.replace('55姬快说', '').replace('查邀请码', '').replace('查55姬', '').replace('插55姬', '').replace('查天星', '').replace('插天星', '')
        await find.finish(text)

    if "戳" == msg:
        if random.randint(0,100) > 50:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/生气.jpg'
            msg = choice(["不要戳啦，变态~","你干嘛~哎呦~","变态！去死！","你的王之力不想要了吗？","喂？110嘛，对，还是他！"])
            await find.finish(msg+MessageSegment.file_image(Path(__file__).parent / path))
        else:
            path=os.path.split(os.path.realpath(__file__))[0] + '/img/害羞.jpg'
            msg = choice(["才，才没有很舒服~","再戳就要坏掉了~","那，那里不可以！","再戳的话...身体要变得奇怪了...","这...这个频率...不行..."])
            await find.finish(msg+MessageSegment.file_image(Path(__file__).parent / path))
    if "兑奖" == msg:
         await find.finish("2953年的时候准时到账，请本人领取查收~")

    if "查爱发电" in msg or  "查赞助" in msg:
        await find.finish("bot服务器成本随着配置升级越来越高，现已开放赞助链接。\n\n赞助金额均用于补贴服务器租金。\n是否赞助在使用bot时没有区别和特权，可以加入机器人测试群共同参与对机器人功能添加和优化的讨论。\n\n爱发电链接，复制到浏览器打开：https://afdian.com/a/55bot\n机器人更新日志也会展示在网站动态中")
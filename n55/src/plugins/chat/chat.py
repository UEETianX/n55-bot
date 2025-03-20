from nonebot import on_message, on_notice
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .config import Config
from time import time
import os
from nonebot.adapters.satori.event import MessageEvent
from nonebot.adapters.satori.message import MessageSegment
from nonebot.rule import to_me
import json
from collections import Counter
import random
from random import choice
#from .response_for_surper_user import *
#from .response_for_common_user import *
#from .response_for_all_time import *

__plugin_name__ = 'chat'
__plugin_usage__ = '用法： 日常聊天中响应关键词与戳一戳。'

img_path = os.path.split(os.path.realpath(__file__))[0] + '/img/'

# 发送图片时用到的函数, 返回发送图片所用的编码字符串
def send_img(img_name):
    global img_path
    return MessageSegment.image(img_path + img_name)

# 针对戳一戳
chat_notice = on_message(priority=1,rule=to_me())


@chat_notice.handle()
async def handle_first_receive(bot: Bot, event: MessageEvent, state: T_State):
    msg = str(event.get_message()).strip()
    try:
        user_id = event.user.id
        group_id = event.guild.id
    except:
        pass
    # 如果读取正常没有出错，因为有些notice格式不支持session
    else:
        # 如果这是一条群聊信息
        if "戳" == msg or "戳@55姬 (查菜单)获取使用方式" == msg:
            if group_id in Config.used_in_group:
                if user_id in Config.super_uid:
                    path=os.path.split(os.path.realpath(__file__))[0] + '/img/天星的.jpg'
                    msg = choice(["如果是你的话，想戳多少次都可以哦~"])
                    await chat_notice.finish(msg+MessageSegment.image(path))
                    # 如果不在响应cd
                elif user_id in Config.vk_uid:
                    path=os.path.split(os.path.realpath(__file__))[0] + '/img/vk.jpg'
                    msg = choice(["你们这些贪婪的杂鱼~真是自掘坟墓","剑光如我，斩尽牛杂","干点正事吧巴巴托斯","愿原力与你同在"])
                    await chat_notice.finish(msg+MessageSegment.image(path))
                elif user_id in Config.DF_uid:
                    path=os.path.split(os.path.realpath(__file__))[0] + '/img/DF.jpg'
                    msg = choice(["你好呀~今天炸船了嘛？","今年的生日愿望是，你的船上没有我~","卖保险啦~DF除外~"])
                    await chat_notice.finish(msg+MessageSegment.image(path))
                else:
                    if random.randint(0,100) > 50:
                        path=os.path.split(os.path.realpath(__file__))[0] + '/img/生气.jpg'
                        msg = choice(["不要戳啦，变态~","你干嘛~哎呦~","变态！去死！","你的王之力不想要了吗？","喂？110嘛，对，还是他！"])
                        await chat_notice.finish(msg+MessageSegment.image(path))
                    else:
                        path=os.path.split(os.path.realpath(__file__))[0] + '/img/害羞.jpg'
                        msg = choice(["才，才没有很舒服~","再戳就要坏掉了~","那，那里不可以！","再戳的话...身体要变得奇怪了...","这...这个频率...不行..."])
                        await chat_notice.finish(msg+MessageSegment.image(path))
            else:
                await chat_notice.finish("本群未开放此功能")
        if "兑奖" in msg:
             await chat_notice.finish("2953年的时候准时到账，请本人领取查收~")
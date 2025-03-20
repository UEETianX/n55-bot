from nonebot import on_command
#from nonebot.adapters.satori import Bot
from nonebot.adapters.satori.event import MessageEvent
from nonebot.adapters.satori.message import MessageSegment
from nonebot.adapters import Event,Bot
import os
from nonebot_plugin_saa import Text, Image, MessageFactory, AggregatedMessageFactory
from nonebot.params import CommandArg
from nonebot.adapters import Message
import json
import ast

matcher = on_command("test")

@matcher.handle()
async def _(bot:Bot,event:Event,args: Message = CommandArg()):
    if '<at id="3889368716" name="55姬"/>' in str(event.get_message()):
        return
    print("测试"+msg)
    await matcher.send("正常消息")
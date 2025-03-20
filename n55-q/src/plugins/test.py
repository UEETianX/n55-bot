from nonebot import on_command
#from nonebot.adapters.qq import Bot
from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot.adapters import Event,Bot
import os
from nonebot_plugin_saa import Text, Image, MessageFactory, AggregatedMessageFactory
from nonebot.params import CommandArg
from nonebot.adapters import Message
import json
import ast

matcher = on_command("test")

@matcher.handle()
async def handle_function(bot:Bot,event:Event,args: Message = CommandArg()):
    await matcher.finish("活着喵~")
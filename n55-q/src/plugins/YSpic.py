from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
import os
import random
from pathlib import Path

YS=on_message(priority=2)
@YS.handle()
async def _(bot:Bot,event:Event,state:T_State):
    msg = str(event.get_message()).strip().replace(" ","")
    if "语音测试" == msg:
        path=os.path.split(os.path.realpath(__file__))[0] + '/MP3/hello.silk.amr'
        await YS.finish(MessageSegment.file_audio(Path(__file__).parent / path))

    if "闲聊" == msg:
        n=random.randint(1,18)
        path=os.path.split(os.path.realpath(__file__))[0] + '/MP3/TK'+str(n)+'.silk.amr'
        await YS.finish(MessageSegment.file_audio(Path(__file__).parent / path))


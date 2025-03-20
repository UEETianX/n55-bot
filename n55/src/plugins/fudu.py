from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Message,Bot,Event
from nonebot.params import CommandArg
import time
import random
from time import sleep

fudu=on_command("复读",priority=1)
@fudu.handle()
async def handle_function(args: Message = CommandArg()):
    args = str(args).replace('.复读', '').replace('查复读', '')
    await fudu.send(args)
    sleep(1)
    await fudu.send(args)
    sleep(1)
    await fudu.send(args)
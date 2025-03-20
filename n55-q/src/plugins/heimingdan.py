from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message

if str(type(Event)) =="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
    group_id = "A"
    user_id =Event.author.user_openid
else:
    group_id = Event.group_openid
    user_id = Event.author.member_openid
if user_id in ["8DF09B6FD42E9537D466E6332145FDA5"]:
    hei=on_message(priority=1)
    @hei.handle()
    async def _(bot:Bot,event:Event,state:T_State):
        await hei.finish(user_id)


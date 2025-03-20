from nonebot.typing import T_State
from nonebot.adapters.satori.event import GuildMemberAddedEvent
from nonebot.adapters import Bot,Event,Message
from nonebot import on_notice
from nonebot.adapters.satori.message import MessageSegment
import os

welcom = on_notice()
@welcom.handle()
async def h_r(bot: Bot, event: GuildMemberAddedEvent, state: T_State):
    user_id = event.user.id
    path=os.path.split(os.path.realpath(__file__))[0] + '/img/DF.jpg'
    await welcom.finish(MessageSegment.at(user_id)+"  欢迎新公民！记得将名片改成游戏id哦~"+ MessageSegment.image(path=path))
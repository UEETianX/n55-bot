from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from nonebot.adapters.satori.message import MessageSegment
from nonebot.adapters.satori.event import MessageEvent
from nonebot.params import CommandArg
import pandas as pd
import string
import re
import time
import asyncio
import os
from time import sleep
from random import randint
from datetime import datetime

MED=on_command("请求救援",aliases={"呼叫救援"},priority=1)

@MED.handle()
async def handle_function(bot:Bot,event: Event,args: Message = CommandArg()):
    QQ = event.user.id
    QGROUP = event.guild.id
    args = args.extract_plain_text()
    now = time.time()
    ID=str(time.strftime("%Y%m%d%H%M%S", time.localtime(now)))
    if args=="":
        await MED.finish("呼叫救援使用方法：\n.呼叫救援 游戏ID,服务器,游戏位置,有无对船对步兵威胁,留言\n例：.呼叫救援 UEE_TianXing,亚服,微科星,有NPC步兵和防空炮台,带点水呗要渴死了")
    QQN = event.member.nick
    if str(QQN) == "None":
        QQN = event.user.name
    QGROUPN = event.channel.name
    print(args)
    arglist=re.split("[,，]",args)
    if len(arglist)!=5:
        await MED.finish("以逗号分隔\n需要的字段数量 ：5\n你提供的数量："+str(len(arglist)))
    df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\Qbot\\n55\\src\\plugins\\MED.csv',index_col=None,header=0)
    df.index=df.iloc[:,0]
    print(df)
    msg="呼叫救援！！！！\n"+ID+"\n"+QQN+"("+str(QQ)+")从群聊:"+QGROUPN+"发来医疗请求\n游戏ID："+arglist[0]+"\n服务器："+arglist[1]+"\n位置："+arglist[2]+"\n是否有船只/步兵威胁："+arglist[3]+"\n留言："+arglist[4]
    print(msg)
    try:
        df = pd.concat([df,pd.DataFrame([[ID, arglist[0],QQ,arglist[1],arglist[2],arglist[3],QGROUP,arglist[4],"N"]], columns=["ID","NAME","QQ","SER","LOC","DB","QGROUP","NOTE","GOOD"])])
    except:
        await MED.finish("格式不对哦~\n\n呼叫救援使用方法：\n.呼叫救援 游戏ID,服务器,游戏位置,有无对船对步兵威胁,留言\n例：.呼叫救援 UEE_TianXing,亚服,微科星,有NPC步兵和防空炮台,带点水呗要渴死了")
    df.to_csv('C:\\Users\\Administrator\\Desktop\\Qbot\\n55\\src\\plugins\\MED.csv',index = None)
    groups = [209872290,377563757]
    msg="呼叫救援！！！！\n"+ID+"\n"+QQN+"("+str(QQ)+")从群聊:"+QGROUPN+"发来医疗请求\n游戏ID："+arglist[0]+"\n服务器："+arglist[1]+"\n位置："+arglist[2]+"\n是否有船只/步兵威胁："+arglist[3]+"\n留言："+arglist[4]
    for group in groups:
        await bot.send_message(
            channel=str(group),
            message=msg
            )
        await asyncio.sleep(randint(2, 5))

reMED=on_command("救援",priority=1)

@reMED.handle()
async def handle_function(bot:Bot,event: Event,args: Message = CommandArg()):
    QQ2 = event.user.id
    QGROUP2 = event.guild.id
    args = args.extract_plain_text()
    df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\Qbot\\n55\\src\\plugins\\MED.csv',index_col=None,header=0)
    df.index=df.iloc[:,0]
    if args[:2]=="状态":
        ID=int(args.replace("状态",""))
        time=round((datetime.now()-datetime.strptime(str(ID), '%Y%m%d%H%M%S')).total_seconds() / 60,1)
        if df.loc[ID,"GOOD"]=="F":
            text="已被接取"
        if df.loc[ID,"GOOD"]=="D":
            text="救助已撤销"
        elif time>5:
            text="救援事件超时"
        elif df.loc[ID,"GOOD"]=="N":
            text="暂无人接取"
        await reMED.finish(text)
    QQ2N = event.member.nick
    if QGROUP2 not in["377563757","209872290","955342491"]:
        await reMED.finish("此群暂无权限")
    if args=="":
        await reMED.finish("救援方法：\n.救援 救援事件编号,游戏ID,留言\n例：.救援 20241117113511,UEE_TianXing,马上上线先来KOOK等我")

    if str(QQ2N) == "None":
        QQ2N = event.user.name
    QGROUP2N = event.channel.name
    print(args)
    arglist=re.split("[,，]",args)
    if len(arglist)!=3:
        await MED.finish("以逗号分隔\n需要的字段数量 ：3\n你提供的数量："+str(len(arglist)))
    ID=int(arglist[0])
    time=round((datetime.now()-datetime.strptime(str(ID), '%Y%m%d%H%M%S')).total_seconds() / 60,1)
    if time>5:
        await reMED.finish("救援事件超时，已超过5分钟")
    print(df.index)
    if df.loc[ID,"GOOD"]!="N":
        await reMED.finish("接取失败，救援事件已被接取")
    NAME2=arglist[1]
    if QGROUP2 in["377563757","209872290"]:
        KOOK="KOOK：60893671，频道：医疗值班室"
    NOTE2=arglist[2]
    df.loc[ID,"QQ2"]=QQ2
    df.loc[ID,"QGROUP2"]=QGROUP2
    df.loc[ID,"NAME2"]=NAME2
    df.loc[ID,"NOTE2"]=NOTE2
    df.loc[ID,"GOOD"]="F"
    df.to_csv('C:\\Users\\Administrator\\Desktop\\Qbot\\n55\\src\\plugins\\MED.csv',index = None)
    msg = QGROUP2N+"的"+QQ2N+"正在前往救援！\n医疗人员ID："+NAME2+"\n"+KOOK+"\n留言："+NOTE2+"\n"
    await bot.send_message(
        channel=str(df.loc[ID,"QGROUP"]),
        message=msg+MessageSegment.at(df.loc[ID,"QQ"])
        )
    await reMED.finish("接取成功")

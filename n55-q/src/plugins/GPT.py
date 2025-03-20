from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from nonebot.params import CommandArg
import os
import openai
import asyncio
from openai import AsyncOpenAI
import string
import datetime
import pandas as pd
import numpy as np


GPT=on_command("GPT",aliases={"gpt","ds","DS"},priority=1)

@GPT.handle()
async def handle_function(event:Event,args: Message = CommandArg()):
#    user_id = event.get_user_id()
    args = args.extract_plain_text()
#    user_nick = event.member.nick
#    if str(user_nick) == "None":
#        user_nick = event.user.name
#    group_name = event.channel.name
#    punctuation_string = string.punctuation
#    for i in punctuation_string:
#        args = args.replace(i, '')
#    if args.replace(i, '')=="":
#        path=os.path.split(os.path.realpath(__file__))[0] + '/img/生气.jpg'
#        path1=os.path.split(os.path.realpath(__file__))[0] + '/MP3/SCA.silk.amr'
#        await GPT.send(MessageSegment.audio(path=path1))
#        await GPT.finish("说词啊！"+MessageSegment.image(path=path))

#    today = datetime.datetime.now()
#    time1 = str(today.year) + "_" + str(today.month) + "_" + str(today.day) + "_" + user_id
#    f=pd.read_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/GPTdaybat.txt")
#    text1=time1 + "A"
#    text2=time1 + "B"
#    if text1 in np.array(f.loc[:,"A"]).tolist() and text2 in np.array(f.loc[:,"A"]).tolist():
#        await GPT.finish("今日次数用完，明天再试试吧~")
#    elif text1 in np.array(f.loc[:,"A"]).tolist():
#        p = pd.DataFrame({"A":[text2]})
#        f = f._append(p,ignore_index = True,sort = False)
#        f.to_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/GPTdaybat.txt",index = False)
#    else:
#        p = pd.DataFrame({"A":[text1]})
#        f = f._append(p,ignore_index = True,sort = False)
#        f.to_csv("C:\\Users\\Administrator\\Desktop\\Qbot\\n55/src/plugins/GPTdaybat.txt",index = False)
    openai.api_key = "yourkey"
    openai.base_url = "https://api.vveai.com/v1/"
    aclient = AsyncOpenAI(
        base_url="ttps://api.vveai.com/v1/",
        api_key="yourkey"  # 替换为你的 API 密钥
    )
    openai.default_headers = {"x-foo": "true"}
    completion = await aclient.chat.completions.create(
#        model="chatgpt-4o-latest",
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "你是个外表呆萌的猫娘，你的名字叫55姬。你使用雌小鬼的语气说话。并且你需要在每一句话的结尾都加上喵~。",
            },
            {
                "role": "user",
                "content": args,
            },
        ],
    )
    msg=completion.choices[0].message.content
    print(msg)
    await GPT.finish(msg+"\n(以上内容为Deepseek生成，实用性和真实性自行判断)")
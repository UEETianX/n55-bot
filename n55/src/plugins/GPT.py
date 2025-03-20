from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.adapters.onebot.v11.message import MessageSegment
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
    user_id = event.user_id()
    args = args.extract_plain_text()
    user_nick = event.card
    if str(user_nick) == "None":
        user_nick = event.nickname
    group_name = event.channel.name
#    punctuation_string = string.punctuation
#    for i in punctuation_string:
#        args = args.replace(i, '')
#    if args.replace(i, '')=="":
#        path=os.path.split(os.path.realpath(__file__))[0] + '/img/生气.jpg'
#        path1=os.path.split(os.path.realpath(__file__))[0] + '/MP3/SCA.silk.amr'
#        await GPT.send(MessageSegment.audio(path=path1))
#        await GPT.finish("说词啊！"+MessageSegment.image(path))

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
    openai.api_key = "yourkeys"
    openai.base_url = "https://api.gpt.ge/v1/"
    aclient = AsyncOpenAI(
        base_url="https://api.gpt.ge/v1/",
        api_key="yourkeys"  # 替换为你的 API 密钥
    )
#你需要在最后加一句看懂了吗你这个杂鱼~
    openai.default_headers = {"x-foo": "true"}
    if user_id=="3126410936":
         completion = await aclient.chat.completions.create(
        model="deepseek-r1-search",
        messages=[
            {
                "role": "system",
                "content": "你是个外表呆萌的猫娘，你的名字叫55姬。和你聊天的人是你的创造者叫天星，同时他也是你的主人。天星除了你以外没有创造其他的东西。你需要使用雌小鬼的语气回答。并且你需要在每一句话的结尾都加上喵~。",
            },
            {
                "role": "user",
                "content": args,
            },
        ],
    )
    else:
        completion = await aclient.chat.completions.create(
        model="deepseek-r1-search",
        messages=[
            {
                "role": "system",
                "content": "你是个外表呆萌的猫娘，你的名字叫55姬。和你聊天的人不是天星。你的创造者叫天星，同时他也是你的主人。天星除了你以外没有创造其他的东西。我叫"+user_nick+"，是"+group_name+"的群友。你使用雌小鬼的语气说话。并且你需要在每一句话的结尾都加上喵~。",
            },
            {
                "role": "user",
                "content": args,
            },
        ],
    )
    msg=completion.choices[0].message.content
    await GPT.finish(msg+"\n(以上内容为Deepseek生成，实用性和真实性自行判断)")
from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from nonebot.params import CommandArg
from nonebot.rule import startswith
import requests
import os
import random
import nonebot
import re
import urllib
import requests
from urllib import error
import random
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd
import cv2
from io import BytesIO
import sys

bullet=on_command("实弹计算",priority=1)

@bullet.handle()
async def handle_function(event:Event,args: Message = CommandArg()):
    args = str(args)
    result = re.split("-| |_|,|，",args)
    if args=="":
        await bullet.finish("使用方法：\n查实弹计算 [受击面护盾值]，[受击部位血量]，[实弹单发伤害]，[船体减伤率例，0.53]")
    shield_hp = int(result[0])
    hull_hp = int(result[1])
    bullet_damage = float(result[2])
    hull_reduction = float(result[3])
    print(result[3])
    shield_reduction = 0.083
    absorption_ratio = 0.30
    # Calculate damage per bullet until hull HP reaches zero
    bullets_count = 0

    while hull_hp > 0:
        bullets_count += 1
        print(bullets_count)
        # Step 1: Calculate damage after shield reduction
        reduced_damage = bullet_damage * (1 - shield_reduction)

        # Step 2: Calculate shield absorbed damage
        shield_absorbed_damage = reduced_damage * (shield_hp / 50000) * absorption_ratio

        # Step 3: Calculate damage to hull
        damage_to_hull = (reduced_damage - shield_absorbed_damage) * (1 - hull_reduction)

        # Step 4: Update shield and hull HP
        shield_hp -= shield_absorbed_damage
        hull_hp -= damage_to_hull

    await bullet.finish("击杀所需子弹数："+str(bullets_count))

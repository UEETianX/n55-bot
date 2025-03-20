from nonebot.plugin.on import on_command,on_regex
from nonebot.rule import to_me
from nonebot.adapters import (
    Bot,
    Event,
    Message
    )
from nonebot.permission import SUPERUSER

from nonebot.matcher import Matcher
from nonebot.params import CommandArg, Arg

from nonebot import logger
import nonebot
import re
import asyncio
import time
import random
import unicodedata

nonebot.load_plugin('nonebot_plugin_russian_ban')

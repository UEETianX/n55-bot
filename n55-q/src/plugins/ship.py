from nonebot.adapters.qq import Bot
from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message
from nonebot.typing import T_State
from nonebot.adapters import Event
import requests
import os
import random
from time import sleep
from pathlib import Path

find=on_message(priority=2)

@find.handle()
async def _(bot:Bot,event:MessageEvent,state:T_State):
    msg = str(event.get_message()).strip().replace(" ","")
    msg = str(event.get_message()).strip().replace(" ","").replace("/飞船","查")
    if msg.startswith('/'):
        msg='查' + msg[1:]
    msg = msg.replace("圣盾","").replace("铁砧","").replace("起源","").replace("武藏","").replace("RSI","").replace("未来","").replace("南船座","").replace("南船","").replace("灰猫","").replace("盾博尔","").replace("埃斯佩利亚","").replace("奥波亚","")
    if "查飞船".lower() == msg.lower():
        await find.finish("输入[查]+飞船名字即可查询\n问题反馈群：209872290")

    if "查F8A".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F8A Lightning.jpg'
        print(path)
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查惩戒".lower() in msg.lower() or "查Retribution".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Retribution.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查梅林".lower() == msg.lower() or "查p52".lower() == msg.lower() or "查Merkin".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/P-52 Merlin.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查阿基米德".lower() == msg.lower() or "查p72".lower() == msg.lower() or "查Archimedes".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/P-72 Archimedes.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查王船".lower() == msg.lower() or "查Kingship".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Kingship.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查莱伦".lower() == msg.lower() or "查锐伦".lower() == msg.lower() or "查Railen".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Railen.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查创世纪".lower() == msg.lower() or "查GenesisStarliner".lower() == msg.lower() or "查Genesis".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Genesis Starliner.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查A2".lower() in msg.lower() or "查大力神A2".lower() == msg.lower() or "查A2HerculesStarlifter".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/A2 Hercules Starlifter.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查C2".lower() in msg.lower() or "查大力神C2".lower() == msg.lower() or "查C2HerculesStarlifter".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/C2 Hercules Starlifter.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查M2".lower() in msg.lower() or "查大力神M2".lower()== msg.lower() or "查M2HerculesStarlifter".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/M2 Hercules Starlifter.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  msg.lower() == "查大力神".lower() or "查HerculesStarlifter".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/C2 Hercules Starlifter.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查大力神[A2/C2/M2]\n\n例：查大力神A2")

    if  "查黑战".lower() in msg.lower() or "查地狱".lower() in msg.lower() or "查战神地狱".lower() in msg.lower() or "查AresStarFighterInferno".lower() == msg.lower() or "查Inferno".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ares Star Fighter Inferno.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查白战".lower() in msg.lower()  or "查离子".lower() in msg.lower() or "查战神离子".lower() in msg.lower() or "查AresStarFighterIon".lower() == msg.lower() or "查Ion".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ares Star Fighter Ion.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查战神".lower() == msg.lower() or "查AresStarFighter".lower() == msg.lower() or "查Ares".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ares Star Fighter Inferno.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查[黑/白]战神\n\n例：查黑战神")

    if  "查星灵A1".lower() == msg.lower() or "查A1".lower() == msg.lower() or "查A1Spirit".lower() == msg.lower() or "查SpiritA1".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/A1 Spirit.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查星灵E1".lower() == msg.lower() or "查E1".lower() == msg.lower() or "查E1Spirit".lower() == msg.lower() or "查SpiritE1".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/E1 Spirit.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查星灵C1".lower() == msg.lower() or "查C1".lower() == msg.lower() or "查C1Spirit".lower() == msg.lower() or "查SpiritC1".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/C1 Spirit.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查星灵".lower() == msg.lower() or "查Spirit".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/C1 Spirit.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查星灵[A1/C1/E1]\n\n例：查星灵A1")

    if  "查水星".lower() in msg.lower() or "查墨丘利".lower() == msg.lower() or "查MercuryStarRunner".lower() == msg.lower() or "查Mercury".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mercury Star Runner.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查MPUVT".lower() == msg.lower() or "查MPUV牵引".lower() == msg.lower() or "查MPUVTractor".lower() == msg.lower() or "查MPUVT".lower() == msg.lower() or "查MPUV-T".lower() == msg.lower() or "查MPUV1T".lower() == msg.lower() or "查MPUV-1T".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/MPUV_Tractor.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查MPUVC".lower() == msg.lower() or "查MPUV货运".lower() == msg.lower() or "查MPUVCargo".lower() == msg.lower() or "查MPUVC".lower() == msg.lower() or "查MPUV-C".lower() == msg.lower() or "查MPUV1C".lower() == msg.lower() or "查MPUV-1C".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/MPUV Cargo.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查MPUVP".lower() == msg.lower() or "查MPUV载人".lower() == msg.lower() or "查MPUVPersonnel".lower() == msg.lower() or "查MPUVP".lower() == msg.lower() or "查MPUV-P".lower() == msg.lower() or "查MPUV1P".lower() == msg.lower() or "查MPUV-1P".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/MPUV Personnel.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查MPUV".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/MPUV Cargo.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查MPUV[载人/货运/牵引]\n\n例：查MPUV载人")

    if  "查SRV".lower() == msg.lower() or "查拖船".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/SRV.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查木筏".lower() == msg.lower() or "查RAFT".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/RAFT.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查鼹鼠".lower() == msg.lower() or "查MOLE".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/MOLE.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查伊德里斯K".lower() == msg.lower() or "查小姨K".lower() == msg.lower() or "查Idris-K".lower() == msg.lower() or "查IdrisK".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Idris-K.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查伊德里斯M".lower() == msg.lower() or "查小姨M".lower() == msg.lower() or "查Idris-M".lower() == msg.lower() or "查IdrisM".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Idris-M.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查伊德里斯P".lower() == msg.lower() or "查小姨P".lower() == msg.lower() or "查Idris-P".lower() == msg.lower() or "查IdrisP".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Idris-P.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查伊德里斯".lower() == msg.lower() or "查小姨".lower() == msg.lower() or "查Idris".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Idris-P.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查伊德里斯[K/M/P]\n\n例：查伊德里斯K")

    if  "查先锋先驱".lower() == msg.lower() or "查先驱".lower() == msg.lower() or "查VanguardHarbinger".lower() == msg.lower() or "查Harbinger".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Vanguard Harbinger.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查先锋重装".lower() == msg.lower() or "查重装".lower() == msg.lower() or "查VanguardHoplite".lower() == msg.lower() or "查Hoplite".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Vanguard Hoplite.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查先锋典狱长".lower() == msg.lower() or "查典狱长".lower() == msg.lower() or "查VanguardWarden".lower() == msg.lower() or "查Warden".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Vanguard Warden.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查先锋哨兵".lower() == msg.lower() or "查哨兵".lower() == msg.lower() or "查VanguardSentinel".lower() == msg.lower() or "查Sentinel".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Vanguard Sentinel.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  msg.lower() == "查先锋".lower() or "查Vanguard".lower() == msg.lower() :
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Vanguard Sentinel.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查先锋[先驱/重装/典狱长/哨兵]\n\n例：查先锋先驱")

    if  "查军刀彗星".lower() == msg.lower() or "查SabreComet".lower() == msg.lower() or "查Comet".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Sabre Comet.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查军刀渡鸦".lower() == msg.lower() or "查渡鸦".lower() == msg.lower() or "查SabreRaven".lower() == msg.lower() or "查Raven".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Sabre Raven.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查军刀".lower() == msg.lower() or "查Sabre".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Sabre.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查回收".lower() in msg.lower() or "查再生者".lower() == msg.lower() or "查Reclaimer".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Reclaimer.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查复仇术士".lower() == msg.lower() or "查复仇者术士".lower() == msg.lower() or "查术士".lower() in msg.lower() or "查AvengerWarlock".lower() == msg.lower() or "查Warlock".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Avenger Warlock.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查复仇泰坦".lower() == msg.lower() or "查复仇者泰坦".lower() == msg.lower() or "查泰坦".lower() in msg.lower() or "查AvengerTitan".lower() == msg.lower() or "查Titan".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Avenger Titan.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查复仇追猎".lower() in msg.lower() or "查复仇者追猎".lower() in msg.lower() or "查追猎".lower() in msg.lower() or "查AvengerStalker".lower() == msg.lower() or "查Stalker".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Avenger Stalker.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  msg.lower() == "查复仇".lower() or msg == "查复仇者" or "查Avenger".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Avenger Titan.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查复仇[术士/泰坦/追猎]\n\n例：查复仇术士")

    if  "查报复".lower() in msg.lower() or "查Retaliator".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Retaliator.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查救赎".lower() in msg.lower() or "查Redeemer".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Redeemer.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查日蚀".lower() == msg.lower() or "查日食".lower() == msg.lower() or "查Eclipse".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Eclipse.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查标枪".lower() == msg.lower() or "查Javelin".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Javelin.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查火神".lower() == msg.lower() or "查Vulcan".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Vulcan.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查短剑勇士".lower() == msg.lower() or "查Gladiusgaliant".lower() == msg.lower() or "查galiant".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Gladius galiant.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查短剑海盗".lower() == msg.lower() or "查海盗短剑".lower() == msg.lower() or "查Gladiuspirate".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Gladius pirate.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查短剑".lower() == msg.lower() or "查剑兰".lower() == msg.lower() or "查Gladius".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Gladius.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查锤头".lower() == msg.lower() or "查锤头鲨".lower() == msg.lower() or "查Hammerhead".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Hammerhead.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查鹦鹉螺".lower() == msg.lower() or "查Nautilus".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Nautilus.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查利爪伯劳".lower() in msg.lower() or "查伯劳".lower() == msg.lower() or "查伯劳鸟".lower() == msg.lower() or "查TalonShrike".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Talon Shrike.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查利爪".lower() == msg.lower() or "查炮鸟".lower() == msg.lower() or "查Talon".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Talon.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查刀锋".lower() == msg.lower() or "查Blade".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Blade_(replica).jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查徘徊".lower() in msg.lower() or "查Prowler".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Prowler.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查死镰".lower() == msg.lower() or "查Scythe".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Scythe_(replica).jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查长刀".lower() == msg.lower() or "查Glaive".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Glaive_(replica).jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查NOX".lower() == msg.lower() or "查诺克斯".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Nox.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查卡图".lower() == msg.lower() or "查Khartu-al".lower() == msg.lower() or "查Khartual".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Khartu-al.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查桑托起亚".lower() == msg.lower() or "查大青椒".lower() == msg.lower() or "查santokiya".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/santokiya.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查巴商".lower() == msg.lower() or "查巴奴商船".lower() == msg.lower() or "查商船".lower() == msg.lower() or "查Merchantman".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Merchantman.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查巴卫".lower() == msg.lower() or "查巴奴防卫者".lower() == msg.lower() or "查巴奴卫士".lower() == msg.lower() or "查防卫者".lower() == msg.lower() or "查Defender".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Defender.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查信使".lower() == msg.lower() or "查Herald".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Herald.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查小刀基础".lower() == msg.lower() or "查Cutter".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cutter.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查掠夺者".lower() == msg.lower() or "查掠夺".lower() == msg.lower() or "查Buccaneer".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Buccaneer.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查毛虫".lower() == msg.lower() or "查Caterpillar".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Caterpillar.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查海妖私掠".lower() == msg.lower() or "查KrakenPrivateer".lower() == msg.lower() or "查白海妖".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Kraken Privateer.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查海妖".lower() == msg.lower() or "查Kraken".lower() == msg.lower() or "查黑海妖".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Kraken.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查海盗船".lower() == msg.lower() or "查Corsair".lower() == msg.lower() or "查海盗".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Corsair.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查秃鹫".lower() == msg.lower() or "查Vulture".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Vulture.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查红弯刀".lower() == msg.lower() or "查CutlassRed".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cutlass Red.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查蓝弯刀".lower() == msg.lower() or "查CutlassBlue".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cutlass Blue.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查黑弯刀".lower() == msg.lower() or "查CutlassBlack".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cutlass Black.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查钢弯刀".lower() == msg.lower() or "查CutlassSteel".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cutlass Steel.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查弯刀".lower() in msg.lower() or "查Cutlass".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cutlass Black.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查[黑/红/蓝/钢]弯刀\n\n例：查黑弯刀")

    if "查白弯刀".lower() == msg.lower():
        await find.finish("没有！下一个！")
    
    if  "查蜻蜓".lower() == msg.lower() or "查Dragonfly".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Dragonfly.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查骡".lower() in msg.lower() or "查Mule".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mule.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查剃刀EX".lower() == msg.lower() or "查RazorEX".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Razor EX.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查剃刀LX".lower() == msg.lower() or "查RazorLX".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Razor LX.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  msg.lower() == "查剃刀".lower() or "查Razor".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Razor.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查狂怒LX".lower() == msg.lower() or "查furyLX".lower() == msg.lower() or "查fury LX".lower() == msg.lower() or "查福瑞LX".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Fury LX.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查狂怒MX".lower() == msg.lower() or "查furyMX".lower() == msg.lower() or "查fury MX".lower() == msg.lower() or "查福瑞MX".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Fury MX.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查狂怒".lower() == msg.lower() or "查fury".lower() == msg.lower() or "查福瑞".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Fury.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查信赖武装".lower() == msg.lower() or "查信赖Tana".lower() == msg.lower() or "查ReliantTana".lower() == msg.lower() or "查Tana".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Reliant Tana.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查信赖科考".lower() == msg.lower() or "查信赖sen".lower() == msg.lower() or "查ReliantSen".lower() == msg.lower() or "查Sen".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Reliant Sen.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查信赖新闻".lower() == msg.lower() or "查信赖mako".lower() == msg.lower() or "查Reliantmako".lower() == msg.lower() or "查mako".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Reliant Mako.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查信赖货运".lower() == msg.lower() or "查信赖kore".lower() == msg.lower() or "查Reliantkore".lower() == msg.lower() or "查kore".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Reliant Kore.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  msg.lower() == "查信赖".lower() or "查Reliant".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Reliant Kore.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查信赖[货运/新闻/科考/武装]\n\n例：查信赖货运")

    if  "查勘探".lower() in msg.lower() or "查Prospector".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Prospector.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查奋进".lower() == msg.lower() or "查Endeavor".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Endeavor.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查奥德赛".lower() == msg.lower() or "查Odyssey".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Odyssey.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查无垠".lower() == msg.lower() or "查Expanse".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Expanse.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查星际远航者双子座".lower() == msg.lower() or "查军油".lower() == msg.lower() or "查双子座".lower() == msg.lower() or "查StarfarerGemini".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Starfarer Gemini.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查星际远航者".lower() == msg.lower() or "查民油".lower() == msg.lower() or "查油船".lower() == msg.lower() or "查加油船".lower() == msg.lower() or "查Starfarer".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Starfarer.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查自由dur".lower() == msg.lower() or "查自由枪骑兵dur".lower() == msg.lower() or "查Freelancerdur".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Freelancer DUR.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查自由max".lower() == msg.lower() or "查自由枪骑兵max".lower() == msg.lower() or "查Freelancermax".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Freelancer MAX.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查自由mis".lower() == msg.lower() or "查自由枪骑兵mis".lower() == msg.lower() or "查Freelancermis".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Freelancer MIS.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查自由基础".lower() == msg.lower() or "查自由枪骑兵基础".lower() == msg.lower() or "查Freelancer".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Freelancer.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  msg.lower() == "查自由".lower() or msg.lower() == "查自由枪骑兵".lower() or msg.lower() == "查自由职业者".lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Freelancer.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("还有多个型号，要查哪个？\n\n查自由[/Dur/Max/Mis]\n\n例：查自由Dur")

    if  "查货A".lower() == msg.lower() or "查货轮A".lower() == msg.lower() or "查HullA".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Hull A.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查货B".lower() == msg.lower() or "查货轮B".lower() == msg.lower() or "查HullB".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Hull B.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查货C".lower() == msg.lower() or "查货轮C".lower() == msg.lower() or "查HullC".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Hull C.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查货D".lower() == msg.lower() or "查货轮D".lower() == msg.lower() or "查HullD".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Hull D.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查货E".lower() == msg.lower() or "查货轮E".lower() == msg.lower() or "查HullE".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Hull E.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查PTV".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/PTV.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查ROC-DS".lower() == msg.lower() or "查ROCDS".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/ROC-DS.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查ROC".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/ROC.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查STV".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/STV.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查新星".lower() in msg.lower() or "查NOVA".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Nova.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查旋风AA".lower() == msg.lower() or "查CycloneAA".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cyclone AA.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查旋风MT".lower() == msg.lower() or "查CycloneMT".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cyclone MT.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查旋风RC".lower() == msg.lower() or "查CycloneRC".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cyclone RC.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查旋风RN".lower() == msg.lower() or "查CycloneRN".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cyclone RN.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查旋风TR".lower() == msg.lower() or "查CycloneTR".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cyclone TR.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查旋风基础".lower() == msg.lower() or "查Cyclone".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cyclone.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查旋风".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cyclone.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("还有多个型号，要查哪个？\n\n查旋风[/AA/MT/RC/RN/TR]\n\n例：查旋风AA")

    if  "查游骑兵CV".lower() == msg.lower() or "查游侠CV".lower() == msg.lower() or "查RangerCV".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ranger CV.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查游骑兵RC".lower() == msg.lower() or "查游侠RC".lower() == msg.lower() or "查RangerRC".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ranger RC.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查游骑兵TR".lower() == msg.lower() or "查游侠TR".lower() == msg.lower() or "查RangerTR".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ranger TR.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查游骑兵".lower() == msg.lower() or "查游侠".lower() == msg.lower() or "查Ranger".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ranger TR.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查游侠[CV/RC/TR]\n\n例：查游侠CV")

    if  "查风暴基础".lower() == msg.lower() or "查Storm".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Storm.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查风暴AA".lower() == msg.lower() or "查StormAA".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/StormAA.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查风暴".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Storm.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("还有多个型号，要查哪个？\n\n查风暴[/AA]\n\n例：查风暴AA")

    if  "查北极星".lower() == msg.lower() or "查Polaris".lower() == msg.lower():
        if str(type(event)) !="<class 'nonebot.adapters.qq.event.C2CMessageCreateEvent'>":
            await find.send("(此提示放置三天)私聊机器人可以不需要@")
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Polaris.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查大熊医疗".lower() in msg.lower() or "查大熊座医疗".lower() in msg.lower() or "查医疗大熊".lower() == msg.lower() or "查医疗熊".lower() == msg.lower() or "查UrsaMedivac".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ursa_Medivac.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查大熊".lower() in msg.lower() or "查Ursa".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ursa.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查天蝎".lower() == msg.lower() or "查天蝎座".lower() == msg.lower() or "查Scorpius".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Scorpius.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查孟加拉".lower() == msg.lower() or "查Bengal".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Bengal.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查山猫".lower() in msg.lower() or "查天猫".lower() in msg.lower() or "查Lynx".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Lynx.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查仙女座级".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/仙女座级.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查仙女".lower() == msg.lower() or "查仙女座".lower() == msg.lower() or "查ConstellationAndromeda".lower() == msg.lower() or "查Andromeda".lower() == msg.lower():
        if random.randint(0,99) > 93:
            path=os.path.split(os.path.realpath(__file__))[0] + '/ship/仙女座级.png'
            await find.send(MessageSegment.file_image(Path(__file__).parent / path))
            sleep(3)
            await find.send("哈哈，骗你哒~")
            sleep(1)
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Constellation Andromeda.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查凤凰".lower() == msg.lower() or "查凤凰座".lower() == msg.lower() or "查ConstellationPhoenix".lower() == msg.lower() or "查Phoenix".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Constellation Phoenix.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查天鹰".lower() == msg.lower() or "查天鹰座".lower() == msg.lower() or "查ConstellationAquila".lower() == msg.lower() or "查Aquila".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Constellation Aquila.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查金牛".lower() == msg.lower() or "查金牛座".lower() == msg.lower() or "查ConstellationTaurus".lower() == msg.lower() or "查Taurus".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Constellation Taurus.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查极光CL".lower() == msg.lower() or "查AuroraCL".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Aurora CL.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查极光ES".lower() == msg.lower() or "查AuroraES".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Aurora ES.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查极光LN".lower() == msg.lower() or "查AuroraLN".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Aurora LN.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查极光LX".lower() == msg.lower() or "查AuroraLX".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Aurora LX.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查极光MR".lower() == msg.lower() or "查AuroraMR".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Aurora MR.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  msg.lower() == "查极光".lower() or "查Aurora".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Aurora MR.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查极光[CL/ES/LN/LX/MR]\n\n例：查极光CL")

    if  "查猎户".lower() in msg.lower() or "查Orion".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Orion.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查英仙".lower() in msg.lower() or "查Perseus".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Perseus.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查蝎心".lower() == msg.lower() or "查电蝎".lower() == msg.lower() or "查心宿二".lower() == msg.lower() or "查天蝎座心宿二".lower() == msg.lower()or "查天蝎座蝎心".lower() == msg.lower() or "查ScorpiusAntares".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Scorpius Antares.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查银河".lower() in msg.lower() or "查Galaxy".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Galaxy.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查螳螂".lower() == msg.lower() or "查Mantis".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mantis.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查阿波罗分诊".lower() == msg.lower() or "查红阿波罗".lower() == msg.lower() or "查Apollo Triage".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Apollo Triage.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查阿波罗医疗".lower() == msg.lower() or "查白阿波罗".lower() == msg.lower() or "查Apollo Medivac".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Apollo Medivac.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查阿波罗".lower() == msg.lower() or "查Apollo".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Apollo Triage.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查[红/白]阿波罗\n\n例：查红阿波罗")

    if  "查开拓".lower() == msg.lower() or "查开拓者".lower() == msg.lower() or "查Pioneer".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Pioneer.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查悬浮驷".lower() == msg.lower() or "查悬浮四".lower() == msg.lower() or "查HoverQuad".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/HoverQuad.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查游牧".lower() in msg.lower() or "查Nomad".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Nomad.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查野马伽马".lower() == msg.lower() or "查野马G".lower() in msg.lower() or "查MustangGamma".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mustang Gamma.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查野马德尔塔".lower() == msg.lower() or "查野马D".lower() in msg.lower() or "查MustangDelta".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mustang Delta.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查野马欧米伽".lower() == msg.lower() or  "查红野马".lower() == msg.lower() or "查野马O".lower() in msg.lower() or "查MustangOmega".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mustang Omega.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查野马贝塔".lower() == msg.lower() or "查野马B".lower() in msg.lower() or "查MustangBeta".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mustang Beta.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查野马阿尔法".lower() == msg.lower() or "查野马A".lower() in msg.lower() or "查MustangAlpha".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mustang Alpha.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if   msg.lower() == "查野马".lower() or "查Mustang".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mustang Alpha.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查野马[阿尔法/贝塔/伽马/德尔塔/欧米伽]\n\n例：查野马阿尔法")

    if  "查100i".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/100i.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查125A".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/125a.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查135C".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/135c.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查300I".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/300i.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
        
    if  "查315P".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/315p.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查325A".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/325a.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查350R".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/350r.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查400i".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/400i.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查600i探索".lower() == msg.lower() or "查600ie".lower() == msg.lower() or "查600iExplorer".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/600i Explorer.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查600i旅游".lower() == msg.lower() or "查600it".lower() == msg.lower() or "查600iTouring".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/600i Touring.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查600i行政".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/600i xingzheng.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查600i".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/600i Explorer.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查600i[探索/旅游/行政]\n\n例：查600i探索")

    if  "查85X".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/85X.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查890".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/890 Jump.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查G12R".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/G12r.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查G12A".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/G12a.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查G12基础".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/G12.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查G12".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/G12.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("还有多个型号，要查哪个？\n\n查G12[/A/R]\n\n例：查G12A")

    if  "查M50".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/M50.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查X1竞速".lower() == msg.lower() or "查X1速".lower() in msg.lower() or "查X1Velocity".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/X1 Velocity.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查X1力".lower() == msg.lower() or "查X1武装".lower() == msg.lower() or "查X1Force".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/X1 Force.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查X1基础".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/X1.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查X1".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/X1.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("还有多个型号，要查哪个？\n\n查X1[/武装/竞速]\n\n例：查X1武装")

    if  "查F8C".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F8C Lightning.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查克拉克".lower() == msg.lower() or "查卡拉克".lower() == msg.lower() or "查Carrack".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Carrack.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查军团兵".lower() == msg.lower() or "查Legionnaire".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Legionnaire.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查军黄".lower() == msg.lower() or "查军黄MK2".lower() == msg.lower() or "查军黄MKII".lower() == msg.lower() or "查F7A".lower() == msg.lower() or "查军用大黄蜂".lower() == msg.lower() or "查军用大黄蜂MK2".lower() == msg.lower() or "查军用大黄蜂MKII".lower() == msg.lower() or "查F7AMK2".lower() == msg.lower() or "查F7AMKII".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7A MK2 Hornet.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查军黄MK1".lower() == msg.lower() or "查军黄MKI".lower() == msg.lower() or "查F7AMK1".lower() == msg.lower() or "查军用大黄蜂MK1".lower() == msg.lower() or "查军用大黄蜂MKI".lower() == msg.lower() or "查F7AMKI".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7A_MK1.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))


    if  "查双鱼座C8R".lower() == msg.lower() or "查C8R".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/C8R Pisces Rescue.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查双鱼座C8X".lower() == msg.lower() or "查C8X".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/C8X Pisces Expedition.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查双鱼座基础".lower() == msg.lower() or "查C8基础".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/C8 Pisces.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查c8".lower() == msg.lower() or "查双鱼座".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/C8 Pisces.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("还有多个型号，要查哪个？\n\n查C8[/X/R]\n\n例：查C8R")

    if  "查坩埚".lower() == msg.lower() or "查Crucible".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Crucible.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查女武神".lower() == msg.lower() or "查瓦尔基里".lower() == msg.lower() or "查Valkyrie".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Valkyrie.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查弩炮".lower() == msg.lower() or "查Ballista".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Ballista.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查斯巴达".lower() == msg.lower() or "查Spartan".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Spartan.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查水龟".lower() == msg.lower() or "查Terrapin".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Terrapin.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查猎鹰".lower() == msg.lower() or "查鹰".lower() == msg.lower() or "查小鹰".lower() == msg.lower() or "查Hawk".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Hawk.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查百夫长".lower() == msg.lower() or "查Centurion".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Centurion.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查箭矢".lower() == msg.lower() or "查箭头".lower() == msg.lower() or "查箭".lower() == msg.lower() or "查Arrow".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Arrow.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查角斗士".lower() == msg.lower() or "查Gladiator".lower() == msg.lower() or "查T8C".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Gladiator.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查解放".lower() in msg.lower() or "查Liberator".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Liberator.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查飓风".lower() == msg.lower() or "查Hurricane".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Hurricane.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if  "查大黄蜂基础".lower() == msg.lower() or "查普黄".lower() == msg.lower() or "查F7C".lower() == msg.lower() or "查F7CHornet".lower() == msg.lower() or "查黄蜂基础".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C Hornet.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查大黄蜂MMK2".lower() == msg.lower() or "查超黄MK2".lower() == msg.lower() or "查超级大黄蜂MK2".lower() == msg.lower() or "查F7CMMK2".lower() == msg.lower() or "查F7C-MMK2".lower() == msg.lower() or "查SuperHornetMK2".lower() == msg.lower() or "查F7CMSuperHornetMK2".lower() == msg.lower() or "查F7C-MSuperHornetMK2".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C-MMK2.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查大黄蜂M".lower() == msg.lower() or "查超黄".lower() == msg.lower() or "查超级大黄蜂".lower() == msg.lower() or "查F7CM".lower() == msg.lower() or "查F7C-M".lower() == msg.lower() or "查SuperHornet".lower() == msg.lower() or "查F7CMSuperHornet".lower() == msg.lower() or "查F7C-MSuperHornet".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C-M Super Hornet.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查大黄蜂R".lower() == msg.lower() or "查追黄".lower() == msg.lower() or "查大黄蜂追踪".lower() == msg.lower() or "查追踪黄".lower() == msg.lower() or "查雷达黄".lower() == msg.lower() or "查追踪大黄蜂".lower() == msg.lower() or "查F7C-RHornetTracker".lower() == msg.lower() or "查F7CRHornetTracker".lower() == msg.lower() or "查F7CR".lower() == msg.lower() or "查F7C-R".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C-R Hornet Tracker.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查大黄蜂S".lower() == msg.lower() or "查隐黄".lower() == msg.lower() or "查大黄蜂幽灵".lower() == msg.lower() or "查鬼蜂".lower() == msg.lower() or "查鬼黄".lower() == msg.lower() or "查幽灵黄".lower() == msg.lower() or "查幽灵蜂".lower() == msg.lower() or "查幽灵大黄蜂".lower() == msg.lower() or "查F7C-SHornetGhost".lower() == msg.lower() or "查F7CSHornetGhost".lower() == msg.lower() or "查F7CS".lower() == msg.lower() or "查F7C-S".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C-S Hornet Ghost.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查大黄蜂MK2".lower() == msg.lower() or "查大黄蜂MKII".lower() == msg.lower() or "查黄蜂MKII".lower() == msg.lower() or "查F7CMKII".lower() == msg.lower() or "查黄蜂MK2".lower() == msg.lower() or "查F7CHornetMK2".lower() == msg.lower() or "查F7CMK2".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C MK2 Hornet.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查大黄蜂".lower() == msg.lower() or "查黄蜂".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C Hornet.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("还有多个型号，要查哪个？\n\n查大黄蜂[/M/R/S/MK2]\n\n例：查大黄蜂M")

    if "查小刀侦察".lower() == msg.lower() or "查小刀侦察兵".lower() == msg.lower()  or "查小刀侦查".lower() == msg.lower() or "查雷达小刀".lower() == msg.lower() or "查CutterScout".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cutter Scout.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))
    
    if "查小刀漫游".lower() in msg.lower() or "查小刀漫步".lower() in msg.lower() or "查小刀探索".lower() == msg.lower() or "查探索小刀".lower() == msg.lower() or "查CutterRambler".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cutter Rambler.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查小刀".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Cutter.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("还有多个型号，要查哪个？\n\n查小刀[/侦察/漫步者]\n\n例：查小刀侦察")

    if "查宙斯CL".lower() == msg.lower() or "查ZeusMkIICL".lower() == msg.lower() or "查ZeusCL".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Zeus_MkII_CL.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查宙斯ES".lower() == msg.lower() or "查ZeusMkIIES".lower() == msg.lower() or "查ZeusES".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Zeus_MkII_ES.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查宙斯MR".lower() == msg.lower() or "查ZeusMkIIMR".lower() == msg.lower() or "查ZeusMR".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Zeus_MkII_MR.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查宙斯".lower() == msg.lower() or "查Zeus".lower() == msg.lower() or "查ZeusMkII".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Zeus_MkII_CL.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查宙斯[CL/ES/MR]\n\n例：查宙斯CL")
    
    if "查速伦".lower() == msg.lower() or "查苏伦".lower() == msg.lower() or "查Syulen".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Syulen.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查天马座".lower() in msg.lower() or "查飞马座".lower() in msg.lower() or "查Pegasus".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Pegasus.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查阿拉斯塔".lower() == msg.lower() or "查Arrastra".lower() == msg.lower() or "查阿拉斯特拉".lower() == msg.lower() or "查碎金机".lower() == msg.lower() or "查研磨机".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Arrastra.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查起源404".lower() == msg.lower() or "查Origin404".lower() == msg.lower() or "查404".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/404.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查变节者".lower() == msg.lower() or "查泰坦变节者".lower() == msg.lower() or "查复仇泰坦变节者".lower() == msg.lower() or "查AvengerTitanRenegade".lower() == msg.lower() or "查Renegade".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Avenger Titan Renegade.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查寻心".lower() in msg.lower() or "查情人黄".lower() == msg.lower() or "查情黄".lower() == msg.lower() or "查F7C-MHornetHeartseeker".lower() == msg.lower() or "查Heartseeker".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C-M Hornet Heartseeker.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查野火".lower() == msg.lower() or "查大黄蜂野火".lower() == msg.lower() or "查黄蜂野火".lower() == msg.lower() or "查F7CHornetWildfire".lower() == msg.lower() or "查Wildfire".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C Hornet Wildfire.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查海盗毛虫".lower() == msg.lower() or "查毛虫海盗".lower() == msg.lower()or "查CaterpillarPirate".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Caterpillar Pirate.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查白野马".lower() == msg.lower() or "查野马维和".lower() in msg.lower() or "查MustangAlphaVindicator".lower() == msg.lower() or "查Vindicator".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Mustang Alpha Vindicator.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查翡翠凤凰".lower() in msg.lower() or "查凤凰翡翠".lower() in msg.lower() or "查绿凤凰".lower() == msg.lower() or "查ConstellationPhoenixEmerald".lower() == msg.lower() or "查PhoenixEmerald".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Constellation Phoenix Emerald.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查女武神解放者".lower() == msg.lower() or "查解放者女武神".lower() == msg.lower() or "查ValkyrieLiberator".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Valkyrie Liberator.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查克拉克远征".lower() in msg.lower() or "查克拉克探索".lower() in msg.lower() or "查远征克拉克".lower() == msg.lower() or "查CarrackExpedition".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Carrack Expedition.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查垃圾车".lower() in msg.lower() or "查扫地车".lower() in msg.lower() or "查清洁车".lower() == msg.lower() or "查猛禽".lower() == msg.lower() or "查RAPTOR".lower() == msg.lower() or "查MISCRAPTOR".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/RAPTOR.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查脉冲LX".lower() in msg.lower() or "查PulseLX".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Pulse LX.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查脉冲".lower() in msg.lower() or "查Pulse".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Pulse.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查军刀火鸟".lower() in msg.lower()  or "查烧鸡".lower() in msg.lower() or "查火鸟".lower() in msg.lower() or "查SabreFirebird".lower() in msg.lower() or "查Firebird".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Sabre_Firebird.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查军刀游隼".lower() in msg.lower()  or "查游隼".lower() in msg.lower() or "查军刀竞速".lower() in msg.lower() or "查SabrePeregrine".lower() in msg.lower() or "查Peregrine".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/SABRE PEREGRINE.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if  "查突击铁甲".lower() in msg.lower()  or "查铁甲突击".lower() in msg.lower()  or "查铁甲突袭".lower() in msg.lower()  or "查铁甲舰突袭".lower() in msg.lower() or "查突袭铁甲".lower() in msg.lower() or "查IRONCLADASSAULT".lower() in msg.lower() or "查ASSAULT".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/IRONCLAD ASSAULT.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查铁甲".lower() in msg.lower() or "查IRONCLAD".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/IRONCLAD.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

 
    if "查星际枪骑兵TAC".lower() == msg.lower() or "查星枪TAC".lower() == msg.lower() or "查STARLANCERTAC".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/STARLANCER TAC.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查星际枪骑兵MAX".lower() == msg.lower() or "查星枪MAX".lower() == msg.lower() or "查STARLANCERMAX".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/STARLANCER MAX.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查星际枪骑兵".lower() == msg.lower() or "查星枪".lower() == msg.lower() or "查STARLANCER".lower() == msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/STARLANCER TAC.jpg'
        await find.send(MessageSegment.file_image(Path(__file__).parent / path))
        await find.finish("有多个型号，要查哪个？\n\n查星际枪骑兵[MAX/TAC]\n\n例：查星际枪骑兵MAX")

    if "查CSV".lower() in msg.lower() or "查CSVMS".lower() in msg.lower() or "查CSV-MS".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/CSV SM.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查无畏".lower() in msg.lower() or "查intrepid".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/intrepid.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查帕拉丁".lower() in msg.lower() or "查圣骑士".lower() in msg.lower() or "查PALADIN".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/PALADIN.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查水龟医疗".lower() in msg.lower() or "查医疗水龟".lower() in msg.lower() or "查Terrapin MEDIC".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Terrapin MEDIC.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查大黄蜂追踪MK2".lower() in msg.lower() or "查追黄MK2".lower() in msg.lower() or "查大黄蜂追踪MKII".lower() in msg.lower() or "查追黄MKII".lower() in msg.lower() or "查F7C-R Hornet Tracker Mk II".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C-R Hornet Tracker Mk II.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查大黄蜂幽灵MK2".lower() in msg.lower() or "查隐黄MK2".lower() in msg.lower() or "查大黄蜂幽灵MKII".lower() in msg.lower() or "查隐黄MKII".lower() in msg.lower() or "查 F7C-S Hornet Ghost Mk II".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/F7C-S Hornet Ghost Mk II.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查守护者QI".lower() in msg.lower() or "查大福瑞QI".lower() in msg.lower() or "查大福瑞拦截".lower() in msg.lower() or "查守护者拦截".lower() in msg.lower() or "查守卫QI".lower() in msg.lower()or "查守卫拦截".lower() in msg.lower() or "查噶点QI".lower() in msg.lower() or "查GuardianQI".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Guardian QI.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查守护者".lower() in msg.lower() or "查大福瑞".lower() in msg.lower() or "查守卫".lower() in msg.lower() or "查噶点".lower() in msg.lower() or "查Guardian".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Guardian.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查机遇".lower() in msg.lower() or "查财富".lower() in msg.lower() or "查小捞".lower() in msg.lower() or "查Fortune".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/Fortune.jpg'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))

    if "查ATLS".lower() in msg.lower():
        path0=os.path.split(os.path.realpath(__file__))[0] + '/ship/ATLS0.png'
        path1=os.path.split(os.path.realpath(__file__))[0] + '/ship/ATLS1.jpg'
        path2=os.path.split(os.path.realpath(__file__))[0] + '/ship/ATLS2.jpg'
        path3=os.path.split(os.path.realpath(__file__))[0] + '/ship/ATLS3.jpg'
        await find.finish("ATLS\n价格：40美元\nWB：35美元\n游戏币：75 600 aUEC\n购买地点：罗威尔/18区"+MessageSegment.image(path=path0)+MessageSegment.image(path=path1)+MessageSegment.image(path=path2)+MessageSegment.image(path=path3))

    if "查摇摇车".lower() in msg.lower():
        path=os.path.split(os.path.realpath(__file__))[0] + '/ship/摇摇车ES.png'
        await find.finish(MessageSegment.file_image(Path(__file__).parent / path))



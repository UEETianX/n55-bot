import psutil
from nonebot.adapters.qq.event import MessageEvent
from nonebot.adapters.qq.message import MessageSegment
from nonebot import on_command,on_message,on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event,Message
from nonebot.params import CommandArg
from nonebot.rule import Rule

sysinfo = on_command("系统状态", priority=1)


@sysinfo.handle()
async def handle_function():
    def cpu_info():
        cpu = str(psutil.cpu_times())
        user   = float(cpu.split('user=')[1].split(',')[0])
        system = float(cpu.split('system=')[1].split(',')[0])
        idle   = float(cpu.split('idle=')[1].split(',')[0])
        return {
            'used' : round(user+system,1),
            'user' : round(user,1),
            'syst' : round(system,1),
            'free' : round(idle,1),
            'prec' : round((1 - idle/(user+system+idle))*100,1)
        }
    
    def mem_info():
        mem = str(psutil.virtual_memory())
        return {
            'total'     : round(float(mem.split('total=')[1].split(',')[0])/(1024**3),1),
            'available' : round(float(mem.split('available=')[1].split(',')[0])/(1024**3),1),
            'percent'   : float(mem.split('percent=')[1].split(',')[0])
        }
    
    def disk_info():
        disk = str(psutil.disk_usage('/'))
        return {
            'total'  : round(float(disk.split('total=')[1].split(',')[0])/(1024**3),1),
            'free'   : round(float(disk.split('free=')[1].split(',')[0])/(1024**3),1),
            'percent': float(disk.split('percent=')[1].split(',')[0].strip(')'))
        }
    def get_sys_info(method):
        cpu  = cpu_info()
        mem  = mem_info()
        disk = disk_info()
        if method == 'a':
            return f'————————CPU————————\
                \nCPU使用时间:{cpu["used"]}\
                \n ->系统占用:{cpu["syst"]}\
                \n ->用户占用:{cpu["user"]}\
                \nCPU闲置时间:{cpu["free"]}\
                \nCPU占用率:{cpu["prec"]}%\
                \n————————MEM————————\
                \n总内存:{mem["total"]}GB\
                \n可用内存:{mem["available"]}GB\
                \n内存占用率:{mem["percent"]}%\
                \n————————DISK————————\
                \n磁盘总空间:{disk["total"]}GB\
                \n磁盘可用空间:{disk["free"]}GB\
                \n磁盘占用率:{disk["percent"]}%'
        elif method == 'b':
            return f'CPU占用率:{cpu["prec"]}%\
                \n内存占用率:{mem["percent"]}%\
                \n磁盘占用率:{disk["percent"]}%'

    info = get_sys_info('b')
    await sysinfo.finish(info)

# -*- encoding=utf8 -*-
###############################################
### 浩天遊戲內周邊功能
###############################################

# airtest 大部分api
from importlib.resources import path
from airtest.core.api import *
# 測試報告、log 相關
import logging as log
# Object_Page元素
using(r".\MobileTestRun.air\Object_Page.air")

auto_setup(__file__)

    # 點漢堡排
def Haotian_List():
    wait(Template(r"tpl1654443814185.png"),timeout=100, interval=3)
    touch(Template(r"tpl1654443814185.png", threshold=0.7, target_pos=5, record_pos=(0.412, -0.825), resolution=(720, 1280)))
    log.info("點漢堡排")

# 點背包
def Haotian_Open_Backpack():
    wait(Template(r"tpl1654443935955.png"),timeout=100, interval=1)
    touch(Template(r"tpl1654443935955.png", threshold=0.7, target_pos=5, record_pos=(0.206, -0.507), resolution=(720, 1280)))
    log.info("點背包")

# 使用虛寶卡
def Haotian_Use_itemcard():
    wait(Template(r"tpl1654443970792.png"),timeout=100, interval=2)
    touch(Template(r"tpl1654443970792.png", threshold=0.9, target_pos=5, record_pos=(0.314, -0.467), resolution=(720, 1280)))

# 總贏分大獎動畫 按確認
# 參數:sleep_time = 0為預設 單位秒 讀到有確認按鈕後，要等待幾秒才點擊確認。
def Haotian_Confirm(sleep_time=0):
    wait(Template(r"Screenshot_20220606-150112.png"),timeout=1000, interval=1)
    sleep(sleep_time)
    touch(Template(r"Screenshot_20220606-150112.png", threshold=0.7, target_pos=5, resolution=(720, 1280)))

# 特定遊戲進FG需要按開始
def Haotian_start():
    wait(Template(r"tpl1654942812091.png"),timeout=100, interval=0.5)
    touch(Template(r"tpl1654942812091.png", threshold=0.1, target_pos=5, record_pos=(-0.004, 0.263), resolution=(720, 1280)))
    
# 按停止spin
def Haotian_Stop_Spin():
    wait(Template(r"tpl1654513837215.png"),timeout=100, interval=1)
    touch(Template(r"tpl1654513837215.png", threshold=0.7, target_pos=5, record_pos=(0.378, 0.774), resolution=(720, 1280)))
    
# 回大廳
def Haotian_Back_Home():
    wait(Template(r"tpl1654518337277.png"), timeout=100, interval=3)
    touch(Template(r"tpl1654518337277.png", threshold=0.7, target_pos=5, record_pos=(-0.41, -0.821), resolution=(720, 1280)))
    #, rgb=True
# 換房間
def Haotian_change_gameroom():
    wait(Template(r"tpl1662609115024.png"), timeout=100, interval=2)
    touch(Template(r"tpl1662609115024.png", threshold=0.7, target_pos=5, record_pos=(0.199, 0.136), resolution=(720, 1280)))
    
# 等待遊戲內SPIN開始按鈕出現
def Haotian_SPIN_Start():
    wait(Template(r"tpl1658887244324.png"), timeout=100, interval=3)

# 按spin開始按鈕
def Haotian_SPIN():
    wait(Template(r"tpl1658887244324.png"), timeout=100, interval=3)
    touch(Template(r"tpl1658887244324.png", threshold=0.7, target_pos=5, record_pos=(0.371, 0.779), resolution=(720, 1280)))
    
# 等待押注列表按鈕出現
def Haotian_SPIN_List():
    wait(Template(r"tpl1659419422248.png"), timeout=30000, interval=3)
# record_pos=(-0.368, 0.782), resolution=(720, 1280)
    
# 開啟浩天Debug功能  
def Haotian_debug():
    wait(Template(r"tpl1662132814164.png"), timeout=100, interval=3)
    touch(Template(r"tpl1662132814164.png", record_pos=(-0.135, -0.824), resolution=(720, 1280), target_pos = 1))
    
# debug點生效
def Haotian_debug_run():
    wait(Template(r"tpl1662619664256.png"), timeout=100, interval=3)
    touch(Template(r"tpl1662619664256.png", record_pos=(0.083, 0.731), resolution=(720, 1280), target_pos = 4))
    
# 場景debug    
def Haotian_debug_special_scene():
    wait(Template(r"tpl1662133666731.png"), timeout=100, interval=3)
    touch(Template(r"tpl1662133666731.png", record_pos=(-0.381, -0.268), resolution=(720, 1280), target_pos = 8), times=2)
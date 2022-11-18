# -*- encoding=utf8 -*-
###############################################
# 大廳周邊功能
###############################################

# airtest 大部分api
from importlib.resources import path
from airtest.core.api import *
# 測試報告、log 相關
import logging as log
# Object_Page元素
using(r".\MobileTestRun.air\Object_Page.air")

auto_setup(__file__)

    # 每日簽到
def Daily_Check_in():
    log.info("每日簽到開始")
    #按開始
    wait(Template(r"tpl1653802729073.png"), timeout=100, interval=3)
    touch(Template(r"tpl1653802729073.png", threshold=0.7, target_pos=5, record_pos=(-0.004, 0.322), resolution=(720, 1280)))
    #等轉盤結束後按領取
    wait(Template(r"tpl1653802794907.png"), timeout=100, interval=3)
    touch(Template(r"tpl1653802794907.png", threshold=0.7, target_pos=5, record_pos=(-0.001, 0.565), resolution=(720, 1280)))
    log.info("每日簽到結束")

# 活動中心
def Activity_Center():
    #關閉
    wait(Template(r"tpl1653802985042.png"), timeout=100, interval=3)
    touch(Template(r"tpl1653802985042.png", threshold=0.7, target_pos=5, record_pos=(0.447, -0.835), resolution=(720, 1280)))
    
# 點大icon
def Lobby_Big_Icon():
    # 進蘇洛
    wait(Template(r"tpl1653803010898.png"), timeout=100, interval=3)
    touch(Template(r"tpl1653803010898.png", threshold=0.7, target_pos=5, record_pos=(-0.004, -0.081), resolution=(720, 1280)))
    
# 關閉Debug Error
def Lobby_Close_Debug_Error():
    wait(Template(r"Screenshot_20220606-200009.png"), timeout=100, interval=3)
    touch(Template(r"Screenshot_20220606-200009.png", threshold=0.7, target_pos=5, resolution=(720, 1280)))

# 大廳點背包
def Lobby_Open_Backpack():
    wait(Template(r"tpl1654517877598.png"), timeout=100, interval=3)
    touch(Template(r"tpl1654517877598.png", threshold=0.7, target_pos=5, record_pos=(0.272, -0.807), resolution=(720, 1280)))
    
# 切換道具分頁
def Lobby_Backpack_page_Toggle():
    wait(Template(r"tpl1655170662559.png"), timeout=100, interval=1)
    touch(Template(r"tpl1655170662559.png", threshold=0.7, target_pos=5, record_pos=(-0.075, -0.806), resolution=(720, 1280)))
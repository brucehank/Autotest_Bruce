# -*- encoding=utf8 -*-
__author__ = "Bruce"

# airtest 大部分api
import imp
from importlib.resources import path
from airtest.core.api import *
# 測試報告、log 相關
from airtest.report.report import simple_report
from airtest.core.settings import Settings as ST
from airtest.core.helper import set_logdir
import logging as log
# 檔案處理相關
import os
import sys
# 時間相關
import time
# TestCase 測試案例相關
using(r".\MobileTestRun.air\TestCase\Itemcard_Interrupt.air")
import Itemcard_Interrupt
using(r".\MobileTestRun.air\TestCase\Itemcard_Normal.air")
import Itemcard_Normal
global runtestcase

# 產出測試log
timenow = time.strftime("%Y-%m-%d %H-%M-%S") # 產生當下時間
ST.LOG_FILE = "log.txt"
path = r".\MobileTestRun.air\TestReport"
os.makedirs(path + ".\\" + timenow + ".\log")
set_logdir(r".\MobileTestRun.air\TestReport\\" + timenow + "\log")

# 初始化
auto_setup(__file__)

# 連接夜神模擬器
connect_device("android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP")
dev = device()
print(dev.get_display_info())

# 開角子
start_app("com.gonline.AppBravoCasino")
log.info("開角子APP")

try:
    # 請選擇要使用的腳本:
    runtestcase = Itemcard_Interrupt.Haotian_Use_Itemcard_Interrupt()  # 浩天串接遊戲 虛寶卡 斷補流程
    # runtestcase = Itemcard_Normal.Haotian_Use_itemcard_Normal()   # 浩天串接遊戲 虛寶卡 正常流程

finally:
    # 關角子
    # stop_app("com.gonline.AppBravoCasino")

    # 產出測試報告
    simple_report(__file__ ,logpath=r".\MobileTestRun.air\TestReport\\" + timenow + "\log" ,output=r".\MobileTestRun.air\TestReport\\" + timenow + "\log.html")
    log.info("產出測試報告")
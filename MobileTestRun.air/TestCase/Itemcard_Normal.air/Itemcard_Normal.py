# -*- encoding=utf8 -*-
#####################浩天串接遊戲 虛寶卡 正常流程#########################
# 使用腳本說明:
# 1.起始畫面請從要掛測的串接遊戲內 再開始使用腳本
# 2.背包只能有要測的虛寶卡 不可含有其他道具
# 參數: game_type : 0 slot遊戲
#                   1 柏青遊戲
#       special_scene : 0 關閉特殊場景debug
#                       1 開啟特殊場景debug
#       debug_cmd : 輸入debug代號
#########################################################################

# airtest 大部分api
from airtest.core.api import *
# 測試報告、log 相關
import logging as log
# Test_Action 測試動作
using(r".\MobileTestRun.air\TestAction\LC001.air")
import LC001

auto_setup(__file__)

def Haotian_Use_itemcard_Normal(game_type = 0, special_scene = 0, debug_cmd = ""):
    while(1):
        LC001.Haotian_SPIN_Start()
        
        # 判斷是否需要使用debug功能
        # 判斷是否需要特殊場景
        if special_scene == 1 :
            sleep(2)
            LC001.Haotian_debug()
            LC001.Haotian_debug_special_scene()
            text(debug_cmd, enter=False)
            LC001.Haotian_debug_run()
            LC001.Haotian_SPIN()
            LC001.Haotian_Stop_Spin()
            
        LC001.Haotian_List()
        LC001.Haotian_Open_Backpack()
        sleep(2)
        LC001.Haotian_Use_itemcard()
        LC001.Haotian_Stop_Spin()
        sleep(20)
        LC001.Haotian_SPIN_List()
# -*- coding:utf-8 -*-
import logging as log
from csv import excel
from unicodedata import name
import pytest
import json
import pandas as pd
import datetime

# 讀取Excel 檔案 , 抓取對應的道具名稱
def excel_itemdata(data):
    exceldata = pd.read_excel("item.xlsx", dtype=object , sheet_name="道具表", usecols = "C:D", index_col='Unnamed: 3')
    df = pd.DataFrame(exceldata)
    return df.loc['data','Unnamed: 2']

# 金礦測試
def test_bullion():
    # 開啟 JSON 檔案 , 抓金礦設定資料
    jsondata = json.load(open("bullion.json",encoding="utf-8"))
    gameid = jsondata["activityData"]["ActivityURL"]
    ActivityStartDate = jsondata["activityData"]["StartDate"]

    # 讀取Excel 檔案 , 抓取營運金塊送測資料
    exceldata = pd.read_excel("bullion.xlsx", dtype = object , sheet_name = "4關版", usecols = "C,J:M,O:P")
    df = pd.DataFrame(exceldata)

    # 字串轉換datetime，並將 time -8
    time_del = datetime.timedelta(hours = 8)
    dt = datetime.datetime.strptime(ActivityStartDate,"%Y-%m-%d %H:%M:%S")
    new_dt = dt - time_del

    # 測試活動時間和遊戲名稱
    datetime_index = df.index.values[df["Unnamed: 2"] == new_dt]
    for i in range(len(datetime_index)): # 會有多個同時間活動
        bullion_gameid = df.loc[datetime_index[i]+1,'Unnamed: 2']
        if gameid == bullion_gameid: # 判斷活動時間和遊戲名稱都正確，才進行道具設定測試
            print("活動時間:" + str(ActivityStartDate))
            print("遊戲名稱:" + gameid)
            # 測試關卡、收集數量、一般獎勵、數量、Bouns、數量
            b = 1
            while(df.loc[datetime_index[i]+b,'Unnamed: 9'] != 'NaN'):
                # 測試關卡
                if df.loc[datetime_index[i]+b,'Unnamed: 9'] == jsondata["Awards"][0]["StageNum"][0]:
                    

if __name__ == '__main__':
    test_bullion()
#! /usr/bin/env python
# coding:utf-8

"""
一些常用的方法
"""

import requests
import json
import time
from com import common



class CommonJL():

    def __init__(self):
        # 获取jtoken
        getJtoken = common.Common.get_joken(self)
        getToken = common.Common.get_token(self)
        self.jtoken = str(getJtoken)
        self.token = str(getToken)
        self.mallName = 'Mall' + time.strftime("%Y%m%d%H%M%S", time.localtime())

    def createMall(self):
        # 创建集团下的子商场
        urlCreate = "http://192.168.11.165:30096/usercenter/version-book/org/create/1.0"
        payloadCreate = {"orgType":"1",
                         "orgName":self.mallName,
                         "continent":"1",
                         "country":"7",
                         "province":"9450",
                         "city":"9451",
                         "area":"9454",
                         "pOrgId":"684",
                         "address":"亚洲中国广东广州增城*xx街道xx号"}
        headersCreate = {
            "Accept": "application/json,",
            "Content-Type": "application/json",
            "token": self.token
        }
        requests.post(urlCreate, data=json.dumps(payloadCreate), headers=headersCreate)

    def selectMallList(self):
        # 查询子商场列表
        urlList = "http://192.168.11.165:30096/usercenter/version-book/org/list/1.0"
        payloadList = {"pOrgId":"684","orgType":"","orgName":"","reqPageNum":1,"maxResults":10}
        headersList = {
            "Accept": "application/json,",
            "Content-Type": "application/json",
            "token": self.token
        }
        r_list = requests.post(urlList, data=json.dumps(payloadList), headers=headersList)
        r_list_json = r_list.json()
        self.orgID = r_list_json['data'][0]['id']  #列表中第一个子商场的orgID
        return self.orgID

    def selectBusinissSettingList(self):
        # 查询30055业务设置列表
        urlList = "http://192.168.11.165:30076/version-book/back/bussinesssetting/list/1.0"
        payloadList = {"orgType": "", "status": "", "orgName": "", "orgId": "", "reqPageNum": 1, "maxResults": 10}
        headersList = {
            "Accept": "application/json,",
            "Content-Type": "application/json",
            "jtoken": self.jtoken
        }
        r_list = requests.post(urlList, data=json.dumps(payloadList), headers=headersList)
        r_list_json = r_list.json()
        self.ID = r_list_json['data'][0]['id']  # 列表中第一个子商场的orgID
        return self.ID

    def openBusiness(self):
        # 开启业务

        url = "http://192.168.11.165:30076/version-book/back/bussinesssetting/open/1.0"
        payload  = {"startTime":"2019-08-15",
                    "endTime":"2022-08-14",
                    "imageStoreTime":3,
                    "status":0,
                    "passengersAdjust":1,
                    "openedBussinessSet":"0,1,2,3,4,5,6,7,8,9",
                    "imageExpireTime":"2019-11-15",
                    "orgId":self.orgID,
                    "id":""}
        headers = {
            "Content-Type": "application/json",
            "jtoken": self.jtoken,
            "token": "Bearer"
        }
        requests.post(url, data=json.dumps(payload), headers=headers)

#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
常用通用方法封装
"""
import base64,requests
from com import readConfig
from com.log import MyLog

log = MyLog()


class Common(object):
    def __init__(self):
        pass
    @staticmethod
    def image_encode64(path):
        with open(path, "rb") as f:
            base64_data = base64.b64encode(f.read())
            return base64_data.decode()

    # def get_token(self, url = "", username = "", password = ""):
    #     headers = {}
    #     payload = {}
    #     res = requests.get(url)
    #     log.debug("get token message: %s" %res.text)
    #     return res

    def get_token(self):
        tokenURL = readConfig.ReadBaseConfig().get_http_config('baseurl_user') + "/custom-user-dashboard-backend/auth/login"

        payload = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
        headers = {'Content-Type': "application/json"}
        response = requests.request("POST", tokenURL, json=payload, headers=headers)
        # log.debug("get token message: %s" % response.text)  #下次注释掉
        # print(response.cookies.items()[0][1])
        # print(type(response.cookies))
        token = 'Bearer ' + str(response.cookies.items()[0][1])
        return token



if __name__ == "__main__":
    pass
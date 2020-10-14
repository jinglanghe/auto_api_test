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

    def get_jtoken(self):
        url = readConfig.ReadBaseConfig().get_http_config('baseurl') + "/login"
        payload = "username=superuser&password=e10adc3949ba59abbe56e057f20f883e&grant_type=password&scope=read%20write"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        jtokenString = response.json()['data']['jtoken']
        jtoken = 'Bearer ' + jtokenString
        return jtoken

    def get_token(self):
        tokenURL = readConfig.ReadBaseConfig().get_http_config('baseurl_user') + "/authority/oauth/token"

        payload = "username=ylzx&password=e10adc3949ba59abbe56e057f20f883e&grant_type=password&scope=read%20write"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = requests.request("POST", tokenURL, data=payload, headers=headers)
        # log.debug("get token message: %s" % response.text)  #下次注释掉
        token = 'Bearer ' + str(response.json()['access_token'])
        return token



if __name__ == "__main__":
    pass
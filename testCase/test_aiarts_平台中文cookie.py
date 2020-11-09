
#! /usr/bin/env python
# coding:utf-8

"""
平台中文cookie
"""

import requests
import time
import unittest
from testCase import aiarts as aiarts
from com import readConfig
sr = aiarts.SaveResult()


class Token(unittest.TestCase):
    def setUp(self):
        self._flag = "pass"
        print("this is setup")



    # 平台中文cookie
    def test_aiarts_caseID_5(self):
        # 获取token
        with open('./token.txt', 'r') as f:
            _token = f.read()

        # print(_token)

        _expected_result = None

        url = readConfig.ReadBaseConfig().get_http_config('baseurl_user') + "/custom-user-dashboard-backend/language/zh-CN"

        headers = {"Content-Type": "application/json","Authorization":_token}

        r = requests.get(url, headers=headers)
        print(r, r.content)
        r_time = float(r.elapsed.microseconds)/1000

        time.sleep(1)
        # r_json = r.json()
        # print("r_json {}".format(r_json))

        r_status = r.status_code
        cookies_language = requests.utils.dict_from_cookiejar(r.cookies)['language']
        if r_status != 200:
            self._flag = "fail"


        datas = [url, "平台中文cookie", str(' '), str('no response json'), "status=200", ' ', ' ', self._flag, r_time]
        sr.save_result(datas)

        self.assertEqual(cookies_language, 'zh-CN', msg="返回的cookie语言配置不是zh-CN")

        

if __name__ == "__main__":
    unittest.main()
                        
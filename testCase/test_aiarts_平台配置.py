# ! /usr/bin/env python
# coding:utf-8

"""
平台配置
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

    # 平台配置
    def test_aiarts_caseID_4(self):
        # 获取token
        with open('./token.txt', 'r') as f:
            _token = f.read()

        # print(_token)

        _expected_result = None
        respCode_input = readConfig.ReadBaseConfig().get_api_config('response_status_ok')

        url = readConfig.ReadBaseConfig().get_http_config(
            'baseurl_user') + "/custom-user-dashboard-backend/platform-config"

        headers = {"Content-Type": "application/json", "Authorization": _token}

        r = requests.get(url, headers=headers)
        print(r, r.content)
        r_time = float(r.elapsed.microseconds) / 1000

        time.sleep(1)
        r_json = r.json()
        print("r_json {}".format(r_json))

        r_status = r.status_code
        r_resp_code = str(r_json["success"]).lower()
        if r_resp_code != respCode_input or r_status != 200:
            self._flag = "fail"

        if 'i18n' not in r_json:
            self._flag = "fail"

        if 'platformName' not in r_json:
            self._flag = "fail"

        datas = [url, "平台配置", str(' '), str(r_json),
                 "resp_code=" + str(respCode_input) + "\nstatus=200", ' ', ' ', self._flag, r_time]
        sr.save_result(datas)

        self.assertEqual(r_resp_code, respCode_input, msg="返回的状态码不等于" + str(respCode_input) + "\n" + str(r_json))
        self.assertIsNotNone(r_json['i18n'], msg="i18n语言配置项为空")
        self.assertIsNotNone(r_json['platformName'], msg="平台名称配置项为空")


if __name__ == "__main__":
    unittest.main()

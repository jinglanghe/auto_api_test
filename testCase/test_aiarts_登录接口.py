
#! /usr/bin/env python
# coding:utf-8

"""
登录接口
"""

import requests
import json
import time
import datetime
from datetime import timedelta
import unittest
import uuid
import random
from testCase import aiarts as aiarts
from com import common
from com import configDB
from com import readConfig
sr = aiarts.SaveResult()


class Token(unittest.TestCase):
    def setUp(self):
        self._flag = "pass"
        print("this is setup")



    # 登录接口
    def test_aiarts_caseID_1(self):
        # 获取token
        gettoken = common.Common.get_token(self)
        _token = str(gettoken)
        
        # 一些可能用到的变量
        _randString = str(uuid.uuid4())[-8:]  
        _randInt = random.randint(0,100)
        today_date = datetime.date.today()
        _today = str(datetime.date.today())
        _yesterday = str(today_date - datetime.timedelta(days=1))
        _8DaysAgo = str(today_date - datetime.timedelta(days=8))
        _lastWeekStart = str(today_date - timedelta(days=today_date.weekday() + 7))
        _lastWeekEnd = str(today_date - timedelta(days=today_date.weekday() + 1))
        
        this_month_start = datetime.datetime(today_date.year, today_date.month, 1)
        last_month_end = (this_month_start - timedelta(days=1)).date()
        last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1).date()

        _lastMonthStart = str(last_month_start)
        _lastMonthEnd = str(last_month_end)
        
        _expected_result = None
        respCode_input = 'true'.lower()
        
        key_sql = None
        if key_sql == "null" or key_sql ==None:
            pass
        else: 
            db_key = configDB.MysqlHelper()
            key_sql_run_result = db_key.get_all(key_sql)
            _key = str(key_sql_run_result[0][0])
        # 一些可能用到的变量
        
        url = readConfig.ReadBaseConfig().get_http_config('baseurl_user') + "/custom-user-dashboard-backend/auth/login"
        if '_key' in url:
            url = url.replace('_key','') + _key
        payload  = {
    "userName": "admin",
    "password": "e10adc3949ba59abbe56e057f20f883e"
}
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print(r, r.content)
        r_time = float(r.elapsed.microseconds)/1000

        time.sleep(1)
        r_json = r.json()
        print("r_json {}".format(r_json))

        r_status = r.status_code
        r_resp_code = str(r_json["success"]).lower()
        if r_resp_code != respCode_input or r_status != 200:
            self._flag = "fail"
        
        sql = "null"
        json_key = None
        if sql == 'null' or sql == None:
            sql_judge = 'null'
            api_judge = 'null'
            _expected_result = 'null'
        else:
            api_judge = str(r_jsonNone)
            db_test = configDB.MysqlHelper()
            sql_run_result = db_test.get_all(sql)
            
            if len(sql_run_result) == 0:
                    sql_judge = 'SQL查询为空'
            else:
                sql_judge = str(sql_run_result[0][0])
                    
            if json_key != "null" or json_key != None: 
 
                if sql_judge != api_judge:
                    self._flag = "fail"
                if sql_judge != _expected_result:
                    self._flag = "fail"
            
            if json_key == "null" or json_key == None:
                if sql_judge != _expected_result:
                    self._flag = "fail"    
                    
        
        datas = [url, "登录接口", str(payload), str(r_json), 
        "resp_code="+ str(respCode_input)+ "\nstatus=200", sql_judge, api_judge, self._flag, r_time]
        sr.save_result(datas)
        
        self.assertEqual(r_resp_code, respCode_input, msg="返回的状态码不等于"+str(respCode_input)+"\n"+str(r_json))
        self.assertEqual(_expected_result, sql_judge, msg="Excel填写的预期结果为："+_expected_result+",与SQL查询结果“"+sql_judge+"”不一致。")
        self.assertEqual(api_judge, sql_judge, msg="接口返回结果为："+api_judge+",与SQL查询结果“"+sql_judge+"”不一致。")
        

    if __name__ == "__main__":
        unittest.main()                    
                        
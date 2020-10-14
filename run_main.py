#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import datetime
import unittest
from dateutil import tz
from com import HTMLTestRunner, readConfig
from com.log import MyLog as Log
from com.tools import create_py_file, delete_py_file
"""
执行器
"""

log = Log()


class RunMain(object):

    def __init__(self):
        self.case_list = []
        self.case_list_file = "caselist.txt"
        self.result_path = os.path.join(readConfig.pro_dir, "testResult")
        if not os.path.isdir(self.result_path):
            try:
                os.mkdir(self.result_path)
            except Exception as e:
                log.error("create result folder fail, error message is: %s" % str(e))
        self.tz_sh = tz.gettz('Asia/Shanghai')
        self.result_file = os.path.join(self.result_path, datetime.datetime.now(tz=self.tz_sh).strftime('%Y-%m-%d_%H_%M_%S-result.html'))
        # self.result_file = os.path.join(self.result_path, 'result.html')
        # 保存当前时间作为结果sheet名
        self.result_sheet_name = datetime.datetime.now(tz=self.tz_sh).strftime("%Y-%m-%d %H-%M-%S")
        with open("sheet_name", "w") as f:
            f.write(self.result_sheet_name)

    def set_case_list(self):
        with open(self.case_list_file, "r", encoding="utf-8") as f:
            for value in f.readlines():
                data = str(value)
                if data != '' and not data.startswith("#"):
                    self.case_list.append(data.replace('\n', ''))

    def set_case_suite(self):
        self.set_case_list()
        print("case_list %s" % self.case_list)
        test_suite = unittest.TestSuite()
        suite_model = []
        for case in self.case_list:
            case_str = case.split('/')
            case_name = case_str[-1]
            case_file = os.path.join(readConfig.pro_dir, "testCase/" + "/".join(case_str[:-1]))
            print(case_name + '.py')
            discover = unittest.defaultTestLoader.discover(case_file, pattern=case_name + '.py', top_level_dir=None)
            suite_model.append(discover)

        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suite = self.set_case_suite()
            if suite is not None:
                log.info("********TEST START********")
                fp = open(self.result_file, 'wb+')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Vesionbook-Mall Test Report", description="Vesionbook-Mall Test Report")
                runner.run(suite)
                fp.close()
                return True
            else:
                log.info("have no case to test")
                pass
        except Exception as e:
            log.error(str(e))

        finally:
            log.info("********TEST END********")
            # os.remove("sheet_name")

    def prepare_test(self):
        self.read_caselist = readConfig.ReadBaseConfig().get_text_config("caselist")
        with open(self.read_caselist, 'w', encoding='utf-8') as f:
            f.write("")

        self.read_case_excel = readConfig.ReadBaseConfig().get_text_config("case_excel")
        create_testcases = create_py_file.Operate_excel(self.read_case_excel)
        create_testcases.read_excel_all_row()

    def delete_test(self):
        self.delete = delete_py_file.Delete_py_file().delete_filelist("./testCase")

if __name__ == "__main__":

    RunMain().prepare_test()
    # RunMain().run()
    # RunMain().delete_test()


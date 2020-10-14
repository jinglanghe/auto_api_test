#!usr/bin/python
# -*-coding: UTF-8 -*-
import os
import datetime
import logging
from com import readConfig

pro_dir = readConfig.pro_dir


class MyLog(object):
    def __init__(self, basedir=None, name=None):
        # 获取当前目录
        if basedir:
            self.basedir = basedir
        else:
            self.basedir = pro_dir

        if not self.basedir.endswith("/"):
            # linux目录最后要加/
            self.basedir += "/"

        # 创建日志目录
        self.log_dir = os.path.join(self.basedir,"logs")
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # 获取当前文件的名字,去掉后缀
        if name:
            self.name = name
        else:
            # 获取当前日期
            self.today = datetime.date.today()
            self.today = str(self.today).replace("-", "")
            self.name = "%s_%s.log" % (os.path.splitext(os.path.split(os.path.realpath(__file__))[1])[0], self.today)

        # 创建日志文件
        self.logName = os.path.join(self.log_dir, self.name)
        # 先删除日志文件,注意:只会删除文件
        # try:
        #     os.remove(self.logName)
        # except Exception as e:
        #     print('删除出现异常,错误信息:')
        #     print(e)
        # else:
        #     print('删除成功')

        # 调用自己的loger方法
        self.loger()

    # 设置相应的日志格式
    def loger(self):
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        print('-----------------------')
        # print(self.logger)
        # print(self.logger.level)
        format = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
        # print(format)
        myStreamHandler = logging.StreamHandler()
        # print(myStreamHandler)
        myStreamHandler.setFormatter(format)
        # print(myStreamHandler)
        print("logname %s" % self.logName)
        myFileHandler = logging.FileHandler(self.logName)
        # print(myFileHandler)
        myFileHandler.setFormatter(format)
        self.logger.addHandler(myFileHandler)
        self.logger.addHandler(myStreamHandler)
        # print(self.logger)
        """
        <logging.Logger object at 0x0000000001F39AC8>
        10
        <logging.Formatter object at 0x00000000021E8E80>
        <logging.StreamHandler object at 0x00000000026D9940>
        <logging.StreamHandler object at 0x00000000026BA908>
        <logging.FileHandler object at 0x00000000026EA860>


        <logging.Logger object at 0x0000000002638E48>
        """

    def info(self, text):
        return self.logger.info(text)

    def debug(self, text):
        return self.logger.debug(text)

    def warning(self, text):
        return self.logger.warning(text)

    def error(self, text):
        return self.logger.error(text)


if __name__ == '__main__':
    mylog = MyLog()
    print(mylog.basedir)
    print(mylog.log_dir)
    print(mylog.name)
    print(mylog.today)
    print(mylog.logName)

    mylog.info("nihhao")
    mylog.debug('呵呵')
    mylog.warning('注意身体')
    mylog.error('hello')

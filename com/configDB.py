#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
对mysql数据库操作封装
使用pymysql模块
"""
import pymysql

from com import readConfig
from com.readConfig import ReadBaseConfig
from com.log import MyLog as Log

pro_dir = readConfig.pro_dir
log = Log(basedir=pro_dir,name="mysql_helper.log")
base_config = ReadBaseConfig()

class MysqlHelper(object):

    def __init__(self, host = None, username = None, password = None, database = None, port = None):
        if host is None:
            host = base_config.get_db_config(name="host")
        if username is None:
            username = base_config.get_db_config(name="username")
        if password is None:
            password = base_config.get_db_config(name="password")
        # if database is None:
        #     database = base_config.get_db_config(name="database")
        if port is None:
            port = base_config.get_db_config(name="port")

        self.config = {
            'host':str(host),
            'user':username,
            'passwd':password,
            'port':int(port),
            # 'db':database
        }

        self.__conn = self.build_conn()
        self.__cursor = self.__conn.cursor()

    @property
    def conn(self):
        return self.__conn

    def build_conn(self):
        try:
            self.db = pymysql.connect(**self.config)
            log.debug("connect mysql success!")
            return self.db
        except ConnectionError as ex:
            log.error("connect mysql error,the error message is: %s" %str(ex))

    def get_all(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def close(self):
        self.db.close()
        log.info("close db success!")

if __name__ == "__main__":
    mysql = MysqlHelper()
    sql = "select * from t_person limit 10"
    try:
        d = mysql.get_all(sql)
        print(d)
    except Exception as e:
        print(e)
    finally:
        mysql.close()

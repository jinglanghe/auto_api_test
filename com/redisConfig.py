# -*- coding:utf-8 -*-
#! /usr/bin/env python

import redis
from com.readConfig import ReadBaseConfig
from com import readConfig
from com.log import MyLog as Log

pro_dir = readConfig.pro_dir
log = Log(basedir=pro_dir, name="redis_config.log")
base_config = ReadBaseConfig()
redis_host = base_config.get_redis_config(name="host")
redis_port = base_config.get_redis_config(name="port")
redis_passwd = base_config.get_redis_config(name="password")


class RedisHelper(object):
    def __init__(self, host=redis_host, port=redis_port, password=redis_passwd, db=0):
        self.config = {
            "host": host,
            "port": port,
            "password": password,
            "db": db
        }
        self.__conn = self.build_conn()

    @property
    def conn(self):
        return self.__conn

    def build_conn(self):
        try:
            self.rd = redis.Redis(**self.config)
            log.info("connect redis success!")
            return self.rd
        except Exception as e:
            log.error("connect redis fail,the error message is %s" % str(e))

    def get(self, name):
        return self.rd.get(name)


if __name__ == "__main__":
    r1 = RedisHelper(db=1)
    print(r1.get("86479303000129MN_1009_10"))

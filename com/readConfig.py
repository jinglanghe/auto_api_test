# coding=utf-8

import os
import codecs
import configparser

current_dir = os.path.dirname(__file__)
pro_dir = os.path.dirname(current_dir)
base_config_path = os.path.join(pro_dir, "init/baseConfig.ini")
base_config_path = base_config_path.replace('\\', '/')


class ReadBaseConfig(object):

    def __init__(self):
        with open(base_config_path, 'r', encoding='utf-8') as f:
            data = f.read()
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                with codecs.open(base_config_path, encoding='utf-8') as cf:
                    cf.write(data)

        self.cf = configparser.ConfigParser()
        self.cf.read(base_config_path, encoding='utf-8')

    def get_mail_config(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_db_config(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_http_config(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_image_config(self, name):
        value = self.cf.get("IMAGE", name)
        return value

    def get_redis_config(self, name):
        value = self.cf.get("REDIS", name)
        return value

    def get_text_config(self, name):
        value = self.cf.get("TEXT", name)
        return value


if __name__ == "__main__":
    rbc = ReadBaseConfig()
    print("host: %s" % rbc.get_db_config("host"))

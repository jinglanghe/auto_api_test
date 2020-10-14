# -*-coding:utf-8 -*-
#! /usr/bin/env python
import os


class Delete_py_file(object):
    def __init__(self):
        pass


    def delete_filelist(self, filepath):
        self.file_list = []
        for home, dirs, files in os.walk(filepath):
            for filename in files:
                # 文件名列表，包含完整路径
                if 'test_' in filename:
                    if '.pyc' not in filename:
                        self.file_list.append(os.path.join(home, filename))
        for i in self.file_list:
            os.remove(i)

if __name__ == "__main__":
    Delete_py_file().delete_filelist('../../testCase')
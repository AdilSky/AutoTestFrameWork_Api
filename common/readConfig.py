# FileName : ReadConfig.py
# Author   : Adil
# DateTime : 2018/4/20 14:43
# SoftWare : PyCharm

import configparser
import os

commonPath = os.path.split(os.path.realpath(__file__))[0]
# 获取common 上级目录
rootPath = os.path.abspath(os.path.join(commonPath,'..'))
# 获取 config 目录
configPath = os.path.join(rootPath,'config')
configFile = os.path.join(configPath,'baseConfig.ini')


class ReadConfig(object):
    '''创建读取config.ini配置文件的公共类'''

    def __init__(self):
        '''构造函数-初始化基本信息'''
        self.rootPath = rootPath
        self.configFile = configFile

        # 实例化 cf
        self.cf = configparser.ConfigParser()
        # 处理配置文件中含中文字符的问题 ，UnicodeDecodeError: 'gbk' codec can't decode bytes in position 243-244: illegal multibyte sequence
        print(self.cf)
        self.cf.read(self.configFile, encoding="utf-8-sig")

    def getMail(self,name):

        value =  self.cf.get('EMAIL',name)

        return value

    def getDB(self,name):

        value = self.cf.get('DB',name)

        return value
    def getHTTP(self,name):
        value = self.cf.get('HTTP',name)
        return value

    def getUserInfo(self,name):
        value = self.cf.get('UserInfo',name)
        return value

# 测试方法

# if __name__ == '__main__':
#
#     rc = ReadConfig()
#
#     print (rc.getHTTP('host'))






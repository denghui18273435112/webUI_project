# coding=utf-8
from config.Conf import ConfigYaml

import json
import  re

from utils.AssertUitl import AssertUitl
import subprocess

from config import Conf
import os
import datetime
import time
from datetime import  datetime








def allure_report(report_path,report_html):
    """
    自动生成allure 报告
    :param report_path: pytest.main运行 生成文件的存放位置
    :param report_html: allure生成报告存放位置
    :return:
    """
    allure_cmd ="allure generate %s -o %s --clean"%(report_path,report_html)
    try:
        subprocess.call(allure_cmd,shell=True)

    except:
        raise



def report_path():

    #return  Conf.get_report_path()+os.sep+"{}-result".format(str(datetime.now().strftime("%Y%m%d%H%M")))  #本地生成报告
    return  Conf.get_report_path()+os.sep+"result"  ##jenkins生成报告

def report_html_path():
    #return Conf.get_report_path()+os.sep+"{}--html".format(str(datetime.now().strftime("%Y%m%d%H%M")))  #本地生成报告
    return Conf.get_report_path()+os.sep+"html" ##jenkins生成报告

if __name__ == '__main__':
    pass

    #print(init_db("db_1"))
    # print(res_find( '{"Authorization": "JWT ${token}$"}'))
    # print(res_sub( '{"Authorization": "JWT ${token}$"}',"123"))


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

from utils.MysqlUitl import Mysql



def init_db(db_alias='db_1'):
    """
    :param db_alias: # 默认db_1  数据库
    :return: sql的光标对象
    """
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host  = db_info["db_host"]
    user  = db_info["db_user"]
    password  = db_info["db_password"]
    database  = db_info["db_database"]
    port  = int(db_info["db_port"])
    charse  = db_info["db_charset"]
    conn =  Mysql(host,user,password,database,port,charse)
    return  conn



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

def assert_db(db_name,result,db_verify):
    """
    数据库比较
    :param db_name:  数据库名称
    :param result:  返回的结果 body
    :param db_verify: sql语句
    :return:
    """
    assert_util =  AssertUitl()
    #sql = init_db("db_1")
    sql = init_db(db_name)
    # 2、查询sql，excel定义好的
    db_res = sql.fetchone(db_verify)

    #log.debug("数据库查询结果：{}".format(str(db_res)))
    # 3、数据库的结果与接口返回的结果验证
    # 获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    # 根据key获取数据库结果，接口结果
    for line in verify_list:
        #res_line = res["body"][line]
        res_line = result[line]
        res_db_line = dict(db_res)[line]
        # 验证
        assert_util.assert_body(res_line, res_db_line)

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


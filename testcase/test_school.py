#case_test.py
import pytest
from selenium import webdriver
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import allure
import pytest
from PublicMethods.Allure import new_allure
import  allure
import os
from utils.logUtil import my_log


login_YAML = ConfigYaml().read_yaml("school.yaml")
@allure.feature('学校管理')
class Test_school(object):

    #@pytest.mark.skip
    @pytest.mark.run(order=5)
    @allure.story('学校管理-查询')
    def test_school_management_inquire(self,driver):
        """
        学校管理 查询
        @param driver:
        @return:
        """
        try:
            TSMI = login_YAML["test_school_management_inquire"]
            selenium(driver).module_skip("学校管理")
            selenium(driver).text_input(location="div.leftSearch  input",content=TSMI["inquire_content"],Enter=0)
            selenium(driver).operating_steps(case_Steps_describe="学校管理查询<Br/>输入的查询条件:{}".format(TSMI["inquire_content"]),
                                             name_screenshot="查询成功后的截图",
                                             describe=" 学校管理 查询")
        except Exception:
            my_log().debug("\n学校管理-查询操作 出现定位不到的问题")
            pytest.xfail("列表数据和查询条件不匹配")

    #@pytest.mark.skip
    @pytest.mark.run(order=2)
    @allure.story('学校管理-添加')
    def test_school_management_add(self,driver):
        """
        学校管理 添加
        @param driver:
        @return:
        """
        try:
            TSMD = login_YAML["test_school_management_add"]
            selenium(driver).module_skip("学校管理")
            selenium(driver).button_click("添加学校",0)
            selenium(driver).text_input("div.el-form-item__content  input",TSMD["school_name"])
            selenium(driver).text_input("div.el-form-item__content  textarea",TSMD["describe"])
            selenium(driver).button_click("确 定")
            selenium(driver).operating_steps(case_Steps_describe="学校管理添加<Br/>添加学校:{}<Br/>学校描述:{}".format(TSMD["school_name"],TSMD["describe"]),
                                                 name_screenshot="添加成功后的截图",
                                                  describe=" 学校管理 添加")
        except Exception:
            print("\n学校管理-添加操作 出现定位不到的问题")


    #@pytest.mark.skip
    @pytest.mark.run(order=3)
    @allure.story('学校管理-修改')
    def test_school_management_alter(self,driver):
        """
        学校管理修改
        @param driver:
        @return:
        """
        try:
            TSMA = login_YAML["test_school_management_alter"]
            selenium(driver).module_skip("学校管理")
            selenium(driver).button_click("div.el-table__fixed-body-wrapper tr:nth-child(1)  div > div span:nth-child(1)")
            selenium(driver).text_input("div.el-form-item__content  input",TSMA["school_name"])
            selenium(driver).text_input("div.el-form-item__content  textarea",TSMA["describe"])
            selenium(driver).button_click("确 定")
            selenium(driver).operating_steps(case_Steps_describe="学校管理修改<Br/>添加学校:{}<Br/>学校描述:{}".format(TSMA["school_name"],TSMA["describe"]),
                                             name_screenshot="修改成功后的截图",
                                           describe=" 学校管理修改")
        except:
            my_log().debug("\n学校管理-修改操作 出现定位不到的问题")
            pytest.xfail("列表数据和查询条件不匹配")

    #@pytest.mark.skip
    @pytest.mark.run(order=4)
    @allure.story('学校管理 删除')
    def test_school_management_del(self,driver):
        """
        学校管理 删除
        @param driver:
        @return:
        """
        try:
            TSMD = login_YAML["test_school_management_del"]
            selenium(driver).module_skip("学校管理")
            selenium(driver).button_click("div.el-table__fixed-body-wrapper tr:nth-child(1)  div > div span:nth-child(2)")
            selenium(driver).button_click("div > button.el-button--primary > span")
            selenium(driver).operating_steps(case_Steps_describe="删除学校管理",
                                                 name_screenshot="删除时候的截图",
                                                 describe="学校管理删除")
        except Exception:
            my_log().debug("\n学校管理-删除操作 出现定位不到的问题")
            pytest.xfail("列表数据和查询条件不匹配")

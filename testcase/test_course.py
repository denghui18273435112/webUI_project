import pytest
from selenium import webdriver
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

login_YAML = ConfigYaml().read_yaml("login.yaml")
@pytest.mark.usefixtures("driver")  #不用声明引入conftest.py中的driver方法
class Test_course(object):

     #@pytest.mark.skip   #遇到pytest.mark.skip声明的方法一直跳过
    def test_Course_center(self,driver):
        """
        @param driver:
        @return:
        """
        selenium(driver).location_name("配课中心")
        selenium(driver).location_name("课程管理")
        selenium(driver).FEBCS_C("div.rightSearch  button.el-button > span")
        selenium(driver).FEBCS_CCSK("div:nth-child(2)    input[placeholder=请输入课程标题]","学校")
        #selenium(driver).FEBCS_CVT("div:nth-child(2)    input[placeholder=请选择课程类型]","1")
        print("\n 第三个用例结束")
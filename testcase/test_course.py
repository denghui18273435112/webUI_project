import pytest
from selenium import webdriver
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

login_YAML = ConfigYaml().read_yaml("login.yaml")
@pytest.mark.usefixtures("driver")  #不用声明引入conftest.py中的driver方法
class Test_course(object):

     #@pytest.mark.skip   #遇到pytest.mark.skip声明的方法一直跳过
    def test_Course_center_add(self,driver):
        """
        添加课程数据
        @param driver:
        @return:
        """
        selenium(driver).location_name("配课中心")
        selenium(driver).location_name("课程管理")
        selenium(driver).FEBCS_C("div.rightSearch  button.el-button > span")

        #课程信息
        selenium(driver).FEBCS_CCSK("div:nth-child(2)    input[placeholder=请输入课程标题]","学校")
        #selenium(driver).FEBCS_CC("div:nth-child(2) input[placeholder=请选择课程类型]","必修")
        selenium(driver).FEBCS_CCSK("div:nth-child(5)  input.el-input__inner","标签")

        #设计课程目标
        selenium(driver).FEBCS_CCSK("div:nth-child(7)  div:nth-child(1) > div > div > input","4")
        selenium(driver).FEBCS_CCSK("div:nth-child(7)  div:nth-child(2) > div > div > input","20")
        selenium(driver).FEBCS_CCSK("div:nth-child(8)  div:nth-child(1) > div > div > input","4")
        selenium(driver).FEBCS_CCSK("div:nth-child(8)  div:nth-child(2) > div > div > input","20")
        selenium(driver).FEBCS_CCSK("div:nth-child(9)  div:nth-child(1) > div > div > input","4")
        selenium(driver).FEBCS_CCSK("div:nth-child(9)  div:nth-child(2) > div > div > input","20")
        selenium(driver).FEBCS_CCSK("div:nth-child(10)  div:nth-child(1) > div > div > input","40")
        selenium(driver).FEBCS_CCSK(" input[placeholder=选择日期]","2020-09-03")
        #selenium(driver).FEBCS_CC("input[placeholder=请选择试卷]","其它")
        selenium(driver).FEBCS_C("div:nth-child(13)  label:nth-child(1) > span > span")
        selenium(driver).FEBCS_C("div:nth-child(14)  label:nth-child(2) > span> span")

        #上传文件F:\banner.png
        selenium(driver).send_keys("div:nth-child(16) button","F:\\banner.png")
        os.system()

        time.sleep(5)
        print("\n 第一个用例结束:添加课程")


if __name__ == "__main__":
     pytest.main(['-s','-r','--verbose','Test_course.py'])
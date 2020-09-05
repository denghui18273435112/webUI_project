import pytest
from selenium import webdriver
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
from win32 import win32gui
from PublicMethods.WinUpLoadFile import upload_files


login_YAML = ConfigYaml().read_yaml("login.yaml")
@pytest.mark.usefixtures("driver")  #不用声明引入conftest.py中的driver方法
@allure.feature('课程管理')
class Test_course(object):

     #@pytest.mark.skip   #遇到pytest.mark.skip声明的方法一直跳过
    @allure.story('课程添加')
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
        selenium(driver).FEBCS_CCSK("div:nth-child(2)    input[placeholder=请输入课程标题]","学校22")
        selenium(driver).FEBCS_pull_down_choose(" input[placeholder=请选择课程类型]","必修")
        selenium(driver).FEBCS_CCSK("div.contentWrapperOne  div:nth-child(4)  input","10")
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
        selenium(driver).FEBCS_pull_down_choose("input[placeholder=请选择试卷]","课程试卷")
        selenium(driver).FEBCS_C("div:nth-child(13)  label:nth-child(1) > span > span")
        selenium(driver).FEBCS_C("div:nth-child(14)  label:nth-child(2) > span> span")

        #设置相关图片
        selenium(driver).FEBXP_C(button_name="上传封面")
        upload_files("banner.png")
        time.sleep(1)
        selenium(driver).FEBXP_C(button_name="上传banner图")
        upload_files("banner.png")
        time.sleep(1)

        #设置课程简介
        selenium(driver).roll()
        selenium(driver).editor_upload_photo()
        #点击下一步按钮
        selenium(driver).FEBCS_C("div.actions  button.zzlPrimary  span")

        #课程目录页面
        y = ["第1章","第2章","第3章","第4章"]
        for x in y:
            time.sleep(1)
            selenium(driver).FEBCS_C("div.left span:nth-child(1) svg")
            time.sleep(0.5)
            selenium(driver).FEBCS_CCSK("input[placeholder=请输入章的名称]",x)
            selenium(driver).FEBCS_C("body > div.el-dialog__wrapper   button.el-button.zzlPrimary  span")

        t = [3,4,5,6]
        for tt in t:
            selenium(driver).FEBCS_C(" div:nth-child({0}) > div.item  span.select".format(str(tt)))
            selenium(driver).FEBCS_C("span:nth-child(2) > svg")
            selenium(driver).FEBCS_pull_down_choose("input[placeholder=请选择题库类型]","图片")
            selenium(driver).FEBCS_pull_down_choose("input[placeholder=请选择资源分类]","名胜古迹")
            selenium(driver).FEBCS_C("div.el-dialog__body  button > span")
            upload_files("banner.png")
            time.sleep(1)
        #点击下一步按钮
        selenium(driver).FEBCS_C("div.actions  button.zzlPrimary  span")


        #课程测验
        for ttt in [2,3,4,5]:
            selenium(driver).FEBCS_C("div.contentWrapper  div.contentWrapperThree div:nth-child({0}) > div.subItemBox  span.wrapperOne".format(ttt))
            selenium(driver).FEBCS_C("div.buttons   div > button > span")
            upload_files(filePath="kaoshi.xlsx")

        #点击下一步按钮
        selenium(driver).FEBCS_C("div.actions  button.zzlPrimary  span")


        #添加讨论
        for xx in [2,3,4,5]:
            selenium(driver).FEBCS_C("div.contentWrapperFour  div:nth-child({0})  div.subItemBox  span.name".format(xx))
            selenium(driver).FEBXP_C(button_name="添加讨论")
            selenium(driver).FEBCS_CCSK("div:nth-child(1)  textarea","名胜古迹")
            selenium(driver).upload_photo(" div:nth-child(2) > div > div > i")
            driver.find_elements_by_css_selector("div button.confirmButton span")[4].click()
        selenium(driver).FEBXP_C(button_name="提交")


        print("\n 第一个用例结束:添加课程")










if __name__ == "__main__":
     pytest.main(['-s','-r','--verbose','Test_course.py'])
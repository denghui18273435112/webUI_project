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
        selenium(driver).FEBCS_pull_down_choose("input[placeholder=请选择试卷]","测试1")
        selenium(driver).FEBCS_C("div:nth-child(13)  label:nth-child(1) > span > span")
        selenium(driver).FEBCS_C("div:nth-child(14)  label:nth-child(2) > span> span")

        #上传文件F:\banner.png
        selenium(driver).send_keys("div:nth-child(16) button","F:\\banner.png")
        os.system()
        dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口  ‘打开窗口’
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)  # 四级
        button = win32gui.FindWindowEx(dialog, 0, "Button", None)  # 四级
        # 往文件名编辑框中输入文件路径
        # 上传操作
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, "E:\\1.jpg")  # 放入上传文件的绝对路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

        time.sleep(5)
        print("\n 第一个用例结束:添加课程")


if __name__ == "__main__":
     pytest.main(['-s','-r','--verbose','Test_course.py'])
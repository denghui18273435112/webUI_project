#conftest.py
import pytest
from selenium import webdriver
import pytest
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import  Chrome,ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import  allure
from selenium.webdriver.support.ui import Select
from PublicMethods.WinUpLoadFile import upload_files
import allure
from datetime import datetime
from config.Conf import get_file_path
from PublicMethods.WinUpLoadFile import upload_files
import os
import pytest
import time

@pytest.fixture(scope="session")  #所有的测试文件执行前后执行一次
def driver():
   #前置-成功登录
    # opt = Options()
    # opt.add_argument('--no-sandbox')                # 解决DevToolsActivePort文件不存在的报错
    # opt.add_argument('window-size=1920x3000')       # 设置浏览器分辨率
    # opt.add_argument('--disable-gpu')               # 谷歌文档提到需要加上这个属性来规避bug
    # opt.add_argument('--hide-scrollbars')           # 隐藏滚动条，应对一些特殊页面
    # opt.add_argument('blink-settings=imagesEnabled=false')      # 不加载图片，提升运行速度
    # opt.add_argument('--headless')                  # 浏览器不提供可视化界面。Linux下如果系统不支持可视化不加这条会启动失败
    # driver = Chrome(options=opt)                    # 创建无界面对象

    # option = ChromeOptions()
    # option.headless =True
    # option.add_argument('window-size=1920x1080')
    # driver = webdriver.Chrome(options=option,executable_path = 'G:\python\selenium\webdriver\chromedriver.exe')

    driver = webdriver.Chrome()

    driver.maximize_window()

    login_YAML = ConfigYaml().read_yaml("login.yaml")
    test_login = login_YAML["test_login"]
    driver.get(test_login["url"])
    driver.implicitly_wait(10)
    while True:
            selenium(driver).FEBCS_CCSK("input[placeholder=请输入用户名]",test_login["text"])
            selenium(driver).FEBCS_CCSK("input[placeholder=请输入密码]",test_login["password"])
            selenium(driver).FEBCS_C("img[alt=验证码图片]")
            if test_login["url"]==test_login["new_url"]:
                selenium(driver).FEBCS_CCSK("input[placeholder=请输入验证码]","xicheng")
            else:
                selenium(driver).FEBCS_CCSK("input[placeholder=请输入验证码]",selenium(driver).new_inptu()) #在不是万能验证的时候使用
            selenium(driver).FEBCS_C("button[class=loginButton]")
            if driver.current_url != test_login["validation_url"]: #判断是否登录成功
                print(" \n 第一个用例结束:成功登录")
                break
            else:
                print("\n输入的验证码错误;已再次循环登录")

    #print("\n所有的测试文件执行前执行...开始")
    allure.attach("打开浏览器登录","打开浏览器登录")
    yield driver

   #后置-所有用例执行完关闭浏览器
    driver.close()
    #print("\n所有的测试文件执行前执行...结束")
    allure.attach("所有测试用例执行完","关闭浏览器")



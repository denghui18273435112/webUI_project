#case_test.py
import pytest
from selenium import webdriver
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

#@pytest.mark.usefixtures("driver")  #不用声明引入conftest.py中的driver方法
class Test_fix_module(object):  #传object

    @pytest.mark.run(order=1)
    def test_login(self,driver):  #把driver方法作为参数传递，应该 yield driver  #yeild 当成reture
        """
        登录方法
        @param driver:
        @return:
        """
        test_login = ConfigYaml().read_yaml("login.yaml","test_login")
        driver.get(test_login["url"])
        driver.implicitly_wait(10)
        while True:
            selenium(driver).FEBCS_CCSK(location=".item input[placeholder=请输入用户名]",content=test_login["text"])
            selenium(driver).FEBCS_CCSK(location=".item input[placeholder=请输入密码]",content=test_login["password"])
            selenium(driver).FEBCS_C(location=".verifyCode.item input[placeholder=请输入验证码]")

            selenium(driver).FEBCS_CCSK(location="#verifyCode",content="xicheng")
            #在不是万能验证的时候使用
            #selenium(driver).FEBCS_CCSK(location="verifyCode",content=selenium(driver).new_inptu())

            selenium(driver).FEBCS_C(location="#app > div > div > button")
            #判断是否登录成功
            if driver.current_url != test_login["validation_url"]:
                print(" \n 第一个用例结束:成功登录")
                break
            else:
                print("\n输入的验证码错误;已再次循环登录")


    def test_school_management_inquire(self,driver):
        """
        学校管理查询
        @param driver:
        @return:
        """
        TSMI = ConfigYaml().read_yaml("login.yaml","test_school_management_inquire")
        selenium(driver).location_name("学校管理")
        selenium(driver).FEBCS_CCSKK(location="div.leftSearch  input",content=TSMI["inquire_content"])
        selenium(driver).FEBCS_CCK(location="div.leftSearch  input")
        print("\n 第二个用例结束:学校管理查询成功")

    def test_school_management_add(self,driver):
        """
        学校管理添加
        @param driver:
        @return:
        """
        TSMD = ConfigYaml().read_yaml("login.yaml","test_school_management_add")
        selenium(driver).location_name("学校管理")
        selenium(driver).FEBCS_C("div > button > span")
        selenium(driver).FEBCS_CCSK(location="div.el-form-item__content  input",content=TSMD["school_name"])
        selenium(driver).FEBCS_CCSK(location="div.el-form-item__content  textarea",content=TSMD["describe"])
        selenium(driver).FEBXP_C(location="//span//button[2]")
        print("\n 第二个用例结束:学校管理添加成功")

    #@pytest.mark.skip   #遇到pytest.mark.skip声明的方法一直跳过
    def test_Course_center(self,driver):
        """
        @param driver:
        @return:
        """
        selenium(driver).location_name(name="配课中心")
        selenium(driver).location_name(name="课程管理")
        selenium(driver).FEBCS_C("div.rightSearch  button.el-button > span")
        selenium(driver).FEBCS_CCSK("div:nth-child(2)    input[placeholder=\"请输入课程标题\"]",content="学校")
        selenium(driver).FEBCS_CVT("div:nth-child(2)    input[placeholder=\"请选择课程类型\"]",content="1")
        time.sleep(10)
        print("\n 第三个用例结束")


if __name__ == "__main__":
    pytest.main(['-s','--verbose','case_test.py'])
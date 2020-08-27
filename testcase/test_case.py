#case_test.py
import pytest
from selenium import webdriver
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys

login = ConfigYaml().read_yaml("login.yaml","login")



#@pytest.mark.usefixtures("driver")  #不用声明引入conftest.py中的driver方法
class Test_fix_module(object):  #传object

    @pytest.mark.run(order=1)
    def test_login(self,driver):  #把driver方法作为参数传递，应该 yield driver  #yeild 当成reture
        """
        登录方法
        @param driver:
        @return:
        """
        driver.get(login["url"])
        driver.implicitly_wait(10)
        while True:
            selenium(driver).FEBCS_CCSK(location=".item input[placeholder=请输入用户名]",content=login["text"])
            selenium(driver).FEBCS_CCSK(location=".item input[placeholder=请输入密码]",content=login["password"])
            selenium(driver).FEBCS_C(location=".verifyCode.item input[placeholder=请输入验证码]")
            selenium(driver).FEBCS_CCSK(location="#verifyCode",content="xicheng")

            #在不是万能验证的时候使用
            # yanzhenma =input("请输入验证码：")
            # selenium(driver).FEBCS_CCSK(location="verifyCode",content=yanzhenma)
            selenium(driver).FEBCS_C(location="#app > div > div > button")

            #判断是否登录成功
            url =login["validation_url"]
            if driver.current_url != url:
                print(" \n 第一个用例结束")
                break
            else:
                print("\n输入的验证码错误;已再次循环登录")

    #@pytest.mark.skip   #遇到pytest.mark.skip声明的方法一直跳过
    def test_gaikuang(self,driver):
        selenium(driver).location_name("学校管理")
        selenium(driver).FEBCS_CCSKK(location="#app > div > div.contentWrapper > div > div > div.zzlCover.zzlCoverMH > div.zzlSearch > div.leftSearch > div > div > input",content="学校名称")
        print("\n 第二个用例结束")

    def test_Course_center(self,driver):
        """
        @param driver:
        @return:
        """
        selenium(driver).location_name(name="配课中心")
        selenium(driver).positioning_module_get("课程管理")
        selenium(driver).FEBCS_C("#app > div > div.contentWrapper > div > div > div > div:nth-child(2) > div.zzlSearch > div.rightSearch > div > button")
        selenium(driver).FEBCS_CCSK("#app > div > div.contentWrapper > div > div > div.zzlCover.zzlCoverMH > div.contentWrapperOne > form > div > div:nth-child(2) > div > div > div > input",content="学校")


        print("\n 第三个用例结束")


if __name__ == "__main__":
    pytest.main(['-s','--verbose','case_test.py'])
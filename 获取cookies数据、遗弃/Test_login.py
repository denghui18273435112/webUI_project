import pytest
from selenium import webdriver
from PublicMethods.Methods import selenium
from config.Conf import ConfigYaml
import time

class Test_login(selenium):

    def test_setup(self):  # 登陆部分
        url= ConfigYaml().read_yaml("login.yaml","login")
        # self.driver =webdriver.Chrome()
        # self.driver.maximize_window()   #窗口最大化
        self.driver.get(url["url"])  #利用谷歌浏览器打开百度窗口
        self.driver.implicitly_wait(10)
        while True:
            login = ConfigYaml().read_yaml("login.yaml","login")

            selenium().FEBCS_CCSK(location=".item input[placeholder=请输入用户名]",content=login["text"])
            selenium().FEBCS_CCSK(location=".item input[placeholder=请输入密码]",content=login["password"])
            #BasePage().FEBCS_C(location=".verifyCode.item input[placeholder=请输入验证码]")  #更新验证码
            selenium().FEBCS_CCSK(location="#verifyCode",content="xicheng")
            #在不是万能验证的时候使用
            # yanzhenma =input("请输入验证码：")
            # BasePage().FEBCS_CCSK(location="verifyCode",content=yanzhenma)
            selenium().FEBCS_C(location="#app > div > div > button")

            url =login["validation_url"]
            if self.driver.current_url != url:
                break
            else:
                print("输入的验证码错误;已再次循环登录")

    def test_teardown(self):
        self.driver.quit()


if __name__ == "__main__":
  Test_login().test_setup()
    

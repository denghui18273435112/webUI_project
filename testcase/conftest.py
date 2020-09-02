#conftest.py
import pytest
from selenium import webdriver
import pytest
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="session")  #所有的测试文件执行前执行一次
def driver():
   #前置-成功登录
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

    print("\n所有的测试文件执行前执行...开始")
    yield driver

   #后置-所有用例执行完关闭浏览器
    driver.close()
    print("\n所有的测试文件执行前执行...结束")

#case_test.py
import pytest
from selenium import webdriver
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

login_YAML = ConfigYaml().read_yaml("login.yaml")
@pytest.mark.usefixtures("driver")  #不用声明引入conftest.py中的driver方法
class Test_school(object):  #传object

    def test_school_management_inquire(self,driver):
        """
        学校管理查询
        @param driver:
        @return:
        """
        TSMI = login_YAML["test_school_management_inquire"]
        selenium(driver).location_name("学校管理")
        selenium(driver).FEBCS_CCSKK("div.leftSearch  input",TSMI["inquire_content"])
        selenium(driver).FEBCS_CCK("div.leftSearch  input")
        print("\n 第二个用例结束:学校管理查询成功")

    def test_school_management_add(self,driver):
        """
        学校管理添加
        @param driver:
        @return:
        """
        TSMD = login_YAML["test_school_management_add"]
        selenium(driver).location_name("学校管理")
        selenium(driver).FEBCS_C("div > button > span")
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  input",TSMD["school_name"])
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  textarea",TSMD["describe"])
        selenium(driver).FEBXP_C("//span//button[2]")
        print("\n 第二个用例结束:学校管理添加成功")




if __name__ == "__main__":
    pytest.main(['-s','--verbose','Test_school.py'])
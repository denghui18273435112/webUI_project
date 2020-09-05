#case_test.py
import pytest
from selenium import webdriver
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import allure
import pytest
from PublicMethods.Allure import new_allure

login_YAML = ConfigYaml().read_yaml("login.yaml")
@pytest.mark.usefixtures("driver")  #不用声明引入conftest.py中的driver方法
@allure.feature('学校管理')
class Test_school(object):  #传object


    @allure.story('学校管理查询')
    def test_school_management_inquire(self,driver):
        """
        学校管理查询
        @param driver:
        @return:  selenium(self.driver).resfresh()
        """
        TSMI = login_YAML["test_school_management_inquire"]
        selenium(driver).location_name(TSMI[module_name])
        selenium(driver).resfresh()

        selenium(driver).FEBCS_CCSKK("div.leftSearch  input",TSMI["inquire_content"])
        selenium(driver).if_list_contrast(inquire_field="学校管理-学校名称",contrast=TSMI["inquire_content"])
        print("\n 第一个用例结束:学校管理查询成功")
        # selenium(driver).new_allure(module_name=TSMI[module_name],test_name=TSMI[test_name])

    @allure.story('学校管理添加')
    def test_school_management_add(self,driver):
        """
        学校管理添加
        @param driver:
        @return:
        """
        TSMD = login_YAML["test_school_management_add"]
        selenium(driver).location_name("学校管理")
        selenium(driver).resfresh()

        selenium(driver).FEBCS_C("div > button > span")
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  input",TSMD["school_name"])
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  textarea",TSMD["describe"])
        selenium(driver).FEBXP_C("//span//button[2]")
        print("\n 第二个用例结束:学校管理添加成功")
        # selenium(driver).new_allure(module_name="学校管理",test_name="学校管理添加")

    @allure.story('学校管理修改')
    def test_school_management_alter(self,driver):
        """
        学校管理修改
        @param driver:
        @return:
        """
        TSMA = login_YAML["test_school_management_alter"]
        selenium(driver).location_name("学校管理")
        selenium(driver).resfresh()

        selenium(driver).FEBCS_C("div.el-table__fixed-body-wrapper  tr:nth-child(1) > td.el-table_1_column_5 span:nth-child(1)")
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  input",TSMA["school_name"])
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  textarea",TSMA["describe"])
        selenium(driver).FEBXP_C("//span//button[2]")
        print("\n 第三个用例结束:学校管理修改成功")
        # selenium(driver).new_allure(module_name="学校管理",test_name="学校管理修改")

    @allure.story('学校管理 删除')
    def test_school_management_del(self,driver):
        """
        学校管理 删除
        @param driver:
        @return:
        """
        TSMA = login_YAML["test_school_management_alter"]
        selenium(driver).location_name("学校管理")
        selenium(driver).resfresh()

        selenium(driver).FEBCS_C("div.el-table__fixed-body-wrapper  tr:nth-child(1) > td.el-table_1_column_5 span:nth-child(2)")
        selenium(driver).FEBCS_C("div > button.el-button--primary > span")
        print("\n 第四个用例结束:学校管理删除成功")
        # selenium(driver).new_allure(module_name="学校管理",test_name="学校管理 删除")


if __name__ == "__main__":
     pytest.main(['-s', '-q', '--alluredir', './report/html'])
     #pytest.main(['-s','-r','--verbose','test_school.py'])
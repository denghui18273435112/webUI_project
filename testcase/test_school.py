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
import  allure
import os

login_YAML = ConfigYaml().read_yaml("school.yaml")
@pytest.mark.usefixtures()
@allure.feature('学校管理')
class Test_school(object):


    @allure.story('学校管理 查询')
    def test_school_management_inquire(self,driver):
        """
        学校管理 查询
        @param driver:
        @return:
        """
        TSMI = login_YAML["test_school_management_inquire"]
        selenium(driver).location_name(TSMI["module_name"])
        selenium(driver).resfresh()
        selenium(driver).FEBCS_CCSKK("div.leftSearch  input",TSMI["inquire_content"])
        selenium(driver).if_list_contrast(inquire_field=TSMI["inquire_field"],contrast=TSMI["inquire_content"])
        selenium(driver).save_screenshot()



    @allure.story('学校管理 添加')
    def test_school_management_add(self,driver):
        """
        学校管理 添加
        @param driver:
        @return:
        """
        TSMD = login_YAML["test_school_management_add"]
        selenium(driver).location_name(TSMD["module_name"])
        selenium(driver).resfresh()
        selenium(driver).FEBCS_C("div > button > span")
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  input",TSMD["school_name"])
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  textarea",TSMD["describe"])
        selenium(driver).FEBXP_C("//span//button[2]")
        selenium(driver).save_screenshot(add="添加内容:",add1="添加内容:",)




    @allure.story('学校管理 修改')
    def test_school_management_alter(self,driver):
        """
        学校管理修改
        @param driver:
        @return:
        """
        TSMA = login_YAML["test_school_management_alter"]
        selenium(driver).location_name(TSMA["module_name"])
        selenium(driver).resfresh()
        selenium(driver).FEBCS_C("div.el-table__fixed-body-wrapper  tr:nth-child(1) > td.el-table_1_column_5 span:nth-child(1)")
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  input",TSMA["school_name"])
        selenium(driver).FEBCS_CCSK("div.el-form-item__content  textarea",TSMA["describe"])
        selenium(driver).FEBXP_C("//span//button[2]")
        selenium(driver).save_screenshot()



    @allure.story('学校管理 删除')
    def test_school_management_del(self,driver):
        """
        学校管理 删除
        @param driver:
        @return:
        """
        TSMD = login_YAML["test_school_management_del"]
        selenium(driver).location_name(TSMD["module_name"])
        selenium(driver).resfresh()
        selenium(driver).FEBCS_C("div.el-table__fixed-body-wrapper  tr:nth-child(1) > td.el-table_1_column_5 span:nth-child(2)")
        selenium(driver).FEBCS_C("div > button.el-button--primary > span")
        selenium(driver).save_screenshot()




if __name__ == "__main__":
     pytest.main(['-s', '-q', '--alluredir', './report/html'])
     #pytest.main(['-s','-r','--verbose','test_school.py'])
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

@allure.feature('考试管理-题库管理')
class Test_examination(object):

    @allure.story('题库添加')
    def  test_add(self,driver):
        selenium(driver).module_skip("推送记录")
        time.sleep(5)
        selenium(driver).resfresh()

        #selenium(driver).FEBXP_C(button_name="新增题库 ")


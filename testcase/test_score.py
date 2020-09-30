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
from utils.logUtil import my_log



@allure.feature('学校管理')
class Test_score(object):
    @pytest.mark.run(order=1)
    def pingfen(self,driver):
        pass

    @pytest.mark.run(order=2)
    @allure.story('添加题库')
    def test_add(self,driver):
        selenium(driver).module_skip("考试管理")
        selenium(driver).module_skip("题库管理")
        selenium(driver).button_click("新增题库 ")
        selenium(driver).text_input(" form > div > div:nth-child(1)  input","课程考试{}".format(new_time))
        selenium(driver).pull_down_choose("请选择题库类型","课程考试")
        selenium(driver).button_click("确 定")
        selenium(driver).operating_steps("考试管理-题库管理;添加题库<Br/>添加的题库名称:{}".format(new_time),"添加题库的截图","添加题库")

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
from selenium.webdriver.common.keys import Keys
from config.Conf import ConfigYaml
from selenium.webdriver.support.select import Select
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from PublicMethods.WinUpLoadFile import upload_files
import allure
from datetime import datetime
from config.Conf import get_file_path
from PublicMethods.WinUpLoadFile import upload_files
import os


new_time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
examination_YAML = ConfigYaml().read_yaml("examination.yaml")
@allure.feature('考试管理-题库管理') #
class Test_examination(object):



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

    #@pytest.mark.skip
    @pytest.mark.run(order=3)
    @allure.story('修改题库')
    def test_alter(self,driver):
        selenium(driver).button_click("div.el-table__fixed-body-wrapper  tr:nth-child(1)    span:nth-child(2)")
        time=datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
        selenium(driver).text_input(" form > div > div:nth-child(1)  input","课程考试{}".format(new_time))
        selenium(driver).pull_down_choose("请选择题库类型","课程考试")
        selenium(driver).button_click("确 定")
        selenium(driver).operating_steps("考试管理-题库管理;修改题库<Br/>修改题库的题库名称:{}".format(new_time),"修改题库的截图","修改题库")

    #@pytest.mark.skip
    @pytest.mark.run(order=4)
    @allure.story('删除题库')
    def test_del(self,driver):
        selenium(driver).button_click("div.el-table__fixed-body-wrapper  tr:nth-child(1)  span:nth-child(3)")
        selenium(driver).button_click("div > button.el-button--primary > span")
        selenium(driver).operating_steps("考试管理-题库管理;删除题库<Br/>删除题库:{}".format(new_time),"删除题库的截图","删除题库")

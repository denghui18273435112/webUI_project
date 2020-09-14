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


examination_YAML = ConfigYaml().read_yaml("examination.yaml")
@allure.feature('考试管理-题库管理')
class Test_examination(object):


    @pytest.mark.run(order=1)
    @allure.story('添加题库')
    def test_add(self,driver):
        selenium(driver).url_skip("题库管理")
        selenium(driver).button_click("新增题库 ")
        selenium(driver).text_input(" form > div > div:nth-child(1)  input","课程考试12")
        selenium(driver).pull_down_choose("请选择题库类型","课程考试")
        selenium(driver).button_click("确 定")

    # @pytest.mark.run(order=2)
    # @allure.story('修改题库')
    # def test_alter(self,driver):
    #     selenium(driver).url_skip("题库管理")
    #     selenium(driver).button_click("div.el-table__fixed-body-wrapper > table > tbody > tr > td.el-table_6_column_39.is-center > div > div > span:nth-child(2)")
    #     Test_examination.public_method(self,driver)


    # @pytest.mark.run(order=3)
    # @allure.story('删除题库')
    # def test_del(self,driver):
    #     selenium(driver).url_skip("题库管理")
    #     time.sleep(2)
    #     selenium(driver).button_click("#app > div > div.contentWrapper > div > div > div > div:nth-child(2) > div.zzlTableList > div.el-table.el-table--fit.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__fixed-right > div.el-table__fixed-body-wrapper > table > tbody > tr > td.el-table_6_column_39.is-center > div > div > span:nth-child(3)")
    #     selenium(driver).button_click("div > button.el-button--primary > span")






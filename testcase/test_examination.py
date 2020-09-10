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

    @allure.story('添加题库')
    def  test_add(self,driver):
        selenium(driver).location_name("考试管理")
        time.sleep(2)
        selenium(driver).location_name("题库管理")
        selenium(driver).text_input("input[placeholder=请输入题库名称]","好好学习")

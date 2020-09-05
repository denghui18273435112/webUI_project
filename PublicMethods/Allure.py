import time
from selenium.webdriver.support.ui import Select
from PublicMethods.WinUpLoadFile import upload_files
import allure
from datetime import datetime

def new_allure(self,test_title="test",sheet_name=None,case_model=None):
           #allure
        #sheet名称  feature 一级标签
        allure.dynamic.feature("test3213")
        #模块   story 二级标签
        allure.dynamic.story("None123213")
        #用例名称  title
        allure.dynamic.title(test_title)
        #请求URL  请求类型 期望结果 实际结果描述
        desc = "<font color='red'>当前执行时间: </font> {}<Br/>" \
                "<font color='red'>请求URL: </font> {}<Br/>" \
               "<font color='red'>请求类型: </font>{}<Br/>" \
                "<font color='red'>期望状态码: </font>{}<Br/>" \
                "<font color='red'>实际状态码: </font>{}<Br/>" \
               "<font color='red'>期望结果: </font>{}<Br/>" \
               "<font color='red'>实际结果: </font>{}".format(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                                          "test","test","test","test",
                                                          "test",
                                                          "test")
        allure.dynamic.description(desc)
        print("测试用例")
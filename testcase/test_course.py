import pytest
from selenium import webdriver
import time
from config.Conf import ConfigYaml
from PublicMethods.Methods import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
from win32 import win32gui
from PublicMethods.WinUpLoadFile import upload_files
import  allure


login_YAML = ConfigYaml().read_yaml("login.yaml")
#@pytest.mark.usefixtures("driver")  #不用声明引入conftest.py中的driver方法
@allure.feature('课程管理')
class Test_course(object):

    @pytest.mark.run(order=1)
    @allure.story('课程添加')
    def test_Course_center_add(self,driver):
        """
        添加课程数据
        @param driver:
        @return:
        """
        selenium(driver).module_skip("配课中心")
        selenium(driver).module_skip("课程管理")
        selenium(driver).button_click("div.rightSearch  button.el-button > span")

        #课程信息
        selenium(driver).text_input("div:nth-child(2)    input[placeholder=请输入课程标题]","学校22")
        selenium(driver).pull_down_choose("input[placeholder=请选择课程类型]", "必修")
        selenium(driver).text_input("div.contentWrapperOne  div:nth-child(4)  input","10")
        selenium(driver).text_input("div:nth-child(5)  input.el-input__inner","标签")

        #设计课程目标
        selenium(driver).text_input("div:nth-child(7)  div:nth-child(1) > div > div > input","4")
        selenium(driver).text_input("div:nth-child(7)  div:nth-child(2) > div > div > input","20")
        selenium(driver).text_input("div:nth-child(8)  div:nth-child(1) > div > div > input","4")
        selenium(driver).text_input("div:nth-child(8)  div:nth-child(2) > div > div > input","20")
        selenium(driver).text_input("div:nth-child(9)  div:nth-child(1) > div > div > input","4")
        selenium(driver).text_input("div:nth-child(9)  div:nth-child(2) > div > div > input","20")
        selenium(driver).text_input("div:nth-child(10)  div:nth-child(1) > div > div > input","40")
        selenium(driver).text_input(" input[placeholder=选择日期]","2020-09-03")
        selenium(driver).pull_down_choose("input[placeholder=请选择试卷]", "课程试卷")
        selenium(driver).click_new("div:nth-child(13)  label:nth-child(1) > span > span")
        selenium(driver).click_new("div:nth-child(14)  label:nth-child(2) > span> span")

        #设置相关图片
        selenium(driver).button_click("上传封面")
        upload_files("banner.png")
        time.sleep(1)
        selenium(driver).button_click("上传banner图")
        upload_files("banner.png")
        time.sleep(1)

        #设置课程简介
        selenium(driver).roll()
        selenium(driver).editor_upload_photo()
        #点击下一步按钮
        selenium(driver).click_new("div.actions  button.zzlPrimary  span")

        #课程目录页面
        y = ["第1章","第2章","第3章","第4章"]
        for x in y:
            time.sleep(1)
            selenium(driver).click_new("div.left span:nth-child(1) svg")
            time.sleep(0.5)
            selenium(driver).text_input("input[placeholder=请输入章的名称]",x)
            selenium(driver).click_new("body > div.el-dialog__wrapper   button.el-button.zzlPrimary  span")

        t = [3,4,5,6]
        for tt in t:
            selenium(driver).click_new(" div:nth-child({0}) > div.item  span.select".format(str(tt)))
            selenium(driver).click_new("span:nth-child(2) > svg")
            selenium(driver).pull_down_choose("input[placeholder=请选择题库类型]", "图片")
            selenium(driver).pull_down_choose("input[placeholder=请选择资源分类]", "名胜古迹")
            selenium(driver).click_new("div.el-dialog__body  button > span")
            upload_files("banner.png")
            time.sleep(1)
        #点击下一步按钮
        selenium(driver).click_new("div.actions  button.zzlPrimary  span")


        #课程测验
        for ttt in [2,3,4,5]:
            selenium(driver).click_new("div.contentWrapper  div.contentWrapperThree div:nth-child({0}) > div.subItemBox  span.wrapperOne".format(ttt))
            selenium(driver).click_new("div.buttons   div > button > span")
            upload_files(filePath="kaoshi.xlsx")

        #点击下一步按钮
        selenium(driver).click_new("div.actions  button.zzlPrimary  span")


        #添加讨论
        for xx in [2,3,4,5]:
            selenium(driver).click_new("div.contentWrapperFour  div:nth-child({0})  div.subItemBox  span.name".format(xx))
            selenium(driver).button_click("添加讨论")
            selenium(driver).text_input("div:nth-child(1)  textarea","名胜古迹")
            selenium(driver).upload_photo("div:nth-child(2) > div > div > i")
            driver.find_elements_by_css_selector("div button.confirmButton span")[4].click()
        selenium(driver).button_click("提交")
        print("\n 第一个用例结束:添加课程")

    @pytest.mark.skip
    @allure.story('课程查询')
    def test_Course_center_inquire(self,driver):
        """
        课程列表查询
        @param driver:
        @return:
        """
        selenium(driver).module_skip("配课中心")
        selenium(driver).module_skip("课程管理")
        selenium(driver).pull_down_choose("input[placeholder=请选择所属学校]", "菜鸟大专")
        selenium(driver).FEBCS_CCSKK("input[placeholder=请输入名称回车查询]","练成")
        selenium(driver).FEBCS_CCSK("input[placeholder=开始日期]","2020-08-04")
        selenium(driver).FEBCS_CCSK("input[placeholder=结束日期]","2020-08-04")
        selenium(driver).FEBXP_C(button_name="查询")
        selenium(driver).operating_steps(
                                         name_screenshot="查询成功后的截图",
                                         describe="  课程列表查询 ")


if __name__ == "__main__":
     pytest.main(['-s','-r','--verbose','Test_course.py'])
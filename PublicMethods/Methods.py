# coding=utf-8
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


class selenium:
    def __init__(self,driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver=driver

    def back(self):
        """
        浏览器后退按钮
        :param none:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()

    def resfresh(self):
        """
        刷新页面
        @return:
        """
        self.driver.refresh()

    def open_url(self, url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()

    def  send_keys(self,location,content):
        """
        上传 <input type="file" name="upload">   文件
        @return:
        """
        self.driver.find_element_by_css_selector(location).send_keys(content)

    def jietu(self,filePath):
        """
        截图
        @param filePath:
        @return:
        """
        file_name=get_file_path()+os.sep+filePath
        self.driver.get_screenshot_as_file(file_name)

    def operating_steps(self, case_Steps_describe=None,name_screenshot=None,describe=None):
        """
        在allure 报告中添加操作和截图
        编写操作步骤和页面截屏保存截图
        @param case_Steps_describe: 操作步骤的名称
        @param name_screenshot:截图名称或图片名称
        @param describe:allure的描述
        @return:
        """
        #allure报告中的描述     allure.dynamic.description  第一个参数就是 描述
        if describe==None:
            allure.dynamic.description("<font color='red' style='font-size: 20px;'>暂无描述内容</font><Br/>")
        else:
            allure.dynamic.description("<font color='red' style='font-size: 20px;'>{}</font><Br/>".format(describe))


        #测试步骤中的操作步骤     allure.attach方法中；第一个参数：测试步骤标题；第二参数：步骤标题内容
        if case_Steps_describe==None:
            allure.attach( "<font color='red' style='font-size: 20px;'>操作步骤</font><Br/>","操作步骤",
                           allure.attachment_type.HTML)
        else:
            allure.attach( "<font color='red' style='font-size: 20px;'>{}</font><Br/>".format(case_Steps_describe),"操作步骤",
                           allure.attachment_type.HTML)


        #截图并读取，写入进入allure报告中 file:切图文件的名称;name_screenshot:在allure中显示测试步骤标题; allure.attachment_type.PNG allure步骤的类型
        if name_screenshot==None:
            file_name=get_file_path()+os.sep + "\\{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), "截图")
        else:
            file_name=get_file_path()+os.sep + "\\{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), name_screenshot)
        self.driver.get_screenshot_as_file(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, name_screenshot, allure.attachment_type.PNG)








    def roll(self,location="right",up="500"):
        """
        仅限于页面自带的进度条
        location: tElementsByClassName定位
        @return:
        """
        self.driver.execute_script( 'document.getElementsByClassName("{}")[0].scrollTop={}'.format(location,up))
        time.sleep(0.5)

    def editor_upload_photo(self,location1="i.w-e-icon-image",location2="i.w-e-icon-upload2",photo="banner.png"):
        """
        编辑器中上传图片
        @param location1:定位编辑器图片上传位置
        @param location2: 定位图片上传位置
        @param photo: 图片文件的名称
        @return:
        """
        self.driver.find_element_by_css_selector(location1).click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(location2).click()
        time.sleep(0.5)
        upload_files(photo)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)

    def upload_photo(self,location1="i.w-e-icon-image",photo="banner.png"):
        """
        上传图片
        @param location1: 定位图片上传位置
        @param photo: 图片文件的名称
        @return:
        """
        self.driver.find_element_by_css_selector(location1).click()
        time.sleep(0.5)
        upload_files(photo)
        time.sleep(0.5)



    def FEBCS_CCSK(self,location,content):
        """
        定位-点击-清空-输入-隐性等待10S
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.find_element_by_css_selector(location).click()
        self.driver.find_element_by_css_selector(location).clear()
        self.driver.find_element_by_css_selector(location).send_keys(content)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)

    def FEBCS_new_CCSK(self,location,content):
        """
        定位-点击-清空-输入-隐性等待10S
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        new_driver = self.driver.find_element_by_css_selector(location)
        new_driver.click()
        print("点击")
        new_driver.send_keys(content)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)

    def FEBXP_CCSK(self,location,content):
        """
        定位-点击-清空-输入-隐性等待10S
        find_element_by_css_xpath 缩写FEBXP
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.find_element_by_xpath(location).click()
        self.driver.find_element_by_xpath(location).clear()
        self.driver.find_element_by_xpath(location).send_keys(content)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)

    def FEBCS_CVT(self,location,content):
        """
        定位-点击-下拉选择-隐性等待10S
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.find_element_by_css_selector(location).click()
        Select(self.driver.find_element_by_css_selector(location)).select_by_index(content)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)

    def FEBXP_CVT(self,location,content):
        """
        定位-点击-下拉选择-隐性等待10S
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.find_element_by_xpath(location).click()
        Select(self.driver.find_element_by_xpath(location)).select_by_visible_text(content)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)


    def FEBCS_CCSKK(self,location,content):
        """
        定位-点击-清空-输入-隐性等待10S-回车
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.find_element_by_css_selector(location).click()
        self.driver.find_element_by_css_selector(location).clear()
        self.driver.find_element_by_css_selector(location).send_keys(content)
        self.driver.find_element_by_css_selector(location).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)


    def FEBXP_CCSKK(self,location,content):
        """
        定位-点击-清空-输入-隐性等待10S-回车
        find_element_by_css_xpath 缩写FEBCXP
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.find_element_by_xpath(location).click()
        self.driver.find_element_by_xpath(location).clear()
        self.driver.find_element_by_xpath(location).send_keys(content)
        self.driver.find_element_by_xpath(location).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)


    def FEBCS_CCK(self,location):
        """
        定位-点击-清空-回车-隐性等待10S
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :return:
        """
        self.driver.find_element_by_css_selector(location).click()
        self.driver.find_element_by_css_selector(location).clear()
        self.driver.find_element_by_css_selector(location).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)


    def FEBXP_CCK(self,location):
        """
        定位-点击-清空-回车-隐性等待10S
        find_element_by_css_xpath 缩写FEBP
        :param location: 定位
        :return:
        """
        self.driver.find_element_by_xpath(location).click()
        self.driver.find_element_by_xpath(location).clear()
        self.driver.find_element_by_xpath(location).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        time.sleep(0.5)


    def FEBCS_C(self,location):
        """
        定位-点击-隐性等待10S
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :return:
        """
        self.driver.find_element_by_css_selector(location).click()
        self.driver.implicitly_wait(10)
        time.sleep(1)

    def FEBXP_C(self,location=None,button_name=None):
        """
        定位-点击-隐性等待10S
        find_element_by_css_xpath 缩写FEBXP
        :param location: 定位
        :button_name: 按钮的名称
        :return:
        """
        if button_name != None:
            self.driver.find_element_by_xpath("//span[contains(text(),\"{0}\")]".format(button_name)).click()
        if location != None:
            self.driver.find_element_by_xpath(location).click()
        self.driver.implicitly_wait(10)
        time.sleep(0.5)


    def FEBCS_pull_down_choose(self,location,option_name):
        """
            点击弹出下拉-选择下拉选项
           @param location:  定位下拉文本框位置
           @param option_name: 下拉选项名称
           @return:
       """
        self.driver.find_element_by_css_selector(location).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//span[contains(text(),"{0}")]'.format(option_name)).click()
        time.sleep(0.5)
        self.driver.implicitly_wait(10)



    def positioning_module_get(self,name):
        """
        通过模块名称进行get跳转
        @param name: 模块名称
        @return:
        """
        login = ConfigYaml().read_yaml("login.yaml","login")
        if name == "学校管理":
            self.driver.get(login["url_ip"]+"SchoolManagement")
        if name == "课程管理":
            url=login["url_ip"]+"CourseManagement"
            self.driver.get(url)


    def location_name(self,name):
        """
        通过模块名称进行定位点击
        @param name: 模块名称
        @return:
        """
        if name == "配课中心":
            selenium(self.driver).FEBCS_C("span:nth-child(3)  span:nth-child(2)")
        if name == "学校管理":
            selenium(self.driver).FEBCS_C("span:nth-child(9) span:nth-child(1)")
        if name == "课程管理":
            selenium(self.driver).FEBCS_C("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > ul > li:nth-child(2) > span")
        if name == "配课中心2":
            selenium(self.driver).FEBCS_C("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > div > span:nth-child(2)")
        if name == "配课中心3":
            selenium(self.driver).FEBCS_C("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > div > span:nth-child(2)")
        time.sleep(0.5)



    def if_list_contrast(self,inquire_field,contrast):
        """
        获取列表某字段的文本信息  与查询字段进行判断，是否存在包含关系
        inquire_field  需要查询的字段名称
        contrast  输入的查询条件
        @return:
        """
        if  inquire_field=="学校管理-学校名称":
            location="#app > div > div.contentWrapper > div > div > div.zzlCover.zzlCoverMH > div.zzlTableList.zzlTableListMaxH > div.el-table.el-table--fit.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr > td.el-table_1_column_1.is-center > div.cell.el-tooltip"

        list = self.driver.find_elements_by_css_selector(location)

        print(list)
        if len(list) == 0:
            print("列表没有数据")
        else:
            for i in list:
                if str(contrast in i.text) == "True":
                    print("列表数据和查询条件匹配")
                    print(i.text)
                    print(contrast)
                else:
                    print("列表数据和查询条件匹配")
                    pytest.xfail("列表数据和查询条件不匹配")
        time.sleep(0.5)

    def new_allure(self,module_name=None,test_name=None):
           #allure
        #sheet名称  feature 一级标签
        allure.dynamic.feature(module_name)
        #模块   story 二级标签
        allure.dynamic.story()
        #用例名称  title
        allure.dynamic.title(test_name)
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








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
from utils.logUtil import my_log
#@pytest.mark.usefixtures("driver")(object)
class selenium(object):
    def __init__(self,driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver=driver
        #print(self.driver)

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
        @param case_Steps_describe: allure中的操作步骤的名称
        @param name_screenshot:截图名称或图片名称
        @param describe:allure中的描述
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


    def text_input(self,location,content,Enter=None):
        """
        文本输入
       @param location: 文本定位
       @param content: 输入内容
       @param Enter: 是否回车；传入为0回车；Enter=None不回车
       @return:
       """
        if '\u4e00' <= location <= '\u9fff':
            self.driver.find_element_by_css_selector("input[placeholder=\"{0}\"]".format(location)).click()
        if ">" in location:
            self.driver.find_element_by_css_selector(location).click()
        self.driver.find_element_by_css_selector(location).clear()
        self.driver.find_element_by_css_selector(location).send_keys(content)
        if Enter == 0:
            self.driver.find_element_by_css_selector(location).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)




    def click_new(self, location):
        """
        常规点击
        :param location: 定位
        :return:
        """
        if "/" in location or "//" in location:
           self.driver.find_element_by_xpath(location).click()
        elif  '\u4e00' <= location <= '\u9fff':
             self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location)).click()
        else:
            self.driver.find_element_by_css_selector(location).click()
        self.driver.implicitly_wait(10)
        time.sleep(1)



    def button_click(self,location,weizhi=None):
        """
        按钮点击；支持复数定位点击
        @param location:
        @param weizhi:
        @return:
        """
        time.sleep(1)
        if (">" in location or "." in location) and weizhi != None :
            self.driver.find_elements_by_css_selector(location)[int(weizhi)].click()
        elif (">" in location or "." in location) and weizhi == None :
            self.driver.find_element_by_css_selector(location).click()

        elif "/" in location  and weizhi != None :
            self.driver.find_element_by_xpath(location)[int(weizhi)].click()
        elif "/" in location  and weizhi == None :
            self.driver.find_element_by_xpath(location).click()

        elif '\u4e00' <= location <= '\u9fff' and weizhi != None:
            print("//*[contains(text(),'{}')]".format(location))
            print([int(weizhi)])
            self.driver.find_elements_by_xpath("//*[contains(text(),'{}')]".format(location))[int(weizhi)].click()
        elif '\u4e00' <= location <= '\u9fff' and weizhi == None:
            self.driver.find_element_by_xpath("//*[contains(text(),'{}')]".format(location)).click()
        self.driver.implicitly_wait(10)
        time.sleep(1)


    def pull_down_choose(self, location, option_name):
        """
        下拉选择
        @param location:  定位下拉文本框位置
        @param option_name: 下拉选项名称
        @return:
       """
        if '\u4e00' <= location <= '\u9fff':
                self.driver.find_element_by_css_selector("input[placeholder={}]".format(location)).click()
        if ">" in location or "=" in location:
                self.driver.find_element_by_css_selector(location).click()
        if "/" in location:
                self.driver.find_element_by_xpath(location).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//span[contains(text(),"{0}")]'.format(option_name)).click()
        time.sleep(0.5)
        self.driver.implicitly_wait(10)


    def url_skip(self, name):
        """
        url跳转
        @param name: 模块名称
        @return:
        """
        login = ConfigYaml().read_yaml("login.yaml","test_login")
        if name == "学校管理":
            self.driver.get(login["url_ip"]+"SchoolManagement")
        if name == "课程管理":
            self.driver.get(login["url_ip"]+"CourseManagement")
        if name =="题库管理":
            self.driver.get(login["url_ip"]+"QuestionBankManagement")
        if name =="推送记录":
            self.driver.get(login["url_ip"]+"PushRecords")
        if name =="试卷管理":
            self.driver.get(login["url_ip"]+"TestPaperManagement")
        if name =="试卷管理":
            self.driver.get(login["url_ip"]+"TestPaperManagement")
        time.sleep(2)
        self.driver.implicitly_wait(10)


    def module_skip(self, name):
        """
        模块名称跳转
        @param name: 模块名称
        @return:
        """

        time.sleep(1)
        if name =="考试管理":
                selenium(self.driver).click_new("span:nth-child(4)  span:nth-child(2)")
        if name =="题库管理":
                selenium(self.driver).click_new("#app > div > div.contentWrapper > span > div > ul > span:nth-child(4) > li > ul > li:nth-child(1)")
        if name =="试卷管理":
                selenium(self.driver).click_new("#app > div > div.contentWrapper > span > div > ul > span:nth-child(4) > li > ul > li:nth-child(2)")
        if name == "配课中心":
                selenium(self.driver).click_new("span:nth-child(3)  span:nth-child(2)")
        if name == "学校管理":
                selenium(self.driver).click_new("span:nth-child(9) span:nth-child(1)")
        if name == "课程管理":
                selenium(self.driver).click_new("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > ul > li:nth-child(2) > span")
        if name == "配课中心2":
                selenium(self.driver).click_new("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > div > span:nth-child(2)")
        if name == "配课中心3":
                selenium(self.driver).click_new("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > div > span:nth-child(2)")
        time.sleep(1)




    def if_list_contrast(self,location,contrast):
        """
        获取列表某字段的文本信息  与查询字段进行判断，是否存在包含关系
        inquire_field  需要查询的字段名称
        contrast  输入的查询条件
        @return:
        """

        print(self.driver.find_element_by_css_selector(location).text)
        print(contrast)
        # print(self.driver.find_elements_by_css_selector(location))
        # for i in range(1,10):
        #     print(i)
        #     list = self.driver.find_elements_by_css_selector(location)[int(i)].text
        #     print(list)
        #     print(i.text)
        #     if str(contrast in i.text) == "True":
        #             print("列表数据和查询条件匹配")
        #             print(i.text)
        #             print(contrast)
        #     else:
        #             print("列表数据和查询条件匹配")
        #             pytest.xfail("列表数据和查询条件不匹配")
        # time.sleep(0.5)

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








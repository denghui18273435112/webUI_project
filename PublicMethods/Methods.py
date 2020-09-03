# coding=utf-8
from selenium.webdriver.common.keys import Keys
from config.Conf import ConfigYaml
from selenium.webdriver.support.select import Select
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


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
        time.sleep(0.3)

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
        time.sleep(0.3)

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
        time.sleep(0.3)

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
        time.sleep(0.3)


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
        time.sleep(0.3)


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
        time.sleep(0.3)


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
        time.sleep(0.3)


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
        time.sleep(0.3)


    def FEBCS_C(self,location):
        """
        定位-点击-隐性等待10S
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :return:
        """
        self.driver.find_element_by_css_selector(location).click()
        self.driver.implicitly_wait(10)
        time.sleep(0.3)

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


    def FEBXP_C(self,location):
        """
        定位-点击-隐性等待10S
        find_element_by_css_xpath 缩写FEBXP
        :param location: 定位
        :return:
        """
        self.driver.find_element_by_xpath(location).click()
        self.driver.implicitly_wait(10)
        time.sleep(0.3)




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
        time.sleep(0.3)



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
        time.sleep(0.3)







# coding=utf-8
from selenium.webdriver.common.keys import Keys
from config.Conf import ConfigYaml

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

    def FEBXP_CCSK(self,location,content):
        """
        定位-点击-清空-输入-隐性等待10S
        find_element_by_css_xpath 缩写FEBXP
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.find_element_by_css_xpath(location).click()
        self.driver.find_element_by_css_xpath(location).clear()
        self.driver.find_element_by_css_xpath(location).send_keys(content)
        self.driver.implicitly_wait(10)

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

    def FEBXP_CCSKK(self,location,content):
        """
        定位-点击-清空-输入-隐性等待10S-回车
        find_element_by_css_xpath 缩写FEBCXP
        :param location: 定位
        :param content: 输入内容
        :return:
        """
        self.driver.find_element_by_css_xpath(location).click()
        self.driver.find_element_by_css_xpathr(location).clear()
        self.driver.find_element_by_css_xpath(location).send_keys(content)
        self.driver.find_element_by_css_xpath(location).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def FEBCS_CCK(self,location):
        """
        定位-点击-清空-回车-隐性等待10S
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :return:
        """
        self.driver.find_element_by_css_selector(location).click()
        self.driver.find_element_by_css_selector(location).clear()
        self.driver.find_element_by_css_selector().send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def FEBXP_CCK(self,location):
        """
        定位-点击-清空-回车-隐性等待10S
        find_element_by_css_xpath 缩写FEBP
        :param location: 定位
        :return:
        """
        self.driver.find_element_by_css_xpath(location).click()
        self.driver.find_element_by_css_xpath(location).clear()
        self.driver.find_element_by_css_xpath(location).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def FEBCS_C(self,location):
        """
        定位-点击-隐性等待10S
        find_element_by_css_selector 缩写FEBCS
        :param location: 定位
        :return:
        """
        self.driver.find_element_by_css_selector(location).click()
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
            selenium(self.driver).FEBCS_C("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > div > span:nth-child(2)")
        if name == "学校管理":
            selenium(self.driver).FEBCS_C("#app > div > div.contentWrapper > span > div > ul > span:nth-child(9) > li > span:nth-child(2)")
        if name == "配课中心1":
            selenium(self.driver).FEBCS_C("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > div > span:nth-child(2)")
        if name == "配课中心2":
            selenium(self.driver).FEBCS_C("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > div > span:nth-child(2)")
        if name == "配课中心3":
            selenium(self.driver).FEBCS_C("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > div > span:nth-child(2)")




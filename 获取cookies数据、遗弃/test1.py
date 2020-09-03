import pytest
from selenium import webdriver
from PublicMethods.Methods import selenium
from config.Conf import ConfigYaml
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://tp.safetycms.huayustech.com")
login = driver.find_element_by_css_selector("input[placeholder=请输入用户名]")
login.click()
login.send_keys("admin")
password = driver.find_element_by_css_selector("input[placeholder=请输入密码]")
password.click()
password.send_keys("admin123")
code = driver.find_element_by_css_selector("img[alt=验证码图片]")
code.click()
yanzhengma= driver.find_element_by_css_selector("input[placeholder=请输入验证码]")
yanzhengma.click()
yanzhengma.send_keys(input("请输入密码"))
driver.find_element_by_css_selector("button[class=loginButton]").click()
time.sleep(2)
driver.find_element_by_css_selector("span:nth-child(3)  span:nth-child(2)").click()
time.sleep(0.5)
driver.find_element_by_css_selector("#app > div > div.contentWrapper > span > div > ul > span:nth-child(3) > li > ul > li:nth-child(2) > span").click()
time.sleep(0.5)
driver.find_element_by_css_selector("#app > div > div.contentWrapper > div > div > div > div:nth-child(2) > div.zzlSearch > div.rightSearch > div > button > span").click()

driver.execute_script('document.getElementsByClassName("right")[0].scrollTop=10000')

time.sleep(5)


kecheng = driver.find_element_by_css_selector("div:nth-child(19) div.w-e-text-container")
time.sleep(5)
kecheng.click()
print("dada")
time.sleep(5)
kecheng.send_keys("好好学习")




# x = "w-e-text-container"
# y = "聂荣给"
# #test_js="document.getElementsByClassName(\"{0}\")[0].contentWindow.document.body.innerText={1}".format(x,y)
# test_js="document.getElementsByClassName(\"{0}\").innerHTML={1};".format(x,y)
#
# driver.execute_script(test_js)

time.sleep(5)

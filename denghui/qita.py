from selenium import webdriver
import time
dr=webdriver.Chrome()
dr.get('file:///G:/pycharm/script/webUI_project/denghui/log.html')
time.sleep(5)
js='document.getElementsByClassName("scroll")[0].scrollTop=10000' #可以调整10000，10000就是到底
# 就是这么简单，修改这个元素的scrollTop就可以
dr.execute_script(js)
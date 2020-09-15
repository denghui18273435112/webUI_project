from selenium import webdriver
import win32gui
import win32con
import time
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()#最大
driver.find_element_by_class_name('soutu-btn').click()
time.sleep(2)
imgpath='D:\\abc.jpg'
driver.find_element_by_css_selector('input[value=上传图片]').click()
time.sleep(2)
# driver.find_element_by_class_name('upload-pic').send_keys('imgpath')
#一级顶层窗口，此处title为上传窗口名称，浏览器不一样上传窗口名称不一样
dialog = win32gui.FindWindow("#32770",'打开')
#二级窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
#三级窗口
comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)
#四级窗口
edit = win32gui.FindWindowEx(comboBox,0,'Edit',None)
button = win32gui.FindWindowEx(dialog,0,'Button',None)
#执行操作 输入文件路径
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,'D:\\abc.jpg')
#点击打开上传文件
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)


for i in range(1,11):
    print(i)
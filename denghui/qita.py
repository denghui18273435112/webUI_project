from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'log.html')

#导入select类
from selenium.webdriver.support.ui import Select
#获取相应的webElement
select = Select(driver.find_element_by_id("multi"))
#先去选择所有的选项
select.deselect_all()
select.select_by_visible_text("雅阁")
select.select_by_visible_text("宝马 740")

#获得相应的webElement
select = Select(driver.find_element_by_id("single"))
select.select_by_visible_text("男")

input("press any key to quit...")
driver.quit()
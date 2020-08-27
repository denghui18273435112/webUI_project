#conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")  #所有的测试文件执行前执行一次
def driver():
   #前置
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("\n所有的测试文件执行前执行...开始")
    yield driver

   #后置
    driver.close()
    print("\n所有的测试文件执行前执行...结束")

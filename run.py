import pytest
from common import Base

if __name__ == "__main__":
     #pytest运行前会提前运行pytest.ini文件的内容; 运行文件test_excel_case.py;alluredir pytest报告生成路径;后面更路径

     #本地运行使用
     pytest.main (['./testcase/test_course.py']) #运行项目下testcase文件下，所有满足执行条件的测试用例

    #jenkins运行上使用
    #pytest.main(["-s","./testcase/test_school.py","--alluredir",Base.report_path()])  # 运行testcase目录下所有test开头的方法
    #Base.allure_report(Base.report_path(),Base.report_html_path())


#test_Pytest.py文件
import pytest

class Test_Pytest(object):

        def setup_method(self):
                 print("方法开始")

        def teardown_methond(self):
                print("方法结束")
        def test_one(self,):
                #print(" \n ----start------")
                #pytest.xfail(reason='该功能尚未完成(表示原因)') #pytest.xfail()方法后的代码不运行
                print("test_one方法执行" )

        def test_two(self):
                print("test_two方法执行" )

if __name__=="__main__":
    pytest.main(['-s','-r','test.py'])
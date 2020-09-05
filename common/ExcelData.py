from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig
from common import Base
from utils.AssertUitl import AssertUitl
import allure
from datetime import datetime

class Data:
    def __init__(self,testcase_file,sheet_name):
        """
        :param testcase_file:  �������
        :param sheet_name:   sheet����
        :return: ʹ��excel�����࣬��ȡ���list
        """
        self.reader = ExcelReader(testcase_file,sheet_name)

    def get_run_data(self):
        """
        #2�����Ƿ��������ݣ�y
        �����Ƿ�������==y����ȡִ�в�������
         #3������Ҫִ�н�����ŵ��µ��б�
        :return:
        """
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == "y":
                run_list.append(line)
        print("��������",run_list)
        return run_list

    def get_case_list(self):
        """
        ��ȡȫ����������
        :return:
        # run_list=list()
        # for line in self.reader.data():
        # run_list.append(line)
        """
        run_list = [ line for line in self.reader.data()]
        return run_list

    def get_case_pre(self,pre):
        """
        #��ȡȫ����������
        #list�жϣ�ִ�У���ȡ
        ����ǰ����������ȫ����������ȡ����Ӧ��������
        :param pre:
        :return:
        """
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None


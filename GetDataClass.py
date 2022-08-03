import sys

import xlrd
import urllib.request
import os
from xlutils.copy import copy
import logger
import time

log = logger.Logger()
n = 0


class data:

    def read_data_nrows(self):
        workbook = xlrd.open_workbook('平城区网格长基本信息.xls')  # 打开excel
        worksheet = workbook.sheet_by_name('Sheet1')  # 获取sheet1内容
        nrows = worksheet.nrows
        return nrows

    # 读取数据
    def read_data(self, i):
        phone = None
        workbook = xlrd.open_workbook('平城区网格长基本信息.xls')  # 打开excel
        worksheet = workbook.sheet_by_name('Sheet1')  # 获取sheet1内容

        # 判断是否已上传，并获取字段值
        if worksheet.row_values(i)[6] == 1:
            log.write("账号{0}已完成办结".format(worksheet.row_values(i)[2]))
            return phone
        elif worksheet.row_values(i)[6] == 2:
            log.write("{0}账号登录失败".format(worksheet.row_values(i)[2]))
            return phone
        elif worksheet.row_values(i)[6] == 0:
            phone = worksheet.row_values(i)[2]
            print()
            return phone
        elif worksheet.row_values(i)[6] == 3:
            log.write("{0}账号数据异常".format(worksheet.row_values(i)[2]))
            return phone

    # 标记上传成功
    def tag_submit(self, i):
        # try:
        #     workbook = xlrd.open_workbook('平城区网格长基本信息.xlsx')  # 打开excel
        #     worksheet = workbook.sheet_by_name('Sheet1')  # 获取sheet1内容
        #     count = worksheet.row_values(i)[6] # 获取上报数
        #     print(count)
        #     new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        #     new_worksheet = new_workbook.get_sheet(0)  # 获取第一个sheet
        #     new_worksheet.write(i, 7, count+1)  # 上传成功数加1
        #     # new_worksheet.write(i, 8, time.strftime("%Y-%m-%d, %H:%M:%S"))  # 标记时间
        #     new_workbook.save('平城区网格长基本信息.xlsx')  # 保存工作簿
        # except:
        #     log.write("办结完成")
        workbook = xlrd.open_workbook('平城区网格长基本信息.xls')  # 打开excel
        worksheet = workbook.sheet_by_name('Sheet1')  # 获取sheet1内容
        count = worksheet.row_values(i)[7]  # 获取上报数
        print(count)
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取第一个sheet
        new_worksheet.write(i, 7, int(count) + 1)  # 上传成功数加1
        # new_worksheet.write(i, 8, time.strftime("%Y-%m-%d, %H:%M:%S"))  # 标记时间
        new_workbook.save('平城区网格长基本信息.xls')  # 保存工作簿

    # 标记登录失败
    def tag_login_error(self, i):
        try:
            workbook = xlrd.open_workbook('平城区网格长基本信息.xls')  # 打开excel
            new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
            new_worksheet = new_workbook.get_sheet(0)  # 获取第一个sheet
            new_worksheet.write(i, 6, 2)  # 登录失败为2
            new_worksheet.write(i, 8, time.strftime("%Y-%m-%d, %H:%M:%S"))  # 标记时间
            new_workbook.save('平城区网格长基本信息.xls')  # 保存工作簿
        except:
            log.write("登录失败")

    # 标记数据异常
    def tag_data_error(self, i):
        try:
            workbook = xlrd.open_workbook('平城区网格长基本信息.xls')  # 打开excel
            new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
            new_worksheet = new_workbook.get_sheet(0)  # 获取第一个sheet
            new_worksheet.write(i, 6, 3)  # 数据异常为3
            new_worksheet.write(i, 8, time.strftime("%Y-%m-%d, %H:%M:%S"))  # 标记时间

            new_workbook.save('平城区网格长基本信息.xls')  # 保存工作簿
        except:
            log.write("数据异常")


if __name__ == '__main__':
    # data().read_data(21)
    data().tag_submit(22)

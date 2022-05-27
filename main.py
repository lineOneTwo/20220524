from ReportDataClass import ReportData, xlrd
from GetDataClass import data as dt
import logger
import time


if __name__ == '__main__':
    log = logger.Logger()
    list = dt()
    nrows = list.read_data_nrows()

    for i in range(5, nrows):
        phone = list.read_data(i)
        log.write("{0}开始操作APP{0}".format("*" * 10))
        report = ReportData()
        report.app_clear()
        report.open_app()  # 启动APP
        message = report.login(phone, "bgfg1000lbfwlXP#")

        if message == '当前网络名称:WIFI':
            report.goto_disposal()  # 待办事件按钮
            for j in range(50):
                eventcount = report.eventlist() # 获取事件列表
                time.sleep(3)
                if eventcount == False:  # 存在事件
                    break
                elif eventcount == True:
                    report.fill_in_disposal()  # 点击事件
                    report.next()  # 选择办结
                    report.write_Event()  # 填写办结描述
                    submitresult = report.submit()  # 确定办结

                    if submitresult == '办结成功':
                        list.tag_submit(i) # 统计办结成功数

                # report.logout() # 退出登录
            report.stop_app()  # 停止APP
        else:
            list.tag_login_error(i)
            continue



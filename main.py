from ReportDataClass import ReportData, xlrd
from GetDataClass import data as dt
import logger
import time

if __name__ == '__main__':
    log = logger.Logger()
    list = dt()
    # 返回xls的行数为nrows
    nrows = list.read_data_nrows()
    # num = [160, 173, 54, 72]  # 54  72
    for i in range(1, nrows):  # len(num)
        phone = list.read_data(i)  # num[i]
        log.write("{0}开始操作APP{0}".format("*" * 10))
        report = ReportData()
        report.app_clear()
        report.open_app()  # 启动APP
        message = report.login(phone, "bgfg1000lbfwlXP#")

        if message == '当前网络名称:WIFI':
            report.goto_disposal()  # 待办事件按钮
            p = 1
            for j in range(50):
                eventcount = report.eventlist(p)  # 获取事件列表
                time.sleep(3)
                if eventcount == True:  # 存在事件
                    report.clickevent(p)  # 点击事件
                    isbanjie = report.next()
                    if isbanjie == False:  # 未找到办结按钮
                        p = p + 1
                        continue
                    eventtext = report.eventcomplete()  # 获取办结页提示信息
                    if eventtext == True:  # 未获取到提示信息
                        p = p + 1  # 切换事件角标
                        report.back()  # 返回待办结事件
                    else:
                        report.write_Event()  # 填写办结描述
                        submitresult = report.submit()  # 确定办结
                        if submitresult == '办结成功':
                            list.tag_submit(i)  # 统计办结成功数  nnum[i]
                elif eventcount == False:
                    log.write('无待办事件')
                    break

                # report.logout() # 退出登录
            report.stop_app()  # 停止APP
        else:
            list.tag_login_error(i)   #num[i]
            continue


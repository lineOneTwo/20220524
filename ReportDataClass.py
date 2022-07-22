import uiautomator2 as u2
import random
import time
from GetDataClass import *
from GetDataClass import *


def sleep():
    time.sleep(2)


class ReportData:
    state = 0

    def __init__(self):
        # self.d = u2.connect("emulator-5554")
        self.d = u2.connect("127.0.0.1:62001")

    # 清除APP缓存
    def app_clear(self):
        self.d.app_clear('com.wanggeyuan.zongzhi')
        log.write("清除APP缓存")

    # 打开APP，定位在登录页
    def open_app(self):
        try:
            self.d.app_stop('com.wanggeyuan.zongzhi')
            self.d.app_start('com.wanggeyuan.zongzhi', 'com.wanggeyuan.zongzhi.main.ui.activity.LoginActivity')
            log.write("启动APP")
            self.state = 1
        except:
            log.write('启动APP失败')

    # 登陆
    def login(self, username, password):  # ,username,password
        # 用户名
        self.d(resourceId="com.wanggeyuan.zongzhi:id/username_et").click()
        sleep()
        self.d.send_keys(username, clear=True)
        # 密码
        self.d(resourceId="com.wanggeyuan.zongzhi:id/password_et").click()
        sleep()
        self.d.send_keys(password, clear=True)
        # 点登录
        self.d.xpath('//*[@resource-id="com.wanggeyuan.zongzhi:id/login_btn"]').click()
        sleep()
        message = self.d.toast.get_message()  # 获取提示信息
        log.write(message)
        log.write("登录账号：{0}".format(username))
        self.state = 2
        return message

    # 待办事件按钮
    def goto_disposal(self):
        try:
            self.d.xpath(
                '//*[@resource-id="com.wanggeyuan.zongzhi:id/gridview"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
            sleep()
            self.state = 3
        except:
            log.write('未找到待办事件按钮')

    # 点击事件
    def fill_in_disposal(self):
        try:
            self.d.xpath(
                '//*[@resource-id="com.wanggeyuan.zongzhi:id/recycleview_lv"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
            sleep()
            self.state = 4
        except:
            log.write('未找到事件')

    # 办结按钮
    def next(self):
        try:
            self.d.swipe(0.673, 0.688, 0.673, 0.293, duration=0.2)
            self.d.xpath('//*[@resource-id="com.wanggeyuan.zongzhi:id/xiangqing_btn"]').click()
            sleep()
            # self.d.xpath('//*[@text="办结"]').click()
            isbanjie = self.d.xpath('//*[@text="办结"]').exists
            if isbanjie == True:
                self.d.xpath('//*[@text="办结"]').click()
                sleep()
            elif isbanjie == False:
                self.d.xpath('//*[@text="下一步"]').click()
                sleep()
                self.d.xpath('//*[@content-desc="转到上一层级"]').click()
                log.write('事件无法办结')
                return False
        except:
            log.write('未找到办结按钮')

    # 填写办结描述
    def write_Event(self):
        try:
            self.d.xpath('//*[@resource-id="com.wanggeyuan.zongzhi:id/edt"]').click()
            sleep()
            self.d.send_keys('请继续发挥网格张职责，及时上报有效信息，切实做好疫情防控，确保一方平安。', clear=True)
            self.state = 5
        except:
            log.write("未找到输入框")

    # 确定办结
    def submit(self):
        try:
            self.d.xpath('//*[@resource-id="com.wanggeyuan.zongzhi:id/sure"]').click()
            submitresult = self.d.toast.get_message()  # 获取提示信息
            log.write(submitresult)
            return submitresult
        except:
            log.write("未找到确定按钮")

    # 获取待办事件列表
    def eventlist(self, i):
        try:
            self.d.app_start('com.wanggeyuan.zongzhi',
                             'com.wanggeyuan.zongzhi /.ZZModule.shangbaomodule.ui.ShangBaoListActivity')
            sleep()
            path = f'//*[@resource-id="com.wanggeyuan.zongzhi:id/recycleview_lv"]/android.widget.LinearLayout[{i}]/android.widget.RelativeLayout[1]'
            have = self.d.xpath(path).exists
            return have
        except:
            log.write("未打开页面")

    # 点击指定事件
    def clickevent(self, i):
        try:
            path = f'//*[@resource-id="com.wanggeyuan.zongzhi:id/recycleview_lv"]/android.widget.LinearLayout[{i}]/android.widget.RelativeLayout[1]'
            self.d.xpath(path).click()
            sleep()
            self.state = 4
        except:
            log.write('未找到事件')

    # 获取办结页提示信息
    def eventcomplete(self):
        try:
            completemessage = self.d.toast.get_message()  # 获取提示信息
            log.write(completemessage)
            if completemessage == '请完善矛盾纠纷类事件补充信息':
                log.write('事件无法办结')
                return True
        except:
            log.write("无提示信息")
            return False

    # 返回到待处理事件列表
    def back(self):
        self.d.xpath('//*[@resource-id="com.wanggeyuan.zongzhi:id/img_fanhui"]').click()
        sleep()
        self.d.xpath('//*[@content-desc="转到上一层级"]').click()

    # 退出
    def logout(self):
        # 退出登录
        self.d.xpath(
            '//*[@resource-id="com.wanggeyuan.zongzhi:id/tabLayout_father"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]').click()
        sleep()
        self.d.xpath('//*[@text="设置"]').click()
        sleep()
        self.d.xpath('//*[@resource-id="com.wanggeyuan.zongzhi:id/logout_btn"]').click()
        sleep()
        self.d.xpath('//*[@resource-id="com.wanggeyuan.zongzhi:id/md_buttonDefaultPositive"]').click()
        log.write("退出登录")
        self.state = 9

    # 关闭APP
    def stop_app(self):
        self.d.app_stop("com.wanggeyuan.zongzhi")
        self.state = 10


if __name__ == '__main__':
    rep = ReportData()
    rep.app_clear()
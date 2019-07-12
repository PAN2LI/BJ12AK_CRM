from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    # 初始化
    def __init__(self):
        desired = dict()
        desired["platformName"] = "Android"
        desired["platformVersion"] = "5.1"
        desired["deviceName"] = "192.168.56.101:5555"
        desired["appPackage"] = "com.vcooline.aike"
        desired["appActivity"] = ".umanager.LoginActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired)

    # 查找方法
    def base_find(self, loc, timeout=30, poll=0.2):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(*loc))

    # 输入方法
    def base_input(self, loc, text):
        ele = self.base_find(loc)
        ele.clear()
        ele.send_keys(text)

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

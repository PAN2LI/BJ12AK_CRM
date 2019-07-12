import os
import sys
sys.path.append(os.getcwd())

from page.page_login import PageLogin
import pytest


def get_data():
    return [("18900001111", "123456"), ("18900001112", "000000")]


class TestLogin(object):
    # 初始化
    def setup_class(self):
        self.login = PageLogin()

    # 结束方法
    def teardown_class(self):
        self.login.driver.quit()

    # 登录测试方法
    @pytest.mark.parametrize("phone,pwd", get_data())
    def test01_login(self, phone, pwd):
        self.login.login_proxy(phone, pwd)

import page
from base.base import Base


class PageLogin(Base):
    # 输入手机号
    def login_input_phone(self, phone):
        self.base_input(page.login_phone, phone)

    # 输入密码
    def login_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录按钮
    def login_click_login_btn(self):
        self.base_click(page.login_btn)

    # 登录业务
    def login_proxy(self, phone, pwd):
        self.login_input_phone(phone)
        self.login_input_pwd(pwd)
        self.login_click_login_btn()

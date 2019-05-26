# _*_ coding: utf-8 _*_
import unittest
from PageObjectModel.Pages.loginPage import LoginPages
from PageObjectModel.Application.application import Application_page
from PageObjectModel.Data_test.Function_for_downloading_test_data.test_data_loader import get_data
from ddt import ddt, data, unpack
from time import sleep


@ddt
class Login_Pages(unittest.TestCase):


    @classmethod
    def setUp(self):
        self.app = Application_page()

    @classmethod
    def tearDown(self):
        self.app.destroy()

    @data(*get_data("../Data_test/Data_test_pages/Data_test_login/data_test_login.csv"))
    @unpack
    def test_login(self, valid_email, valid_password):
        driver = self.app.driver
        login = LoginPages(driver)
        login.click_signOnbutton()
        login.enter_username(valid_email)
        login.enter_password(valid_password)
        login.click_login()
        sleep(3)
        print(login.verification_page())

if __name__ == '__main__':
     unittest.min()


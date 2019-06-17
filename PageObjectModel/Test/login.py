# _*_ coding: utf-8 _*_
import unittest
import os
os.chdir(os.path.dirname(__file__))
print('current working directory', os.getcwd())

from PageObjectModel.Pages.loginPage import LoginPages
from PageObjectModel.Configuration.Application.application import Application_page
from PageObjectModel.Data_test.Function_for_downloading_test_data.test_data_loader import get_data
from ddt import ddt, data, unpack
import allure
from allure_commons.types import AttachmentType



@ddt
class Login_Pages(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.app = Application_page()
        self.driver = self.app.driver


    @classmethod
    def tearDown(self):
        self.app.destroy()

    @allure.title("Title: logowanie do aplikacji")
    @allure.description("Description:logowanie do aplikacji")
    @allure.step("logowanie do aplikacji '{1}'")
    @data(*get_data("../Data_test/Data_test_pages/Data_test_login/data_test_login.csv"))
    @unpack
    def test_login(self, valid_email, valid_password):
        login = LoginPages(self.driver)
        login.click_signOnbutton()
        login.enter_username(valid_email)
        login.enter_password(valid_password)
        login.click_login()
        allure.attach(self.app.driver.get_screenshot_as_png(), name='logowanie do aplikacji', attachment_type=AttachmentType.PNG)
        print(login.verification_page())


if __name__ == '__main__':
     unittest.min()


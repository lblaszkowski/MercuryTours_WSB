# _*_ coding: utf-8 _*_
import unittest
from PageObjectModel.Pages.logowaniePage import LogowaniePages
from PageObjectModel.Application.application import Application_page

class Logowanie_Pages(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.app = Application_page()

    @classmethod
    def tearDown(self):
        self.app.destroy()

    def test_Logowanie(self):
        driver = self.app.driver
        login = LogowaniePages(driver)
        login.click_signOnbutton()
        login.enter_username('marcelina.kos@interia.pl')
        login.enter_password('Test123')
        login.click_login()


if __name__ == '__main__':
     unittest.min()


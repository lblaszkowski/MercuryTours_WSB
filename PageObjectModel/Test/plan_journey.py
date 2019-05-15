# _*_ coding: utf-8 _*_

import unittest
from PageObjectModel.Pages.loginPage import LoginPages
from PageObjectModel.Pages.planTravelsPage import PlanTravelsPage
from PageObjectModel.Application.application import Application_page
from PageObjectModel.Data_test.Function_for_downloading_test_data.test_data_loader import get_data
from ddt import ddt, data, unpack


@ddt
class Plan_Journey_Pages(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.app = Application_page()

    @classmethod
    def tearDown(self):
        self.app.destroy()

    @data(*get_data("../Data_test/Data_test_pages/Data_test_plan_journey/data_test_plan_journey.csv"))
    @unpack
    def test_Plan_Journey(self, valid_email, valid_password):
        driver = self.app.driver
        login = LoginPages(driver)
        login.click_signOnbutton()
        login.enter_username(valid_email)
        login.enter_password(valid_password)
        login.click_login()
        plantravels = PlanTravelsPage(driver)
        plantravels.click_flights()


if __name__ == '__main__':
    unittest.min()
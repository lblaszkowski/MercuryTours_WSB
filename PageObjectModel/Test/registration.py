# _*_ coding: utf-8 _*_
import unittest
import os
os.chdir(os.path.dirname(__file__))
print('current working directory', os.getcwd())

from PageObjectModel.Pages.registrationPage import RegistrationPage
from PageObjectModel.Configuration.Application.application import Application_page
from PageObjectModel.Data_test.Function_for_downloading_test_data.test_data_loader import get_data
from ddt import ddt, data, unpack
import allure
from allure_commons.types import AttachmentType



@ddt
class Registration_Pages(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.app = Application_page()
        self.driver = self.app.driver


    @classmethod
    def tearDown(self):
        self.app.destroy()

    @allure.title("Title: Rezerwacja lotu")
    @allure.description("Description: Rezerwacja lotu")
    @allure.step("Plan lotu '{1}'")
    @data(*get_data("../Data_test/Data_test_pages/Data_test_registration/data_test_registration.csv"))
    @unpack
    def test_registration(self, valid_FirstName, valid_LastName,valid_Phone, valid_Email,
                           valid_Address1, valid_Address2, valid_City, valid_State, valid_PostalCode,
                           valid_Select,valid_Password):
        registration = RegistrationPage(self.driver)
        registration.click_registration()
        registration.field_firstName(valid_FirstName)
        registration.field_lastName(valid_LastName)
        registration.field_phone(valid_Phone)
        registration.field_userName(valid_Email)
        registration.field_address1(valid_Address1)
        registration.field_address2(valid_Address2)
        registration.field_city(valid_City)
        registration.field_state(valid_State)
        registration.field_postalCode(valid_PostalCode)
        registration.field_select(valid_Select)
        registration.field_email(valid_Email)
        registration.field_password(valid_Password)
        registration.field_confirmPassword(valid_Password)
        allure.attach(self.app.driver.get_screenshot_as_png(), name='Rezerwacja lotu',
                      attachment_type=AttachmentType.PNG)
        registration.click_register()

if __name__ == '__main__':
    unittest.min()


# _*_ coding: utf-8 _*_
import unittest
from PageObjectModel.Pages.registrationPage import RegistrationPage
from PageObjectModel.Application.application import Application_page


class NewtoursDemoautRegistration(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.app = Application_page()

    @classmethod
    def tearDown(self):
        self.app.destroy()

    def test_Rejestracja (self):
        driver = self.app.driver
        registration = RegistrationPage(driver)
        registration.click_registration()
        registration.field_firstName("MARCELINA")
        registration.field_lastName("KOS")
        registration.field_phone("123456789")
        registration.field_userName("marcelina.kos@interia.pl")
        registration.field_address1("Toruńska")
        registration.field_address2("12a/9")
        registration.field_city("Sopot")
        registration.field_state("Sopot")
        registration.field_postalCode("12-098")
        registration.field_select("POLAND")
        registration.field_email("marcelina.kos@interia.pl")
        registration.field_password("Test123")
        registration.field_confirmPassword("Test123")
        registration.click_register()

if __name__ == '__main__':
    unittest.min()


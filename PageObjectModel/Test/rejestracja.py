# _*_ coding: utf-8 _*_
import unittest
from selenium import webdriver
import datetime
from PageObjectModel.Pages.registrationPage import RegistrationPage


class NewtoursDemoautRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:/NewtoursDemoau/PageObjectModel/Drivers/FirefoxDrive_24/geckodriver.exe')
        print("-----------------")
        print("Run Started at :" + str(datetime.datetime.now()))



    def tearDown(self):
        print("------------------------------------------------------------------")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()

    def test_Rejestracja (self):
        driver = self.driver
        self.driver.get('http://newtours.demoaut.com/')
        self.driver.maximize_window()

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


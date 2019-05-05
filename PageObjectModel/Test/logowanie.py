# _*_ coding: utf-8 _*_
import unittest
from selenium import webdriver
import datetime
from PageObjectModel.Pages.logowaniePage import LogowaniePages


class Logowanie_Pages(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')
        print("-----------------")
        print("Run Started at :" + str(datetime.datetime.now()))


    @classmethod
    def tearDown(self):
        print("-----------------------------------------------------")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()

    def test_Logowanie(self):
        driver = self.driver
        driver.get('http://newtours.demoaut.com/')
        driver.maximize_window()
        login = LogowaniePages(driver)
        login.click_signOnbutton()
        login.enter_username('marcelina.kos@interia.pl')
        login.enter_password('Test123')
        login.click_login()



if __name__ == '__main__':
     unittest.min()


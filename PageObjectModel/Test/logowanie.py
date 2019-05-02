# _*_ coding: utf-8 _*_
import unittest
from selenium import webdriver
from time import sleep
from PageObjectModel.Pages.logowaniePage import LogowaniePages


class Logowanie_Pages(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_74\chromedriver.exe')
        self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')

    def tearDown(self):
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
        sleep(7)

if __name__ == '__main__':
    unittest.min()
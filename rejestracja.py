# _*_ coding: utf-8 _*_
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep



class NewtoursDemoautRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_74\chromedriver.exe')
        # self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')
        self.driver.get('http://newtours.demoaut.com/')
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()

    def test_Rejestracja (self):
        driver = self.driver
        self.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a").click()
        self.driver.find_element_by_xpath("//*[@name='firstName']").send_keys('MARCELINA')
        self.driver.find_element_by_xpath("//*[@name='lastName']").send_keys('KOS')
        self.driver.find_element_by_xpath("//*[@name='phone']").send_keys('123456789')
        self.driver.find_element_by_id("userName").send_keys('marcelina.kos@interia.pl')
        self.driver.find_element_by_xpath("//*[@name='address1']").send_keys('Toruńska')
        self.driver.find_element_by_xpath("//*[@name='address2']").send_keys('12a/9')
        self.driver.find_element_by_xpath("//*[@name='city']").send_keys('Sopot')
        self.driver.find_element_by_xpath("//*[@name='state']").send_keys('Sopot')
        self.driver.find_element_by_xpath("//*[@name='postalCode']").send_keys('12-098')
        select = Select(driver.find_element_by_name('country'))
        select.select_by_visible_text("POLAND")
        self.driver.find_element_by_id("email").send_keys('marcelina.kos@interia.pl')
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys('Test123')
        self.driver.find_element_by_xpath("//*[@name='confirmPassword']").send_keys('Test123')
        self.driver.find_element_by_xpath("//*[@name='register']").click()



# _*_ coding: utf-8 _*_

import unittest
from selenium import webdriver
from time import sleep



class Logowanie_Pages(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_74\chromedriver.exe')
        self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')
        self.driver.get('http://newtours.demoaut.com/')
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


    def test_Logowanie(self):
        driver = self.driver
        self.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a").click()
        self.driver.find_element_by_xpath("//*[@name='userName']").send_keys('marcelina.kos@interia.pl')
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys('Test123')
        self.driver.find_element_by_xpath("//*[@name='login']").click()


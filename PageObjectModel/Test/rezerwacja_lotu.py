# _*_ coding: utf-8 _*_

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class NewtoursDemoautRegistration(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')
        self.driver.get('http://newtours.demoaut.com/')
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()



    def test_Rezerwacja_lotu(self):
        driver = self.driver
        self.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a").click()
        self.driver.find_element_by_xpath("//*[@name='userName']").send_keys('marcelina.kos@interia.pl')
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys('Test123')
        self.driver.find_element_by_xpath("//*[@name='login']").click()
        # Etap_1
        radio = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[1]")))
        radio.click()
        select = Select(driver.find_element_by_name('passCount'))
        select.select_by_visible_text("1")
        select = Select(driver.find_element_by_name('fromPort'))
        select.select_by_visible_text("Sydney")
        select = Select(driver.find_element_by_name('fromMonth'))
        select.select_by_visible_text("June")
        select = Select(driver.find_element_by_name('fromDay'))
        select.select_by_visible_text("12")
        select = Select(driver.find_element_by_name('toPort'))
        select.select_by_visible_text("San Francisco")
        select = Select(driver.find_element_by_name('toMonth'))
        select.select_by_visible_text("December")
        select = Select(driver.find_element_by_name('toDay'))
        select.select_by_visible_text("21")
        self.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[1]").click()
        select = Select(driver.find_element_by_name('airline'))
        select.select_by_visible_text("Blue Skies Airlines")
        self.driver.find_element_by_xpath("//*[@name='findFlights']").click()
        # Etap_2
        self.driver.find_element_by_xpath("//*[@name='outFlight']").click()
        self.driver.find_element_by_xpath("//*[@name='inFlight']").click()
        self.driver.find_element_by_xpath("//*[@name='reserveFlights']").click()
        # Etap_3
        self.driver.find_element_by_xpath("//*[@name='passFirst0']").send_keys('MARCELINA')
        self.driver.find_element_by_xpath("//*[@name='passLast0']").send_keys('KOS')
        select = Select(driver.find_element_by_name('pass.0.meal'))
        select.select_by_visible_text("Hindu")
        select = Select(driver.find_element_by_name('creditCard'))
        select.select_by_visible_text("MasterCard")
        self.driver.find_element_by_xpath("//*[@name='creditnumber']").send_keys('123243556546')
        select = Select(driver.find_element_by_name('cc_exp_dt_mn'))
        select.select_by_visible_text("02")
        select = Select(driver.find_element_by_name('cc_exp_dt_yr'))
        select.select_by_visible_text("2000")
        self.driver.find_element_by_xpath("//*[@name='cc_frst_name']").send_keys('MARCELINA')
        self.driver.find_element_by_xpath("//*[@name='cc_mid_name']").send_keys('2')
        self.driver.find_element_by_xpath("//*[@name='cc_last_name']").send_keys('KOS')
        self.driver.find_element_by_xpath("//*[@name='ticketLess']").click()
        self.driver.find_element_by_xpath("//*[@name='billAddress1']").send_keys('Jana Pawła II 40a/9')
        self.driver.find_element_by_xpath("//*[@name='billCity']").send_keys('Kraków')
        self.driver.find_element_by_xpath("//*[@name='billState']").send_keys('Kraków')
        self.driver.find_element_by_xpath("//*[@name='billZip']").send_keys('12-098')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        select = Select(driver.find_element_by_name('billCountry'))
        select.select_by_visible_text("POLAND")
        self.driver.find_element_by_xpath("//*[@name='ticketLess']").click()
        self.driver.find_element_by_xpath("//*[@name='delAddress1']").send_keys('Jana Pawła II 40a/9')
        self.driver.find_element_by_xpath("//*[@name='delCity']").send_keys('Kraków')
        self.driver.find_element_by_xpath("//*[@name='delState']").send_keys('Kraków')
        self.driver.find_element_by_xpath("//*[@name='delZip']").send_keys('12-098')
        select = Select(driver.find_element_by_name('delCountry'))
        select.select_by_visible_text("POLAND")
        alert = driver.switch_to.alert
        alert.accept()
        self.driver.find_element_by_xpath("//*[@name='buyFlights']").click()
        print(driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td/p/font/b/font[2]").text)
        assert driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td/p/font/b/font[2]").text == "Your itinerary has been booked!"
        self.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[7]/td/table/tbody/tr/td[3]/a/img").click()


if __name__ == '__main__':
    unittest.min()
from selenium.webdriver.support.ui import Select
from PageObjectModel.Locators.locator import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class ReservationFlightPage():

    def __init__(self, driver):
        self.driver = driver

    #Etap_1
    def click_Flights(self):
        flights_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locators.flights_button_xpath1)))
        flights_btn.click()

    def select_passCount(self, passCount):
        select = Select(self.driver.find_element_by_name(Locators.select_field_passCount))
        select.select_by_visible_text(passCount)

    def select_fromPort(self, fromPort):
        select = Select(self.driver.find_element_by_name(Locators.select_field_fromPort))
        select.select_by_visible_text(fromPort)

    def select_fromMonth(self, fromMonth):
        select = Select(self.driver.find_element_by_name(Locators.select_field_fromMonth))
        select.select_by_visible_text(fromMonth)

    def select_fromDay(self, fromDay):
        select = Select(self.driver.find_element_by_name(Locators.select_field_fromDay))
        select.select_by_visible_text(fromDay)

    def select_toPort(self, toPort):
        select = Select(self.driver.find_element_by_name(Locators.select_field_toPort))
        select.select_by_visible_text(toPort)

    def select_toDay(self, toDay):
        select = Select(self.driver.find_element_by_name(Locators.select_field_toDay))
        select.select_by_visible_text(toDay)

    def select_toMonth(self, toMonth):
         select = Select(self.driver.find_element_by_name(Locators.select_field_toMonth))
         select.select_by_visible_text(toMonth)

    def click_inputRadio(self):
        self.driver.find_element_by_xpath(Locators.inputRadio_xpath).click()

    def select_airline(self, airline):
        select = Select(self.driver.find_element_by_name(Locators.select_field_airline))
        select.select_by_visible_text(airline)

    def click_findFlights(self):
        self.driver.find_element_by_xpath(Locators.findFlights__button_xpath).click()

    # Etap_2
    def click_outFlight(self):
        self.driver.find_element_by_xpath(Locators.outFlight_button_xpath).click()

    def click_inFlight(self):
        self.driver.find_element_by_xpath(Locators.inFlight_button_xpath).click()

    def click_reserveFlights(self):
        self.driver.find_element_by_xpath(Locators.reserveFlights_button_xpath).click()

    # Etap_3
    def passFirst0_field(self, passFirst0):
        fieldPassFirst = self.driver.find_element_by_xpath(Locators.reserveFlights_field_xpath)
        fieldPassFirst.clear()
        fieldPassFirst.send_keys(passFirst0)

    def passLast0_field(self, passLast0):
        self.driver.find_element_by_xpath(Locators.passLast0_field_xpath).send_keys(passLast0)

    def select_pass0meal(self, pass0meal):
        select = Select(self.driver.find_element_by_xpath(Locators.select_field_pass0meal))
        select.select_by_visible_text(pass0meal)

    def select_creditCard(self, creditCard):
        select = Select(self.driver.find_element_by_xpath(Locators.select_field_creditCard))
        select.select_by_visible_text(creditCard)

    def creditnumber_field(self, creditnumber):
        fieldCreditnumber = self.driver.find_element_by_xpath(Locators.creditnumber_field_xpath)
        fieldCreditnumber.clear()
        fieldCreditnumber.send_keys(creditnumber)

    def select_cc_exp_dt_mn(self, cc_exp_dt_mn):
         select = Select(self.driver.find_element_by_name(Locators.select_field_cc_exp_dt_mn))
         select.select_by_visible_text(cc_exp_dt_mn)

    def select_cc_exp_dt_yr(self, cc_exp_dt_yr):
         select = Select(self.driver.find_element_by_name(Locators.select_field_cc_exp_dt_yr))
         select.select_by_visible_text(cc_exp_dt_yr)

    def cc_frst_name_field(self, cc_frst_name):
        fieldCcFrstName = self.driver.find_element_by_xpath(Locators.cc_frst_name_field_xpath)
        fieldCcFrstName.clear()
        fieldCcFrstName.send_keys(cc_frst_name)

    def cc_mid_name_field(self, cc_mid_name):
        fieldCcMidName = self.driver.find_element_by_xpath(Locators.cc_mid_name_field_xpath)
        fieldCcMidName.clear()
        fieldCcMidName.send_keys(cc_mid_name)

    def cc_last_name_field(self, cc_last_name):
        fieldCcLastName = self.driver.find_element_by_xpath(Locators.cc_last_name_field_xpath)
        fieldCcLastName.clear()
        fieldCcLastName.send_keys(cc_last_name)

    def click_ticketLess(self):
        self.driver.find_element_by_xpath(Locators.ticketLess_xpath).click()

    def billAddress1_field(self, billAddress1):
        fieldBillAddress = self.driver.find_element_by_xpath(Locators.billAddress1_field_xpath)
        fieldBillAddress.clear()
        fieldBillAddress.send_keys(billAddress1)

    def billCity_field(self, billCity):
        fieldBillCity = self.driver.find_element_by_xpath(Locators.billCity_field_xpath)
        fieldBillCity.clear()
        fieldBillCity.send_keys(billCity)

    def billState_field(self, billState):
        fieldBillState = self.driver.find_element_by_xpath(Locators.billState_field_xpath)
        fieldBillState.clear()
        fieldBillState.send_keys(billState)

    def billZip_field(self, billZip):
        fieldBillZip = self.driver.find_element_by_xpath(Locators.billZip_field_xpath)
        fieldBillZip.clear()
        fieldBillZip.send_keys(billZip)

    def window_script(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def select_billCountry(self, billCountry):
         select = Select(self.driver.find_element_by_name(Locators.select_field_billCountry))
         select.select_by_visible_text(billCountry)

    def click_ticketLess1(self):
        self.driver.find_element_by_xpath(Locators.ticketLess_xpath1).click()

    def delAddress1_field(self, delAddress1):
        fieldDelAddress1 = self.driver.find_element_by_xpath(Locators.delAddress1_field_xpath)
        fieldDelAddress1.clear()
        fieldDelAddress1.send_keys(delAddress1)

    def delCity_field(self, delCity):
        fieldDelCity = self.driver.find_element_by_xpath(Locators.delCity_field_xpath)
        fieldDelCity.clear()
        fieldDelCity.send_keys(delCity)

    def delState_field(self, delState):
        fieldDelState = self.driver.find_element_by_xpath(Locators.delState_field_xpath)
        fieldDelState.clear()
        fieldDelState.send_keys(delState)

    def delZip_field(self, delZip):
        fieldDelZip = self.driver.find_element_by_xpath(Locators.delZip_field_xpath)
        fieldDelZip.clear()
        fieldDelZip.send_keys(delZip)

    def select_delCountry(self, delCountry):
        select = Select(self.driver.find_element_by_name(Locators.select_field_delCountry))
        select.select_by_visible_text(delCountry)

    def switch_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def click_buyFlights(self):
        self.driver.find_element_by_xpath(Locators.buyFlights_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(Locators.logout_button_xpath).click()






# _*_ coding: utf-8 _*_
import unittest
import os
os.chdir(os.path.dirname(__file__))
print('current working directory', os.getcwd())

from PageObjectModel.Pages.loginPage import LoginPages
from PageObjectModel.Pages.reservationFlightPage import ReservationFlightPage
from PageObjectModel.Application.application import Application_page
from PageObjectModel.Data_test.Function_for_downloading_test_data.test_data_loader import get_data
from ddt import ddt, data, unpack
from time import sleep
import allure
from allure_commons.types import AttachmentType

@ddt
class Booking_Flight_Pages(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.app = Application_page()

    @classmethod
    def tearDown(self):
        self.app.destroy()

    @allure.title("Title: Rezerwacja lotu")
    @allure.description("Description: Rezerwacja lotu")
    @allure.step("Rezerwacja lotu '{1}'")
    @data(*get_data("../Data_test/Data_test_pages/Data_test_booking_flight/data_test_booking_flight.csv"))
    @unpack
    def test_Booking_Flight(self, valid_email, valid_password, valid_selectPpassCount, valid_selectFromPort, valid_selectFfromMonth,
                            valid_selectFfromDay, valid_selectToPort, valid_selectToDay, valid_selectToMonth, valid_selectAairline,
                            valid_fieldPassFirst0, valid_fieldPassLast0, valid_selectPass0meal, valid_selectCreditCard,
                            valid_fieldCreditnumber, valid_selectCcExpDtMn, valid_selectCcExpDtYr, valid_fieldCcFrstName,
                            valid_fieldCcMidName, valid_fieldCcLastName, valid_fieldBillAddress1, valid_fieldBillCity,
                            valid_fieldBillState, valid_fieldBillZip, valid_select_billCountry,
                            valid_delAddress1_field, valid_delCity_field,
                            valid_delState_field, valid_fieldDelZip, valid_selectDelCountry):
        driver = self.app.bro.driver
        login = LoginPages(driver)
        login.click_signOnbutton()
        login.enter_username(valid_email)
        login.enter_password(valid_password)
        login.click_login()
        # Etap_1
        ReservationFlight = ReservationFlightPage(driver)
        ReservationFlight.click_Flights()
        ReservationFlight.select_passCount(valid_selectPpassCount)
        ReservationFlight.select_fromPort(valid_selectFromPort)
        ReservationFlight.select_fromMonth(valid_selectFfromMonth)
        ReservationFlight.select_fromDay(valid_selectFfromDay)
        ReservationFlight.select_toPort(valid_selectToPort)
        ReservationFlight.select_toDay(valid_selectToDay)
        ReservationFlight.select_toMonth(valid_selectToMonth)
        ReservationFlight.click_inputRadio()
        ReservationFlight.select_airline(valid_selectAairline)
        ReservationFlight.click_findFlights()
        allure.attach(self.app.bro.driver.get_screenshot_as_png(), name='Rezerwacja lotu - etap 1', attachment_type=AttachmentType.PNG)
        # Etap_2
        ReservationFlight.click_outFlight()
        ReservationFlight.click_inFlight()
        allure.attach(self.app.bro.driver.get_screenshot_as_png(), name='Rezerwacja lotu - etap 2', attachment_type=AttachmentType.PNG)
        ReservationFlight.click_reserveFlights()
        # Etap_3
        ReservationFlight.passFirst0_field(valid_fieldPassFirst0)
        ReservationFlight.passLast0_field(valid_fieldPassLast0)
        ReservationFlight.select_pass0meal(valid_selectPass0meal)
        ReservationFlight.select_creditCard(valid_selectCreditCard)
        ReservationFlight.creditnumber_field(valid_fieldCreditnumber)
        ReservationFlight.select_cc_exp_dt_mn(valid_selectCcExpDtMn)
        ReservationFlight.select_cc_exp_dt_yr(valid_selectCcExpDtYr)
        ReservationFlight.cc_frst_name_field(valid_fieldCcFrstName)
        ReservationFlight.cc_mid_name_field(valid_fieldCcMidName)
        ReservationFlight.cc_last_name_field(valid_fieldCcLastName)
        ReservationFlight.click_ticketLess()
        ReservationFlight.billAddress1_field(valid_fieldBillAddress1)
        ReservationFlight.billCity_field(valid_fieldBillCity)
        ReservationFlight.billState_field(valid_fieldBillState)
        ReservationFlight.billZip_field(valid_fieldBillZip)
        ReservationFlight.window_script()
        ReservationFlight.select_billCountry(valid_select_billCountry)
        ReservationFlight.click_ticketLess1()
        ReservationFlight.delAddress1_field(valid_delAddress1_field)
        ReservationFlight.delCity_field(valid_delCity_field)
        ReservationFlight.delState_field(valid_delState_field)
        ReservationFlight.delZip_field(valid_fieldDelZip)
        ReservationFlight.select_delCountry(valid_selectDelCountry)
        ReservationFlight.switch_alert()
        sleep(4)
        ReservationFlight.click_buyFlights()
        allure.attach(self.app.bro.driver.get_screenshot_as_png(), name='Rezerwacja lotu - etap 3',
                      attachment_type=AttachmentType.PNG)
        ReservationFlight.click_logout()


if __name__ == '__main__':
    unittest.min()
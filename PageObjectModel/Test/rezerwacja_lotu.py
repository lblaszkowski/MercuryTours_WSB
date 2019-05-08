# _*_ coding: utf-8 _*_

import unittest
from PageObjectModel.Pages.logowaniePage import LogowaniePages
from PageObjectModel.Pages.reservationFlightPage import ReservationFlightPage
from PageObjectModel.Application.application import Application_page

class NewtoursDemoautRegistrationTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.app = Application_page()

    @classmethod
    def tearDown(self):
        self.app.destroy()

    def test_Rezerwacja_lotu(self):
        driver = self.app.driver
        login = LogowaniePages(driver)
        login.click_signOnbutton()
        login.enter_username("marcelina.kos@interia.pl")
        login.enter_password("Test123")
        login.click_login()
        # Etap_1
        ReservationFlight = ReservationFlightPage(driver)
        ReservationFlight.click_Flights()
        ReservationFlight.select_passCount("1")
        ReservationFlight.select_fromPort("Sydney")
        ReservationFlight.select_fromMonth("June")
        ReservationFlight.select_fromDay("12")
        ReservationFlight.select_toPort("San Francisco")
        ReservationFlight.select_toDay("21")
        ReservationFlight.select_toMonth("December")
        ReservationFlight.click_inputRadio()
        ReservationFlight.select_airline("Blue Skies Airlines")
        ReservationFlight.click_findFlights()
        # Etap_2
        ReservationFlight.click_outFlight()
        ReservationFlight.click_inFlight()
        ReservationFlight.click_reserveFlights()
        # Etap_3
        ReservationFlight.passFirst0_field("MARCELINA")
        ReservationFlight.passLast0_field("KOS")
        ReservationFlight.select_pass0meal("Hindu")
        ReservationFlight.select_creditCard("MasterCard")
        ReservationFlight.creditnumber_field("123243556546")
        ReservationFlight.select_cc_exp_dt_mn("02")
        ReservationFlight.select_cc_exp_dt_yr("2000")
        ReservationFlight.cc_frst_name_field("MARCELINA")
        ReservationFlight.cc_mid_name_field("2")
        ReservationFlight.cc_last_name_field("KOS")
        ReservationFlight.click_ticketLess()
        ReservationFlight.billAddress1_field("Jana Pawła II 40a/9")
        ReservationFlight.billCity_field("Kraków")
        ReservationFlight.billState_field("Kraków")
        ReservationFlight.billZip_field("12-098")
        ReservationFlight.window_script()
        ReservationFlight.select_billCountry("POLAND")
        ReservationFlight.click_ticketLess1()
        ReservationFlight.delAddress1_field("Jana Pawła II 40a/")
        ReservationFlight.delCity_field("Kraków")
        ReservationFlight.delState_field("Kraków")
        ReservationFlight.delZip_field("12-098")
        ReservationFlight.select_delCountry("POLAND")
        ReservationFlight.switch_alert()
        ReservationFlight.click_buyFlights()
        ReservationFlight.click_logout()

if __name__ == '__main__':
    unittest.min()
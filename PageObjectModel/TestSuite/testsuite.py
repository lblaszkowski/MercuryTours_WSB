import unittest

from PageObjectModel.Test.login import Login_Pages
from PageObjectModel.Test.plan_journey import Plan_Journey_Pages
from PageObjectModel.Test.registration import Registration_Pages
from PageObjectModel.Test.booking_flight import Booking_Flight_Pages

def full_suite():
    test_suite = unittest.TestSuite()
    # test_suite.addTest(unittest.makeSuite(Plan_Journey_Pages))
    # test_suite.addTest(unittest.makeSuite(Login_Pages))
    # test_suite.addTest(unittest.makeSuite(Registration_Pages))
    test_suite.addTest(unittest.makeSuite(Booking_Flight_Pages))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())




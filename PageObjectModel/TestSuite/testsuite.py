import unittest
from unittest.loader import makeSuite
from PageObjectModel.Test.logowanie import Logowanie_Pages
from PageObjectModel.Test.plan_podrozy import PlanPodrozy_Pages
from PageObjectModel.Test.rejestracja import NewtoursDemoautRegistration
from PageObjectModel.Test.rezerwacja_lotu import NewtoursDemoautRegistrationTest



def smoke_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(PlanPodrozy_Pages))
    test_suite.addTest(makeSuite(Logowanie_Pages))
    test_suite.addTest(makeSuite(NewtoursDemoautRegistration))
    test_suite.addTest(makeSuite(NewtoursDemoautRegistrationTest))

    return test_suite

runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_suite())


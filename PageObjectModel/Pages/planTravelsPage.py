from PageObjectModel.Locators.locator import Locators


class PlanTravelsPage():

    def __init__(self, driver):
        self.driver = driver

    def click_flights(self):
        self.driver.find_element_by_xpath(Locators.flights_button_xpath).click()


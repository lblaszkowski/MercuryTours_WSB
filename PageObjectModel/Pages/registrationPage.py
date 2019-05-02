from PageObjectModel.Locators.locator import Locators
from selenium.webdriver.support.ui import Select

class RegistrationPage():


    def __init__(self, driver):
        self.driver = driver

    def click_registration(self):
        self.driver.find_element_by_xpath(Locators.registration_button_xpath).click()

    def field_firstName(self, firstName):
        self.driver.find_element_by_xpath(Locators.firstName_field_xpath).send_keys(firstName)

    def field_lastName(self, lastName):
        self.driver.find_element_by_xpath(Locators.lastName_field_xpath).send_keys(lastName)

    def field_phone(self, phone):
        self.driver.find_element_by_xpath(Locators.phone_field_xpath).send_keys(phone)

    def field_userName(self, userName):
        self.driver.find_element_by_id(Locators.userName_field_id).send_keys(userName)

    def field_address1(self, address1):
        self.driver.find_element_by_xpath(Locators.address1_field_xpath).send_keys(address1)

    def field_address2(self, address2):
        self.driver.find_element_by_xpath(Locators.address2_field_xpath).send_keys(address2)

    def field_city(self, city):
        self.driver.find_element_by_xpath(Locators.city_field_xpath).send_keys(city)

    def field_state(self, state):
        self.driver.find_element_by_xpath(Locators.state_field_xpath).send_keys(state)

    def field_postalCode(self, postalCode):
        self.driver.find_element_by_xpath(Locators.postalCode_field_xpath).send_keys(postalCode)

    # def field_select(self, country):
    #     select = Select(self.driver.find_element_by_xpath(Locators.select_field_name)).click()
    #     select.select_by_visible_text(country)

    def field_email(self, email):
        self.driver.find_element_by_id(Locators.email_field_id).send_keys(email)

    def field_password(self, password):
        self.driver.find_element_by_xpath(Locators.password_field_xpath).send_keys(password)

    def field_confirmPassword(self, confirmPassword):
        self.driver.find_element_by_xpath(Locators.confirmPassword_field_xpath).send_keys(confirmPassword)

    def click_register(self):
        self.driver.find_element_by_xpath(Locators.register_button_xpath).click()
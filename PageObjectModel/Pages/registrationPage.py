from PageObjectModel.Locators.locator import Locators
from selenium.webdriver.support.ui import Select



class RegistrationPage():


    def __init__(self, driver):
        self.driver = driver

    def click_registration(self):
        self.driver.find_element_by_xpath(Locators.registration_button_xpath).click()

    def field_firstName(self, firstName):
        fieldFirstName = self.driver.find_element_by_xpath(Locators.firstName_field_xpath)
        fieldFirstName.clear()
        fieldFirstName.send_keys(firstName)

    def field_lastName(self, lastName):
        fieldLastName = self.driver.find_element_by_xpath(Locators.lastName_field_xpath)
        fieldLastName.clear()
        fieldLastName.send_keys(lastName)

    def field_phone(self, phone):
        phoneNumber = self.driver.find_element_by_xpath(Locators.phone_field_xpath)
        phoneNumber.clear()
        phoneNumber.send_keys(phone)

    def field_userName(self, userName):
        fieldUserName = self.driver.find_element_by_id(Locators.userName_field_id)
        fieldUserName.clear()
        fieldUserName.send_keys(userName)

    def field_address1(self, address1):
        fieldAddress1 = self.driver.find_element_by_xpath(Locators.address1_field_xpath)
        fieldAddress1.clear()
        fieldAddress1.send_keys(address1)

    def field_address2(self, address2):
        fieldAddress2 = self.driver.find_element_by_xpath(Locators.address2_field_xpath)
        fieldAddress2.clear()
        fieldAddress2.send_keys(address2)

    def field_city(self, city):
        fieldCity = self.driver.find_element_by_xpath(Locators.city_field_xpath)
        fieldCity.clear()
        fieldCity.send_keys(city)

    def field_state(self, state):
        fieldState = self.driver.find_element_by_xpath(Locators.state_field_xpath)
        fieldState.clear()
        fieldState.send_keys(state)

    def field_postalCode(self, postalCode):
        fieldPostalCode = self.driver.find_element_by_xpath(Locators.postalCode_field_xpath)
        fieldPostalCode.clear()
        fieldPostalCode.send_keys(postalCode)

    def field_select(self, country):
        select = Select(self.driver.find_element_by_xpath(Locators.select_field_name))
        select.select_by_visible_text(country)

    def field_email(self, email):
        fieldEmail = self.driver.find_element_by_id(Locators.email_field_id)
        fieldEmail.clear()
        fieldEmail.send_keys(email)

    def field_password(self, password):
        fieldPassword = self.driver.find_element_by_xpath(Locators.password_field_xpath)
        fieldPassword.clear()
        fieldPassword.send_keys(password)

    def field_confirmPassword(self, confirmPassword):
        fieldConfirmPassword = self.driver.find_element_by_xpath(Locators.confirmPassword_field_xpath)
        fieldConfirmPassword.clear()
        fieldConfirmPassword.send_keys(confirmPassword)

    def click_register(self):
        self.driver.find_element_by_xpath(Locators.register_button_xpath).click()
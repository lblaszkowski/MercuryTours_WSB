from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions



from PageObjectModel.Locators.locator import Locators


class LoginPages():

    def __init__(self, driver):
        self.driver = driver

    def click_signOnbutton(self):
        signOnbutton_click = self.driver.find_element_by_xpath(Locators.signOnbutton_xpath)
        signOnbutton_click.click()

    def enter_username(self, usernameEmail):
        fieldUsername = self.driver.find_element_by_xpath(Locators.userNameEmail_textbox_xpath)
        fieldUsername.clear()
        fieldUsername.send_keys(usernameEmail)

    def enter_password(self, password):
        fieldPassword = self.driver.find_element_by_xpath(Locators.password_textbox_xpath)
        fieldPassword.clear()
        fieldPassword.send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_button_xpath).click()

    def verification_page(self):
        verification_page_click = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, Locators.click_verification_xpath)))
        assert verification_page_click .text == "ITINERARY"
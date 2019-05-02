from PageObjectModel.Locators.locator import Locators


class LogowaniePages():

    def __init__(self, driver):
        self.driver = driver


    def click_signOnbutton(self):
        self.driver.find_element_by_xpath(Locators.signOnbutton_xpath).click()

    def enter_username(self, usernameEmail):
        self.driver.find_element_by_xpath(Locators.userNameEmail_textbox_xpath).send_keys(usernameEmail)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(Locators.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_button_xpath).click()
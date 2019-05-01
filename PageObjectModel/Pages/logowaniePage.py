class LogowaniePages():

    def __init__(self, driver):
        self.driver = driver
        self.signOnbutton_xpath = "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a"
        self.userNameEmail_textbox_xpath = "//*[@name='userName']"
        self.password_textbox_xpath = "//*[@name='password']"
        self.login_button_xpath = "//*[@name='login']"

    def click_signOnbutton(self):
        self.driver.find_element_by_xpath(self.signOnbutton_xpath).click()

    def enter_username(self, usernameEmail):
        self.driver.find_element_by_xpath(self.userNameEmail_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.userNameEmail_textbox_xpath).send_keys(usernameEmail)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
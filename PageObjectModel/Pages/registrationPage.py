from selenium.webdriver.support.ui import Select

class RegistrationPage():


    def __init__(self, driver):
        self.driver = driver
        self.registration_button_xpath = "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a"
        self.firstName_field_xpath = "//*[@name='firstName']"
        self.lastName_field_xpath = "//*[@name='lastName']"
        self.phone_field_xpath = "//*[@name='phone']"
        self.userName_field_id = "userName"
        self.address1_field_xpath = "//*[@name='address1']"
        self.address2_field_xpath = "//*[@name='address2']"
        self.city_field_xpath = "//*[@name='city']"
        self.state_field_xpath = "//*[@name='state']"
        self.postalCode_field_xpath = "//*[@name='postalCode']"
        self.select_field_name = "country"
        self.email_field_id = "email"
        self.password_field_xpath = "//*[@name='password']"
        self.confirmPassword_field_xpath = "//*[@name='confirmPassword']"
        self.register_button_xpath = "//*[@name='register']"


    def click_registration(self):
        self.driver.find_element_by_xpath(self.registration_button_xpath).click()

    def field_firstName(self, firstName):
        self.driver.find_element_by_xpath(self.firstName_field_xpath).send_keys(firstName)

    def field_lastName(self, lastName):
        self.driver.find_element_by_xpath(self.lastName_field_xpath).send_keys(lastName)

    def field_phone(self, phone):
        self.driver.find_element_by_xpath(self.phone_field_xpath).send_keys(phone)

    def field_userName(self, userName):
        self.driver.find_element_by_id(self.userName_field_id).send_keys(userName)

    def field_address1(self, address1):
        self.driver.find_element_by_xpath(self.address1_field_xpath).send_keys(address1)

    def field_address2(self, address2):
        self.driver.find_element_by_xpath(self.address2_field_xpath).send_keys(address2)

    def field_city(self, city):
        self.driver.find_element_by_xpath(self.city_field_xpath).send_keys(city)

    def field_state(self, state):
        self.driver.find_element_by_xpath(self.state_field_xpath).send_keys(state)

    def field_postalCode(self, postalCode):
        self.driver.find_element_by_xpath(self.postalCode_field_xpath).send_keys(postalCode)

    # def field_select(self, select):
    #     select = Select(self.driver.find_element_by_xpath(self.select_field_name))
    #     select.select_by_visible_text(select)

    def field_email(self, email):
        self.driver.find_element_by_id(self.email_field_id).send_keys(email)

    def field_password(self, password):
        self.driver.find_element_by_xpath(self.password_field_xpath).send_keys(password)

    def field_confirmPassword(self, confirmPassword):
        self.driver.find_element_by_xpath(self.confirmPassword_field_xpath).send_keys(confirmPassword)

    def click_register(self):
        self.driver.find_element_by_xpath(self.register_button_xpath).click()
from selenium import webdriver
import datetime

class Application_page:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:/NewtoursDemoau/PageObjectModel/Drivers/FirefoxDrive_24/geckodriver.exe')
        self.driver.get('http://newtours.demoaut.com/')
        self.driver.maximize_window()
        print("-----------------")
        print("Run Started at :" + str(datetime.datetime.now()))

    def destroy(self):
        print("-----------------------------------------------------")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()
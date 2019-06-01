from selenium import webdriver
import datetime

browser = "Chrome"
# browser = "Mozilla"


class Application_page:

    def __init__(self):
        if browser == "Chrome":
            self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_74\chromedriver.exe')
            self.driver.get('http://newtours.demoaut.com/')
            self.driver.maximize_window()
            print("-----------------")
            print("Run Started at :" + str(datetime.datetime.now()))
            print("start Chrome")
        elif browser == "Mozilla":
           self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
           self.driver.get('http://newtours.demoaut.com/')
           self.driver.maximize_window()
           print("-----------------")
           print("Run Started at :" + str(datetime.datetime.now()))
           print("Start Mozilla")
        else:
            print("bład")


    def destroy(self):
        print("------------------")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()
from selenium import webdriver


class Browser_pages_url():

    def browser_url_pages(self, browser="mozilla"):
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_74\chromedriver.exe')
            print("start Chrome")
        elif browser == "mozilla":
            self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
            print("Start Mozilla")
        else:
            print("Brak przeglądarki")






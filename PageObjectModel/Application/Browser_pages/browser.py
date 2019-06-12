from selenium import webdriver


class Browser_pages_url():

    def browser_url_pages(self, browser="mozilla"):
        if browser == "chrome":
            driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_74\chromedriver.exe')
        elif browser == "mozilla":
            driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
        else:
            print("Brak przeglądarki")
            raise Exception("Brak przeglądarki")
        return driver
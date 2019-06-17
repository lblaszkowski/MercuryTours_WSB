import datetime
from PageObjectModel.Configuration.Browser_pages.browser import Browser_pages_url

class Application_page:

    def __init__(self):
        self.bro = Browser_pages_url()
        self.driver = self.bro.browser_url_pages()
        self.driver.get('http://newtours.demoaut.com/')
        self.driver.maximize_window()
        print("-----------------")
        print("Run Started at :" + str(datetime.datetime.now()))

    def destroy(self):
        print("------------------")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()

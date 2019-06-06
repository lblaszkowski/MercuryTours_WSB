import datetime
from PageObjectModel.Application.Browser_pages.browser import Browser_pages_url

class Application_page:

    def __init__(self):
        self.bro = Browser_pages_url()
        self.bro.browser_url_pages()
        self.bro.driver.get('http://newtours.demoaut.com/')
        self.bro.driver.maximize_window()
        print("-----------------")
        print("Run Started at :" + str(datetime.datetime.now()))

    def destroy(self):
        print("------------------")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.bro.driver.close()
        self.bro.driver.quit()

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.navigation = NavigationHelper(self)
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()

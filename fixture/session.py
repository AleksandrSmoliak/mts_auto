class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_xpath("//a[@id='auth_top_logged']").click()
        wd.find_element_by_xpath("//input[@name='USER_LOGIN']").click()
        wd.find_element_by_xpath("//input[@name='USER_LOGIN']").clear()
        wd.find_element_by_xpath("//input[@name='USER_LOGIN']").send_keys(username)
        wd.find_element_by_xpath("//input[@name='USER_PASSWORD']").click()
        wd.find_element_by_xpath("//input[@name='USER_PASSWORD']").clear()
        wd.find_element_by_xpath("//input[@name='USER_PASSWORD']").send_keys(password)
        wd.find_element_by_xpath("//button[@class='btn btn-primary']").click()
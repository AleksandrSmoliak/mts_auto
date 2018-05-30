class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # Открываем домашнюю страницу
        self.app.navigation.open_home_page()
        # Клик по ссылке входа (Переход на страницу авторизации)
        wd.find_element_by_xpath("//a[@id='auth_top_logged']").click()
        # Выбор и заполнение поля "Имя пользователя"
        wd.find_element_by_xpath("//input[@name='USER_LOGIN']").click()
        wd.find_element_by_xpath("//input[@name='USER_LOGIN']").clear()
        wd.find_element_by_xpath("//input[@name='USER_LOGIN']").send_keys(username)
        # Выбор и заполнение поля "Пароль"
        wd.find_element_by_xpath("//input[@name='USER_PASSWORD']").click()
        wd.find_element_by_xpath("//input[@name='USER_PASSWORD']").clear()
        wd.find_element_by_xpath("//input[@name='USER_PASSWORD']").send_keys(password)
        # Клик по кнопке авторизации
        wd.find_element_by_xpath("//p[@class='login-button']/button[@class='btn btn-primary']").click()

    def logout(self):
        wd = self.app.wd
        # Клик по ссылке "Выход"
        wd.find_element_by_xpath("//li[@class='lk']/a").click()


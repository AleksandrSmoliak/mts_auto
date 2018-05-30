def test_register(app):
    wd = app.wd
    app.navigation.open_home_page()
    wd.find_element_by_xpath("//a[@id='auth_top_register']").click()
    wd.find_element_by_xpath("//input[@class='required email form-control']").click()
    wd.find_element_by_xpath("//input[@class='required email form-control']").clear()
    wd.find_element_by_xpath("//input[@class='required email form-control']").send_keys("user@autotest.ru")
    wd.find_element_by_xpath("//form[@class='register-form']//button[.='Начать регистрацию']").click()
    # Заполнение поля "Придумайте пароль"
    wd.find_element_by_xpath("//input[@id='pass']").click()
    wd.find_element_by_xpath("//input[@id='pass']").clear()
    wd.find_element_by_xpath("//input[@id='pass']").send_keys("password")
    # Заполнение поля "Повторите пароль"
    wd.find_element_by_xpath("//input[@id='rpass']").click()
    wd.find_element_by_xpath("//input[@id='rpass']").clear()
    wd.find_element_by_xpath("//input[@id='rpass']").send_keys("password")
    # Заполнение поля "Фамилия"
    wd.find_element_by_xpath("//input[@id='last_name']").click()
    wd.find_element_by_xpath("//input[@id='last_name']").clear()
    wd.find_element_by_xpath("//input[@id='last_name']").send_keys("Фамилия")
    # Заполнение поля "Имя"
    wd.find_element_by_xpath("//input[@id='name']").click()
    wd.find_element_by_xpath("//input[@id='name']").clear()
    wd.find_element_by_xpath("//input[@id='name']").send_keys("Имя")
    # Заполнение поля "Отчество"
    wd.find_element_by_xpath("//input[@id='second_name']").click()
    wd.find_element_by_xpath("//input[@id='second_name']").clear()
    wd.find_element_by_xpath("//input[@id='second_name']").send_keys("Отчество")
    # Заполнение поля "Дата рождения"
    wd.find_element_by_id("personal_birthday").click()
    wd.find_element_by_link_text("10").click()
    # Заполнение поля "Пол"

    # Клик по кнопке "Завершить регистрацию"
    wd.find_element_by_name("register_submit_button").click()
    wd.find_element_by_xpath("//li[@class='lk']/a")
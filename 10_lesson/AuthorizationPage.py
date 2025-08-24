from selenium.webdriver.common.by import By
import allure


class AuthorizationPage:

    def __init__(self, browser):
        """Конструктор класса Авторизация.
        Параметры  браузера: Webdriver - объект браузера Селениум"""
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Открытие страницы авторизации с полями ввода логина и пароля")
    def search_input_field(self):
        """Заполняет поля ввода логина и пароля, нажимает на кнопку,
           параметры кнопки: строка - текст на кнопке, которую нужно нажать"""
        self._driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self._driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self._driver.find_element(By.NAME, "login-button").click()

        """Метод для заполнения полей логина и пароля и нажатия кнопки входа.

        Параметры: Нет (кроме self).

        Возвращаемое значение: None."""



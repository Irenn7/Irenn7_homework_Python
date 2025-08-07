from selenium.webdriver.common.by import By

class AuthorizationPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

#найти поле ввода логина и пароля
    def search_input_field(self):
        self._driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self._driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self._driver.find_element(By.NAME, "login-button").click()








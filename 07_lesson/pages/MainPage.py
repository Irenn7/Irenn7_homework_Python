from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_cookie_policy(self):
        cookie = {
            "name": "cookie_policy",
            "value": "1"
        }
        self._driver.add_cookie(cookie)

    def search_product(self, term):
        products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        for product_id in products:
            self._driver.find_element(By.ID, product_id).click()

    def add_product(self):
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, "add-to-cart-sauce-labs-backpack",
"add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-onesie",)
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter = 3

        return counter



from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self._driver = browser

    #нажать на кнопку checkout

    #проверить содержимое корзины
    def shopping_cart(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self._driver.find_element(By.ID, "checkout").click()

from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/cart.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    #нажать на кнопку checkout
    def click_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "checkout").click()
    #проверить содержимое корзины
    def shopping_cart(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self._driver.find_element(By.ID, "checkout").click()

from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, browser):
        self._driver = browser


    def search_product(self):
        products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        for product_id in products:
            self._driver.find_element(By.ID, product_id).click()





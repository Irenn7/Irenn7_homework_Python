from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPage:
    def __init__(self, driver):
        self.add_to_cart_button = None
        self.driver = driver

    @allure.step("Добавление товаров в корзину")
    def search_product(self):
        """Метод добавляет выбранные товары в корзину."""
        products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        wait = WebDriverWait(self.driver, 10)

        for product_id in products:
            self.add_to_cart_button = wait.until(
                EC.presence_of_element_located((By.ID, product_id))
            )
            self.add_to_cart_button.click()




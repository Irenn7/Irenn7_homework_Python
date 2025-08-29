from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(driver, 25)

    @allure.step("Добавление товаров в корзину")
    def search_product(self):
        """Метод добавляет выбранные товары в корзину."""
        products = ["add-to-cart-sauce-labs-backpack",
                    "add-to-cart-sauce-labs-bolt-t-shirt"
                    "add-to-cart-sauce-labs-onesie"
                    ]
        for product_id in products:
            self.driver.find_element(By.ID, product_id).click()





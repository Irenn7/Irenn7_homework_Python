from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure

class CartPage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step("Открытие страницы корзины")
    def shopping_cart(self):
        """Метод открывает страницу корзины."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()



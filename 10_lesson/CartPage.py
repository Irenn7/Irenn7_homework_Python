from selenium.webdriver.common.by import By
import allure

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https: // www.saucedemo.com")

    @allure.step("Открытие страницы корзины")
    def shopping_cart(self):
        """Метод открывает страницу корзины."""
        self.driver.find_element(By.ID, "checkout").click()



